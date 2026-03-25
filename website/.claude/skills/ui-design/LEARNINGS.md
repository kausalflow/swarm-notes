# Learnings — UI/UX Design

## What works
- `py-20 px-6` as default section padding works consistently across all sections → visually harmonious without Lighthouse impact (2026-03-15)
- `shadow-lg` instead of `shadow-[0_25px_50px_-12px_rgba(0,0,0,0.15)]` — Tailwind standard shadow is themeable and sufficient for card elevation (2026-03-15)

## Anti-Patterns
- `py-32` (128px) is too generous for standard sections — creates visual inconsistency with other sections using `py-20` (80px) (2026-03-15)
- `rounded-lg` on cards contradicts the design system (`rounded-xl`). Inconsistency is not detectable by automated checks — only through manual code review (2026-03-15)
- `font-bold` on h3 instead of `font-semibold` — subtle difference, but the design system defines clear hierarchy: bold for h1/h2, semibold for h3/h4 (2026-03-15)
