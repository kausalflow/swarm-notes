# Learnings — Astro Framework

## What works
- `context: import('astro').APIContext` as inline type import for API route parameters — fixes TS7006 without extra import statement (2026-03-15)
- `context.site ?? 'https://fallback.dev'` as fallback for `site` in RSS feed — fixes TS2322 (URL | undefined not assignable to string | URL) (2026-03-15)

## Anti-Patterns
