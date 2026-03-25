import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';

const vault = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "../vault" }),
});

export const collections = { vault };
