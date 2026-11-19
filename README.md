# azharuddin.space

Personal technology hub for Mohammad Azharuddin — Lead Integration Architect, Pega CSSA, and Software Engineer since December 2012.

**Live site:** https://azharuddin.space

---

## Local Development

**Requirements:** Node.js ≥ 18 (Tested on Node 20)

```bash
# Install dependencies
npm install

# Start local development server (http://localhost:4321)
npm run dev

# Run production build (18 static routes)
npm run build

# Preview production build locally
npm run preview
```

---

## Verified Professional Credentials

All personal and professional information has been cross-checked and verified against official LinkedIn profiles (`Profile.pdf`) and employment records:

- **Identity & Contact:** Verified public email (`azhar4114@gmail.com`), LinkedIn (`https://www.linkedin.com/in/azhar4114/`), and GitHub (`https://github.com/azhar4114`).
- **Tenure:** Continuous enterprise software engineering experience since **December 2012** across Cognizant, Astreya (Google account), and Wipro Technologies.
- **Observability & Integrations:** Splunk (AWS Technology Add-ons, SPL query optimization, log analytics), RESTful microservices, and Python data pipelines.
- **Pega Platform:** Certified Senior System Architect (CSSA), Certified System Architect (CSA), and LSA candidate.
- **Education:** B.E. in Electrical, Electronics and Communications Engineering from Osmania University (2008 – 2012, First Class with Distinction).
- **Executive Resume PDF:** Modern one-page executive resume generated at [`public/resume/Mohammad_Azharuddin_Resume.pdf`](public/resume/Mohammad_Azharuddin_Resume.pdf).

---

## Projects & Case Studies (Content Collections)

Managed in [`src/content/projects/`](src/content/projects/):
- `ai-crm.mdx` — Full-stack AI CRM platform (FastAPI, React, TypeScript, Gemini/OpenAI integration, openpyxl ingestion)
- `aforapple.mdx` — Interactive educational web application (`aforapple.fun`) & companion Android app
- `agla-owner.mdx` — Serverless property discovery architecture prototype (`aowner.in`) on GitHub Pages + Google Apps Script
- `enterprise-workflow-engineering.mdx` — Pega Platform 8.8.3, case lifecycles, queue processors & guardrails
- `chrome-extensions-automation.mdx` — Google India internal automation suite (CSAT, Netco, search & time tracking)
- `cloud-integration-engineering.mdx` — Google Drive APIs, GCP Cloud Storage syncing & BigQuery analytics

---

## Technical Writing

Managed in [`src/content/writing/`](src/content/writing/):
- `practical-browser-extensions-enterprise.mdx` — Chrome Extensions architecture, content script sandboxing & client-side caching
- `reliable-api-retry-mechanisms.mdx` — Idempotency, exponential backoff with jitter, and observability
- `event-driven-integration-patterns.mdx` — Cloud service event streams, DLQs, and resilience

---

## Deployment to Cloudflare Pages

1. Push this repository to your GitHub account (`azhar4114/azharuddin-space`).
2. In [Cloudflare Pages](https://pages.cloudflare.com), select **Create a project** → **Connect to Git**.
3. Choose the `azharuddin-space` repository.
4. Framework preset: **Astro**.
5. Build command: `npm run build`
6. Output directory: `dist`
7. Click **Save and Deploy**.
8. Assign the custom domain `azharuddin.space` in Cloudflare Pages dashboard after verifying existing DNS records.
