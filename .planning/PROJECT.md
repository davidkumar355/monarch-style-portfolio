# Monarch Intelligence Network

## What This Is

The Monarch Intelligence Network is a three-tier full-stack web application designed as a declassified intelligence-dossier-themed portfolio for David, a Data Science student transitioning from graphic design. It bridges a cinematic, highly interactive frontend (HTML, Tailwind CSS, GSAP) with a robust Python backend (FastAPI) to demonstrate cross-disciplinary expertise.

## Core Value

Provide a seamless, production-ready full-stack portfolio that demonstrates the ability to handle both creative, high-fidelity UI design and secure, structured backend engineering.

## Requirements

### Validated

- ✓ Cinematic boot sequence, clearance access state, and TV-static overlays.
- ✓ Baseline single-page HTML layout with profile, case files, capabilities, and contact form.

### Active

- [ ] Scaffold FastAPI Python backend with modular routing (`/api/projects` and `/api/transmit`).
- [ ] Implement CORS middleware to allow index.html to communicate with the local FastAPI server.
- [ ] Decouple project data into backend schema/JSON store, adding `github_url` and `streamlit_dashboard_url`.
- [ ] Build GET `/api/projects` endpoint and update index.html to fetch and render case files dynamically.
- [ ] Update frontend contact form to capture Name, Frequency (Email), and Transmission Log (Message).
- [ ] Implement POST `/api/transmit` endpoint on the backend with SMTP/SendGrid integration for inbox routing.
- [ ] Extract social links to a centralized configuration block in the frontend.
- [ ] Add `.env` configuration guide for securing API keys, mail credentials, and routing URLs.

### Out of Scope

- Production deployment setup (Docker, AWS) — Currently focusing on local developer setup, dependencies, and code structure.

## Context

- Frontend: [index.html](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/index.html) (Tailwind CDN, GSAP animations, HTML5 Canvas).
- Backend: Python (FastAPI, Uvicorn, Pydantic, python-dotenv).

## Constraints

- Do not alter the aesthetic or GSAP animations in the frontend.
- Strict separation of project endpoints and communication endpoints.
- Avoid hardcoded credentials or links in components.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| FastAPI Backend | High performance, automatic Swagger documentation, and easy Python ML integration. | — Pending |
| SMTP/SendGrid | Simplicity in setting up instant notification routing to David's personal inbox. | — Pending |

---
*Last updated: 2026-07-10 after Initialization*
