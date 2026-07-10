# Phase 3 Context: Secure Channel & Form Handling

## Phase Goal
The objective of Phase 3 is to update the secure contact form on the frontend to capture inputs and send them to the backend endpoint `POST /api/transmit`, which will trigger an email transmission to David's personal email using SendGrid.

## Success Criteria
1. **POST `/api/transmit` Endpoint**: Successfully parses transmission log payloads and forwards them to SendGrid client helper.
2. **SendGrid Integration**: Sends structured email containing Name, Frequency (Email), and Transmission Log to David's personal inbox (secured with API keys).
3. **Frontend Contact Form AJAX**: Captures the form inputs in [index.html](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/index.html) and executes an AJAX POST request, handling success/failure states with visual terminal-style response logs.

## Key Decisions & Technical Approach
1. **SendGrid Email Client**: Use the `sendgrid` library in Python to route emails.
2. **Centralized Secure Transmission API Endpoint**: The backend acts as the gateway to prevent exposing API keys to the client.
3. **Visual Terminal Logs**: Update the contact form's status element `div#transmission-log` with boot-scrambler text or status outputs reflecting the network transmission state.

## Constraints & Risks
- **API Key Leakage**: SendGrid API keys must not be hardcoded in the codebase; they will be loaded from a `.env` file (which will be completed in Phase 4, but initialized here).

## Files Affected
- [backend/main.py](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/backend/main.py) — Wire SendGrid mail dispatch helper.
- [index.html](file:///d:/PythonLearn/Monarch%20UI%20Portfolio/index.html) — Wire the contact form submission handler.

## Verification Plan
1. Test POST `/api/transmit` using curl or Postman.
2. Verify console prints incoming transmission and logs SendGrid status codes.
