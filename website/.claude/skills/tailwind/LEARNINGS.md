# Learnings — Tailwind CSS

## What works
- `hover:shadow-xl hover:shadow-primary/40` instead of `hover:shadow-[0_20px_50px_rgba(59,130,246,0.6)]` — themeable, automatically adapts to primary color changes (2026-03-15)
- `z-0` / `z-10` Tailwind classes instead of `style="z-index: 0/1"` — eliminates inline styles without visual difference (2026-03-15)

## Anti-Patterns
- `rgba(59,130,246,0.6)` in arbitrary shadows is hardcoded blue — shadow stays wrong when primary color changes. Always use `shadow-primary/XX` instead (2026-03-15)
- `bg-zinc-900` in AuthLayout is a hardcoded Tailwind color in a rarely used layout — caught by grep checks in `src/**/*.astro`, should be `bg-foreground` or a semantic token (2026-03-15)
