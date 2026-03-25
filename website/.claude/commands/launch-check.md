---
description: Run a production-readiness check across all skill KPIs
---

# Launch Check

Führe einen umfassenden Production-Readiness-Check durch, der alle Skill-KPIs auf einmal misst.

## Lighthouse (alle 4 Kategorien)

Wenn ein Server läuft (dev oder preview), Lighthouse ausführen und ALLE 4 Scores reporten:

```bash
npx lighthouse <URL> --output=json --output-path=./lighthouse-report.json --chrome-flags="--headless --no-sandbox"
```

| Kategorie | Ziel | Verantwortlicher Skill |
|-----------|------|----------------------|
| Performance | >90 | `ui-design` |
| Accessibility | >90 | `accessibility` |
| Best Practices | >90 | `qa` |
| SEO | >90 | `content-seo` |

Zusätzlich aus Performance die Detail-Metriken extrahieren:
- FCP (First Contentful Paint) → Ziel <1.8s
- LCP (Largest Contentful Paint) → Ziel <2.5s
- TBT (Total Blocking Time) → Ziel <200ms
- CLS (Cumulative Layout Shift) → Ziel <0.1

## Skill-spezifische Checks

### 1. Astro Framework
```bash
npx tsc --noEmit 2>&1 | grep "error TS" | wc -l
npm run build
```
- TypeScript Errors: Ziel 0
- Build: Muss durchlaufen, keine Warnings

### 2. Tailwind CSS
Grep-Checks (kein Build nötig):
- Hardcoded Colors: `(bg|text|border)-(red|blue|green|yellow|purple|pink|gray|slate|zinc)-[0-9]+` in `src/**/*.astro`
- Inline Styles: `style="` in `src/**/*.astro`
- tailwind.config.mjs: Darf nicht existieren

### 3. QA / Code-Qualität
```bash
npm run lint
npm run format:check
```
- Lighthouse Best Practices: >90
- ESLint Errors: Ziel 0
- ESLint Warnings: Ziel 0
- Formatting Issues: Ziel 0

### 4. Accessibility
- Lighthouse Accessibility: >90
- Pa11y Errors: 0 (`npx pa11y <URL> --reporter=json`)
- Images ohne Alt: `<img` ohne `alt=` in `src/`
- Buttons ohne Label: `<button` ohne Text-Content oder `aria-label`

### 5. Content & SEO
- Lighthouse SEO: >90
- Seiten ohne Description: `.astro` Dateien in `src/pages/` ohne `description` Prop
- Heading-Hierarchie: Prüfe auf übersprungene Ebenen

### 6. UI/UX Design
- Lighthouse Performance: >90 (FCP, LCP, TBT, CLS)
- Konsistente Section-Paddings prüfen
- Heading-Skala prüfen

## Output-Format

Ergebnisse als übersichtlichen Report ausgeben:

```markdown
## Launch Check Results

### ✅ Astro Framework
- TypeScript Errors: 0
- Build: OK (X.Xs)

### ✅ Tailwind CSS
- Hardcoded Colors: 0
- Inline Styles: 0
- tailwind.config.mjs: nicht vorhanden ✓

### ⚠️ QA / Code-Qualität
- ESLint Errors: 0
- ESLint Warnings: 3
- Formatting: OK

### ✅ Accessibility
- Images ohne Alt: 0
- Buttons ohne Label: 0

### ❌ Content & SEO
- 3 Seiten ohne meta description
- Lighthouse SEO: nicht gemessen (Server nicht aktiv)

### ✅ UI/UX Design
- Section-Paddings: konsistent
- Heading-Hierarchie: OK

---

## Empfehlungen
1. [Prioritisierte Fixes, höchste Priorität zuerst]
2. [...]
```

### Status-Legende
- ✅ = Alle KPIs erfüllt
- ⚠️ = Warnings, aber keine Blocker
- ❌ = Fehler, die vor Launch gefixt werden müssen

## Hinweise

- Lighthouse-Checks erfordern einen laufenden Dev-Server (`npm run dev`)
- Pa11y erfordert Installation (`npx pa11y`)
- Für Details zu einzelnen Skills: die jeweilige SKILL.md konsultieren
