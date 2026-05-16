# Behaviour & performance

## Response times (`POST /api/getResponses`)

| Scenario | Result |
|----------|--------|
| Valid question | 200 OK, ~3–5s (4 parallel Groq calls) |
| Empty string | 400 Bad Request |
| > 1000 characters | 400 Bad Request |
| XSS attempt in input | 200 OK — HTML escaped at render (`textContent`) |
| One persona fails | Per-persona fallback |
| All rate-limited | Mix of fallbacks, no 500 |

## Tokens

Groq free tier: **100k tokens/day**. With `max_tokens=150` per persona × 4, expect on the order of **~125–165 questions/day** depending on prompts (roughly **600–800 tokens** per round-trip).

## Startup checks

`validate_startup()` before bind: `GROQ_API_KEY`, live ping, 4 personas from `persona.json`, port available — else exit 1.

## Security (short)

- 1000 char server-side cap  
- No `innerHTML` for user content on the roast UI path  
- Stateless — no DB  
