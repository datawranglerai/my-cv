import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

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
    links: z.array(z.object({ label: z.string(), url: z.url({ protocol: /^https?$/ }) })).min(1),
    highlights: z.array(z.object({ value: z.string(), label: z.string() })).default([]),
  }),
});

export const collections = { projects };
