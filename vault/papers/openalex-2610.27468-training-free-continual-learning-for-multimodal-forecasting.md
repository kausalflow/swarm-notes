---
# CSL-compatible fields
title: "Training-Free Continual Learning for Multimodal Forecasting via Prompt Evolution"
author:
  - literal: "Laurent Mombaerts"
  - literal: "Jonathan Taws"
  - literal: "Jacopo Gargano"
  - literal: "Dinesh Gaddam"
  - literal: "Kevin George"
  - literal: "Srijan Tiwari"
  - literal: "Shreyas Rajesh"
issued:
  date-parts:
    - [2026, 10, 20]
url: "https://arxiv.org/abs/2610.27468"

# Custom fields
paper_id: "2610.27468"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "multimodal"
  - "continual-learning"
  - "prompt-tuning"
  - "retrieval-augmented-generation"
  - "benchmark"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:39:34Z"
created_at: "2026-10-23T09:39:34Z"
---

# Training-Free Continual Learning for Multimodal Forecasting via Prompt Evolution

**Authors**: Laurent Mombaerts, Jonathan Taws, Jacopo Gargano, Dinesh Gaddam, Kevin George, Srijan Tiwari, Shreyas Rajesh
**Date**: 2026-10-20
**Paper ID**: [openalex:2610.27468](https://arxiv.org/abs/2610.27468)

## Summary

This paper presents a training-free continual learning approach for multimodal time series forecasting by evolving a textual guidance block using outcome-driven reflection within a frozen LLM forecaster's prompt. Evaluated on a strictly contamination-controlled multimodal benchmark spanning search indices, currencies, and commodities with web-retrieved news, the method outperforms traditional time series foundation models while reducing adaptation costs from GPU-days to dollars. The authors further characterize the feedback loop, examine modal suppression phenomena under error-only objectives, and demonstrate successful transferability to newer language models.

## Key Contributions

- Introduces a training-free continual learning framework for multimodal forecasting that uses prompt evolution with outcome-driven reflection to update a guidance block for frozen LLMs.
- Achieves superior performance on a refreshed multimodal benchmark (GM MASE 0.776 vs 0.898 for TabPFN-TS-3) with strict contamination control under strict knowledge cutoff constraints.
- Demonstrates that evolved guidance transfers to more recent models without measurable performance loss while incurring minimal update costs compared to retraining.
- Provides extensions including compiling guidance into executable tools and characterizing the impact of text modalities and short-horizon forecasting advantages.

## Limitations

Error-only objectives silently suppress the text modality, and in-loop improvements overstate out-of-loop gains by 2-3x unless an untouched monitor arbitrates.

## Open Questions & Future Work

- [[multi-period-rolling-continual-deployment]]

## Archivist Review

Approved the open question regarding multi-period rolling continual deployment as it captures a genuine downstream research limitation identified in the paper. Rejected the proposed concept because it represents a paper-local system name/combination rather than a widely reusable standalone ML primitive.

### Approved Open Questions
- Multi-Period Rolling Continual Deployment: Extending continual deployment from single executed cycles to robust multi-period evaluations is essential to prove the practical viability of training-free prompt evolution in production environments subject to continuous structural breaks.

### Rejected Candidates
- [concept] Training-Free Continual Learning via Prompt Evolution (`training-free-continual-learning-for-multimodal-forecasting-via-prompt-evolution`) - paper_local: The core idea of prompt evolution for continual forecasting is a paper-specific combination of general prompt optimization and LLM time-series forecasting rather than a distinct standalone mechanism note.

## Links

- [Abstract](https://arxiv.org/abs/2610.27468)
- [PDF](https://arxiv.org/pdf/2610.27468)

