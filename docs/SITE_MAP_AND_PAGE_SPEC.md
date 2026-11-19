# Site Map and Page Specification

## Main navigation

- `/` — Home
- `/about` — About
- `/experience` — Experience
- `/projects` — Projects
- `/writing` — Writing
- `/lab` — Lab & Tools
- `/services` — Services
- `/contact` — Contact
- `/resume` — Resume

Supporting:
- `/projects/[slug]`
- `/writing/[slug]`
- `/lab/[tool]` (optional; tools may also be embedded on `/lab`)
- `/now`
- `/uses`
- `/privacy`

## 1. Home `/`

Purpose: communicate identity and route each audience to useful content.

Sections:
1. Hero with tagline and intro.
2. Primary CTAs: Explore projects, View resume.
3. Compact expertise list.
4. Selected projects.
5. Career snapshot.
6. Latest articles.
7. Developer tools preview.
8. Collaboration CTA.
9. Footer/social links.

Draft hero:
Eyebrow: SOFTWARE ENGINEER · TECHNOLOGY ENTHUSIAST · BUILDER
H1: Turning ideas into useful software.
Body: “I'm a software engineer with 13+ years of experience building enterprise applications, integrations, cloud solutions and automation. I also build independent products and share practical engineering knowledge.”
CTA: Explore projects / View resume.

Mark years of experience as content requiring verification before publication.

## 2. About `/about`

Purpose: human context and professional philosophy.

Sections:
- Introduction.
- Career journey.
- Engineering interests.
- Working approach.
- Current learning/building interests.
- Links to experience, projects and contact.

Keep personal details limited to what the owner chooses to make public.

## 3. Experience `/experience`

Purpose: recruiter-friendly career history.

Display:
- Reverse chronological timeline.
- Employer, client (only where permitted), role, dates.
- Responsibilities and verified outcomes.
- Technology tags.
- Link to relevant public case study if available.

Initial career sequence supplied by owner in prior discussions:
- Cognizant / Cisco Splunk assignment: December 2025–present.
- Cognizant / Verizon: preceding assignment; exact end date must be checked.
- Cognizant / Google India: March 2022–June 2024 (verify).
- Astreya / Google India: November 2015–February 2022 (verify).
- Wipro: December 2012–October 2015 (verify).

Do not hardcode the sequence as final until checked against the current resume. Prefer central data file.

## 4. Projects `/projects`

Purpose: demonstrate applied engineering and product thinking.

Project listing:
- Project title.
- Short problem/solution summary.
- Category.
- Technology tags.
- Status (only if current and accurate).
- Link to case study/demo/repository where public.

Initial candidates:
1. AForApple — independent educational technology product.
2. Cloud integration and observability engineering — sanitised professional case study.
3. Enterprise workflow engineering — sanitised Pega case study.
4. Developer productivity experiments — personal projects, only once a working demo exists.

Each detail page should include:
- Overview.
- Problem.
- Constraints.
- Approach.
- Architecture.
- Key decisions.
- Challenges.
- Outcome (verified, no invented metrics).
- Lessons learned.
- Links/assets.

## 5. Writing `/writing`

Purpose: searchable technical knowledge base.

Features:
- Article list.
- Categories and tags.
- Search/filter if useful.
- Publication/update date.
- Reading time.
- Article detail pages.
- Table of contents for long posts.
- Code syntax highlighting.
- Related articles.
- RSS feed if straightforward.

Suggested categories:
Splunk, Cloud, Python, Go, Pega, APIs, DevOps, Testing, Observability, Engineering.

## 6. Lab `/lab`

Purpose: useful browser-based utilities and technical experiments.

Initial tools:
- JSON formatter/validator.
- Base64 encode/decode.
- Cron expression helper.
Optional next:
- Regex tester.
- JWT inspector (decode locally; do not claim signature verification).
- API response viewer using sample/local input.

Every tool:
- Explain what it does.
- Include sample input.
- Provide clear validation/errors.
- Have copy/reset controls where appropriate.
- Process user input locally in the browser.
- Never transmit entered secrets/tokens/content to a server.
- Include a privacy note.

## 7. Services `/services`

Purpose: communicate potential collaboration areas without pretending to be a large agency.

Possible service areas:
- Custom web application development.
- API and system integration.
- Cloud integration engineering.
- Internal tools and dashboards.
- Workflow automation.
- Technical mentoring/training.

Each service should explain the problem it solves, likely deliverables and how to enquire. Only publish services the owner is comfortable accepting.

## 8. Contact `/contact`

Include:
- Public professional email (configurable; verify before launch).
- LinkedIn.
- GitHub.
- Optional contact form only after a real provider/backend is configured.
- Clear expected enquiry types.

Do not publish personal phone number by default. Never display fake form success.

## 9. Resume `/resume`

- Short introduction.
- Resume PDF download.
- Optional HTML summary.
- Last updated date.
- Link to LinkedIn.

Use a configurable asset path. Never assume a stale resume is current.

## 10. Now `/now`

Optional lightweight page:
- What I'm working on.
- What I'm learning.
- What I'm building.
- Professional interests.

Owner updates manually, perhaps monthly.

## 11. Uses `/uses`

Optional list of development setup, tools, editors and services the owner actually uses. Do not invent hardware/software details.

## 12. Privacy `/privacy`

Explain:
- Whether analytics are used.
- Whether contact form submissions are stored.
- Whether browser tools process data locally.
- Any third-party embeds/services.
Keep accurate to the actual implementation.
