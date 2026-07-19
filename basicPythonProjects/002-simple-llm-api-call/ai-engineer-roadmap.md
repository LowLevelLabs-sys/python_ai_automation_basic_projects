# AI Engineer Roadmap — Faried
Last updated: July 19, 2026

## Current Level Summary
Faried is a D3 Informatics graduate with a background in JavaScript (React, Node, Express — practically strong, but built without solid fundamentals) and C (completed Quary Notetaker, a CLI notetaker project). He has completed a Contact Book CLI (Python OOP, full CRUD + JSON persistence) and has now finished the Simple LLM API Call project — a working Gemini API chat script with multi-turn conversation memory and persistent session ID across restarts. Through these two projects he has worked through: composition vs. inheritance, reference vs. copy semantics, `@classmethod`, real bug fixing (wrong dict key, SSE response format, `stream: true` leftover), HTTP requests with `requests`, environment variables with `python-dotenv`, live API JSON parsing, class design and refactoring, and recognizing when *not* to abstract. Class/data structure design is no longer the biggest gap — it's improving steadily. The remaining frontier is prompt engineering and building applications on top of the API layer he now understands.

## Confirmed Strengths
- Strong self-awareness about learning gaps (explicitly identified the "jump to trending tools before fundamentals" pattern and corrected course)
- Solid systems/CLI fundamentals from C (Quary Notetaker completed end-to-end)
- Can now reason correctly about composition vs. inheritance and reference vs. copy semantics when pushed to think it through
- Willing to push back on suggested patterns rather than accept them at face value (e.g. correctly challenged whether `from_dict()` was actually necessary for a single call site, and got it right)
- **HTTP requests with `requests`** — can independently build headers, body, and POST requests to a live API
- **Environment variables** — stores and loads API keys via `.env` + `python-dotenv`; understands why this matters (GitHub secret block experienced firsthand)
- **Live API JSON parsing** — can navigate nested JSON responses from a real API (e.g. `response["steps"][1]["content"][0]["text"]`)
- **Refactoring instinct** — recognized that `set_id()` was adding unnecessary indirection and removed it without being prompted; used readability as a valid technical reason
- Working Docker + n8n + WSL2 environment already set up
- Clear, mature articulation of long-term goals: the target is becoming an AI engineer able to design/build/evaluate/scale AI systems for businesses of increasing complexity — UMKM automation is the first market entry point, not the ceiling

## Active Gaps
- **Prompt engineering** — no hands-on experience yet shaping model behavior through system instructions, few-shot examples, or output formatting
- **Streaming responses (SSE)** — understands that `stream: true` changes the response format to Server-Sent Events, but hasn't studied or implemented it yet
- **Class/data structure design** — improving, but still benefits from deliberate design-first practice before coding (explicitly identified by himself as his own weak point)

## Recently Completed
- **Simple LLM API Call (Python, July 16–19)** — working Gemini chat script built across three sessions. v1: basic POST request to `/v1/interactions`, env vars, `.gitignore`, parsing `steps[]` array. v2: refactored into a `Gemini` class with multi-turn memory via `previous_interaction_id`. v3: persisted `previous_interaction_id` to a JSON file so conversation history survives restarts; removed `set_id()` method in favor of readable inline assignment.
- **Contact Book (Python, OOP) — finished, pushed to GitHub.** Full CRUD + JSON persistence.
- Quary Notetaker (CLI notetaker in C)
- Learning Journal Mentor, Software Engineering Mentor, AI Engineering Mentor, Systems & Network Programming Mentor custom Claude skills
- Clarified long-term journey framing: Software Engineer → AI Engineer → Build AI Applications → Build AI Products → Build AI Automation Business → serve increasingly complex problems (UMKM = first market, not the ceiling)

## Recommended Next Concepts
1. **Prompt engineering** — system instructions, output formatting, few-shot examples. The API layer is solid now; it's time to learn how to actually shape model behavior through the prompt. Directly useful for the Caption/Hook Generator project.
2. **SSE / streaming responses** — `stream: true` was encountered and intentionally deferred; worth studying when ready to build more responsive UIs or CLI experiences.
3. **Deliberate design-first practice** — future projects should still start with an explicit sketch of classes and relationships before any code; improving but not fully habitual yet.
4. **Error handling & resilience** — `response.raise_for_status()` is in place, but no retry logic, rate limit handling, or user-friendly error messages yet. Worth adding as projects grow.

## Project Ideas (progressively harder)
1. ~~Contact Book~~ — **done.**
2. ~~Simple LLM API Call~~ — **done.** Foundation for all future LLM projects.
3. **`003-caption-hook-generator` (next)** — a clean, dedicated CLI tool that takes a topic/niche as input, sends it to Gemini with a system instruction that makes it behave as a content script generator, and returns formatted captions/hooks for @LowLevelLabs / @devEyeCandy. New project (not an extension of 002) — teaches prompt engineering, system instructions, and output formatting in a focused scope. Directly useful for his content business.
4. **(Future) Small RAG or agent-style project** — once basic API calls and prompt engineering are comfortable, a natural next stretch toward the "AI Applications" layer of his long-term roadmap.

## Long-Term Journey Framing (for context, not a to-do)
Software Engineer → AI Engineer → Build AI Applications → Build AI Products → Build AI Automation Business → serve increasingly complex problems. UMKM automation is the first market/entry point, not the end goal — the actual target is becoming an AI engineer capable of designing, building, evaluating, and scaling AI systems for businesses of increasing size and complexity.
