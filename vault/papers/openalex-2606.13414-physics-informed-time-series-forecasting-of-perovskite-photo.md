---
# CSL-compatible fields
title: "Physics-informed time-series forecasting of perovskite photoluminescence stability"
author:
  - literal: "Alexander Wieczorek"
  - literal: "Manuel Kober‐Czerny"
  - literal: "Fábio Lopes"
  - literal: "Austin George Kuba"
  - literal: "L. Müller"
  - literal: "Christian M. Wolff"
  - literal: "Jason Hattrick-Simpers"
  - literal: "Sebastian Siol"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.13414"

# Custom fields
paper_id: "2606.13414"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "forecasting"
  - "cnn-lstm-time-series-hybrid"
  - "interpretability"
architectures:
  - "cnn-lstm-time-series-hybrid"
datasets:
  []
concept_slugs:
  - "physics-informed-time-series-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:36:54Z"
created_at: "2026-06-14T08:36:54Z"
---

# Physics-informed time-series forecasting of perovskite photoluminescence stability

**Authors**: Alexander Wieczorek, Manuel Kober‐Czerny, Fábio Lopes, Austin George Kuba, L. Müller, Christian M. Wolff, Jason Hattrick-Simpers, Sebastian Siol
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.13414](https://arxiv.org/abs/2606.13414)

## Summary

This paper presents a physics-informed time-series forecasting approach to accelerate stability evaluations of metal halide perovskites. By integrating physical domain knowledge into a hybrid CNN-LSTM architecture, the model accurately predicts long-term photoluminescence degradation using data from accelerated heat and light stress tests. The methodology improves predictive performance compared to standard baselines while providing essential insights into the stability descriptors governing material degradation.

## Key Contributions

- Introduces a physics-informed CNN-LSTM architecture that predicts long-term photoluminescence degradation of perovskite semiconductors from accelerated stress testing.
- Demonstrates that physics-based featurization enhances model explainability, allowing for the identification of stability descriptors during the degradation process.
- Outperforms traditional time-series forecasting benchmarks on a newly curated dataset of 167 perovskite samples comprising over 86,000 spectra.

## Key Concepts

- [[physics-informed-time-series-forecasting]]: A forecasting approach that incorporates physical domain knowledge into deep learning models to predict long-term material stability.

## Archivist Review

The paper proposes a physics-informed CNN-LSTM approach for material stability forecasting. I approved the concept 'Physics-Informed Time-Series Forecasting' as it represents a robust, reusable paradigm for integrating domain-specific physical laws into time-series models, which is central to the paper's contribution. No other concepts, datasets, or open questions were sufficiently novel or distinct from existing vault entries to warrant standalone notes.

### Approved Concepts
- Physics-Informed Time-Series Forecasting: Integrates physical degradation mechanisms with deep learning to improve predictive reliability and interpretability in materials science.

## Links

- [Abstract](https://arxiv.org/abs/2606.13414)
- [PDF](https://arxiv.org/pdf/2606.13414)

