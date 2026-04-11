---
# CSL-compatible fields
title: "SBBTS: A Unified Schrödinger-Bass Framework for Synthetic Financial Time Series"
author:
  - literal: "Alexandre Alouadi"
  - literal: "Grégoire Loeper"
  - literal: "Célian Marsala"
  - literal: "Othmane Mazhar"
  - literal: "Huyên Pham"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2604.07159"

# Custom fields
paper_id: "2604.07159"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "synthetic-data-augmentation"
  - "diffusion-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "schrodinger-bass-bridge-for-time-series"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:53:51Z"
created_at: "2026-04-11T05:53:51Z"
---

# SBBTS: A Unified Schrödinger-Bass Framework for Synthetic Financial Time Series

**Authors**: Alexandre Alouadi, Grégoire Loeper, Célian Marsala, Othmane Mazhar, Huyên Pham
**Date**: 2026-04-08
**Paper ID**: [openalex:2604.07159](https://arxiv.org/abs/2604.07159)

## Summary

The paper introduces the Schrödinger-Bass Bridge for Time Series (SBBTS), a framework designed to generate synthetic time series that capture both marginal distributions and temporal dynamics. By addressing the limitations of existing methods that struggle to jointly model drift and stochastic volatility, SBBTS enables efficient learning through a decomposition into conditional transport problems. Empirical results on the Heston model and S&P 500 data show that SBBTS accurately recovers stochastic volatility parameters and effectively serves as a data augmentation tool to enhance financial forecasting performance.

## Key Contributions

- Introduces SBBTS, a unified framework for generating synthetic financial time series by jointly calibrating drift and volatility.
- Enables tractable decomposition into conditional transport problems, facilitating efficient learning of multi-step temporal dynamics.
- Demonstrates that SBBTS-generated synthetic data improves downstream forecasting performance, resulting in higher Sharpe ratios compared to models trained only on real data.

## Open Questions & Future Work

- [[sbbts-convergence-guarantees]]

## Key Concepts

- [[schrodinger-bass-bridge-for-time-series]]: A unified framework extending Schrödinger-Bass formulations to multi-step time series for joint drift and volatility modeling.

## Archivist Review

I approved the SBBTS concept as it represents a distinct advancement in synthetic financial time series generation that bridges diffusion and transport methods. I also approved the convergence open question due to the framework's reliance on iterative neural training in a high-stakes domain. I rejected the beta-calibration question as it describes standard hyperparameter tuning rather than a fundamental research bottleneck.

### Approved Concepts
- Schrödinger-Bass Bridge for Time Series: It provides a novel mathematical framework to jointly calibrate drift and volatility in synthetic time series generation, overcoming limitations of existing diffusion-based and martingale transport methods.

### Approved Open Questions
- Formal convergence of SBBTS: Providing theoretical convergence guarantees is essential for the reliability and trustworthiness of generative models in high-stakes financial applications, where the stability of the learned drift and volatility is critical.

### Rejected Candidates
- [open_question] Systematic calibration of β (`sbbts-beta-calibration`) - generic: Hyperparameter tuning is a routine technical implementation detail rather than an unresolved foundational research problem.

## Links

- [Abstract](https://arxiv.org/abs/2604.07159)
- [PDF](https://arxiv.org/pdf/2604.07159)

