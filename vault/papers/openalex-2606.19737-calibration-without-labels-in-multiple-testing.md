---
# CSL-compatible fields
title: "Calibration without labels in multiple testing"
author:
  - literal: "Adway S. Wadekar"
  - literal: "Jake A. Soloff"
issued:
  date-parts:
    - [2026, 6, 18]
url: "https://arxiv.org/abs/2606.19737"

# Custom fields
paper_id: "2606.19737"
paper_source: "openalex"
domain: "nlp"
tags:
  - "evaluation"
  - "robustness"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-21T08:54:08Z"
created_at: "2026-06-21T08:54:08Z"
---

# Calibration without labels in multiple testing

**Authors**: Adway S. Wadekar, Jake A. Soloff
**Date**: 2026-06-18
**Paper ID**: [openalex:2606.19737](https://arxiv.org/abs/2606.19737)

## Summary

This paper addresses the challenge of calibrating probability claims in multiple hypothesis testing, where ground truth labels are fundamentally unavailable. The authors treat these claims as probabilistic forecasts and derive a pseudo-labeling strategy using ordered p-value spacings to estimate local false discovery rates. This approach enables the application of post-hoc calibration techniques, revealing significant miscalibration in existing q-value metrics across psychology and neuroscience datasets.

## Key Contributions

- Formulates multiple testing error claims as approximately calibrated forecasts of the null hypothesis.
- Introduces a pseudo-label construction method based on ordered p-value spacings to enable stochastic calibration assessment without ground truth labels.
- Demonstrates through a large-scale empirical survey that q-values in psychology and neuroscience literature are often severely miscalibrated.

## Open Questions & Future Work

- [[non-uniform-null-pseudo-label-construction]]

## Archivist Review

The paper presents a methodology for calibrating hypothesis testing error metrics without ground truth, which is a specialized statistical task outside the primary scope of time-series forecasting. While innovative, it does not introduce a reusable architectural or temporal modeling concept relevant to the vault's time-series focus. I have approved the open question regarding null distribution assumptions as it is a fundamental theoretical challenge in statistical calibration that applies to broader predictive tasks.

### Approved Open Questions
- Non-uniform null pseudo-label construction: The current pseudo-labeling framework is restricted to p-values; extending it to other common test statistics would significantly broaden the applicability of post-hoc calibration in statistical modeling and empirical Bayes methods.

### Rejected Candidates
- [open_question] Non-uniform null pseudo-labels (`non-uniform-null-pseudo-labels`) - other: The original candidate title is too brief and ambiguous; I have rewritten it for clarity and precision as a standalone research direction.

## Links

- [Abstract](https://arxiv.org/abs/2606.19737)
- [PDF](https://arxiv.org/pdf/2606.19737)

