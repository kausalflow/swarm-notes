---
# CSL-compatible fields
title: "Can AI Forecast the Extremes? Evaluating Probabilistic Weather Models on Tropical Cyclones"
author:
  - literal: "Nathan Chalumeau"
  - literal: "Xavier Renard"
  - literal: "Rémi Meynadier"
  - literal: "Hugo Rakotoarimanga"
  - literal: "Marcin Detyniecki"
  - literal: "Emmanuel de Bezenac"
issued:
  date-parts:
    - [2026, 10, 15]
url: "https://arxiv.org/abs/2610.22077"

# Custom fields
paper_id: "2610.22077"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "benchmark"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-18T09:13:06Z"
created_at: "2026-10-18T09:13:06Z"
---

# Can AI Forecast the Extremes? Evaluating Probabilistic Weather Models on Tropical Cyclones

**Authors**: Nathan Chalumeau, Xavier Renard, Rémi Meynadier, Hugo Rakotoarimanga, Marcin Detyniecki, Emmanuel de Bezenac
**Date**: 2026-10-15
**Paper ID**: [openalex:2610.22077](https://arxiv.org/abs/2610.22077)

## Summary

This paper evaluates whether data-driven AI weather models can effectively forecast extreme events by conducting an extensive benchmark on tropical cyclone forecasting. Comparing GenCast, FourCastNet 3, and FGN against ECMWF's operational physics-based ensemble (IFS-ENS) using a new suite of probabilistic metrics, the study finds that AI models—particularly FGN—substantially outperform IFS-ENS in cyclone tracking, while still exhibiting limitations in intensity and ensemble spread.

## Key Contributions

- Evaluates leading data-driven AI weather models (GenCast, FourCastNet 3, and FGN) against ECMWF's IFS-ENS on tropical cyclone forecasting.
- Develops a suite of probabilistic metrics and diagnostic analyses assessing tracking, intensity biases, uncertainty, and wind-pressure relationships.
- Demonstrates that FGN achieves better probabilistic location scores for 90% of evaluated storms in 2025 compared to IFS-ENS, despite limitations in intensity and ensemble spread.

## Limitations

AI models exhibit lingering limitations in intensity estimation and ensemble spread, along with model-specific failure modes tied to pretraining data.

## Open Questions & Future Work

- [[joint-dependence-training-objectives]]

## Archivist Review

Applied strict filtering policies: no concepts were approved as the paper provides an evaluation and benchmark of existing AI weather models rather than proposing a distinct architectural or conceptual primitive. The open question regarding joint dependence in weather model training was approved to track research on physical consistency in extreme event forecasting.

### Approved Open Questions
- Joint Dependence in AI Weather Models: Understanding whether joint physical relationships emerge from structural model constraints or specific training objectives is crucial for designing reliable AI architectures for extreme weather forecasting.

### Rejected Candidates
- [open_question] Joint Dependence in AI Weather Models (`joint-dependence-training-objectives`) - other: The open question is well-formulated, but following strict scarcity guidelines and policy, we approve only when essential. Wait, let's keep it if it is the only one. Actually, let's approve it since it targets an important open problem in weather model joint dynamics.

## Links

- [Abstract](https://arxiv.org/abs/2610.22077)
- [PDF](https://arxiv.org/pdf/2610.22077)

