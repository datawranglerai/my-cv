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

The [Validate site workflow](.github/workflows/validate.yml) builds and validates pushes and pull requests. Every push to `main`, including a merged pull request, automatically publishes the site after the build and validation pass. Pull requests and pushes to other branches validate without deploying. Manual deployment from `main` remains available.

On 16 September 2026, GitHub Pages was verified to use **GitHub Actions** as its publishing source, with the `jameswolman.dev` custom domain and HTTPS enforcement preserved. The `github-pages` environment permits deployments from `main`.

Follow this sequence to publish the Astro migration:

1. Open [Settings → Pages](https://github.com/datawranglerai/my-cv/settings/pages). Under **Build and deployment → Source**, confirm **GitHub Actions** is selected. If it still says **Deploy from a branch**, switch it before merging the migration. Preserve `jameswolman.dev` and **Enforce HTTPS**. Skip the suggested workflow templates; this repository already contains the deployment workflow.
2. Open [the portfolio branch comparison](https://github.com/datawranglerai/my-cv/compare/main...feature/portfolio), create a pull request from `feature/portfolio` into `main`, and merge once its checks pass.
3. After merging, open [Actions → Validate site](https://github.com/datawranglerai/my-cv/actions/workflows/validate.yml) and select the run triggered by the push to `main`. Deployment starts automatically; no manual trigger is needed.
4. Confirm both jobs finish successfully. `build` compiles Astro, uploads the `dist/` artifact and validates the generated site. `deploy` publishes that artifact to GitHub Pages after validation passes. A skipped `deploy` job is expected for pull requests and runs on other branches. If the build or validation fails, deployment is skipped.
5. Visit [the CV](https://jameswolman.dev/) and [portfolio](https://jameswolman.dev/portfolio/), then open a project page. Check navigation, images, the custom domain, HTTPS and the expected `noindex, nofollow` metadata.

For subsequent releases, merge verified changes into `main`, then repeat steps 3–5 to monitor the automatic deployment and check the live site.

To deploy manually, open **Actions → Validate site → Run workflow**, select **main**, and click the green **Run workflow** button. This builds, validates and publishes the selected branch's current revision; deployment is restricted to `main`.

Official references: [Astro on GitHub Pages](https://docs.astro.build/en/guides/deploy/github/), [GitHub Pages publishing sources](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
