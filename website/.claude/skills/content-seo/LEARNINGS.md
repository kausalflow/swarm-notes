# Learnings — Content & SEO

## What works
- Title without brand duplication: Layout appends `| AstroDeck` automatically, so pass page title without "AstroDeck" → clean `<title>` tag (2026-03-15)

## Anti-Patterns
- Meta description under 150 characters: Lighthouse scores SEO at 100/100 even with 143 characters since minimum length is not a hard criterion. The 150-character target in SKILL.md is a best-practice guideline, not mandatory — but still worth aiming for (2026-03-15)
- Title duplication "AstroDeck ... | AstroDeck" — happens when page title already contains the brand name and the layout appends `| AstroDeck` again (2026-03-15)
