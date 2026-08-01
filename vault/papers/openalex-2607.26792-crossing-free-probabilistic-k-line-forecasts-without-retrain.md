---
# CSL-compatible fields
title: "Crossing-Free Probabilistic K-Line Forecasts Without Retraining"
author:
  - literal: "Runyao Yu"
  - literal: "Yuchen Tao"
  - literal: "Yujie Chen"
  - literal: "Wentao Wang"
  - literal: "Derek W. Bunn"
issued:
  date-parts:
    - [2026, 7, 29]
url: "https://arxiv.org/abs/2607.26792"

# Custom fields
paper_id: "2607.26792"
paper_source: "openalex"
domain: "finance"
tags:
  - "forecasting"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "k-line-quantile-sequential-projection-kqsp"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-01T07:23:12Z"
created_at: "2026-08-01T07:23:12Z"
---

# Crossing-Free Probabilistic K-Line Forecasts Without Retraining

**Authors**: Runyao Yu, Yuchen Tao, Yujie Chen, Wentao Wang, Derek W. Bunn
**Date**: 2026-07-29
**Paper ID**: [openalex:2607.26792](https://arxiv.org/abs/2607.26792)

## Summary

Probabilistic K-line forecasting predicts open-high-low-close (OHLC) prices along with uncertainty, but often suffers from quantile crossing and K-line crossing inconsistencies. Existing solutions typically tackle only one of these issues via specialized architectures or penalized training. To address this, the authors propose K-line--Quantile Sequential Projection (KQSP), a parameter-free and training-free post-hoc reconciliation method applicable to any forecasting model. Experiments show that KQSP reduces both crossing rates to zero while preserving predictive accuracy and introducing minimal corrections.

## Key Contributions

- Introduces K-line--Quantile Sequential Projection (KQSP), a parameter-free and training-free post-hoc reconciliation method for probabilistic OHLC K-line forecasts.
- Simultaneously eliminates both quantile crossing and K-line crossing errors across diverse forecasting models and pretrained foundation models without retraining.
- Demonstrates that KQSP reduces both crossing rates to zero while preserving predictive accuracy and yielding smaller corrections than existing alternatives.

## Open Questions & Future Work

- [[improving-predictive-accuracy-alongside-crossing-elimination]]

## Key Concepts

- [[k-line-quantile-sequential-projection-kqsp]]: A parameter-free and training-free reconciliation method that eliminates both quantile and K-line crossing in probabilistic OHLC forecasts.

## Archivist Review

Approved the core K-line-Quantile Sequential Projection (KQSP) concept as a reusable, training-free post-hoc reconciliation method for financial forecasting. Approved one clear open question regarding the trade-off between post-hoc consistency correction and predictive accuracy under model bias. No datasets met the strict novelty and naming criteria for standalone vault notes.

### Approved Concepts
- K-line-Quantile Sequential Projection (KQSP): It introduces a parameter-free and training-free reconciliation method that simultaneously eliminates both quantile crossing and K-line crossing for probabilistic OHLC forecasts without requiring model retraining.

### Approved Open Questions
- Improving Predictive Accuracy Alongside Crossing Elimination: This is technically important because post-hoc correction methods currently risk preserving underlying model bias or poor predictions despite achieving structural consistency.

## Links

- [Abstract](https://arxiv.org/abs/2607.26792)
- [PDF](https://arxiv.org/pdf/2607.26792)

