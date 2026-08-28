---
# CSL-compatible fields
title: "Missing the Butterfly and Predicting the Past: Features or Bugs of Accurate AI Weather Models?"
author:
  - literal: "Pedram Hassanzadeh"
  - literal: "Weidong Li"
  - literal: "Y.Qiang Sun"
  - literal: "Jiangdi Wang"
  - literal: "Alexander Wikner"
  - literal: "Justin Finkel"
  - literal: "Jonathan Weare"
issued:
  date-parts:
    - [2026, 8, 25]
url: "https://arxiv.org/abs/2608.25835"

# Custom fields
paper_id: "2608.25835"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
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
processed_at: "2026-08-28T17:00:26Z"
created_at: "2026-08-28T17:00:26Z"
---

# Missing the Butterfly and Predicting the Past: Features or Bugs of Accurate AI Weather Models?

**Authors**: Pedram Hassanzadeh, Weidong Li, Y.Qiang Sun, Jiangdi Wang, Alexander Wikner, Justin Finkel, Jonathan Weare
**Date**: 2026-08-25
**Paper ID**: [openalex:2608.25835](https://arxiv.org/abs/2608.25835)

## Summary

This paper investigates the physical fidelity and unexpected accuracy of AI weather prediction (AIWP) models by examining observation-based reanalysis, a general circulation model, and the Lorenz system. The authors demonstrate that AI models can skillfully backcast (predict the past) and miss the butterfly effect, tracing these phenomena to the coarse-graining of training data. When coarse-graining is reduced, models exhibit more physics-like behavior such as the arrow of time and butterfly-like effects, but their forecast accuracy consequently declines.

## Key Contributions

- Demonstrated that AI weather prediction models can skillfully predict the past (backcast), despite such backcasting appearing to violate the second law of thermodynamics.
- Showed that both forecasting and backcasting models miss the butterfly effect due to the inevitable coarse-graining of training data.
- Revealed that reducing coarse-graining makes AI predictions more physics-like and restores the arrow of time and butterfly effect, but at the cost of declining forecast accuracy.
- Explained AIWP forecast skill as implicitly learning how fast, small scales affect large scales without inheriting rapid error growth.

## Open Questions & Future Work

- [[theoretical-scaling-laws-ai-weather]]

## Archivist Review

Applied strict scarcity and novelty filtering. The paper offers profound insights into coarse-graining, backcasting, and the absence of the butterfly effect in AI weather models, but these are primarily observational and analytical findings rather than reusable algorithmic components. Therefore, no new concepts are approved, while the fundamental open question regarding theoretical scaling laws for AI weather prediction is retained.

### Approved Open Questions
- Theoretical Scaling Laws for AI Weather Models: Understanding the theoretical scaling limits of AI weather models is crucial for predicting data requirements and optimizing resource allocation for future weather and climate foundation models.

### Rejected Candidates
- [concept] Backcasting Analysis in AI Weather Prediction (`backcasting-analysis-ai-weather`) - paper_local: Too paper-specific as an evaluation lens rather than a reusable standalone forecasting mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2608.25835)
- [PDF](https://arxiv.org/pdf/2608.25835)

