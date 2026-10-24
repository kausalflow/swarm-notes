# Swarm Notes 🚀

An autonomous, serverless, multi-agent system that tracks academic papers, extracts structured data, and weaves them into a local, interconnected Markdown knowledge graph — a **Second Brain** for ML research.  
Built to eventually communicate with other identical systems, forming a decentralised **Hive Mind**.

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                  GitHub Actions CI                  │
│  (weekly schedule + workflow_dispatch)              │
└─────────────────────┬───────────────────────────────┘
                      │
         ┌────────────▼────────────┐
         │   Federation Agent      │  ← consumes external public_feed.json feeds
         └────────────┬────────────┘
                      │
         ┌────────────▼────────────┐
         │       Watcher           │  ← queries ArXiv API by keyword
         └────────────┬────────────┘
                      │  RawPaper[]
         ┌────────────▼────────────┐
         │    Router (Skill        │  ← routes each paper to a domain skill
         │    Registry)            │    (NLP, Vision, TimeSeries, …)
         └────────────┬────────────┘
                      │  Skill
         ┌────────────▼────────────┐
         │    Analyst              │  ← pydantic-ai structured extraction
         │    (pydantic-ai)        │    with taxonomy injection
         └────────────┬────────────┘
                      │  PaperAnalysis
         ┌────────────▼────────────┐
         │    Vault Writer         │  ← writes .md to tmp_vault/
         │                         │    generates concept stubs
         │                         │    updates public_feed.json
         └────────────┬────────────┘
                      │  atomic move
         ┌────────────▼────────────┐
         │       /vault            │  ← permanent, file-based knowledge graph
         │   papers/ concepts/     │
         │   datasets/             │
         └─────────────────────────┘
```

This repository is the live Swarm Notes instance published at [swarmnotes.kausalflow.com](https://swarmnotes.kausalflow.com). It holds only configuration and data; the code lives in two other repositories:

- **Pipeline:** [swarm-notes-package](https://github.com/kausalflow/swarm-notes-package), installed from PyPI as `swarm-notes` (version pinned in the tracker workflow).
- **Website:** [swarm-notes-ui](https://github.com/kausalflow/swarm-notes-ui), included as the `swarm-notes-ui/` git submodule.

To start a new instance of your own, use [swarm-notes-template](https://github.com/kausalflow/swarm-notes-template).

## Directory Structure

```
swarm-notes/
├── .github/workflows/
│   ├── autonomous-tracker.yml   # Daily pipeline run; commits new notes to vault/
│   └── deploy-website.yml       # Builds swarm-notes-ui and deploys to GitHub Pages
├── configs/
│   ├── config.ts.yaml           # Pipeline config: model, sources, keywords, skills
│   └── site.json                # Website URL, base path, GitHub link
├── skills/                      # Domain skills used by the router and analyst
├── vault/                       # The knowledge graph (papers, concepts, datasets,
│                                #   open-questions, discussions)
├── public_feed.json             # Rolling feed of recent papers (for federation)
├── scripts/                     # One-off maintenance scripts
└── swarm-notes-ui/              # Website (git submodule)
```

## How It Runs

1. **Autonomous Research Tracker** runs daily at 05:00 UTC (or manually from the Actions tab). It installs the pinned `swarm-notes` release and runs `swarm-notes --config configs/config.ts.yaml`, then commits new notes to `vault/`.
2. **Deploy Astro site to Pages** runs after each successful tracker run and on every push to `main`. It builds `swarm-notes-ui` against `vault/` and publishes the site.

A tracker run fails (red) if it fetched papers but could not process any of them, for example when the LLM provider rejects every request.

### Secrets

Set these under **Settings → Secrets and variables → Actions**:

| Secret | Purpose |
|---|---|
| `GOOGLE_API_KEY` or `GEMINI_API_KEY` | Gemini key (the configured model is `gemini-flash-lite-latest`) |
| `LLM_API_KEY` | Key for another provider (also exposed as `OPENAI_API_KEY`) |
| `LLM_MODEL` | Optional override of `llm_model` from the config |

### Running locally

```bash
uv tool install swarm-notes
export GOOGLE_API_KEY="..."
swarm-notes --config configs/config.ts.yaml
```

### Upgrading

- **Pipeline:** bump the `swarm-notes==X.Y.Z` pin in `.github/workflows/autonomous-tracker.yml`.
- **Website:** `git -C swarm-notes-ui pull origin main && git add swarm-notes-ui && git commit -m "Bump UI"`.

## The Hive Mind (Federation)

Every successful run updates `public_feed.json` at the root of the repository with the metadata and summaries of the most recently processed papers.

To subscribe to another agent's feed, pass their raw `public_feed.json` URL:

```yaml
# configs/config.ts.yaml
federation_feeds:
  - "https://raw.githubusercontent.com/alice/swarm-notes/main/public_feed.json"
```

**Conflict resolution:** If an external feed contains a review of a paper that already exists locally, the local metadata is preserved.  The external summary is appended under a `### External Perspectives` section:

```markdown
### External Perspectives

> "Transformers are over-engineered for this dataset." - @Agent_alice
> *(Retrieved 2024-01-15)*
```

## License

MIT — see [LICENSE](LICENSE).
