---
name: tailwind
description: Use when writing or reviewing any CSS class, changing colors, modifying globals.css, or when hardcoded colors or inline styles are detected.
---

# Tailwind CSS Skill

## Domain

Tailwind v4 Expertise, @theme-Direktive, OKLCH, Utilities, Dark Mode

## KPIs

| Metrik | Ziel | Messung |
|--------|------|---------|
| Hardcoded Colors | 0 | Grep: `(bg\|text\|border)-(red\|blue\|green\|yellow\|purple\|pink\|gray\|slate\|zinc)-[0-9]+` in src/ |
| Inline Styles | 0 | Grep: `style="` in src/**/*.astro |
| tailwind.config.mjs | existiert nicht | Glob-Check |

## Regeln

### Tailwind v4 Setup

AstroDeck verwendet Tailwind CSS v4 via `@tailwindcss/vite` (NICHT `@astrojs/tailwind`).

- Kein `tailwind.config.mjs` — Config lebt in CSS
- `@theme` Direktive für Token-Registration
- `.dark` Klasse für Dark-Mode-Overrides

### @theme vs .dark

```css
/* Token-Registration (Tailwind kennt diese als Utilities) */
@theme {
  --color-primary: oklch(11.2% 0.0079 286.75);
  --color-primary-foreground: oklch(100% 0 0);
}

/* Dark-Mode-Overrides (nur Werte ändern, keine neuen Tokens) */
.dark {
  --color-primary: oklch(100% 0 0);
  --color-primary-foreground: oklch(11.41% 0.0079 286.75);
}
```

### OKLCH Farbformat

```
oklch(lightness% chroma hue)
```

- **Lightness**: 0-100% (0 = schwarz, 100 = weiß)
- **Chroma**: Farbintensität (0 = grau, 0.1-0.4 = lebendig)
- **Hue**: Farbwinkel in Grad (0-360)

Häufige Hues: Rot ~25, Orange ~70, Gelb ~100, Grün ~145, Blau ~250, Lila ~300

### --color- Prefix

Alle Farb-Tokens verwenden `--color-` Prefix:

```css
--color-background      /* ✅ */
--background             /* ❌ veraltet */
```

### Utility-Patterns

```
/* Responsive (mobile-first) */
text-base md:text-lg lg:text-xl

/* Hover/Focus States */
hover:bg-primary/90 focus:ring-2 focus:ring-ring

/* Transitions */
transition-colors duration-200

/* Dark Mode (automatisch via CSS-Variablen) */
bg-background text-foreground  /* funktioniert in beiden Modi */
```

### Common Mistakes

| Fehler | Korrekt |
|--------|---------|
| `@astrojs/tailwind` | `@tailwindcss/vite` |
| `tailwind.config.mjs` | CSS `@theme` Direktive |
| `hsl(220 14% 96%)` | `oklch(96.27% 0.0044 286.32)` |
| `bg-blue-500` | `bg-primary` |
| `text-gray-600` | `text-muted-foreground` |
| `dark:bg-gray-900` | `bg-background` (automatisch) |
| `style="color: red"` | `text-destructive` |

### Dark-Mode-Pattern

Farben NICHT mit `dark:` Prefix steuern. Stattdessen CSS-Variablen nutzen, die automatisch in `.dark` überschrieben werden:

```astro
<!-- ❌ Falsch -->
<div class="bg-white dark:bg-gray-900 text-black dark:text-white">

<!-- ✅ Richtig -->
<div class="bg-background text-foreground">
```

## Non-Negotiable

Diese Regeln gelten immer — auch unter Zeitdruck, auch bei "nur einem schnellen Fix":

- **Keine hardcoded Colors.** `bg-blue-500` ist nie "nur vorübergehend" — es wird vergessen und bricht beim nächsten Theme-Wechsel.
- **Keine inline styles.** Auch nicht "nur für diesen einen Sonderfall". Tailwind Utilities decken alles ab.
- **OKLCH only.** "HSL ist lesbarer" ist kein Argument — das gesamte Design System basiert auf OKLCH. Mischen zerstört die Farbkonsistenz.
- **Kein `tailwind.config.mjs`.** Auch nicht "weil ein Package es erwartet". Config lebt in CSS via `@theme`.
- **Kein `@astrojs/tailwind`.** AstroDeck nutzt `@tailwindcss/vite`. Die alte Integration ist inkompatibel mit Tailwind v4.

## Vor dem Anwenden

Lies `LEARNINGS.md` in diesem Verzeichnis, um bekannte Anti-Patterns zu vermeiden.
