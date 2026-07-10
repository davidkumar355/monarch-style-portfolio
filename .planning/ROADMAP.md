# Roadmap: Monarch Intelligence Network (Full-Stack Transition)

## Overview

Transitioning the static cinematic dossier portfolio into a production-ready, three-tier full-stack application by connecting a FastAPI backend with the HTML/CSS/JS frontend.

## Phases

- [x] **Phase 1: Backend Scaffolding & CORS** - Initialize Python environment, FastAPI boilerplate, CORS middleware, and routing structure. (completed 2026-07-10)
- [x] **Phase 2: Project Data Decoupling** - Implement schema/JSON project store, GET `/api/projects` endpoint, and update index.html to fetch projects. (completed 2026-07-10)
- [x] **Phase 3: Secure Channel & Form Handling** - Upgrade the contact form inputs, write POST `/api/transmit` endpoint, and integrate SMTP/SendGrid email routing. (completed 2026-07-10)
- [x] **Phase 4: Configurations & Security** - Centralize links in config, set up `.env` instructions, secure credentials, and finalize system. (completed 2026-07-10)

## Phase Details

### Phase 1: Backend Scaffolding & CORS

**Goal**: Establish the Python backend execution environment and basic middleware.
**Depends on**: Nothing
**Success Criteria**:

  1. FastAPI server boots locally and exposes a Swagger UI.
  2. CORS middleware is configured to accept requests from the frontend file/origin.

**Plans**: 2/2 plans complete

Plans:

- [x] 01-01-PLAN.md
- [x] 01-02-PLAN.md
- [x] 01-01: Scaffold FastAPI environment, virtualenv, and install requirements.
- [x] 01-02: Create `main.py` with CORS and core router mappings.

### Phase 2: Project Data Decoupling

**Goal**: Remove hardcoded projects from frontend and populate them dynamically via GET API.
**Depends on**: Phase 1
**Success Criteria**:

  1. GET `/api/projects` returns valid JSON matching the ML project details.
  2. Frontend parses JSON and renders cards in Case Files grid dynamically.

**Plans**: 2/2 plans complete

Plans:

- [x] 02-01-PLAN.md
- [x] 02-02-PLAN.md

- [x] 02-01: Implement project schemas and GET `/api/projects` in backend.
- [x] 02-02: Implement fetch logic in index.html to dynamically render project cards.

### Phase 3: Secure Channel & Form Handling

**Goal**: Route transmission form logs from dossier straight to David's email inbox.
**Depends on**: Phase 2
**Success Criteria**:

  1. POST `/api/transmit` parses Name, Frequency (Email), and Transmission Log.
  2. Form submissions trigger email dispatch to David's personal email via SMTP/SendGrid.

**Plans**: 2/2 plans complete

Plans:

- [x] 03-01-PLAN.md
- [x] 03-02-PLAN.md

- [x] 03-01: Implement POST `/api/transmit` endpoint and mail dispatcher logic in backend.
- [x] 03-02: Update contact form element, GSAP submit handling, and AJAX submission.

### Phase 4: Configurations & Security

**Goal**: Secure credentials and extract static social links to configuration.
**Depends on**: Phase 3
**Success Criteria**:

  1. Sensitive variables (emails, API keys) are loaded from `.env` on the backend.
  2. Frontend links use a centralized JS configuration object.

**Plans**: 1/1 plans complete

Plans:

- [x] 04-01-PLAN.md

- [x] 04-01: Extract link settings, implement `.env` config guides, and finalize build.

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Backend Scaffolding & CORS | 2/2 | Complete   | 2026-07-10 |
| 2. Project Data Decoupling | 2/2 | Complete   | 2026-07-10 |
| 3. Secure Channel & Form Handling | 2/2 | Complete   | 2026-07-10 |
| 4. Configurations & Security | 1/1 | Complete   | 2026-07-10 |
