# Depth AI Council

**[Live demo →](https://depth-chi.vercel.app)**

A retro terminal in the browser: fake boot, four AI personas, and a UI that reacts when you use it wrong. Vanilla HTML/CSS/JS on the front; Flask + Groq on the back.

<p align="center">
  <video src="https://github.com/user-attachments/assets/fe68a8a8-42df-468a-845d-d45d26a3c447"
    width="720"
    controls
    loop
    muted
    playsinline
    style="max-width: 100%; border-radius: 8px;">
  </video>
</p>

---

## What it is

You click **power**, sit through a scripted boot (BIOS → breach → `ROAST_COUNCIL.exe` → four “entities”), pick a **language** (EN / HI / ML / ZH / KO), then ask one question. Four panels answer at once with typewriter text and a pop-in animation.

Most of the work is **frontend** (~2.7k lines in `frontend/index.html`): CRT layers, boot sequence, fake window buttons, 4th-wall dialogs. The backend runs four Groq calls in parallel and returns JSON.

---

## Boot flow

1. **Power** — landing screen, then boot window  
2. **BIOS** — green typed lines, security scan  
3. **Breach** — red panic, screen shake, entity list (`MOM.exe`, `HATER.dll`, …)  
4. **Hacker lines** — e.g. *“we saw you click that power button”*  
5. **Language** — keys `1`–`5` in the terminal (also a menu on the main screen)  
6. **Council** — input + four persona terminals  

**Traffic lights** (red / yellow / green) on boot and main windows: they don’t really minimize — they open snarky system alerts. **Close** on the council runs a shutdown animation.

---

## Fourth wall (try on the live site)

After boot finishes, `fourthWall` watches input. Random Win95-style dialogs, no API.

| Try | Result |
|-----|--------|
| Idle ~45s | System alert |
| Paste code / `npm` / `git` | Blocked + security dialog |
| Type `ls` etc. and Enter | Same |
| Fast mouse movement | Motion sickness dialog |
| Right-click | Context menu blocked |
| Ctrl+C, F12 | Keyboard / devtools dialogs |
| Resize window a lot | Window anxiety dialog |

---

## Personas

| | Name | Angle |
|---|------|--------|
| | Worried Mom | Over-the-top concern |
| | The Hater | Short, brutal |
| | Conspiracist | Everything is connected |
| | Hype Man | Hype regardless of facts |

---

## Stack

| | |
|---|---|
| Frontend | HTML, CSS, JS, Tailwind CDN — Vercel |
| Backend | Flask, Groq `llama-3.3-70b-versatile` — Render |
| Pattern | `ThreadPoolExecutor`, timeouts, per-persona fallbacks |

Also in repo: `POST /council/debate` (heavier 4-stage pipeline) and `frontend/cf/depth-ai-council-final.html` for the older serious UI.

---

## Run locally

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env   # GROQ_API_KEY
python app.py
```

```bash
python -m http.server 8080   # from repo root
```

Open http://localhost:8080/ — redirects to the app.  
`frontend/index.html` uses the production Render URL by default; for local API use `http://localhost:5000/api/getResponses` in the `fetch` call.

---

## Background

Started as a multi-agent “council” with long conversations. Hit Groq rate limits and four-wall-of-text UX. Narrowed to one-shot roasts; kept the elaborate terminal UI because that’s what makes the project interesting.
