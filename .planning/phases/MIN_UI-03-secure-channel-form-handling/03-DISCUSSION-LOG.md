# Phase 3 Discussion Log: Secure Channel & Form Handling

## Discussion History

### 2026-07-10 — Email Integration & Form Intercept
- **Topic**: Wiring the email dispatcher securely.
- **Decision**: 
  - We will use `python-dotenv` to load the `SENDGRID_API_KEY` and target emails.
  - If the SendGrid key is missing in the environment, we will gracefully print to console and return a simulated success payload to avoid blocking development/testing when keys are not configured yet.
  - The contact form's default submission behavior must be intercepted (`event.preventDefault()`) to avoid page reloads, allowing visual terminal feedback within the dossier.
