---
# CSL-compatible fields
title: "Local and Global Recursive Ridge Regression for Online Residual Correction of Frozen Multivariate Forecasters under Label Delay"
author:
  - literal: "Takumi Fujimoto"
  - literal: "Hiroaki Nishi"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2610.29604"

# Custom fields
paper_id: "2610.29604"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "efficient-transformer"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "GeneralMLSkill"
processed_at: "2026-10-24T09:12:17Z"
created_at: "2026-10-24T09:12:17Z"
---

# Local and Global Recursive Ridge Regression for Online Residual Correction of Frozen Multivariate Forecasters under Label Delay

**Authors**: Takumi Fujimoto, Hiroaki Nishi
**Date**: 2026-10-21
**Paper ID**: [openalex:2610.29604](https://arxiv.org/abs/2610.29604)

## Summary

This paper proposes DRiC, a method for online residual correction of frozen multivariate time series forecasters under label delay. By fitting recursive ridge regressions on leading discrete cosine transform coefficients of forecasts, inputs, and residuals, DRiC achieves substantial error reduction while maintaining a minimal, non-expanding memory footprint. Local and global variants provide flexible trade-offs between per-channel adaptation and memory efficiency, while an error-scale guard ensures robustness against anomalous or missing data. Extensive evaluations across multiple backbones and datasets demonstrate that DRiC significantly outperforms prior state-of-the-art online correction baselines while requiring a fraction of their retained state.

## Key Contributions

- Proposes DRiC (DCT Ridge Corrector), an online residual correction method for frozen multi-horizon forecasters under label delay using recursive ridge regression on discrete cosine transform (DCT) coefficients.
- Introduces local (DRiC-L) and global (DRiC-G) variants to trade off between channel-specific adaptation and compact state sizes that do not scale with channel count.
- Implements a guard mechanism that tracks running error scales to skip updates on anomalous blocks and clip issued corrections, preventing severe degradation on noisy or missing data.
- Demonstrates superior error reduction and state efficiency across 126 evaluation conditions using DLinear, PatchTST, and iTransformer backbones on seven prominent time series datasets.

## Limitations

DRiC-G and DRiC-L can underperform compared to heavier, non-compact baseline methods on extremely high-channel datasets like Traffic where large state capacities are advantageous.

## Archivist Review

We applied strict selection standards, rejecting the paper-local open question concerning historical context window trade-offs for DCT-based correction because it is an incremental hyperparameter investigation rather than a foundational bottleneck. No standalone concepts met the threshold for vault inclusion.

### Rejected Candidates
- [open_question] Optimal Context Window for Residual Correction (`optimal-context-window-residual-correction`) - paper_local: The question explores a specific hyperparameter/feature design trade-off regarding historical context length in online residual correction, which is too narrow and paper-local.

## Links

- [Abstract](https://arxiv.org/abs/2610.29604)
- [PDF](https://arxiv.org/pdf/2610.29604)

