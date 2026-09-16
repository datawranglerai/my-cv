# James Wolman's CV and portfolio

A static Astro site using shared terminal styling. The CV lives at `/`, the portfolio at `/portfolio/`, and project case studies at `/portfolio/projects/{slug}/`.

## Local development

Use Node 24 LTS (`nvm use` if you use nvm), then:

```sh
npm ci
npm run dev
```

`npm test` builds the site and validates generated pages, internal links, static assets, indexing metadata, analytics and preservation of the original CV content. `npm run preview` serves the production build locally.

Optional Astro/TypeScript diagnostics can run without adding application dependencies:

```sh
npm exec --yes --package=@astrojs/check --package=typescript -- astro-check
```

## Editing

- `src/content/projects/*.md`: project metadata and case-study copy. The filename determines the URL slug. Keep existing filenames stable when changing a display title.
- `src/content.config.ts`: project fields and validation.
- `src/assets/projects/`: original project screenshots, named by project slug.
- `src/components/CvContent.astro`: existing CV content.
- `src/layouts/TerminalLayout.astro` and `src/styles/global.css`: shared layout, themes and visual styling.
- `public/`: fonts, vendored analytics, robots policy and custom-domain configuration.
- `DESIGN.md`: design decisions and remaining editorial questions.

Each project needs a title, summary, context, role, order and at least one link. Collaborators, status, tags, highlights and a featured flag are optional. Keep external resources in frontmatter `links`, where the template adds analytics consistently. Optional sections may be omitted; do not invent dates, outcomes or metrics to fill the template.

To add or replace a portfolio preview, put the original image in `src/assets/projects/` and add this optional frontmatter field to the project's Markdown file. The path is relative to that file; `alt` must describe the screenshot and cannot be empty.

```yaml
screenshot:
  src: ../../assets/projects/aime.png
  alt: AI.M.E. dashboard showing the FTSE 350 AI maturity assessment.
```

Each preview appears beneath its summary on the portfolio overview and links to the case study. Astro generates responsive WebP images at build time; previews retain their full proportions and load lazily. See [Astro images in content collections](https://docs.astro.build/en/guides/images/#images-in-content-collections). The intake folder `screenshots/projects/` is ignored by Git; the copies in `src/assets/projects/` are the maintained source assets.

## Search indexing

All pages carry `noindex, nofollow`. Crawling is allowed so search engines can read that directive; a blanket `Disallow` can prevent this. See [Google's guidance](https://developers.google.com/search/docs/crawling-indexing/block-indexing).

## Deployment

The GitHub workflow builds and validates pushes and pull requests. Deployment runs only when the workflow is manually dispatched from `main`, after validation passes.

The repository was configured to publish the root of `main` through legacy GitHub Pages at implementation time. This migration moves the root site into Astro, so a direct push or merge to `main` while legacy publishing is enabled could interrupt the live CV. Treat this as a release prerequisite:

1. Before pushing or merging the migration to `main`, change **Settings → Pages → Source** to **GitHub Actions**, preserving the existing `jameswolman.dev` custom domain.
2. Merge the verified migration to `main`.
3. Manually run **Validate site** on `main`. Its deployment job publishes the validated `dist/` artifact.
4. Check the live CV, portfolio routes, custom domain and noindex metadata.

No remote settings, branch pushes or deployments were performed during local implementation. The local build is ready for review; release requires the sequence above.

Official references: [Astro on GitHub Pages](https://docs.astro.build/en/guides/deploy/github/), [GitHub Pages publishing sources](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
