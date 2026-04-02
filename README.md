# Depth AI Council

A multi-agent reasoning system that runs any question through a 4-stage cognitive pipeline: psychological diagnosis → debate routing → parallel persona generation → synthesis.

Live: [depth-chi.vercel.app](https://depth-chi.vercel.app) (frontend) / Render (backend)

---

## Two Modes

### Serious Council

Four advisors with distinct, grounded philosophies respond to your question simultaneously, then a synthesis stage produces a 150-word consensus with concrete action steps.

| Advisor | Lens |
|---------|------|
| **Marcus** | Risk and asymmetry (Taleb, skin in the game) |
| **Alex** | Strategy and leverage (Thiel, zero-to-one thinking) |
| **Maya** | Customer reality (Mom Test, what users actually want) |
| **Turing** | Engineering clarity (Brooks, what to simplify or cut) |

### Roast Council

The same question, different panel: Worried Mom, The Hater, The Conspiracist, The Hype Man. Shorter responses, entirely different energy.

---

## 4-Stage Pipeline

```
User question
     │
     ▼
Stage 1 — Psychological Brief
   Diagnoses the hidden fear behind the surface question.
   Is this Validation Seeking? Fear of Failure? Identity Crisis?
     │
     ▼
Stage 2 — Debate Router
   Decides who speaks first, urgency level (1–10),
   and the core tension the council should argue about.
     │
     ▼
Stage 3 — Parallel Persona Generation
   All 4 advisors run concurrently via ThreadPoolExecutor.
   Each reads from a markdown knowledge base (Taleb, Mom Test,
   Brooks, Thiel/Helmer) before responding.
     │
     ▼
Stage 4 — Synthesis
   A diplomatic summary acknowledging where advisors disagreed,
   extracting what each was right about, and producing 3
   time-bound action steps + 1 named pitfall.
```

---

## Stack

- **Backend**: Flask + Groq (Llama 3.3 70B), deployed on Render
- **Frontend**: Vanilla HTML/CSS/JS, deployed on Vercel
- **Concurrency**: `ThreadPoolExecutor` for parallel LLM calls
- **Knowledge bases**: Markdown files per advisor (strategy, risk, engineering, customer research)

---

## Running Locally

```bash
cd backend
pip install -r requirements.txt

# Create .env
echo "GROQ_API_KEY=your_key" > .env

python app.py
# Backend at http://localhost:5000

# In another terminal, open frontend/index.html directly
# or use: python -m http.server 3000 --directory ../frontend
```

API endpoints:
- `POST /council/debate` — full 4-stage pipeline, returns all stages as JSON
- `POST /api/getResponses` — Roast Council, fast parallel responses
- `GET /health` — API + persona status check

---

## Why It Exists

The original idea was more ambitious: a full council of AI agents each with persistent memory, disagreeing with each other across sessions. That hit API rate limits quickly and the UX was chaotic.

What shipped instead is more focused — one question, one session, four disciplined perspectives, one synthesis. The psychological brief stage is the part that actually changed how it felt to use: instead of getting four opinions on what you asked, you get four opinions on what you *meant* to ask.