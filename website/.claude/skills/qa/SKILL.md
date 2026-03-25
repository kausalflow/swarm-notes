---
name: qa
description: Use when completing any task (final validation step), running audits, preparing for deployment, or when ESLint/TypeScript/build errors occur.
---

# QA Skill

## Domain

Testing, Validierung, Code-Qualität, Launch-Readiness

## KPIs

| Metrik | Ziel | Messung |
|--------|------|---------|
| Lighthouse Best Practices | >90 | Lighthouse JSON → `categories.best-practices.score * 100` |
| ESLint Errors | 0 | `npm run lint -- --format json` |
| ESLint Warnings | 0 | `npm run lint -- --format json` |
| Formatting Issues | 0 | `npm run format:check` |
| HTML Validation Errors | 0 | `npx html-validate dist/` |

## Regeln

### Build-Pipeline

```bash
# Vollständige QA-Pipeline
npm run lint          # ESLint Errors/Warnings
npm run format:check  # Prettier Formatting
npx tsc --noEmit      # TypeScript Errors
npm run build         # Astro Build (0 Errors, 0 Warnings)
```

### Pre-Launch-Checklist

#### Content
- [ ] Kein Platzhalter-Content ("Lorem ipsum", "TODO", "FIXME")
- [ ] Alle Links funktionieren (keine `#` oder `javascript:void(0)`)
- [ ] Bilder haben beschreibende Alt-Texte
- [ ] Texte sind korrekturgelesen

#### Branding
- [ ] Logo ersetzt (nicht mehr AstroDeck-Standard)
- [ ] Favicon gesetzt (`public/favicon.svg`)
- [ ] OG-Image erstellt (`public/og-image.png`, 1200×630px)
- [ ] Site-Title und Description in `astro.config.mjs`

#### Legal
- [ ] Impressum vorhanden (DACH-Pflicht)
- [ ] Datenschutzerklärung vorhanden
- [ ] Cookie-Banner konfiguriert (wenn Tracking aktiv)

#### Analytics & Forms
- [ ] Analytics-Code eingebunden (wenn gewünscht)
- [ ] Formulare senden an korrekte Endpoints
- [ ] Formulare haben Honeypot/CAPTCHA

#### Performance
- [ ] Lighthouse Performance >90
- [ ] Bilder optimiert (WebP/AVIF, responsive sizes)
- [ ] Keine unnötigen `client:load` Direktiven
- [ ] External Scripts mit SRI

### Lighthouse-Ziele

| Kategorie | Minimum | Ideal |
|-----------|---------|-------|
| Performance | 90 | 95+ |
| Accessibility | 90 | 95+ |
| Best Practices | 90 | 95+ |
| SEO | 90 | 95+ |

### Responsive-Testing Breakpoints

| Gerät | Breite | Prüfen |
|-------|--------|--------|
| Mobile S | 375px | Layout, Navigation, Text-Größe, Touch-Targets ≥44px, kein Overflow |
| Tablet | 768px | Grid-Umbrüche (1→2 cols), Mobile-Subnav noch sichtbar |
| Laptop | 1024px | Volle Navigation + Sidebar sichtbar, Grid-Layouts (2→3 cols) |
| Desktop | 1280px | Max-Width Container zentriert, keine Stretching-Probleme |

**Responsive Pflicht-Checks:**

- [ ] Jede Seite mit Sidebar hat eine mobile Sub-Navigation (collapsible "On this page" dropdown)
- [ ] `hidden lg:block` Elemente haben IMMER ein mobile Äquivalent (`lg:hidden`)
- [ ] Kein horizontaler Scroll auf 375px Breite (besonders `<pre>` und `<table>`)
- [ ] Navigation erreichbar auf Mobile (Hamburger-Menü ODER Dropdown)
- [ ] Grid-Layouts stacken korrekt: `grid-cols-1` als Base, dann `md:grid-cols-2`
- [ ] Container-Padding steigt mit Viewport: `px-4 sm:px-6 md:px-12`
- [ ] Touch-Targets mindestens 44×44px (Links, Buttons, Nav-Items)

### Dark-Mode-Testing

- [ ] Alle Seiten in Dark Mode prüfen
- [ ] Keine weißen Flächen oder unlesbarer Text
- [ ] Bilder/Icons sichtbar (kein schwarzes Logo auf schwarzem Hintergrund)
- [ ] Toggle funktioniert und persistiert Auswahl

### Cross-Browser

- [ ] Chrome/Edge (Chromium)
- [ ] Firefox
- [ ] Safari (WebKit)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

## Non-Negotiable

Diese Regeln gelten immer — auch unter Zeitdruck, auch bei "ist nur ein kleines Update":

- **Kein Commit ohne `npm run build`.** "Hab nur Text geändert" — auch Content-Änderungen können den Build brechen (fehlende Frontmatter-Felder, kaputte Links).
- **Kein ESLint-Ignore ohne Kommentar.** `// eslint-disable-next-line` ist erlaubt, aber nur mit Begründung warum die Regel hier nicht greift.
- **Kein Überspringen der QA-Pipeline.** "Ist dringend" ist keine Ausnahme. Die Pipeline (`lint → format → tsc → build`) dauert unter 30 Sekunden.
- **Lighthouse immer alle 4 Kategorien.** Nie nur Performance messen und den Rest ignorieren. Ein Score-Drop in einer Kategorie ist ein Blocker.
- **Responsive-Test ist Teil von QA.** "Sieht auf meinem Monitor gut aus" zählt nicht. Mindestens 375px und 1280px müssen geprüft werden.

## Vor dem Anwenden

Lies `LEARNINGS.md` in diesem Verzeichnis, um bekannte Anti-Patterns zu vermeiden.
