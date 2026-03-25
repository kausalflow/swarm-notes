// @ts-check
import { defineConfig } from 'astro/config';
import wikiLinkPlugin from 'remark-wiki-link';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const vaultAbsPath = path.resolve(__dirname, '../vault');

let allFiles = [];
try {
  allFiles = fs.readdirSync(vaultAbsPath, { recursive: true });
} catch (e) {
  console.warn("Could not read vault directory", e);
}

const slugToPath = {};
allFiles.forEach(file => {
  if (typeof file === 'string' && file.endsWith('.md')) {
    const slug = path.basename(file, '.md').toLowerCase();
    slugToPath[slug] = file.replace(/\\/g, '/').replace(/\.md$/, '');
  }
});

// https://astro.build/config
export default defineConfig({
  site: 'https://kausalflow.github.io',
  base: '/swarm-cruise',
  markdown: {
    remarkPlugins: [
      [wikiLinkPlugin, {
        pathFormat: 'obsidian',
        wikiLinkClassName: 'wiki-link',
        hrefTemplate: (permalink) => {
          const lower = permalink.toLowerCase();
          const mapped = slugToPath[lower] || permalink;
          return `/swarm-cruise/${mapped}`;
        }
      }]
    ]
  }
});
