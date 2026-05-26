## Project

TrustVoice AI is a voice-enabled agentic RAG assistant for enterprises.

## Goal

Build a hackathon-ready MVP that lets users upload trusted documents, ask questions, receive cited answers, and get a clear “not found in sources” response when evidence is missing.

## MVP Scope

Build:
- PDF/text upload
- Document parsing
- Chunking
- Embeddings
- Vector retrieval
- Grounded answers
- Citations
- Gap detection
- Safe visible agent steps: Plan → Search → Verify → Answer
- Voice input
- Voice output
- Clean demo UI

Do not build yet:
- Full SharePoint integration
- Full Azure Blob integration
- Multi-tenant RBAC
- Admin dashboard
- Complex analytics
- Fine-tuning

## Product Positioning

This is not just a chatbot. It is a trustworthy enterprise knowledge assistant that reduces hallucinations by grounding every answer in user-provided data.

## Demo Flow

1. Upload an enterprise-style PDF.
2. Ask: “What are the key risks mentioned in this document?”
3. Show cited answer.
4. Ask: “What is the 2026 budget?”
5. If not present, say: “I could not find this in the uploaded sources.”
6. Ask a question using voice.
7. Read answer aloud using text-to-speech.

## Engineering Principles

- Prefer minimal, working code.
- Do not rewrite the whole repo.
- Keep changes small and reviewable.
- Prioritize demo reliability.
- Use existing libraries and architecture where possible.
- Run tests or local app after changes.
- Always explain changed files.
