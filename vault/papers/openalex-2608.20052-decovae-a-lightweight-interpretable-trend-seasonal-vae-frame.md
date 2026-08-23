---
# CSL-compatible fields
title: "DecoVAE: a Lightweight Interpretable Trend-Seasonal VAE Framework for Efficient Probabilistic Time Series Forecasting"
author:
  - literal: "Alexander Marusov"
  - literal: "Dmitry Anikin"
  - literal: "Alexey Zaytsev"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.20052"

# Custom fields
paper_id: "2608.20052"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "variational-autoencoder"
  - "vae"
  - "probabilistic-forecasting"
  - "interpretability"
  - "benchmark"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "decovae"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-23T05:19:07Z"
created_at: "2026-08-23T05:19:07Z"
---

# DecoVAE: a Lightweight Interpretable Trend-Seasonal VAE Framework for Efficient Probabilistic Time Series Forecasting

**Authors**: Alexander Marusov, Dmitry Anikin, Alexey Zaytsev
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.20052](https://arxiv.org/abs/2608.20052)

## Summary

DecoVAE is a lightweight interpretable trend-seasonal VAE framework for probabilistic time series forecasting that explicitly decomposes time series into trend and seasonal components. The trend stream uses a differential regularizer for smoothness, while the seasonal stream utilizes a frequency-domain complex Gaussian VAE to capture amplitude and phase. Across seven benchmarks, DecoVAE achieves substantial accuracy improvements alongside significant reductions in model weight and runtime.

## Key Contributions

- Proposes DecoVAE, a lightweight interpretable trend-seasonal variational autoencoder framework that explicitly decomposes time series into trend and seasonal components using domain-specific inductive biases.
- Applies a structural smoothness differential regularizer (analogous to the Hodrick-Prescott filter) on the latent trajectory for the trend stream and a complex Gaussian VAE operating in the frequency domain for the seasonal stream.
- Achieves accuracy reductions of up to 14.96% in CRPS and 23.30% in NMAE for short-term forecasting, and up to 52.68% and 26.51% for long-term horizons across seven real-world benchmarks.
- Reduces model weight by up to 93% and accelerates runtime speed by up to 74% compared to the second-best competitive baseline.

## Open Questions & Future Work

- [[efficient-probabilistic-time-series-forecasting]]

## Key Concepts

- [[decovae]]: A lightweight interpretable trend-seasonal VAE framework that explicitly decomposes time series into trend and seasonal components for efficient probabilistic forecasting.

## Archivist Review

Approved the central DecoVAE framework concept because it introduces a distinct trend-seasonal VAE architecture with a differential regularizer and complex Gaussian frequency-domain modeling. Also approved the open question regarding efficient probabilistic time series forecasting trade-offs under high-dimensional settings.

### Approved Concepts
- DecoVAE: Core proposed architecture and framework combining trend and seasonal components via VAEs with inductive biases for probabilistic time series forecasting.

### Approved Open Questions
- Efficient Probabilistic Time Series Forecasting: This addresses the persistent quality-computation trade-off in generative probabilistic forecasting models.

## Links

- [Abstract](https://arxiv.org/abs/2608.20052)
- [PDF](https://arxiv.org/pdf/2608.20052)

