from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from langchain_core.documents import Document
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_text_splitters import RecursiveCharacterTextSplitter

from generic_rag.parsers.config import AppSettings, ParserSelection
from generic_rag.parsers.connect_sources import docling_parser as docling_doc_parser
from generic_rag.parsers.parser import extract_text_from_pdf

logger = logging.getLogger(__name__)


SUPPORTED_UPLOAD_EXTENSIONS = {".pdf", ".txt", ".md"}


def _parse_file(file_path: Path, settings: AppSettings) -> list[Document]:
    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        if settings.parser_selection == ParserSelection.docling:
            parsed_doc = docling_doc_parser(str(file_path))
            text = parsed_doc.export_to_markdown()
        else:
            text = extract_text_from_pdf(file_path, settings)
        return [Document(page_content=text, metadata={"source": str(file_path), "page": 1, "filetype": "pdf"})]

    if suffix in {".txt", ".md"}:
        text = file_path.read_text(encoding="utf-8", errors="ignore")
        return [
            Document(
                page_content=text,
                metadata={"source": str(file_path), "page": 1, "filetype": suffix.lstrip(".")},
            )
        ]

    raise ValueError(f"Unsupported file extension: {suffix}")


def ingest_uploaded_files(file_paths: list[str | Path], settings: AppSettings, vector_store: Any) -> list[dict[str, Any]]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.pdf.chunk_size,
        chunk_overlap=settings.pdf.chunk_overlap,
        add_start_index=settings.pdf.add_start_index,
    )

    statuses: list[dict[str, Any]] = []

    for raw_path in file_paths:
        path = Path(raw_path)
        suffix = path.suffix.lower()
        status: dict[str, Any] = {"path": str(path), "status": "skipped", "chunks": 0}

        if suffix not in SUPPORTED_UPLOAD_EXTENSIONS:
            status["error"] = f"Unsupported extension {suffix}"
            statuses.append(status)
            continue

        try:
            docs = _parse_file(path, settings)
            splits = splitter.split_documents(docs)
            filtered_splits = filter_complex_metadata(splits)
            vector_store.add_documents(documents=filtered_splits)
            status["status"] = "ingested"
            status["chunks"] = len(filtered_splits)
        except Exception as exc:
            logger.exception("Failed to ingest uploaded file %s", path)
            status["status"] = "failed"
            status["error"] = str(exc)

        statuses.append(status)

    return statuses
