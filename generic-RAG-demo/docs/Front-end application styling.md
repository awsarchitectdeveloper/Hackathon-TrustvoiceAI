
# Chainlit Front-end Customization Guide

## 1. Custom Logo and Favicon

You can personalize the Chainlit application to reflect your organization’s branding by adding a custom logo, favicon, and login page background.

###  Logo and Favicon

Chainlit supports both **light** and **dark** modes. To ensure your logo displays correctly in both themes:

- Prepare two logo files:
  - `logo_light.png` (for light mode)
  - `logo_dark.png` (for dark mode)
- Place these files in a folder named `/public` next to your application.

Once you restart the application, Chainlit will automatically use the appropriate logo based on the selected theme.

> **Note**: Browsers often cache assets like logos and favicons. You may need to clear your browser cache to see the updated images.

###  Favicon

To update the favicon:

- Add a file named `favicon` (e.g., `favicon.ico` or `favicon.png`) to the `/public` folder.
- Restart the application to apply the new favicon.

###  Login Page Background

If authentication is enabled, you can customize the background image of the login page:

1. Open the `.chainlit/config.toml` file.
2. Add or modify the following section:

```toml
[UI]
# Custom login page image, relative to public directory or external URL
login_page_image = "/public/custom-background.jpg"

# Optional: Add filters using Tailwind CSS (no dark/light variants)
# login_page_image_filter = "brightness-50 grayscale"
# login_page_image_dark_filter = "contrast-200 blur-sm"
```

## 2. Change Colours
...

## 3. Dutch Translation
...


## 3. Replace the default logo with TrustVoice AI

If you still see a Sogeti/Capgemini logo in the center of the chat screen, Chainlit is loading the existing logo assets from `public/`.

Do the following:

1. Prepare your TrustVoice AI logo images:
   - `logo_light.png` for light theme
   - `logo_dark.png` for dark theme
2. Replace these files in `public/`:
   - `public/logo_light.png`
   - `public/logo_dark.png`
3. (Optional) Replace `public/favicon.png` with a TrustVoice AI favicon.
4. Fully restart Chainlit.
5. Hard-refresh the browser (`Ctrl+Shift+R`) or clear cache.

> Chainlit uses these filenames automatically; no Python code change is required when file names stay the same.
