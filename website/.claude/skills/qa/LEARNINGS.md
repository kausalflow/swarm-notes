# Learnings — QA

## What works
- `interface Foo extends Bar {}` → `type Foo = Bar` cleanly fixes `no-empty-object-type` ESLint error (2026-03-15)
- `// eslint-disable-next-line` for `env.d.ts` triple-slash reference is acceptable since Astro requires this file (2026-03-15)

## Anti-Patterns
- Prettier cannot parse `<!-- Astro comments -->` inside `.map()` expressions — causes parse error in `format:check`. Comments in `.map()` must be replaced with `{/* JSX comments */}` or removed (2026-03-15)
- `@vercel/analytics/astro` causes a 404 on `/_vercel/insights/script.js` in local preview server, dropping Lighthouse Best Practices from 100 to 96. Not a production issue, but distorts local Lighthouse measurements (2026-03-15)
