---
# CSL-compatible fields
title: "Turning time series into algebraic equations: Symbolic machine learning for interpretable modeling of chaotic time series"
author:
  - literal: "Madhurima Panja"
  - literal: "Grace Younes"
  - literal: "Chittaranjan Hens"
  - literal: "Tanujit Chakraborty"
issued:
  date-parts:
    - [2026, 10, 29]
url: "https://arxiv.org/abs/2603.07261"

# Custom fields
paper_id: "2603.07261"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "interpretability"
  - "explainability"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-31T10:39:15Z"
created_at: "2026-10-31T10:39:15Z"
---

# Turning time series into algebraic equations: Symbolic machine learning for interpretable modeling of chaotic time series

**Authors**: Madhurima Panja, Grace Younes, Chittaranjan Hens, Tanujit Chakraborty
**Date**: 2026-10-29
**Paper ID**: [openalex:2603.07261](https://arxiv.org/abs/2603.07261)

## Summary

This paper introduces two complementary symbolic forecasters designed to learn explicit, interpretable algebraic equations from chaotic time series data to address the black-box limitations of deep learning. The symbolic neural forecaster uses an end-to-end differentiable architecture, whereas the symbolic tree forecaster leverages evolutionary symbolic regression balancing accuracy and complexity. Experiments across 132 low-dimensional chaotic attractors and two real-world datasets demonstrate competitive one-step-ahead forecasting performance paired with transparent analytical insights into underlying dynamics.

## Key Contributions

- Proposed two complementary symbolic forecasters—a symbolic neural forecaster and a symbolic tree forecaster—that learn explicit algebraic equations from chaotic time series.
- Evaluated the approaches on a benchmark of 132 low-dimensional chaotic attractors and two real-world time series (weekly dengue incidence and Niño 3.4 index) using a rolling-window one-step-ahead forecasting setting.
- Demonstrated that symbolic forecasters achieve competitive prediction accuracy while offering transparent analytical equations that reveal underlying system dynamics.

## Open Questions & Future Work

- [[multi-step-symbolic-forecasting-stability]]
- [[multivariate-symbolic-equation-discovery]]

## Archivist Review

Approved two clear open questions concerning multi-step iterative stability and multivariate extension for symbolic time series forecasting. No permanent standalone concepts met the high reusability threshold, and no specific canonical datasets were introduced.

### Approved Open Questions
- Multi-Step Symbolic Forecasting Stability: Assessing multi-step-ahead iterative stability is vital for determining whether symbolic equations can serve as true generative dynamical models rather than short-term autoregressive smoothers.
- Multivariate Symbolic Equation Discovery: Real-world physical and biological systems are driven by multiple interacting variables, making multivariate extension essential for practical scientific discovery.

### Rejected Candidates
- [open_question] Constrained Symbolic Dynamical Modeling (`constrained-symbolic-dynamical-modeling`) - low_impact: Routine future direction regarding physical constraints in symbolic regression that does not introduce a unique transferable paradigm.

## Links

- [Abstract](https://arxiv.org/abs/2603.07261)
- [PDF](https://arxiv.org/pdf/2603.07261)

