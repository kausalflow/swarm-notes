---
# CSL-compatible fields
title: "DeRegiME: Deep Regime Mixtures for Probabilistic Forecasting under Distribution Shift"
author:
  - literal: "Kieran Wood"
  - literal: "Stefan Zohren"
  - literal: "Stephen J. Roberts"
issued:
  date-parts:
    - [2026, 5, 19]
url: "https://arxiv.org/abs/2605.19231"

# Custom fields
paper_id: "2605.19231"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "gaussian-process"
  - "mixture-of-experts"
architectures:
  []
datasets:
  []
concept_slugs:
  - "deregime"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-22T08:17:14Z"
created_at: "2026-05-22T08:17:14Z"
---

# DeRegiME: Deep Regime Mixtures for Probabilistic Forecasting under Distribution Shift

**Authors**: Kieran Wood, Stefan Zohren, Stephen J. Roberts
**Date**: 2026-05-19
**Paper ID**: [openalex:2605.19231](https://arxiv.org/abs/2605.19231)

## Summary

DeRegiME is a multi-horizon probabilistic forecasting framework that addresses distribution shift by separating latent uncertainty regimes from the primary signal. Unlike traditional mixture heads, it employs a sparse variational Gaussian process with a nonstationary regime-mixing kernel to softly assign forecast locations to learned residual patterns. This approach provides an interpretable decomposition of mean, residual, and noise, significantly improving predictive performance under various types of non-stationarity.

## Key Contributions

- Introduced DeRegiME, a direct multi-horizon probabilistic forecasting framework that uses a sparse variational Gaussian process gate for interpretable mean-residual-noise decomposition.
- Enabled explicit modeling of latent residual uncertainty regimes, allowing the framework to better handle abrupt, gradual, and horizon-dependent distribution shifts.
- Demonstrated state-of-the-art performance across ten time-series benchmarks, achieving a 20.3% improvement in negative log predictive density (NLPD) over standard deep probabilistic baselines.

## Open Questions & Future Work

- [[amortization-of-regime-uncertainty-parameters]]

## Key Concepts

- [[deregime]]: A direct multi-horizon probabilistic forecaster that uses a sparse variational Gaussian process to softly assign forecast locations to latent uncertainty regimes.

## Archivist Review

I have approved the core framework 'DeRegiME' as a distinct approach to probabilistic forecasting that separates signal from residual uncertainty. I have also formulated a targeted open question regarding the amortization of regime parameters, focusing on the limitation of fixed base kernels and the need for cross-dataset parameter sharing in modern foundation model architectures. All other candidates were rejected as they were either generic or lacked sufficient potential for reusability.

### Approved Concepts
- Deep Regime Mixture of Experts (DeRegiME): It introduces a novel architectural paradigm for probabilistic forecasting that explicitly models residual uncertainty regimes via a sparse Gaussian process gate, rather than simple mixture heads.

### Approved Open Questions
- Amortizing Regime Uncertainty Parameters: The current reliance on isotropic kernels limits the model's expressive capacity in complex regimes, and lack of amortization hinders the ability to leverage cross-dataset information.

## Links

- [Abstract](https://arxiv.org/abs/2605.19231)
- [PDF](https://arxiv.org/pdf/2605.19231)

