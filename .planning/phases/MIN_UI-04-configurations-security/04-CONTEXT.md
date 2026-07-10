# Phase 4 Context: Configurations & Security

## Phase Goal
The objective of Phase 4 is to secure the API keys and email credentials on the backend using a `.env` file (with `.env.example` placeholder template), extract static social links on the frontend to a centralized configuration block, and verify that the `.env` file is excluded from version control via `.gitignore`.

## Success Criteria
1. **`.env` Configuration**: Backend loads SendGrid credentials dynamically from environment variables, never hardcoded.
2. **`.gitignore` Integration**: `.env` file is added to the git ignore list.
3. **Frontend Links Configuration**: Centralize social media links (LinkedIn, Instagram, GitHub) into a javascript config block in [index.html](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/index.html) so they can be managed in one place.

## Key Decisions & Technical Approach
1. **Use dotenv**: Use `python-dotenv` on backend startup to read variables.
2. **`.env.example` Creation**: Document placeholders so David can copy it to `.env` locally.
3. **JS Global Config Object**: Define a `const CONFIG = { github: "...", linkedin: "...", instagram: "..." }` block at the top of the `<script>` tag in [index.html](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/index.html), and populate links dynamically in the footer.

## Constraints & Risks
- **Credential Leakage**: Double-check that `.env` is ignored by git status before committing.

## Files Affected
- [backend/main.py](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/backend/main.py) — Confirm `load_dotenv()` call is active.
- [index.html](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/index.html) — Add centralized Javascript CONFIG block and wire links dynamically.
- [backend/.env.example](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/backend/.env.example) — [NEW] Create placeholder env template.
- [.gitignore](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/.gitignore) — [NEW] Add `.env` to ensure it is ignored.

## Verification Plan
1. Check `git status` to verify `.env` is untracked/ignored.
2. Run backend to verify it compiles and loads variables correctly.
3. Open `index.html`, verify that footers/links redirect to correct URL references dynamically.
