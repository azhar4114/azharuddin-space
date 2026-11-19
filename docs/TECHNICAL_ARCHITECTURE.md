# Technical Architecture — azharuddin.space

## 1. Recommended stack

### Core
- Astro (current stable compatible release)
- TypeScript
- Tailwind CSS (current stable compatible release)
- Astro Content Collections
- Markdown/MDX

### UI
- Astro components for layout and content.
- Native HTML/CSS/JavaScript for simple utilities.
- Add Preact only if a component genuinely benefits from a client-side framework.
- Lucide icons or another consistent lightweight icon package.

### Content/data
- Markdown/MDX for articles and case studies.
- Typed local data for experience, skills, navigation and social links.
- No database in v1.

### Hosting and delivery
- Cloudflare Pages or equivalent static hosting.
- GitHub repository.
- GitHub Actions or hosting-native Git integration for build/deploy.
- Custom domain `azharuddin.space` configured after DNS access is available.

### Quality
- TypeScript checks.
- ESLint if useful.
- Prettier.
- Lighthouse/PageSpeed checks.
- Link checking.
- Automated build in CI.

## 2. Architecture principles

- Static-first and SEO-friendly.
- Minimal JavaScript shipped to browser.
- Content stored in version control.
- Reusable layouts/components.
- Centralised theme tokens.
- No secrets in frontend code.
- No backend until required.
- All browser tools operate locally.

## 3. Suggested folder structure

```text
azharuddin-space/
├── public/
│   ├── favicon.svg
│   ├── images/
│   ├── resume/
│   └── og/
├── src/
│   ├── components/
│   ├── layouts/
│   ├── content/
│   │   ├── projects/
│   │   └── writing/
│   ├── data/
│   │   ├── experience.ts
│   │   ├── skills.ts
│   │   ├── navigation.ts
│   │   └── site.ts
│   ├── pages/
│   ├── styles/
│   └── utils/
├── docs/
├── astro.config.mjs
├── package.json
├── tsconfig.json
└── README.md
```

## 4. Content schemas

### Project
Suggested fields:
- `title`: string
- `description`: short summary
- `slug`: generated or filename
- `category`: independent | professional-case-study | experiment
- `status`: published | in-progress | archived
- `featured`: boolean
- `technologies`: string[]
- `coverImage`: optional path
- `demoUrl`: optional URL
- `repositoryUrl`: optional URL
- `publishedAt`: optional date
- `updatedAt`: optional date
- `confidentialityNote`: internal authoring field; never render publicly

Project body sections:
- Overview
- Problem
- Constraints
- Approach
- Architecture
- Engineering decisions
- Challenges
- Outcome
- Lessons learned

### Article
Suggested fields:
- `title`
- `description`
- `pubDate`
- `updatedDate`
- `tags`
- `category`
- `draft`
- `heroImage` (optional)
- `readingTime` (derived if practical)

### Experience
Suggested fields:
- `employer`
- `client` (optional; only if public)
- `role`
- `startDate`
- `endDate` (null for current)
- `summary`
- `highlights`
- `technologies`
- `visibility` (public/private)
- `verified` (authoring-only flag)

Do not render entries marked private or unverified.

## 5. Site configuration

Create a single site configuration module for:
- Site title.
- Site URL.
- Owner name.
- Tagline.
- Default description.
- Public email.
- LinkedIn URL.
- GitHub URL.
- Resume asset path.
- Availability badge visibility.
- Social image.
- Analytics configuration.

Use explicit placeholder values where details are not confirmed. Do not guess.

## 6. Browser tools

All tools should run entirely in the browser.

### JSON formatter
- Input textarea.
- Format action.
- Validate action.
- Clear and copy actions.
- Show parse errors clearly.
- Never send content to an API.

### Base64
- Encode/decode text using browser-supported APIs where appropriate.
- Handle Unicode correctly (UTF-8).
- Show invalid input errors.
- Do not transmit data.

### Cron helper
- Accept a cron expression.
- Explain fields and common examples.
- If next-run calculation is implemented, use a maintained, tested library and document timezone assumptions.
- Do not pretend a simplified parser fully validates every cron dialect.

### Future JWT inspector
- Decode header and payload locally.
- Explicitly state that decoding does not verify signature or trustworthiness.
- Never send tokens to a server.

## 7. SEO

- Unique title and description per route.
- Canonical URL.
- XML sitemap.
- robots.txt.
- Open Graph and Twitter/X card metadata.
- Structured data where accurate:
  - Person
  - WebSite
  - Article
  - SoftwareApplication for tools if appropriate
- Semantic HTML and descriptive link text.
- Human-readable slugs.
- Avoid duplicate content.
- Add noindex to drafts and internal pages as appropriate.

## 8. Performance

Targets:
- Keep pages static wherever possible.
- Minimise client-side JavaScript.
- Optimise images and use modern formats.
- Lazy-load below-the-fold images.
- Avoid large animation libraries.
- Avoid layout shifts; specify image dimensions/aspect ratios.
- Use font-display swap or system fallbacks.
- Test mobile network performance.

Use Lighthouse as a diagnostic tool; do not claim a score without measuring it.

## 9. Security and privacy

- No credentials, API keys or tokens in repository or browser bundle.
- Do not add analytics that collect unnecessary personal information.
- Contact form must not claim to submit unless a provider is actually configured.
- Browser utilities must not transmit user-entered data.
- Use safe rendering for user-provided text.
- Add external link `rel` protections when opening new tabs.
- Keep dependencies limited and updated.
- Do not embed third-party widgets without understanding their privacy implications.

## 10. Deployment

Initial deployment:
1. Push repository to GitHub.
2. Connect repository to Cloudflare Pages.
3. Set build command based on generated Astro project (commonly `npm run build`).
4. Set output directory to `dist`.
5. Deploy preview branch.
6. Test preview.
7. Configure custom domain and DNS for `azharuddin.space`.
8. Verify HTTPS, canonical URL, sitemap and social metadata.

Do not change DNS until the owner has access to the domain registrar and understands existing DNS records. Preserve existing email-related DNS records.

## 11. Maintainability

- Keep content separate from layout.
- Use typed data.
- Avoid duplicated markup.
- Document how to add projects and articles.
- Keep dependencies small.
- Ensure the site can be built locally with documented commands.
