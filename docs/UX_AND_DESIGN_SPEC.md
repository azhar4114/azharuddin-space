# UX and Design Specification — azharuddin.space

## 1. Design concept

A modern engineering workspace with a professional editorial layer.

The site should feel:
- Technical, but not intimidating.
- Minimal, but not empty.
- Confident, but not boastful.
- Personal, but not overly casual.
- Dark, but highly readable.

Avoid:
- Hacker/Matrix clichés.
- Neon overload.
- Terminal text as the main content format.
- Excessive gradients, glassmorphism or glow.
- Overuse of cards, pills and badges.
- Stock photos of anonymous developers at laptops.
- Large decorative animations.

## 2. Colour tokens

Use CSS variables so the theme can be tuned centrally.

| Token | Suggested value | Use |
|---|---|---|
| `--color-bg` | `#10141D` | Main page background |
| `--color-surface` | `#171E2B` | Cards and panels |
| `--color-surface-raised` | `#1D2736` | Hover/raised surfaces |
| `--color-border` | `#2B3748` | Dividers and borders |
| `--color-text` | `#F4F7FC` | Main text |
| `--color-muted` | `#A6B2C2` | Secondary text |
| `--color-subtle` | `#78879A` | Metadata |
| `--color-accent` | `#75B8FF` | Links and primary accent |
| `--color-accent-hover` | `#9ACBFF` | Hover accent |
| `--color-success` | `#70C99A` | Optional availability/status |
| `--color-warning` | `#E7BD72` | Warnings |

Do not rely on colour alone to communicate status.

## 3. Typography

Recommended:
- Headings/body: Inter or Manrope.
- Code, labels and technical metadata: JetBrains Mono.

Guidelines:
- Body text should be comfortable to read (roughly 16–18px desktop).
- Body line height around 1.6–1.75.
- Article line length around 65–80 characters.
- Use a clear type scale; avoid too many sizes.
- Use monospace sparingly for tags, command snippets, dates and technical labels.

Use system fallbacks and avoid blocking page rendering while fonts load.

## 4. Layout and spacing

- Content max width: approximately 1120–1200px.
- Article reading width: approximately 720–780px.
- Main horizontal gutters: 24px desktop, 16–20px mobile.
- Use a consistent spacing scale based on 4px or 8px increments.
- Sections should have generous vertical separation.
- Use subtle 1px borders and restrained corner radii.
- Cards should be used for project/article/tool groupings, not every text block.

## 5. Header and navigation

Desktop:
- Brand mark/name on left.
- Navigation links on right.
- Resume CTA can be a visually distinct link/button.
- Header may be sticky if it does not consume excessive viewport space.

Mobile:
- Compact brand.
- Accessible menu button.
- Menu closes after navigation.
- Correct focus management and Escape-key support.
- No horizontal overflow.

Main nav:
Home, About, Experience, Projects, Writing, Lab, Services, Contact.
Resume can be a prominent CTA rather than a primary nav item.

## 6. Homepage hierarchy

1. Header.
2. Hero:
   - Small eyebrow: SOFTWARE ENGINEER · TECHNOLOGY ENTHUSIAST · BUILDER.
   - H1: “Turning ideas into useful software.”
   - 2–3 sentence introduction.
   - Primary CTA: Explore projects.
   - Secondary CTA: View resume.
   - Optional social links.
3. Technology/discipline summary.
4. Selected projects (3 or 4).
5. Career snapshot.
6. Latest writing (3 articles).
7. Lab/tools preview.
8. Collaboration/services CTA.
9. Footer.

Do not make the hero overly tall. On common laptop screens, the main proposition and at least one CTA should be visible without excessive scrolling.

## 7. Components

Build reusable components:
- `SiteHeader`
- `MobileNavigation`
- `SiteFooter`
- `SectionHeading`
- `ButtonLink`
- `SocialLinks`
- `ProjectCard`
- `ArticleCard`
- `ToolCard`
- `ExperienceTimeline`
- `SkillGroup`
- `TagList`
- `CallToAction`
- `CodeBlock`
- `Breadcrumbs`
- `TableOfContents` (for longer articles)

Use semantic HTML. Do not create custom controls when a native element is sufficient.

## 8. Interaction and motion

- Subtle hover/focus transitions (roughly 150–220ms).
- Visible keyboard focus rings.
- Buttons and links have clear hover states.
- Respect `prefers-reduced-motion`.
- No autoplay video/audio.
- No cursor-following effects or scroll-jacking.
- Avoid animation libraries unless needed.

## 9. Responsive behaviour

Test at minimum:
- 360px mobile.
- 390px mobile.
- 768px tablet.
- 1024px laptop.
- 1440px desktop.

Rules:
- Mobile-first layout.
- Cards stack naturally.
- Project imagery maintains aspect ratio.
- Navigation remains usable by keyboard and touch.
- Code blocks can scroll horizontally without breaking page width.
- Tables have a mobile fallback.
- No fixed-width elements that cause overflow.

## 10. Images and visual assets

Do not use generic stock imagery merely to fill space.

Prefer:
- Custom project screenshots supplied by the owner.
- Recreated/sanitised architecture diagrams.
- CSS shapes or abstract technical motifs.
- Small diagrams and illustrations that explain a real concept.

Until real assets are provided, create attractive text-first layouts and neutral placeholders that are easy to replace.

All meaningful images need useful alt text. Decorative images should have empty alt text.

## 11. Accessibility

Target WCAG 2.2 AA where practical:
- Semantic headings in correct order.
- Keyboard-accessible navigation and tools.
- Sufficient contrast.
- Labels and error messages for inputs.
- No colour-only status indicators.
- Reduced-motion support.
- Accessible name for icon-only controls.
- Focus not obscured by sticky headers.
- Skip-to-content link.

## 12. Brand details

Brand text: `AZHARUDDIN` or `azharuddin.space`.
Optional compact monogram: `A.`.
Primary tagline: “Turning ideas into useful software.”
Tone: clear, thoughtful, technically informed, grounded and approachable.
