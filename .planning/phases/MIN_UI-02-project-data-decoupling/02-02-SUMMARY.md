---
phase: MIN_UI-02-project-data-decoupling
plan: 02
subsystem: ui
tags: [javascript, html, gsap]
requires:
  - phase: MIN_UI-02-project-data-decoupling
    provides: Updated GET /api/projects schema and return payload containing 5 complete project dossiers
provides:
  - "Dynamic case file rendering driven by backend fetch API"
  - "Interactive dossier modal buttons linking directly to project dashboard and repository"
affects:
  - MIN_UI-03-secure-channel-form-handling
tech-stack:
  added: []
  patterns: [Client-side AJAX fetching, DOM template compiling]
key-files:
  created: []
  modified: [index.html]
key-decisions:
  - "Executed fetch immediately on DOMContentLoaded in parallel with boot sequence to avoid visual delay"
patterns-established: []
requirements-completed: [02-02]
coverage:
  - id: D4
    description: "index.html fetches and renders case dossiers from /api/projects"
    requirement: "02-02"
    verification:
      - kind: other
        ref: "grep -q 'loadProjects' index.html"
        status: pass
    human_judgment: false
duration: 4 min
completed: 2026-07-10
status: complete
---

# Phase 2 Plan 2: Implement fetch logic in index.html Summary

**Dynamic client-side fetching and rendering in index.html from GET /api/projects**

## Performance

- **Duration:** 4 min
- **Started:** 2026-07-10T10:53:00Z
- **Completed:** 2026-07-10T10:57:00Z
- **Tasks:** 1
- **Files modified:** 1

## Accomplishments
- Replaced hardcoded dossier cards with an empty projects-container.
- Added loadProjects() AJAX handler fetching from backend.
- Structured project templates matching previous design exactly.
- Added dynamic click links to modal repository and Streamlit buttons.

## Task Commits

1. **Task 1: Replace hardcoded project cards with dynamic container and fetch request** - `012e806` (feat)

## Files Created/Modified
- `index.html` - Integrated loader client and modal handlers.

## Decisions Made
- Executed projects loader in parallel with boot sequence to hide network latency.

## Deviations from Plan
None - plan executed exactly as written.

## Issues Encountered
None

## User Setup Required
None

## Next Phase Readiness
- Frontend is dynamically consuming project data.

---
*Phase: MIN_UI-02-project-data-decoupling*
*Completed: 2026-07-10*
