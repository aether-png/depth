# Embed `demo.mp4` in the README (GitHub only)

GitHub **does not** play `<video src="demo.mp4">` from your repo — it strips that tag.  
It **does** play videos hosted on `githubusercontent.com` / `user-attachments` after you upload through the web editor.

## Steps (~2 minutes)

1. Open **[Edit README](https://github.com/alokjgeorge5/depth/edit/main/README.md)** on GitHub (pencil icon).
2. **Drag `demo.mp4`** from your project folder into the editor (or use “Attach files…” at the bottom).
3. GitHub inserts a URL like one of these:
   - `https://github.com/user-attachments/assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
   - `https://user-images.githubusercontent.com/.../demo.mp4`
4. **Copy that URL.**
5. In `README.md`, find the `<video>` tag and replace `REPLACE_ME` in:
   ```html
   <video src="https://github.com/user-attachments/assets/REPLACE_ME" width="80%" controls loop muted playsinline></video>
   ```
   with your full URL (keep `width`, `controls`, `loop`).
6. **Delete** the auto-inserted markdown line GitHub added (duplicate) if you only want one player.
7. Commit on GitHub or pull locally and push.

## Centered player (Reddit / Bobby Hadz pattern)

```html
<p align="center" width="100%">
  <video src="YOUR_URL_HERE" width="80%" controls loop muted playsinline></video>
</p>
```

- **`controls`** — required; users click play (autoplay is blocked anyway).
- **`loop`** — replays the 8s clip.
- **`width="80%"`** — scales on mobile.

## Why `demo.mp4` in the repo still exists

The file in git is your source copy (~6 MB). The README player uses GitHub’s CDN URL from the upload step above.

Reference: [Bobby Hadz — embed video in GitHub README](https://bobbyhadz.com/blog/embed-video-into-github-readme-markdown)
