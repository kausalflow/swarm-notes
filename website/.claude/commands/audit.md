---
description: Run a comprehensive quality audit on the project
---

# Project Audit

Perform a comprehensive quality check of the AstroDeck project.

## Audit Categories

### 1. Code Quality
```bash
npm run lint
npm run format:check
npx tsc --noEmit
```

### 2. Build Verification
```bash
npm run build
```
Check for warnings or errors in the build output.

### 3. Import Consistency
Use the Grep tool to search for relative imports that should use `@/` alias:
- Pattern: `from ['"]\.\.\/` in `src/**/*.{astro,ts,tsx}` files

### 4. Hardcoded Colors
Use the Grep tool to search for hardcoded Tailwind colors instead of CSS variables:
- Pattern: `(bg|text|border)-(red|blue|green|yellow|purple|pink|gray|slate|zinc)-[0-9]+` in `src/**/*.astro` files
- Exceptions: Intentional use in decorative elements is acceptable

### 5. Deprecated Patterns
Check for patterns that are no longer valid in Astro 6:
- `ViewTransitions` import (should be `ClientRouter`)
- `import { z } from 'astro:content'` (should be `from 'astro/zod'`)
- `import { z } from 'astro:schema'` (should be `from 'astro/zod'`)
- HSL color values in `globals.css` (should be OKLCH)
- `tailwind.config.mjs` file (Tailwind v4 uses CSS-based config)

### 6. Accessibility
Check for:
- [ ] Images without alt text: search for `<img` without `alt=`
- [ ] Buttons without accessible labels
- [ ] Missing ARIA attributes on interactive elements
- [ ] Proper heading hierarchy (h1 -> h2 -> h3, no skipping)

### 7. SEO
Verify each page has:
- [ ] Unique title tag
- [ ] Meta description (150-160 chars)
- [ ] OpenGraph tags (via SEO component)
- [ ] Proper heading hierarchy

### 8. Performance
- [ ] Run `npm run build` - check bundle size
- [ ] Verify images use Astro's `<Image />` component where possible
- [ ] Check for unnecessary `client:load` directives (prefer `client:visible` or `client:idle`)
- [ ] External scripts have SRI integrity attributes

### 9. Theme Consistency
- [ ] All color tokens use `--color-` prefix with OKLCH format
- [ ] Both `@theme` and `.dark` blocks are in sync
- [ ] No inline styles (`style="..."`)

## Skills

Für Details: `qa` und `accessibility` Skills konsultieren (`.claude/skills/qa/SKILL.md`, `.claude/skills/accessibility/SKILL.md`).

## Output Format

```markdown
## Audit Results

### Passed
- [List of passed checks]

### Warnings
- [List of warnings with file locations]

### Issues
- [List of issues that need fixing]

### Recommendations
- [Suggested improvements]
```
