---
name: content-seo
description: Use when creating or editing pages, blog posts, or content files, adding meta tags, or when Lighthouse SEO drops below 90.
---

# Content & SEO Skill

## Domain

Content Collections, Meta Tags, OpenGraph, Structured Data, RSS, Sitemap

## KPIs

| Metrik | Ziel | Messung |
|--------|------|---------|
| Lighthouse SEO | >90 | Lighthouse JSON → `categories.seo.score * 100` |
| Seiten ohne Description | 0 | Grep: Seiten ohne `description` Prop |
| Seiten ohne OG-Image | 0 | HTML-Check in dist/ |

## Regeln

### Content Collections Schema

```typescript
// src/content.config.ts
import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string().max(160),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    heroImage: z.string().optional(),
    draft: z.boolean().default(false),
    tags: z.array(z.string()).default([]),
    author: z.string().default('Team'),
  }),
});
```

### SEO Component Usage

```astro
---
import BaseLayout from '@/layouts/BaseLayout.astro';

const title = "Seitentitel — Markenname";
const description = "Beschreibung der Seite, 150-160 Zeichen, mit relevantem Keyword am Anfang.";
---

<BaseLayout title={title} description={description}>
  <!-- Content -->
</BaseLayout>
```

### Meta-Description Best Practices

- **Länge**: 150-160 Zeichen (Google schneidet bei ~160 ab)
- **Keyword**: Relevantes Keyword am Anfang
- **Unique**: Jede Seite braucht eine eigene Description
- **Actionable**: Call-to-Action oder Nutzenversprechen
- **Kein Duplicate**: Nie dieselbe Description für mehrere Seiten

### OpenGraph Tags

```html
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{description}" />
<meta property="og:image" content="{siteUrl}/og-image.png" />
<meta property="og:url" content="{canonicalUrl}" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="{siteName}" />
```

- OG-Image: 1200×630px, PNG oder JPG
- Immer absolute URLs verwenden

### Twitter Cards

```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{description}" />
<meta name="twitter:image" content="{siteUrl}/og-image.png" />
```

### Canonical URLs

```astro
<link rel="canonical" href={Astro.url.href} />
```

- Jede Seite braucht eine Canonical URL
- Verhindert Duplicate-Content-Probleme
- AstroDeck setzt dies automatisch im BaseLayout

### Sitemap

```javascript
// astro.config.mjs
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://example.com',  // PFLICHT für Sitemap
  integrations: [sitemap()],
});
```

- `site` in `astro.config.mjs` MUSS gesetzt sein
- Sitemap wird automatisch bei `npm run build` generiert
- Ergebnis: `dist/sitemap-index.xml`

### RSS-Feed

```typescript
// src/pages/rss.xml.ts
import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const blog = await getCollection('blog');
  return rss({
    title: 'Blog Title',
    description: 'Blog Description',
    site: context.site,
    items: blog.map((post) => ({
      title: post.data.title,
      pubDate: post.data.pubDate,
      description: post.data.description,
      link: `/blog/${post.id}/`,
    })),
  });
}
```

### Structured Data (JSON-LD)

```astro
<script type="application/ld+json" set:html={JSON.stringify({
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": siteName,
  "url": siteUrl,
})} />
```

Für Blog-Posts:

```astro
<script type="application/ld+json" set:html={JSON.stringify({
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": title,
  "description": description,
  "datePublished": pubDate,
  "author": { "@type": "Person", "name": author },
})} />
```

### Heading-Hierarchie für SEO

- Jede Seite genau ein `<h1>`
- `<h2>` für Hauptabschnitte
- `<h3>` für Unterabschnitte
- Keine Ebenen überspringen (h1 → h3 ohne h2)

## Non-Negotiable

Diese Regeln gelten immer — auch unter Zeitdruck, auch bei "SEO ist nicht so wichtig":

- **Jede Seite braucht eine Meta-Description.** "Ist nur eine interne Seite" — Google indexiert alles was öffentlich erreichbar ist.
- **Jede Seite braucht genau ein `<h1>`.** Null oder mehrere h1 zerstören die Heading-Hierarchie und kosten SEO-Punkte.
- **Keine doppelten Titles.** "AstroDeck ... | AstroDeck" passiert wenn der Page-Title den Brand enthält — das Layout hängt ihn automatisch an.
- **Canonical URL ist Pflicht.** Auch bei "einfachen" Seiten. Ohne Canonical entstehen Duplicate-Content-Probleme bei Crawlern.
- **Structured Data nicht raten.** JSON-LD Schema muss valide sein. Lieber weglassen als fehlerhaftes Schema ausliefern — Google bestraft invalides Markup.

## Vor dem Anwenden

Lies `LEARNINGS.md` in diesem Verzeichnis, um bekannte Anti-Patterns zu vermeiden.
