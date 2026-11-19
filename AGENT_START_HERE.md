# Coding Agent Instructions — azharuddin.space

You are the senior product designer, frontend architect and implementation engineer for **azharuddin.space**, a personal technology hub for Mohammad Azharuddin.

## Your task

Build a polished, production-ready first version of the website from the specifications in this repository. The website must serve three audiences:

1. Recruiters and hiring managers evaluating professional experience.
2. Developers and technology enthusiasts exploring engineering work and technical writing.
3. Potential clients evaluating independent software development and consulting capabilities.

The visual direction is a **dark developer aesthetic with professional minimalism**. The result should feel like a thoughtful engineer's digital workspace: polished, restrained, credible, fast and easy to navigate. Do not make it look like a generic agency template, gaming dashboard or terminal-only theme.

## Mandatory first steps

Before coding:

1. Read every file in `docs/`.
2. Inspect the existing repository and preserve useful existing work.
3. Summarise the implementation approach, identify any genuine blockers, and propose a short task sequence.
4. Do not ask questions for details that can safely remain configurable or be represented as clearly marked content placeholders.
5. Do not invent personal facts, employment dates, metrics, client achievements, testimonials, contact details, or external profile URLs.

## Technical direction

Use:
- Astro with TypeScript
- Tailwind CSS (use the current stable version and its recommended Astro integration)
- Astro Content Collections for projects and articles
- Markdown/MDX for editorial content
- Lucide icons or a consistent lightweight icon set
- Mermaid or SVG for architecture diagrams where useful
- Static-first deployment suitable for Cloudflare Pages

Use the current stable compatible package versions at implementation time. Avoid unnecessary dependencies. Prefer Astro components and native browser APIs. Add Preact or another island framework only if a real interactive feature requires it.

Do not add a backend or database for version 1. Contact should use a configurable email link or a clearly documented provider integration placeholder; do not create a fake working form.

## Build order

Follow `docs/IMPLEMENTATION_PLAN.md`. At minimum, deliver:
- Shared layout, header, footer, theme tokens and responsive navigation.
- Home, About, Experience, Projects, Writing, Lab, Services, Contact and Resume routes.
- Reusable project and article cards.
- Data-driven experience and skills.
- Three initial project case-study entries, with careful placeholder/sanitised descriptions.
- Two starter technical articles or clearly labelled draft articles.
- At least three working client-side utilities: JSON formatter/validator, Base64 encoder/decoder and cron expression helper (the cron helper may explain expressions rather than calculate next-run times if no reliable library is used).
- SEO metadata, sitemap, robots.txt, Open Graph defaults and accessible semantics.
- A README with local development, build, deployment and content-editing instructions.

## Design requirements

Follow `docs/UX_AND_DESIGN_SPEC.md` closely:
- Deep navy background, slate surfaces, off-white text and restrained blue accent.
- Strong typography hierarchy; use a clean sans-serif plus monospace for code/metadata.
- Comfortable line lengths and generous whitespace.
- Responsive mobile-first layouts.
- Subtle transitions only; respect `prefers-reduced-motion`.
- Clear visible focus states and keyboard navigation.
- No decorative animation that harms performance or readability.
- Avoid emoji as interface icons.

## Content requirements

Use `docs/CONTENT_AND_PERSONAL_BRAND.md` and `docs/SITE_MAP_AND_PAGE_SPEC.md`.

Use this positioning as a starting point:
“Turning ideas into useful software.”

The homepage should communicate that Azharuddin is an experienced software engineer who works across enterprise software, integrations, cloud engineering and automation, and also builds independent products and shares practical knowledge.

Where facts need verification, use a central editable data file and/or explicit `TODO: VERIFY` markers. Never silently publish guessed details.

## Quality bar

- No broken links, dead buttons or fake functionality.
- All navigation and CTAs must work.
- All pages must have meaningful titles and descriptions.
- All interactive tools must work locally in the browser and must not upload user-entered content.
- Validate user input and handle errors gracefully.
- Ensure mobile layout at narrow widths.
- Run lint/type checks/build where configured and fix errors.
- Provide a concise final report: implemented routes, components, tools, commands run, build status, deployment steps and remaining content placeholders.

## Do not do these things

- Do not add fabricated testimonials, client logos, endorsements or ratings.
- Do not claim availability for work unless represented by a configurable flag.
- Do not publish private phone numbers or personal information by default.
- Do not expose employer/client confidential information.
- Do not build a login system, admin dashboard, database, AI chatbot or paid subscription flow in v1.
- Do not use stock imagery just to fill empty space. Prefer typography, CSS, diagrams and genuine project screenshots supplied later.
- Do not make every section a card. Use cards only where they improve grouping.

Start by reading the specifications, then implement the foundation and homepage before expanding to the remaining routes.
