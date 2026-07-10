# Phase 4 Discussion Log: Configurations & Security

## Discussion History

### 2026-07-10 — Security Hardening & Centralized Configuration
- **Topic**: Restricting keys exposure and centralizing links.
- **Decision**: 
  - We will put the `.env` file inside the `backend/` directory or root directory. Having a `.env.example` in both or the root is common. Let's create `backend/.env.example` to guide the setup.
  - On the frontend, we will extract all the hardcoded social links (like GitHub, Instagram, LinkedIn) into a global CONFIG object. This makes updating links simple for the user without diving deep into HTML structures.
