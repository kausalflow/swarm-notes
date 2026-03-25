---
description: Customize the AstroDeck theme colors and design tokens
---

# Customize Theme

Modify the design system in `src/styles/globals.css` using Tailwind CSS v4's `@theme` directive and OKLCH color format.

## Current Theme Location

All design tokens are in `src/styles/globals.css` under:
- `@theme { ... }` - Light mode colors (Tailwind v4 token registration)
- `.dark { ... }` - Dark mode color overrides

## Available Tokens

```css
/* Core */
--color-background      /* Page background */
--color-foreground      /* Primary text */

/* Primary (buttons, links, CTAs) */
--color-primary
--color-primary-foreground

/* Secondary */
--color-secondary
--color-secondary-foreground

/* Muted (subtle backgrounds, secondary text) */
--color-muted
--color-muted-foreground

/* Accent (highlights) */
--color-accent
--color-accent-foreground

/* Cards & Borders */
--color-card
--color-card-foreground
--color-border
--color-input
--color-ring
```

## How to Customize

1. **Read current values** from `src/styles/globals.css`
2. **Ask user** for new colors (hex, HSL, OKLCH, or color name)
3. **Convert to OKLCH** format: `oklch(lightness% chroma hue)`
4. **Update both** `@theme` and `.dark` sections
5. **Check contrast** - foreground must be readable on background

## OKLCH Color Format

```
oklch(lightness% chroma hue)
```

- **Lightness**: 0-100% (0 = black, 100 = white)
- **Chroma**: Color intensity (0 = grayscale, 0.1-0.4 = vivid)
- **Hue**: Color angle in degrees (0-360)

Common hues: Red ~25, Orange ~70, Yellow ~100, Green ~145, Blue ~250, Purple ~300

## Example Transformation

User wants: "Make primary color forest green"

```css
/* Before (in @theme block) */
--color-primary: oklch(11.2% 0.0079 286.75);

/* After */
--color-primary: oklch(45% 0.15 145);  /* Forest green */
```

## Important Rules

- **Always use OKLCH format** - `oklch(L% C H)` (NOT HSL, NOT hex)
- **Use `--color-` prefix** for all tokens (Tailwind v4 convention)
- **Update both themes** - `@theme` block and `.dark` block
- **Test contrast** - primary-foreground must be readable on primary (4.5:1 minimum)
- **Never create a tailwind.config.mjs** - Tailwind v4 uses CSS-based config only

## Skills

Für Farbtheorie und Utility-Patterns: `ui-design` und `tailwind` Skills konsultieren (`.claude/skills/ui-design/SKILL.md`, `.claude/skills/tailwind/SKILL.md`).

## Checklist

- [ ] Colors in correct OKLCH format
- [ ] Light mode updated (`@theme` block)
- [ ] Dark mode updated (`.dark` block)
- [ ] Token names use `--color-` prefix
- [ ] Contrast ratio checked (4.5:1 minimum)
- [ ] Tested in browser (both light and dark mode)
