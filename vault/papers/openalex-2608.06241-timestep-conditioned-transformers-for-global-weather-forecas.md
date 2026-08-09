---
# CSL-compatible fields
title: "Timestep-Conditioned Transformers for Global Weather Forecasting"
author:
  - literal: "Sam Levang"
  - literal: "Fran Bartolić"
  - literal: "Ty Dickinson"
  - literal: "Chase Dwelle"
  - literal: "Paulius Rauba"
  - literal: "Viktor Cikojevic"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2608.06241"

# Custom fields
paper_id: "2608.06241"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "forecasting"
  - "time-series"
  - "autoregressive"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-09T05:40:21Z"
created_at: "2026-08-09T05:40:21Z"
---

# Timestep-Conditioned Transformers for Global Weather Forecasting

**Authors**: Sam Levang, Fran Bartolić, Ty Dickinson, Chase Dwelle, Paulius Rauba, Viktor Cikojevic
**Date**: 2026-08-06
**Paper ID**: [openalex:2608.06241](https://arxiv.org/abs/2608.06241)

## Summary

This paper introduces GEM-3, a probabilistic global weather forecasting model that overcomes the traditional trade-off between fixed short and long autoregressive timesteps through explicit multi-timestep inference. Utilizing a single set of trained weights whose timestep can be configured at inference time, GEM-3 balances sub-daily predictability and long-range stability. Built upon a lightweight neighborhood-attention transformer architecture with roughly 134 million parameters, GEM-3 achieves near-SOTA probabilistic skill and stable extended-range rollouts via mixed-timestep training.

## Key Contributions

- Introduces GEM-3, a probabilistic global weather forecasting model featuring explicit multi-timestep inference that allows configuring the model timestep at inference time using a single set of trained weights.
- Demonstrates that mixed-timestep training consistently improves rollout stability relative to timestep-specialist models.
- Utilizes a lightweight neighborhood-attention transformer architecture with approximately 134 million parameters on an equirectangular grid, achieving near-SOTA medium-range probabilistic skill and stable extended-range rollouts.

## Archivist Review

Applied strict selectivity standards. The paper proposes a domain-specific weather forecasting architecture and training technique (GEM-3) that, while effective for meteorology, does not introduce standalone foundational mechanisms or open questions of general machine learning significance.

### Rejected Candidates
- [open_question] Scaling Timestep Range in Weather Models (`scaling-timestep-range-in-global-weather-models`) - low_impact: The question deals with specific scalingtrade-offs of weather modeling architectures and does not represent a broad, reusable machine learning research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.06241)
- [PDF](https://arxiv.org/pdf/2608.06241)

