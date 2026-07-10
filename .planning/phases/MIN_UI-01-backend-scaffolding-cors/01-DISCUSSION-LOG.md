# Phase 01: Backend Scaffolding & CORS - Discussion Log

**Date:** 2026-07-10
**Phase:** 1 (Backend Scaffolding & CORS)

## Discussion Points & Decisions

### 1. Python Environment Setup
- **Options Considered**: Global python install, custom conda venv, local python venv.
- **Decision**: Set up a local Python virtual environment (`venv`) using the `d:/python/python.exe` binary.
- **Rationale**: Keeps dependencies isolated and uses David's exact Python binary location.

### 2. Routing Structure
- **Options Considered**: Modular routers from day one vs. single-file main.py setup.
- **Decision**: Start with a single `backend/main.py` file containing placeholder schemas and mock data for Phase 1.
- **Rationale**: Minimizes code complexity and makes it easier to verify CORS issues and routing connectivity first.

### 3. CORS Origins Policy
- **Options Considered**: Allow only localhost port domains vs. allow all origins (`*`).
- **Decision**: Allow wildcard (`*`) origins for development.
- **Rationale**: Ensures the frontend can access the backend whether opened as a local `file://` or hosted via Live Server or dynamic ports.

### 4. Environment Variables
- **Options Considered**: Place in `backend/` folder vs. at project root.
- **Decision**: Put the `.env` configuration file at the project root for unified workspace loading.
- **Rationale**: Easy to access and configure across all components.

---

*Log of decisions finalized on 2026-07-10*
