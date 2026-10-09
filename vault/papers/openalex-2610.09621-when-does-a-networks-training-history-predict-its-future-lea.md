---
# CSL-compatible fields
title: "When does a network's training history predict its future learning better than its current state? Evidence from a response probe and a forecasting screen"
author:
  - literal: "M. Hofmann"
  - literal: "Patrick Mäder"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2610.09621"

# Custom fields
paper_id: "2610.09621"
paper_source: "openalex"
domain: "nlp"
tags:
  - "pre-training"
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
processed_at: "2026-10-09T11:36:07Z"
created_at: "2026-10-09T11:36:07Z"
---

# When does a network's training history predict its future learning better than its current state? Evidence from a response probe and a forecasting screen

**Authors**: M. Hofmann, Patrick Mäder
**Date**: 2026-10-07
**Paper ID**: [openalex:2610.09621](https://arxiv.org/abs/2610.09621)

## Summary

This paper investigates whether a neural network's training history predicts its future learning better than its current state. Using multi-layer perceptrons under various history regimes and a response probe, as well as a companion screen on synthetic regression runs, the authors find that training history improves predictions only when the current state is not yet informative about the target. Specifically, low-dimensional history states did not outperform current state models in short probe tasks, and history-based forecasting of final error became indistinguishable from current validation error after initial epochs.

## Key Contributions

- Demonstrated that a small history state of at most four dimensions did not improve upon a calibrated model of the current state for predicting future learning measured by a short probe.
- Conducted a companion screen on 1,560 synthetic regression runs showing that history models forecast the final error better than the current validation error after 12 of up to 240 epochs, but became indistinguishable after 48 epochs.
- Established across both studies that training history is informative only while the current state is not yet informative about the target.

## Open Questions & Future Work

- [[unified-horizon-training-history-prediction]]

## Archivist Review

Applied strict selectivity standards. The only candidate provided was an open question, which is a duplicate or heavily overlaps with existing vault questions on long-horizon temporal prediction limits and state-versus-history modeling boundaries. Therefore, all candidates were rejected to maintain vault cleanliness.

### Approved Open Questions
- Varying Target Horizon Within Systems: Crucial for unifying disparate findings on learning curves and plasticity, helping establish precise boundaries for when checkpoint-only monitoring is sufficient versus when full trajectory telemetry is required.

### Rejected Candidates
- [open_question] Varying Target Horizon Within Systems (`unified-horizon-training-history-prediction`) - duplicate_existing: duplicate_existing

## Links

- [Abstract](https://arxiv.org/abs/2610.09621)
- [PDF](https://arxiv.org/pdf/2610.09621)

