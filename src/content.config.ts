import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const localPdfPattern = /^\/(?!\/)(?:[^/?#]+\/)*[^/?#]+\.pdf$/i;
const projectLinkUrl = z.union([
  z.url({ protocol: /^https?$/ }),
  z.string().regex(localPdfPattern),
]);

const projectLink = z.object({
  label: z.string(),
  url: projectLinkUrl,
  download: z.boolean().optional(),
}).superRefine((link, context) => {
  if (link.download && !localPdfPattern.test(link.url)) {
    context.addIssue({
      code: 'custom',
      path: ['download'],
      message: 'download links must reference a root-relative PDF',
    });
  }
});

const projects = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/projects' }),
  schema: ({ image }) => z.object({
    title: z.string(),
    summary: z.string(),
    context: z.enum(['Professional', 'Personal', 'Open source', 'Hackathon']),
    role: z.string(),
    collaborators: z.array(z.string()).default([]),
    status: z.string().optional(),
    order: z.number().int().positive(),
    featured: z.boolean().default(false),
    screenshot: z.object({
      src: image(),
      alt: z.string().trim().min(1),
    }).optional(),
    tags: z.array(z.string()).default([]),
    links: z.array(projectLink).min(1),
    highlights: z.array(z.object({ value: z.string(), label: z.string() })).default([]),
  }),
});

export const collections = { projects };
