---
name: accessibility
description: Use when creating or modifying any UI element visible to the user, reviewing HTML markup, adding interactive elements, or when Lighthouse Accessibility drops below 90.
---

# Accessibility Skill

## Domain

WCAG 2.1 AA, ARIA, Keyboard Navigation, Kontrast, Screen Readers

## KPIs

| Metrik | Ziel | Messung |
|--------|------|---------|
| Lighthouse Accessibility | >90 | Lighthouse JSON → `categories.accessibility.score * 100` |
| Pa11y Errors | 0 | `npx pa11y <URL> --reporter=json` |
| Images ohne Alt | 0 | Grep: `<img` ohne `alt=` in src/ |

## Regeln

### WCAG 4 Prinzipien

1. **Wahrnehmbar** — Inhalte für alle Sinne zugänglich
2. **Bedienbar** — Keyboard-navigierbar, genug Zeit
3. **Verständlich** — Lesbar, vorhersehbar, fehlertolerant
4. **Robust** — Kompatibel mit Assistive Technologies

### Semantic HTML

```html
<!-- ✅ Semantisch -->
<nav>...</nav>
<main>...</main>
<article>...</article>
<aside>...</aside>
<header>...</header>
<footer>...</footer>
<section aria-labelledby="section-title">
  <h2 id="section-title">...</h2>
</section>

<!-- ❌ Div-Suppe -->
<div class="nav">...</div>
<div class="main">...</div>
```

### ARIA-Patterns

```html
<!-- Buttons mit Icons (ohne sichtbaren Text) -->
<button aria-label="Menü öffnen">
  <MenuIcon aria-hidden="true" />
</button>

<!-- Expandable Content -->
<button aria-expanded="false" aria-controls="panel-1">Toggle</button>
<div id="panel-1" role="region">...</div>

<!-- Live Regions (dynamische Updates) -->
<div aria-live="polite" aria-atomic="true">
  {statusMessage}
</div>

<!-- Dekorative Elemente -->
<img src="decoration.svg" alt="" aria-hidden="true" />
```

### Keyboard-Navigation

- Alle interaktiven Elemente per Tab erreichbar
- Sichtbarer Focus-Indikator: `focus:ring-2 focus:ring-ring focus:ring-offset-2`
- Escape schließt Modals/Dropdowns
- Enter/Space aktiviert Buttons
- Pfeiltasten für Listen/Tabs/Menüs

### Farbkontrast

| Element | Minimum Ratio |
|---------|--------------|
| Normaler Text | 4.5:1 |
| Großer Text (>18pt / >14pt bold) | 3:1 |
| UI-Elemente & Grafiken | 3:1 |

### Focus-Management

```css
/* Basis Focus-Style (bereits in AstroDeck) */
focus:outline-none focus-visible:ring-2 focus-visible:ring-ring

/* Focus bei Modals */
/* Trap focus innerhalb des Modals */
/* Restore focus beim Schließen */
```

### Formulare

```html
<!-- Immer Label mit Input verknüpfen -->
<label for="email">E-Mail</label>
<input id="email" type="email" aria-required="true" aria-describedby="email-help" />
<p id="email-help" class="text-sm text-muted-foreground">Wir senden keine Spam-Mails.</p>

<!-- Fehlermeldungen -->
<input aria-invalid="true" aria-describedby="email-error" />
<p id="email-error" role="alert" class="text-sm text-destructive">Bitte gültige E-Mail eingeben.</p>
```

### Skip-Links

```astro
<!-- Bereits in AstroDeck BaseLayout -->
<a href="#main-content" class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-50 focus:px-4 focus:py-2 focus:bg-background focus:text-foreground focus:rounded-md">
  Zum Inhalt springen
</a>
```

### AstroDeck-spezifische Checks

- [ ] Dark Mode Toggle hat `aria-label` und zeigt aktuellen Zustand
- [ ] Mobile Menu: `aria-expanded`, Focus-Trap, Escape zum Schließen
- [ ] Logo-Link hat beschreibenden `aria-label` (z.B. "AstroDeck — Zur Startseite")
- [ ] Social-Links haben `aria-label` mit Plattform-Name
- [ ] Cookie-Banner: Keyboard-navigierbar, Focus-Trap

## Non-Negotiable

Diese Regeln gelten immer — auch unter Zeitdruck, auch bei "ist nur ein internes Tool":

- **Kein Element ohne alt-Text.** Auch nicht "weil es ein Template ist" — Templates setzen den Standard für tausende Projekte die darauf aufbauen.
- **Kein `div` statt `button` für klickbare Elemente.** Auch nicht "weil es einfacher ist". Ein `div` ist nicht fokussierbar, nicht per Tastatur bedienbar, und wird von Screen Readern ignoriert.
- **Kein Commit ohne Heading-Hierarchie.** "Ist nur eine Landingpage" ist keine Ausrede — Screen Reader navigieren via Headings.
- **Dark Mode ist Pflicht ab Tag 1.** "Machen wir später" funktioniert nicht — CSS-Variablen müssen von Anfang an stimmen, Nachbesserung ist doppelte Arbeit.
- **Keyboard-Navigation ist kein Nice-to-have.** "User nutzen eh nur die Maus" ist falsch — 25% der Nutzer verwenden Tastatur, Assistive Technology oder beides.

## Vor dem Anwenden

Lies `LEARNINGS.md` in diesem Verzeichnis, um bekannte Anti-Patterns zu vermeiden.
