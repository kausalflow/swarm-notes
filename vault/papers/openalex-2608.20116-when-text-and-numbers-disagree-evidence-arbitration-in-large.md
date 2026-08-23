---
# CSL-compatible fields
title: "When Text and Numbers Disagree: Evidence Arbitration in Large Language Models"
author:
  - literal: "Mattia Carletti"
  - literal: "Edward Phillips"
  - literal: "Fredrik Gustafsson"
  - literal: "Patitapaban Palo"
  - literal: "Lei Clifton"
  - literal: "Danielle Belgrave"
  - literal: "Xiao Gu"
  - literal: "David A. Clifton"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.20116"

# Custom fields
paper_id: "2608.20116"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "multimodal"
  - "tool-use"
  - "benchmark"
  - "evaluation"
  - "robustness"
  - "reasoning"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-23T05:19:51Z"
created_at: "2026-08-23T05:19:51Z"
---

# When Text and Numbers Disagree: Evidence Arbitration in Large Language Models

**Authors**: Mattia Carletti, Edward Phillips, Fredrik Gustafsson, Patitapaban Palo, Lei Clifton, Danielle Belgrave, Xiao Gu, David A. Clifton
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.20116](https://arxiv.org/abs/2608.20116)

## Summary

This paper investigates how large language models arbitrate between conflicting evidence sources—specifically textual summaries, numerical time series, and external tool outputs—using a controlled synthetic benchmark generated from latent risk trajectories. Across open-weight instruction-tuned models, the authors find that arbitration is systematic rather than random, with models showing strong text-versus-number biases, favoring temporal recency over explicit reliability cues, and over-relying on external forecasts. These findings expose critical failure modes in tool-augmented decision systems when heterogeneous evidence sources disagree.

## Key Contributions

- Introduced a controlled synthetic benchmark utilizing latent risk trajectories to generate conflicting numerical time series and natural language summaries for evaluating evidence arbitration in LLMs.
- Demonstrated across open-weight instruction-tuned models that arbitration behavior is systematic, revealing consistent text-versus-number preferences and over-reliance on external forecasts over direct contextual evidence.
- Identified that LLMs follow temporal recency more consistently than explicit reliability cues, highlighting key failure modes in tool-augmented decision systems.

## Limitations

Evaluated primarily on open-weight instruction-tuned models using synthetic conflicts generated from latent risk trajectories; further work is needed on complex real-world multi-modal decision environments.

## Open Questions & Future Work

- [[real-world-multimodal-evidence-arbitration]]

## Archivist Review

Applied strict selection standards, rejecting generic terms and approving only one open question concerning real-world multimodal evidence arbitration that poses a fundamental challenge for tool-augmented LLM decision systems.

### Approved Open Questions
- Real-World Multimodal Evidence Arbitration: Understanding whether heuristic arbitration strategies observed in synthetic benchmarks persist or shift when facing unconstrained, noisy, and heterogeneous real-world data is critical for safe deployment in high-stakes domains like healthcare and finance.

## Links

- [Abstract](https://arxiv.org/abs/2608.20116)
- [PDF](https://arxiv.org/pdf/2608.20116)

