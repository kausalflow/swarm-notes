# research-cruise 🚀

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

## Directory Structure

```
research-cruise/
├── .github/
│   └── workflows/
│       └── autonomous-tracker.yml   # CI/CD pipeline
├── vault/
│   ├── papers/                      # One .md file per paper
│   ├── concepts/                    # Auto-generated concept stubs
│   └── datasets/                    # Dataset stubs
├── src/
│   ├── config.py                    # Configuration & env vars
│   ├── vault_manager.py             # Staging pattern (tmp_vault → vault)
│   ├── watcher.py                   # ArXiv API watcher agent
│   ├── router.py                    # Skill registry router
│   ├── analyst.py                   # pydantic-ai extraction agent
│   ├── vault_writer.py              # Markdown writer + public_feed.json
│   ├── federation.py                # Hive Mind federation agent
│   └── main.py                      # Pipeline orchestrator
├── taxonomy.json                    # Controlled vocabulary (tags, domains)
├── public_feed.json                 # Rolling feed of last 20 papers (for federation)
└── requirements.txt
```

## Quick Start

### Prerequisites

- Python 3.11+
- An OpenAI-compatible API key

### Local Run

```bash
# Install dependencies
pip install -r requirements.txt

# Set your API key
export LLM_API_KEY="sk-..."

# Optionally customise keywords
export ARXIV_KEYWORDS="mamba,diffusion model,retrieval augmented generation"

# Run the pipeline
python -m src.main
```

### Configuration (Environment Variables)

| Variable | Default | Description |
|---|---|---|
| `LLM_API_KEY` | *(required)* | API key for the LLM provider |
| `LLM_MODEL` | `openai:gpt-4o-mini` | pydantic-ai model string |
| `ARXIV_KEYWORDS` | See `config.py` | Comma-separated search terms |
| `ARXIV_MAX_RESULTS_PER_KEYWORD` | `5` | Papers fetched per keyword |
| `ARXIV_TOTAL_CAP` | `20` | Hard cap on total papers per run |
| `FEDERATION_FEEDS` | *(empty)* | Comma-separated external feed URLs |
| `PUBLIC_FEED_MAX_ITEMS` | `20` | Max entries kept in `public_feed.json` |

## CI/CD Setup

1. Fork this repository.
2. Add your API key as a repository secret named **`LLM_API_KEY`** (Settings → Secrets → Actions).
3. The pipeline runs automatically every Monday at 06:00 UTC.  
   You can also trigger it manually from the **Actions** tab using **workflow_dispatch**.

## The Hive Mind (Federation)

Every successful run updates `public_feed.json` at the root of the repository with the metadata and summaries of the last 20 processed papers.

To subscribe to another agent's feed, pass their raw `public_feed.json` URL:

```bash
export FEDERATION_FEEDS="https://raw.githubusercontent.com/alice/research-cruise/main/public_feed.json,https://raw.githubusercontent.com/bob/research-cruise/main/public_feed.json"
python -m src.main
```

Or set `federation_feeds` in the **workflow_dispatch** inputs.

**Conflict resolution:** If an external feed contains a review of a paper that already exists locally, the local metadata is preserved.  The external summary is appended under a `### External Perspectives` section:

```markdown
### External Perspectives

> "Transformers are over-engineered for this dataset." - @Agent_alice
> *(Retrieved 2024-01-15)*
```

## Vault File Format

Each paper note uses hybrid YAML frontmatter (CSL-compatible fields + custom fields):

```yaml
---
# CSL-compatible fields
title: "Attention Is All You Need"
author:
  - literal: "Ashish Vaswani"
issued:
  date-parts:
    - [2017, 6, 12]
url: "https://arxiv.org/abs/1706.03762"

# Custom fields
arxiv_id: "1706.03762"
domain: "nlp"
tags:
  - "transformer"
  - "attention-mechanism"
architectures:
  - "encoder-decoder"
datasets:
  - "WMT 2014"
skill: "NLPSkill"
processed_at: "2024-01-15T06:00:00Z"
---
```

Body sections: **Summary**, **Key Contributions**, **Key Concepts** (with relative links to `../concepts/`), **Datasets**, **Limitations**, **Links**.

## Taxonomy

`taxonomy.json` contains the controlled vocabulary of tags, architectures, and domains injected into the analyst's system prompt.  This prevents LLM hallucination and keeps metadata consistent.  Edit `taxonomy.json` to add new terms.

## License

MIT — see [LICENSE](LICENSE).