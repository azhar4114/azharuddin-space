// src/content/config.ts
import { defineCollection, z } from 'astro:content';

const projects = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    category: z.enum(['independent', 'professional-case-study', 'experiment']),
    status: z.enum(['published', 'in-progress', 'archived']).default('published'),
    statusLabel: z.string().optional(),
    problem: z.string().optional(),
    role: z.string().optional(),
    featured: z.boolean().default(false),
    technologies: z.array(z.string()),
    coverImage: z.string().optional(),
    demoUrl: z.string().url().optional(),
    repositoryUrl: z.string().url().optional(),
    publishedAt: z.coerce.date().optional(),
    updatedAt: z.coerce.date().optional(),
  }),
});

const writing = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    tags: z.array(z.string()).default([]),
    category: z.string().optional(),
    draft: z.boolean().default(false),
    heroImage: z.string().optional(),
  }),
});

export const collections = { projects, writing };
