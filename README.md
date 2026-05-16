<div align="center">

<h1 style="color:#33ff41; margin-bottom:0.25em;">Depth AI Council</h1>
<p style="color:#a1a1aa; margin-top:0;">Retro terminal · four AI personas · UI that talks back</p>

<p>
  <a href="https://depth-chi.vercel.app"><strong style="color:#d946ef;">▶ Live demo</strong></a>
</p>

<!-- Poster loads instantly (~11 KB). Video (~6 MB) only when clicked — no spinner on README load. -->
<a href="https://github.com/user-attachments/assets/fe68a8a8-42df-468a-845d-d45d26a3c447">
 
</a>


</div>

---

## What it is

Click **power**, sit through boot (BIOS → breach → `ROAST_COUNCIL.exe` → four entities), pick a **language** (EN / HI / ML / ZH / KO), ask one question. Four panels answer with typewriter text and a pop-in animation.

Most of the project is **frontend** (`frontend/index.html`, ~2.7k lines): CRT layers, boot script, fake window chrome, `fourthWall` dialogs. Backend: four parallel Groq calls, JSON back.

---

## Boot flow

| Step | What happens |
|------|----------------|
| **Power** | Landing screen → boot window |
| **BIOS** | Green typed lines, security scan |
| **Breach** | Red panic, shake, `MOM.exe` / `HATER.dll` / … |
| **Voice** | *“we saw you click that power button”* |
| **Language** | Keys `1`–`5` (menu on main screen too) |
| **Council** | Input + four persona terminals |

Red / yellow / green window buttons open **snarky alerts**, not a real window manager. **Close** runs a shutdown animation.

---

## Fourth wall

Try on the [live app](https://depth-chi.vercel.app) after boot finishes.

| Try | Result |
|-----|--------|
| Idle ~45s | System alert |
| Paste code / `npm` / `git` | Blocked + dialog |
| Type `ls` + Enter | Same |
| Fast mouse movement | Motion sickness dialog |
| Right-click | Blocked |
| Ctrl+C, F12 | Keyboard / devtools dialogs |

---

## Personas

| Name | Angle |
|------|--------|
| **Worried Mom** | Over-the-top concern |
| **The Hater** | Short, brutal |
| **Conspiracist** | Everything is connected |
| **Hype Man** | Hype regardless of facts |

---

## Stack

| | |
|---|---|
| Frontend | HTML, CSS, JS, Tailwind — **Vercel** |
| Backend | Flask, Groq Llama 3.3 70B — **Render** |
| Also | `POST /council/debate` · serious UI in `frontend/cf/` |

<details>
<summary><b>Run locally</b></summary>

```bash
cd backend && pip install -r requirements.txt
cp .env.example .env   # GROQ_API_KEY
python app.py
```

```bash
python -m http.server 8080   # repo root
```

`frontend/index.html` points at production Render by default; use `http://localhost:5000/api/getResponses` for local API.

</details>

---

<p style="color:#71717a; font-size:0.9em;">
Started as a multi-agent council; rate limits and UX pushed it to a one-shot roast terminal. The UI is the point.
</p>
