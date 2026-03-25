import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    author: z.string().default('AstroDeck Team'),
    image: z.string().optional(),
    tags: z.array(z.string()).default([]),
  }),
});

const vault = defineCollection({
  loader: glob({ pattern: '**/*.md', base: '../vault' }),
});

export const collections = { blog, vault };
