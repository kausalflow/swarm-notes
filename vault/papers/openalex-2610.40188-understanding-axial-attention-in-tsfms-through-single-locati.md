---
# CSL-compatible fields
title: "Understanding axial attention in TSFMs through single location regression"
author:
  - literal: "Andrei-Tiberiu Pantea"
  - literal: "Aymeric Dieuleveut"
issued:
  date-parts:
    - [2026, 10, 29]
url: "https://arxiv.org/abs/2610.40188"

# Custom fields
paper_id: "2610.40188"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "transformer"
  - "attention-mechanism"
  - "self-attention"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-01T11:34:14Z"
created_at: "2026-11-01T11:34:14Z"
---

# Understanding axial attention in TSFMs through single location regression

**Authors**: Andrei-Tiberiu Pantea, Aymeric Dieuleveut
**Date**: 2026-10-29
**Paper ID**: [openalex:2610.40188](https://arxiv.org/abs/2610.40188)

## Summary

This paper investigates the theoretical properties of axial attention in Time Series Foundation Models (TSFMs) by extending the Single Location Regression framework to 2D structured data. The authors propose an analytically tractable axial attention predictor, proving it achieves Bayes optimality under specific asymptotic regimes while simpler semi-linear models fail. Additionally, they prove the global convergence of Projected Gradient Descent under appropriate temperature scaling, supported by numerical experiments emphasizing inverse temperature scheduling.

## Key Contributions

- Extended the Single Location Regression framework to 2D structured data to analyze axial attention mechanisms in time series foundation models.
- Proved that an analytically tractable axial attention predictor achieves Bayes optimality under a specific asymptotic regime, while semi-linear simplifications fail.
- Proved global convergence of Projected Gradient Descent to optimal oracle parameters under specific temperature scaling.
- Validated theoretical findings with extensive numerical experiments demonstrating the importance of inverse temperature scheduling.

## Archivist Review

Rigorously applied the vault policy: rejected the primary concept because it originates in prior work (Marion et al., 2025) and rejected the open question as a routine multi-head extension. Approved zero candidates to maintain high vault selectivity.

### Rejected Candidates
- [concept] Single Location Regression (`single-location-regression`) - not_novel: Single Location Regression is introduced by Marion et al. (2025) rather than being a novel conceptual contribution of this paper.
- [open_question] Multi-Token Axial Attention Regression (`multi-token-axial-attention-regression`) - low_impact: The open question is a routine extension of single-token analysis to multi-head settings without a deeply specified theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.40188)
- [PDF](https://arxiv.org/pdf/2610.40188)

