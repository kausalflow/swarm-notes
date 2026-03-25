---
name: ui-design
description: Use when creating or modifying any visible UI element, adjusting spacing or typography, reviewing visual consistency, or when Lighthouse Performance drops below 90.
---

# UI/UX Design Skill

## Domain

Visual Hierarchy, Spacing, Typography, OKLCH-Farbtheorie, Layout-Patterns

## KPIs

| Metrik | Ziel | Messung |
|--------|------|---------|
| Lighthouse Performance | >90 | Lighthouse JSON → `categories.performance.score * 100` |
| First Contentful Paint | <1.8s | Lighthouse JSON → `audits.first-contentful-paint` |
| Largest Contentful Paint | <2.5s | Lighthouse JSON → `audits.largest-contentful-paint` |
| Cumulative Layout Shift | <0.1 | Lighthouse JSON → `audits.cumulative-layout-shift` |
| Total Blocking Time | <200ms | Lighthouse JSON → `audits.total-blocking-time` |

## Regeln

### Heading-Skala

```
h1: text-5xl md:text-7xl font-bold      → Hero-Headlines
h2: text-3xl md:text-5xl font-bold      → Section-Headlines
h3: text-xl md:text-2xl font-semibold   → Sub-Headlines, Card-Titles
h4: text-lg font-semibold               → Feature-Titles
p:  text-base/text-lg text-muted-foreground → Body
```

- `font-bold` für Headlines (h1, h2)
- `font-semibold` für Sub-Headlines (h3, h4)
- Niemals `font-extrabold` oder `font-black` verwenden

### Section-Padding-System

```
Standard-Section:  py-20 px-6
Kompakte Section:  py-12 px-6
Hero-Section:      py-24 px-6  oder  min-h-[80vh] px-6
CTA-Section:       py-16 px-6
```

### Container-Widths

```
Standard Content:   max-w-7xl mx-auto
Narrow Content:     max-w-4xl mx-auto (text-heavy, centered)
Wide Content:       max-w-none (full-width backgrounds)
Card Container:     max-w-5xl mx-auto (default BaseLayout)
```

### Grid-Patterns

```
2-Spalten:  grid md:grid-cols-2 gap-8
3-Spalten:  grid md:grid-cols-2 lg:grid-cols-3 gap-8
4-Spalten:  grid grid-cols-2 md:grid-cols-4 gap-6
Features:   grid md:grid-cols-2 lg:grid-cols-3 gap-8
```

### Card-Pattern

```astro
<div class="rounded-xl border border-border bg-card p-6 shadow-sm">
  <h3 class="text-xl font-semibold mb-2">{title}</h3>
  <p class="text-muted-foreground">{description}</p>
</div>
```

- Immer `rounded-xl` (nicht `rounded-lg` oder `rounded-md`)
- Immer `border border-border` für Konsistenz
- Immer `bg-card` (nicht `bg-white` oder `bg-gray-50`)
- Padding: `p-6` Standard, `p-8` für große Cards

### Responsive Design Rules

Every component and page MUST be verified at all breakpoints before completion.

**Breakpoints (test in this order):**

| Breakpoint | Width | Key checks |
|------------|-------|------------|
| Mobile S | 375px | Single column, no horizontal overflow, readable text, touch targets ≥44px |
| Mobile L | 428px | Same as above, slightly more breathing room |
| Tablet | 768px (`md:`) | Grid columns kick in (1→2), sidebar may still be hidden |
| Laptop | 1024px (`lg:`) | Full navigation visible, sidebar navigation appears |
| Desktop | 1280px (`xl:`) | Max-width containers centered, no stretching |

**Responsive patterns:**

```
Navigation:     Mobile = collapsible dropdown/hamburger, lg: = sidebar or full nav
Grids:          grid-cols-1 → md:grid-cols-2 → lg:grid-cols-3
Sidebar:        lg:hidden → lg:block (absolute positioned, outside flow)
Mobile subnav:  Sticky collapsible "On this page" dropdown (lg:hidden)
Typography:     text-3xl md:text-5xl (scale up, never scale down)
Padding:        px-4 sm:px-6 md:px-12 (increase with viewport)
```

**Common responsive anti-patterns to catch:**

- `hidden` without a mobile alternative (content disappears on mobile)
- Fixed widths (`w-[500px]`) without responsive fallback
- Sidebar navigation only visible on desktop with no mobile equivalent
- Horizontal scroll caused by wide `<pre>` blocks without `overflow-x-auto`
- Touch targets smaller than 44×44px on mobile
- Text too small on mobile (minimum `text-sm` / 14px for body)

### Design-Consistency-Checklist

- [ ] Heading-Hierarchie eingehalten (h1 → h2 → h3, kein Überspringen)
- [ ] Einheitliche Section-Paddings (`py-20 px-6`)
- [ ] Farben nur via CSS-Variablen (`text-primary`, nicht `text-blue-500`)
- [ ] Konsistente Border-Radius (`rounded-xl`)
- [ ] Mobile-first Responsive (alle Breakpoints geprüft: 375px, 768px, 1024px, 1280px)
- [ ] Mobile Navigation vorhanden (kein `hidden lg:block` ohne mobile Alternative)
- [ ] Kein horizontaler Overflow auf Mobile
- [ ] Dark Mode getestet

## Non-Negotiable

Diese Regeln gelten immer — auch unter Zeitdruck, auch bei "nur einem schnellen Prototyp":

- **Kein Commit ohne Responsive-Check.** "Machen wir später responsive" funktioniert nie — es wird vergessen und User sehen eine kaputte Mobile-Version.
- **Section-Padding ist `py-20 px-6`.** "Etwas mehr Luft mit `py-32`" zerstört die visuelle Konsistenz über alle Sections hinweg.
- **Farben nur via CSS-Variablen.** "Nur hier kurz `bg-white`" bricht Dark Mode sofort — ohne dass man es merkt bis jemand umschaltet.
- **Kein `rounded-lg` oder `rounded-md`.** Das Design System nutzt `rounded-xl`. Inkonsistenz fällt auf, auch wenn einzelne Abweichungen "besser aussehen".
- **Mobile-first ist Pflicht.** Desktop-first "und dann anpassen" produziert Overflow, zu kleine Touch-Targets und fehlende Navigation auf Mobile.

## Vor dem Anwenden

Lies `LEARNINGS.md` in diesem Verzeichnis, um bekannte Anti-Patterns zu vermeiden.
