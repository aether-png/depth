# Depth AI Council

> **Multi-Agent Deliberation System** — Get perspectives from AI-powered personas that debate your ideas through a structured cognitive pipeline.

![Status](https://img.shields.io/badge/Status-Proof%20of%20Concept-blue)
![Python](https://img.shields.io/badge/Python-3.11-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🧠 Architecture Overview

Depth AI Council implements a **4-Stage Hybrid Cognitive Pipeline** that orchestrates multi-persona deliberation using parallel LLM invocations. The system performs **real-time psychological analysis** to route user queries through specialized AI agents (Marcus, Alex, Maya, Turing), leveraging a `ThreadPoolExecutor` for concurrent response generation. A final **synthesis stage** reconciles divergent perspectives into actionable consensus.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        HYBRID COGNITIVE PIPELINE                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌──────────────────┐     ┌──────────────────┐     ┌───────────────┐  │
│   │  STAGE 1         │     │  STAGE 2         │     │  STAGE 3      │  │
│   │  Psychological   │────▶│  Debate Router   │────▶│  Parallel     │  │
│   │  Brief (Gemini)  │     │  (Groq)          │     │  Personas     │  │
│   └──────────────────┘     └──────────────────┘     └───────────────┘  │
│                                                             │          │
│                            ┌────────────────────────────────┘          │
│                            ▼                                           │
│                     ┌──────────────────┐                               │
│                     │  STAGE 4         │                               │
│                     │  Synthesis       │                               │
│                     │  (Consensus)     │                               │
│                     └──────────────────┘                               │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| **Multi-Agent Orchestration** | 4 distinct AI personas with domain-specific knowledge bases |
| **Psychological Routing** | Diagnoses hidden intent to optimize persona selection |
| **Concurrent Execution** | ThreadPoolExecutor enables parallel LLM calls (sub-3s latency) |
| **Knowledge Ingestion** | Markdown-based KB files enrich persona responses |
| **Graceful Degradation** | Fallback responses ensure system resilience |

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/depth-ai-council.git
cd depth-ai-council

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp backend/.env.example backend/.env
# Add your GROQ_API_KEY to .env

# Run the server
python backend/app.py
```

The server starts at `http://localhost:5000`

---

## 📁 Project Structure

```
depth-ai-council/
├── backend/
│   ├── app.py              # Flask API + Cognitive Pipeline
│   ├── personas.py         # Persona management & loader
│   ├── persona.json        # Persona definitions
│   ├── kb_strategy.md      # Knowledge base: Strategic frameworks
│   ├── kb_engineering.md   # Knowledge base: Engineering principles
│   ├── kb_risk.md          # Knowledge base: Risk assessment
│   └── kb_mom_test.md      # Knowledge base: Customer research
├── frontend/
│   └── index.html          # Interactive UI (single-file app)
├── requirements.txt
└── README.md
```

---

## 🛠 API Reference

### POST `/council/debate`
Execute the full 4-stage cognitive pipeline.

**Request:**
```json
{
  "question": "Should I pivot my SaaS to a new market?"
}
```

**Response:**
```json
{
  "success": true,
  "pipeline_stages": {
    "psychological_brief": { ... },
    "debate_parameters": { ... }
  },
  "debate": [
    { "speaker": "Marcus", "message": "..." },
    { "speaker": "Alex", "message": "..." }
  ],
  "synthesis": "The Council has reached a difficult consensus..."
}
```

### GET `/health`
System health check with API connectivity status.

---

## 📋 Planned v2.0 Features

- [ ] **PostgreSQL State Persistence** — Migrate from in-memory storage to durable conversation history
- [ ] **Docker Containerization** — Production-ready deployment with `docker-compose`
- [ ] **Rate Limiting Middleware** — Flask-Limiter integration for API protection
- [ ] **WebSocket Streaming** — Real-time response streaming for improved UX
- [ ] **Persona Studio** — Web-based UI for custom persona creation
- [ ] **Observability Suite** — OpenTelemetry integration for pipeline tracing
- [ ] **Multi-LLM Arbitrage** — Intelligent routing between Groq, OpenAI, and Anthropic

---

## 🔧 Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Flask 2.3 + Gunicorn |
| LLM Provider | Groq (Llama 3.3 70B) |
| Concurrency | Python ThreadPoolExecutor |
| Frontend | Vanilla HTML/CSS/JS |
| Deployment | Render / Vercel Edge |

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center">
  <em>Built with 🧠 for those who debate with themselves</em>
</p>