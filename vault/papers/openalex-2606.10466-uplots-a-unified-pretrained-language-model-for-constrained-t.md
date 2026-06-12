---
# CSL-compatible fields
title: "UPLOTS: A Unified Pretrained Language Model for Constrained Time-series Generation"
author:
  - literal: "Du Yin"
  - literal: "Hao Xue"
  - literal: "Jinliang Deng"
  - literal: "Yang Yang"
  - literal: "Shuang Ao"
  - literal: "Arian Prabowo"
  - literal: "Flora D. Salim"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.10466"

# Custom fields
paper_id: "2606.10466"
paper_source: "openalex"
domain: "time-series"
tags:
  - "language-model"
  - "transformer"
  - "generative-model"
  - "time-series"
  - "forecasting"
  - "data-augmentation"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "prompt-guided-time-series-generation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:53:04Z"
created_at: "2026-06-12T08:53:04Z"
---

# UPLOTS: A Unified Pretrained Language Model for Constrained Time-series Generation

**Authors**: Du Yin, Hao Xue, Jinliang Deng, Yang Yang, Shuang Ao, Arian Prabowo, Flora D. Salim
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.10466](https://arxiv.org/abs/2606.10466)

## Summary

UPLOTS addresses the fragmentation in time-series generation by utilizing a unified, prompt-guided transformer backbone capable of generating time-series under various constraints. By employing a prompt-to-pattern mapping and dynamic multi-dataset loss re-weighting, the model learns to synthesize diverse temporal structures from multiple domains simultaneously. Experiments show that the framework effectively generalizes to held-out constraint combinations and serves as a robust tool for data augmentation in scenarios with limited real-world data.

## Key Contributions

- Introduces UPLOTS, a unified, prompt-guided transformer architecture for constrained time-series generation that eliminates the need for dataset-specific models.
- Implements a novel prompt-to-pattern mapping and dynamic multi-dataset loss re-weighting to internalize diverse temporal structures.
- Demonstrates superior generalization in held-out constraint scenarios and improved data augmentation performance in data-scarce regimes across four real-world benchmarks.

## Open Questions & Future Work

- [[zero-shot-distribution-shift-evaluation-for-tsg]]

## Key Concepts

- [[prompt-guided-time-series-generation]]: A generative approach to time-series modeling where learned prompts control the synthesis of specific temporal patterns.

## Archivist Review

I approved the concept of prompt-guided generation as it captures the architectural shift toward controllable, unified generative modeling, and the open question on zero-shot evaluation as it addresses a fundamental limitation in current foundation model benchmarks for time-series. The proposed 'UPLOTS Framework' was rejected as a local project name in favor of the more descriptive and reusable concept 'Prompt-guided Time-series Generation'. No datasets were approved because the paper relies on established, routine benchmarks rather than introducing a novel one.

### Approved Concepts
- Prompt-guided Time-series Generation: It represents a shift from dataset-specific generation to prompt-controllable, unified generative modeling for time-series.

### Approved Open Questions
- Zero-shot distribution shift evaluation: Verifying zero-shot transferability is essential to determine whether generative frameworks are learning reusable domain-invariant temporal structures or merely memorizing training datasets.

## Links

- [Abstract](https://arxiv.org/abs/2606.10466)
- [PDF](https://arxiv.org/pdf/2606.10466)

