# Phase 2 Context: Project Data Decoupling

## Phase Goal
The objective of Phase 2 is to decouple the project data from the frontend and fetch it dynamically from the FastAPI backend endpoint `GET /api/projects`.

## Success Criteria
1. **GET `/api/projects` Endpoint**: Returns valid JSON array of project objects containing `github_url` and `streamlit_dashboard_url`.
2. **Frontend Dynamic Rendering**: [index.html](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/index.html) successfully fetches the projects array on load and renders cards inside the "Case Files" grid, preserving all styling and GSAP hover animations.

## Key Decisions & Technical Approach
1. **Pydantic Model for Projects**: Expose structured project details via Pydantic model.
2. **AJAX Fetch Integration**: Use vanilla browser `fetch()` API in [index.html](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/index.html) script block to make a GET request to `http://127.0.0.1:8000/api/projects`.
3. **Keep Animations**: Ensure newly appended DOM nodes have GSAP event listeners attached or use event delegation so that the cyberpunk visual hover effects work exactly as they did in the static version.

## Constraints & Risks
- **GSAP Animation Binding**: If nodes are dynamically rendered after GSAP initializes, hover animations may fail. We must initialize GSAP hover bounds *after* the fetch-and-render completes.
- **Port/Origin Conflicts**: Ensure CORS remains configured to allow local file or server origins.

## Files Affected
- [backend/main.py](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/backend/main.py) — Verify/add any extra schema properties.
- [index.html](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/index.html) — Rewrite hardcoded grid to draw from fetched array.

## Verification Plan
1. Start FastAPI server.
2. Curl/fetch `http://127.0.0.1:8000/api/projects` and check structure.
3. Open `index.html` in browser, verify case files grid is populated and hover effects are working correctly.
