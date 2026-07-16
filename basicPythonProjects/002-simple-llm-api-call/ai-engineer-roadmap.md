# AI Engineer Roadmap — Faried
Last updated: July 16, 2026

## Current Level Summary
Faried is a D3 Informatics graduate with a background in JavaScript (React, Node, Express — practically strong, but built without solid fundamentals) and C (completed Quary Notetaker, a CLI notetaker project). He just **completed** a Contact Book CLI project in Python (OOP) — full CRUD (add/search/edit/delete) with JSON persistence, committed and pushed to GitHub. Through that project he worked through composition vs. inheritance, reference vs. copy semantics (and how it differs from C's memory model), `@classmethod` vs. calling a constructor directly, and several real bugs he found and fixed himself with light guidance (`json.load` vs `loads`, data being overwritten because `__init__` didn't load existing file data, a discarded return value from `from_dict()`). He self-identified his biggest challenge as class/data structure design, not debugging, and named "think through design more, go step by step" as his own takeaway. He has no hands-on experience yet with HTTP APIs or calling LLMs programmatically — that's the immediate next step. He has strong parallel infrastructure exposure (Docker in WSL2, n8n running locally) and strong theoretical/business context (target market, content strategy, automation use cases) that is ahead of his current hands-on AI-engineering skill.

## Confirmed Strengths
- Strong self-awareness about learning gaps (explicitly identified the "jump to trending tools before fundamentals" pattern and corrected course)
- Solid systems/CLI fundamentals from C (Quary Notetaker completed end-to-end)
- Can now reason correctly about composition vs. inheritance and reference vs. copy semantics when pushed to think it through (initially guessed inheritance, corrected with a concrete analogy)
- Willing to push back on suggested patterns rather than accept them at face value (e.g. correctly challenged whether `from_dict()` was actually necessary for a single call site, and got it right)
- Working Docker + n8n + WSL2 environment already set up
- Clear, mature articulation of long-term goals: the target is becoming an AI engineer able to design/build/evaluate/scale AI systems for businesses of increasing complexity — UMKM automation is the first market entry point, not the ceiling

## Active Gaps
- No practical experience with HTTP requests, calling external APIs, or parsing JSON from a live API response (vs. local file JSON, which he's now solid on)
- No experience yet with prompt engineering or working with LLM responses programmatically
- Class/data structure design is still the shakiest part of OOP for him — needs more practice reasoning through relationships *before* writing code, not just once corrected

## Recently Completed
- **Gemini Interactions API (konsep, July 16)** — eksplorasi endpoint `/v1beta/interactions` vs `generateContent`; paham struktur request/response (`steps`, `model_output`), multi-turn via `previous_interaction_id`. **Next: baca docs resmi dulu sebelum implementasi ke kode.**
- **Contact Book (Python, OOP) — finished, pushed to GitHub.** Full CRUD + JSON persistence.
- Quary Notetaker (CLI notetaker in C)
- Learning Journal Mentor, Software Engineering Mentor, AI Engineering Mentor, Systems & Network Programming Mentor custom Claude skills
- Clarified long-term journey framing: Software Engineer → AI Engineer → Build AI Applications → Build AI Products → Build AI Automation Business → serve increasingly complex problems (UMKM = first market, not the ceiling)

## Recommended Next Concepts
1. **HTTP requests & JSON handling from a live API (no AI yet)** — reason: isolate "how do requests/responses work over the network" as its own small skill (using `requests`) before adding an LLM into the mix. He already has solid local JSON handling from Contact Book, so this mainly adds the network/HTTP layer.
2. **API keys & environment variables** — reason: needed before any real API key touches his code, and a good habit to build now rather than after a key leaks somewhere.
3. **Free-tier LLM API call (Gemini)** — reason: first real AI-engineering step, once the above are solid; low-stakes since it's free, and reinforces the same request/response/JSON pattern he'll need for n8n and future paid APIs.
4. **Deliberate design-first practice** — reason: he named this himself as his weak point and his own intended fix; future projects should start with an explicit "sketch the classes and their relationships" step before any code, rather than defaulting straight to implementation.

## Project Ideas (progressively harder)
1. ~~Contact Book~~ — **done.**
2. **AI Caption/Hook Generator (Gemini free tier)** — CLI tool that takes a topic, calls Gemini API, returns generated captions/hooks for @LowLevelLabs / @devEyeCandy content. Current active next project: teaches env vars for API keys, HTTP requests, JSON parsing from a real API, and prompt construction — directly useful for his content business, reasonable stretch from current level. In progress: currently at the "what do I even need (requests library, HTTP basics)" planning stage, not yet coding.
3. **(Future) Small RAG or agent-style project** — once basic API calls and prompt engineering are comfortable, a natural next stretch toward the "AI Applications" layer of his long-term roadmap.

## Long-Term Journey Framing (for context, not a to-do)
Software Engineer → AI Engineer → Build AI Applications → Build AI Products → Build AI Automation Business → serve increasingly complex problems. UMKM automation is the first market/entry point, not the end goal — the actual target is becoming an AI engineer capable of designing, building, evaluating, and scaling AI systems for businesses of increasing size and complexity.
