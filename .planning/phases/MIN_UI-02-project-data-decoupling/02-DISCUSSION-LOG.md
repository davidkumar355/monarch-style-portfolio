# Phase 2 Discussion Log: Project Data Decoupling

## Discussion History

### 2026-07-10 — Decoupling Strategy & Animation Safety
- **Topic**: How to fetch and insert project elements without breaking GSAP.
- **Decision**: 
  - We will extract the static HTML structure of a single project card.
  - In [index.html](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/index.html), we will replace the hardcoded cards with an empty container `<div id="projects-container"></div>`.
  - On page load (or after the boot sequence), we fetch the projects array.
  - Iterate and compile cards, then insert them.
  - Re-run GSAP scroll triggers or hover event bindings *after* the DOM elements are inserted.
  - Verify that the layout remains responsive and fits David's case-file dossier aesthetic.
