# Phase 01: Backend Scaffolding & CORS - Context

**Gathered:** 2026-07-10
**Status:** Ready for planning

<domain>
## Phase Boundary

Set up the Python execution environment (virtualenv), install core dependencies (FastAPI, Uvicorn, Pydantic, python-dotenv), create `main.py` with CORS middleware configured for development origins, and structure the basic project/transmission endpoints.

</domain>

<decisions>
## Implementation Decisions

### Environment and Virtualenv
- **D-01:** Create a Python virtual environment (`venv`) using the user-specified Python executable at `d:/python/python.exe`.
- **D-02:** Track and install backend package dependencies via `requirements.txt` containing `fastapi`, `uvicorn`, `pydantic`, `python-dotenv`, and `sendgrid`.

### Backend Routing and Structure
- **D-03:** Use a single `main.py` file placed inside a `backend/` directory for Phase 1 to establish the API structure, with router endpoints for `/api/projects` and `/api/transmit`.
- **D-04:** Organize code so it is easily refactorable into dedicated routers (e.g., `projects.py`, `transmit.py`) in future phases.

### CORS Configuration
- **D-05:** Configure FastAPI's `CORSMiddleware` with `allow_origins=["*"]` to enable requests from any local file origin (`file://`) or local dev server address (e.g. `localhost:5500`, `localhost:3000`).

### the agent's Discretion
- Port configuration (default to port 8000).
- Basic router schema fields for placeholder data models.

</decisions>

<specifics>
## Specific Ideas

- Basic endpoints must return simple JSON matching the expected project data structure and message payload.

</specifics>

<canonical_refs>
## Canonical References

- `.planning/PROJECT.md` — Active scope definition, tech stack constraints.
- `.planning/ROADMAP.md` — Phase list, success criteria, plan structure.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- [index.html](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/index.html) — Contains the frontend structure, Tailwind, and GSAP. Needs to make AJAX fetch requests in later phases.

### established Patterns
- Single page app with local browser rendering.

### Integration Points
- Frontend will call `http://127.0.0.1:8000/api/projects` and `http://127.0.0.1:8000/api/transmit`.

</code_context>

<deferred>
## Deferred Ideas

- Integration of SendGrid / SMTP email dispatchers — Deferred to Phase 3.
- Fetch request integration inside index.html script block — Deferred to Phase 2.

</deferred>

---

*Phase: 01-backend-scaffolding-cors*
*Context gathered: 2026-07-10*
