# Design

## Source of truth

Status: Active. Updated: 2026-09-23.

Surfaces: the existing CV at `/`, a portfolio overview, and seven project pages.
Confirmed requirements: separate project URLs under `/portfolio/projects/{project-name}`; visual continuity with the CV; hiring managers for senior AI/data leadership roles as the primary audience, future collaborators as secondary; both CV and portfolio unindexed. Research and responsible-AI judgement remain useful supporting evidence. James identifies AI.M.E. as the strongest research example and confirms its methodology may be discussed publicly.

The shared layout, content collection, overview and seven project pages are implemented. The site is published through GitHub Pages at `jameswolman.dev`. This document governs that implementation and records editorial gaps.

Evidence reviewed:

- Original `index.html`, preserved in Git history and the local migration snapshot: existing content, theme tokens, terminal shell, responsive rules, scripts and indexing metadata. Current source is `src/components/CvContent.astro`, `src/layouts/TerminalLayout.astro`, `src/styles/global.css` and `src/scripts/`.
- `public/fonts/`, `public/vendor/goatcounter/count.js`, both validators in `scripts/`, `tests/fixtures/cv_baseline.json`, `.github/workflows/validate.yml`, `public/CNAME`, `public/.nojekyll`, `public/robots.txt` and `.gitignore`.
- Original CV context and requirements in `.omx/context/cv-terminal-site-20260521T071034Z.md` and `.omx/plans/`; the historical desktop screenshot in `.omx/artifacts/thought-leadership/baseline-desktop.png`. That image is a visual reference, not a fresh browser check.
- James's project descriptions and subsequent clarification, retained privately in `.omx/context/portfolio-20260912T223044Z.md`.
- Project screenshots supplied by James in `screenshots/projects/`, with maintained copies in `src/assets/projects/` named by the stable project slugs below.
- James's description and supplied screenshot for Assassin's Creed Timeline, added on 23 September 2026. The copy uses that description and the visible atlas controls; the live site could not be retrieved during this update.
- Where Was I? implementation reviewed in `/Users/jameswolman/PycharmProjects/page-sage`: `backend/main.py`, `src/pagesage/core/`, `src/pagesage/rag/`, `config.yml`, `frontend/src/App.js`, the retrieval/summary regression tests and associated architecture/optimisation documentation. The case study describes narrative query decomposition, diversity-aware selection, page filters, token-budgeted summarisation, cached work, configurable embedding providers and device authentication without sign-up. The single-pass summary path is optional; documentation-only performance figures and absolute spoiler guarantees are excluded. Private evidence and the page-index caveat are recorded in `.omx/artifacts/portfolio/where-was-i-source-review.md`.
- [Astro collections](https://docs.astro.build/en/guides/content-collections/), [routing](https://docs.astro.build/en/guides/routing/), [layouts](https://docs.astro.build/en/basics/astro-pages/) and [GitHub Pages deployment](https://docs.astro.build/en/guides/deploy/github/).
- [James's published AI.M.E. methodology](https://braidr.ai/blog/braidrs-ai-maturity-evaluation-index-showing-our-workings/) and [Braidr's campaign](https://braidr.ai/ai-maturity-evaluation-index-ftse350/).
- [Google's noindex guidance](https://developers.google.com/search/docs/crawling-indexing/block-indexing).

At intake, no design contract, component library or browser-test suite existed. James has now supplied one screenshot for each of the seven projects. The portfolio overview uses these previews alongside its typography; the AI.M.E. case study also includes an explanatory diagram. Several supplied project URLs failed initial browser retrieval; their content remains based on James's descriptions and existing CV unless a source is identified below.

## Brand

Retain the CV's thoughtful, technical and personal character: terminal chrome, monospace type, restrained cyan/amber/purple accents and light/dark themes.

Trust comes from precise contributions, real examples, linked sources, appropriately qualified results and clear collaborator credit. Use ordinary navigation and readable prose. Avoid simulated terminal input, stock AI imagery, unsupported scientific claims and promotional exaggeration.

## Product goals

- Help a hiring reviewer quickly understand what James investigated or built, what he personally contributed, how he led the work where applicable, and what evidence supports the outcome.
- Offer enough technical depth for a reviewer to inspect methods, significant decisions and limitations.
- Give prospective collaborators concrete examples of interests and ways of working.
- Make each project independently shareable in an application or conversation.
- Keep the CV and portfolio unindexed, as explicitly requested.

First-release non-goals: a wider CV redesign or rewrite, a blog, filtering/search for the project list, a CMS, a backend, accounts, live metric polling, or embedded replicas of the project applications. Publishing changes to production is a separate implementation step.

Success signals: all seven projects are reachable from the overview; a detail page identifies purpose and contribution before its technical narrative; evidence links work; the CV's appearance and existing behaviour survive the migration; all generated pages carry the indexing directive.

## Personas and jobs

Primary: hiring managers considering James for senior AI/data leadership roles, as confirmed in his latest audience selection. Foreground programme ownership, technical decisions, collaboration and delivery; retain depth in research methods and responsible-AI judgement for specialist reviewers. Support both a short first read and deeper examination. Do not infer a specific employer's assessment rubric.

Secondary: potential project partners examining relevant methods, outputs and collaboration experience. Contact links should lead to the existing email and LinkedIn destinations.

Visitors may arrive directly on a project page, including on mobile, without first seeing the CV.

## Information architecture

| Route | Role |
| --- | --- |
| `/` | Existing CV with a visible Portfolio link |
| `/portfolio/` | Short introduction, prominent AI.M.E. entry, six further project entries and contact links |
| `/portfolio/projects/{slug}` | A complete, independently readable project case study |

Use persistent CV/Portfolio navigation, an active-page indication, and a breadcrumb from each project to the overview. Keep project titles and commands understandable as standard links. The terminal window title can reflect `~/cv`, `~/portfolio`, or the current project.

Project inventory and stable slugs:

| Project | Slug | Context | Source |
| --- | --- | --- | --- |
| AI.M.E. | `aime` | Professional, Braidr | https://aime.braidr.ai/ftse350 |
| Where Was I? | `where-was-i` | Personal | https://wherewasi.co.uk |
| Upstream | `upstream` | Professional, Braidr and Fieldcraft Studios | https://good.braidr.ai/upstream |
| Declassified Reclassified | `declassified-reclassified` | Personal research and writing | https://gist.github.com/datawranglerai/562e5abacc232ef9c540dfde913e211c |
| Talk Data to Me | `talk-data-to-me` | Gemma 3n Impact Challenge entry | https://www.kaggle.com/competitions/google-gemma-3n-hackathon/writeups/talk-data-to-me |
| Self-hosting n8n on Google Cloud Run | `self-host-n8n-on-gcr` | Open-source guide | https://github.com/datawranglerai/self-host-n8n-on-gcr |
| Assassin's Creed Timeline | `assassins-creed-timeline` | Personal | https://assassinscreed.fyi/ |

Overview: one expanded AI.M.E. entry followed by six project entries using the CV's existing list and divider vocabulary. Each entry has a title, short purpose statement, context/contribution metadata and a link to the case study. Place one supplied screenshot beneath each summary, preserve its full proportions, and use a subtle border consistent with the terminal styling. Each preview links to its case study. Preserve the established order, with Assassin's Creed Timeline appended as the seventh project.

Project hierarchy:

1. Title, short purpose statement, role/team credit, dates/status when known, and relevant external links.
2. A concise summary of the problem, contribution and supported outcome.
3. The research question or practical problem and its constraints.
4. Method, important decisions, and an architecture diagram or example where useful.
5. Evaluation, results and supporting evidence that actually exist.
6. Limitations, lessons and current work, with completed and ongoing work distinguished.
7. Back to portfolio, next project, and contact links.

This is a shared structure with optional sections. A maintained deployment guide and a journalistic analysis should retain their own purposes and evidence types. Missing evidence is a drafting gap, not a reason to invent a benchmark or show an empty section.

AI.M.E. is the first template example. Attribute programme leadership, evaluation methodology and research design to James; credit the small engineering team. Explain the coordinator, pillar specialists with isolated contexts, assessor council and 180+ criteria. An annotated finding/source/confidence example would demonstrate auditability. The published methodology also describes deterministic calculation and evidence-constrained reporting; these can support a deeper methods section with attribution.

AI.M.E. is in production, with completed and published FTSE AIM 100 and FTSE 350 assessments. James continues to lead and maintain the research agent system, which runs on demand for other use cases. Use “In production” for the project's overall status and identify each published study separately in the narrative.

Keep study metrics attached to the correct cohort and date. James supplied AIM 100 figures of 100 companies in two weeks at about $1–$2 per company. The parent/subsidiary representativeness test has been designed; no findings from it have been supplied.

## Design principles

- Put purpose, individual contribution and evidence high on each page.
- Layer detail through headings and an optional contents list; keep essential content visible.
- Reuse existing visual tokens and list patterns across the CV and portfolio.
- Make ordinary links and browser navigation sufficient for the complete reading experience.
- Use real project artifacts and explanatory diagrams only when they improve understanding.
- Keep claims proportional to evidence. Traceability, confidence ratings and measured validity are distinct concepts.

## Visual language

Reuse the current CSS custom properties. Dark palette anchors: background `#0f111a`, text `#d8dee9`, cyan `#8be9fd`, amber `#ffcb6b`, purple `#c792ea`. Light mode uses the existing warm background and darker accent counterparts.

Use JetBrains Mono for body text and metadata, and the existing Big Blue Terminal treatment for display headings. Maintain the current body line height of 1.65 and existing type hierarchy. Long research explanations need generous paragraph spacing.

Start with the existing 820px shell width, 22px terminal radius, subtle dividers, window chrome, scanlines and vignette. Let diagrams fit the available content width; adapt their layout before widening the entire reading surface. Reuse the existing spacing rhythm rather than introducing an unrelated card system.

Retain the CV's existing animation and reduced-motion behaviour. Project reading should not wait for typing animations. Screenshots retain their genuine colours; diagrams use shared theme tokens with readable labels and text equivalents.

## Components

Reusable pieces in `src/components/` and `src/layouts/`:

- Base layout: head metadata, noindex directive, fonts, theme bootstrap, analytics and root asset paths.
- Terminal shell: window title/chrome and accessible persistent theme control.
- Site navigation: CV and Portfolio links with an active state.
- Project entry: featured and standard variants sharing the same content fields, with an optional screenshot beneath the summary on the overview.
- Case-study layout: heading/summary, role and status metadata, optional contents, article body and footer navigation.
- Where Was I? includes the supplied Product Hunt follow badge beneath its opening paragraph. Use Product Hunt's official light/dark images, selected by the existing site theme, at 250 × 54px with responsive sizing, a subtle theme-token outline and visible keyboard focus. Preserve the supplied destination and click tracking; no extra client script is needed.
- Evidence figure: image or code-native diagram, descriptive caption and source link.
- Existing contact links and section/list primitives.

One global stylesheet owns shared tokens and primitives. Content entries own project facts and ordering; optional page-specific CSS only handles genuine layout differences. Do not duplicate an independent portfolio palette or theme toggle implementation.

## Accessibility

Proposed target: WCAG 2.2 AA. Verify text contrast in both themes, visible keyboard focus, semantic landmarks, one meaningful h1, logical headings, descriptive links, adequate touch targets and no reliance on colour alone.

Use native anchors and buttons. Give diagrams a text explanation, meaningful images alt text, and decorative terminal details appropriate hidden semantics. Preserve reduced-motion support. Reading, navigation and evidence access must work without client JavaScript. Focus must remain visible despite overlays or terminal clipping.

## Responsive behavior

Retain the existing 640px breakpoint as the starting point. At narrow widths, stack metadata and previews above article text; wrap navigation and long project titles without horizontal page overflow. Keep the full title in the document even when window chrome truncates it.

Use one reading column. Diagrams should reflow or have an accessible vertical equivalent. Tables may scroll within a labelled container when necessary. Verify at 375px mobile, an intermediate tablet width, and 1440px desktop, in both themes and at increased text size.

## Interaction states

Static HTML delivers the article and navigation immediately. Avoid artificial loading states. Set image dimensions and load nonessential images lazily to reduce layout movement on slow connections.

Omit unavailable optional content instead of showing empty cards or disabled links. Invalid project URLs should reach an unindexed 404 page with useful CV/Portfolio navigation. No-results states and form success states are unnecessary for the proposed first release.

Links must have clear hover/focus states. Keep existing theme persistence and accessible switch announcements. External project availability must not prevent someone from reading the local case study.

## Content voice

Use clear first-person prose consistent with the CV, British English, and concrete descriptions of decisions and results. Use “I” for James's work and explicit team credit for shared work. Explain unfamiliar acronyms once.

Where Was I? follows James's supplied DevHunt/Product Hunt passages: conversational, personal and concise, with roughly 350 words of case-study copy. Credit his friend Adrian as co-creator; retain the strongest implementation choices without turning the page into a technical inventory.

Preserve original project purposes and distinguish research findings, product capabilities, intended benefits and ongoing work. AI for Good work is not automatically evidence of AI safety research. Avoid generic claims of transformation or unexplained technology lists.

Use AI.M.E. consistently as the display name, expanded as Agentic AI Maturity Evaluation. Keep quantitative claims dated and attributed. Do not turn source visibility into proof of complete internal organisational capability; the published methodology explicitly limits assessment to public evidence.

## Implementation constraints

Framework: Astro 7.3.2 with static output, a local Markdown projects collection, one shared case-study route and the existing CSS. Use Node 24 LTS. Astro collections support structured local content; `getStaticPaths()` supplies the individual routes at build time. Content changes require rebuilding. See the official Astro references above.

Current metadata: the filename supplies a stable slug; title, summary, context, role, order and HTTP(S) links are required. Collaborators, status, tags, highlights, the featured flag and a screenshot are optional. A screenshot contains a local `src` path relative to the Markdown file and nonempty descriptive `alt` text. All seven current entries have one. Astro's native image processing generates responsive WebP previews with explicit dimensions and lazy loading, preserving the original proportions. Maintain the originals in `src/assets/projects/`; `screenshots/projects/` is the ignored intake folder. Use Markdown for the narrative. Dates can be introduced when established; they are not required fields.

The CV uses the shared layout with its content, fragment IDs, theme behaviour, console features and existing links preserved, adding Portfolio navigation. Root-relative asset URLs keep fonts and the vendored analytics script working on nested routes. The small local theme script replaces the theme-change CDN dependency while preserving saved preferences and accessible switch behaviour. GitHub Pages uses GitHub Actions as its publishing source. The workflow builds and validates pushes and pull requests, then deploys successful pushes or manual dispatches from `main`. The custom domain remains `jameswolman.dev`.

Indexing requirement: every generated HTML page, including CV, portfolio, projects and 404, emits `<meta name="robots" content="noindex, nofollow">`. The new `public/robots.txt` allows crawling so supporting search engines can read that directive. Google documents that crawl blocking prevents detection of noindex. Do not claim search-engine removal has occurred solely because a build passes. No search-oriented sitemap is generated.

Preserve GoatCounter's vendored script, integrity and raw-click behaviour. Adapt its validator to generated HTML, root-relative assets and all pages; retain unique outgoing event names and valid fragment targets. Standard page navigation can use pageview tracking; avoid inventing unnecessary interaction events.

Implementation sequence:

1. Capture CV behaviour and appearance before migration; make Astro build the CV through the shared layout and assets.
2. Build the overview and AI.M.E. page from a project collection; use this example to settle the article and evidence layout.
3. Populate the other six pages from confirmed descriptions and available materials, tracking unresolved copy separately.
4. Verify the complete static output and prepare the build/deploy workflow for the existing host.

Acceptance checks: nine main pages plus 404 build; all seven project routes and navigation links resolve; unknown slugs reach the 404; fonts and scripts load at nested URLs; noindex is emitted everywhere and robots permits reading it; reading/navigation do not depend on JavaScript; themes persist with accessible controls; the CV remains visually consistent; outgoing analytics and fragments validate; mobile/desktop, keyboard and reduced-motion checks pass. `npm test` builds and runs the committed static/regression checks. Local browser evidence and screenshots are recorded under `.omx/artifacts/portfolio/`; these generated artifacts are not deployed.

## Open questions

- [ ] James/source review: clarify the AIM 100 cost boundary, dates and evidence links before using its figures as headline metrics.
- [ ] James: establish which non-public materials, if any, can be used for Upstream. AI.M.E.'s openness does not establish their disclosure boundaries. Draft from supplied descriptions and public materials in the meantime.
- [ ] James/source review: fill project-specific contribution, dates, evaluation and outcome details for the other six pages where available. Do not invent results to fill a template.
- [x] James supplied and selected one screenshot for each of the seven projects; the maintained inventory is `src/assets/projects/`, with one PNG named for each stable slug above.

These gaps are recorded for content drafting and implementation. They do not prevent review of the proposed design, and this document does not treat them as settled facts.
