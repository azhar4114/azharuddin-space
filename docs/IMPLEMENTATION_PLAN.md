# Implementation Plan — azharuddin.space

## Guiding approach

Build in vertical slices. Deploy a useful professional site early, then add the technical hub features. Do not spend the first week building an elaborate design system without shipping pages.

## Phase 0 — Repository and decisions

Tasks:
- Inspect repository.
- Initialise Astro + TypeScript.
- Add Tailwind.
- Add formatting/lint/type-check scripts.
- Add README and docs.
- Establish theme tokens and base layout.

Acceptance:
- Project installs cleanly.
- Local dev server starts.
- Production build succeeds.
- No unnecessary backend/database dependencies.

## Phase 1 — Foundation and homepage

Tasks:
- Header and responsive navigation.
- Footer.
- Base layout and SEO component.
- Homepage hero.
- Expertise summary.
- Featured project cards.
- Career snapshot.
- Latest writing preview.
- Contact CTA.

Acceptance:
- Looks polished at 360px, 768px and 1440px.
- All navigation links work.
- Resume and social links use configurable placeholders until verified.
- No console errors.
- Build passes.

## Phase 2 — Professional portfolio

Tasks:
- About page.
- Experience timeline.
- Skills grouping.
- Projects listing.
- Project detail template.
- Resume page and PDF asset placeholder.

Acceptance:
- Career data is centralised.
- Unverified dates/details are marked and not represented as confirmed.
- Project case studies have consistent structure.
- Professional and independent projects are distinguishable.

## Phase 3 — Technical knowledge hub

Tasks:
- Writing listing.
- Article template.
- Tags/categories.
- Markdown code highlighting.
- RSS if straightforward.
- Add initial article drafts.

Acceptance:
- Articles have metadata and readable typography.
- Code blocks are accessible and horizontally scrollable on small screens.
- Draft articles do not appear publicly unless explicitly published.

## Phase 4 — Developer lab

Tasks:
- JSON formatter/validator.
- Base64 encode/decode.
- Cron expression helper.
- Sample inputs, copy/reset and validation states.
- Privacy note for each tool.

Acceptance:
- Tools work without server requests.
- Errors are handled.
- Keyboard operation works.
- No data is sent to external services.

## Phase 5 — Services and contact

Tasks:
- Services page.
- Contact page.
- Configure public email and social links.
- Optional contact provider only if owner chooses one.

Acceptance:
- No fake form submission.
- Services reflect capabilities the owner is willing to offer.
- Contact route works and has spam/privacy considerations if form is used.

## Phase 6 — SEO, QA and launch

Tasks:
- Sitemap and robots.
- Open Graph metadata.
- Structured data.
- Favicon and social preview.
- Analytics (optional, privacy-conscious).
- Link audit.
- Mobile and accessibility audit.
- Lighthouse checks.
- Deployment preview and custom domain.

Acceptance:
- Production build passes.
- No broken internal links.
- All images have appropriate alt handling.
- Focus states and keyboard navigation work.
- No horizontal overflow at target viewport sizes.
- HTTPS works on custom domain.
- Existing DNS/email records are not accidentally removed.

## Suggested first milestone

For the first coding-agent session, implement only:
1. Astro project foundation.
2. Theme tokens.
3. Header/footer.
4. Responsive homepage.
5. About page.
6. Experience page shell.
7. Projects listing shell.
8. README and local run instructions.

Have the agent stop and report before expanding into every feature. Review the design and content before proceeding.

## Definition of done for each page

- Responsive.
- Semantic and accessible.
- Correct title/description.
- No dead controls.
- No fabricated claims.
- No console/build errors.
- Content is editable without changing shared layout components.
