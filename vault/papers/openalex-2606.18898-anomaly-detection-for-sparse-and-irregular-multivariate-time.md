---
# CSL-compatible fields
title: "Anomaly Detection for Sparse and Irregular Multivariate Time Series with Latent SDEs"
author:
  - literal: "Martin Uray"
  - literal: "Dominik Geng"
  - literal: "Florian Gräf"
  - literal: "Stefan Huber"
  - literal: "Roland Kwitt"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.18898"

# Custom fields
paper_id: "2606.18898"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "stochastic-differential-equation"
  - "generative-model"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "latent-sde-anomaly-detection"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:17:00Z"
created_at: "2026-06-20T08:17:00Z"
---

# Anomaly Detection for Sparse and Irregular Multivariate Time Series with Latent SDEs

**Authors**: Martin Uray, Dominik Geng, Florian Gräf, Stefan Huber, Roland Kwitt
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.18898](https://arxiv.org/abs/2606.18898)

## Summary

This paper addresses the challenge of anomaly detection in sparse and irregularly sampled multivariate time series, which conventional models often struggle to process due to assumptions of uniform sampling. The authors introduce a generative approach using latent stochastic differential equations (SDEs) to model the underlying continuous-time dynamics of the data. This framework naturally handles irregular sampling and missing observations while capturing cyclic behaviors. Experimental results demonstrate that this method outperforms existing state-of-the-art models and exhibits superior robustness to severe data sparsity.

## Key Contributions

- Proposes a generative anomaly detection framework leveraging Latent SDEs to model continuous-time dynamics in multivariate time series.
- Provides a robust solution for irregularly sampled and sparse data where conventional uniform-sampling methods fail.
- Achieves state-of-the-art performance across six multivariate time series anomaly detection benchmarks.

## Open Questions & Future Work

- [[latent-torus-for-multi-periodic-dynamics]]

## Key Concepts

- [[latent-sde-anomaly-detection]]: A generative approach for anomaly detection using latent SDEs that inherently models continuous-time dynamics to manage missing data and irregular sampling.

## Archivist Review

The paper provides a principled approach for anomaly detection in sparse, irregular multivariate time series using Latent SDEs. I approved the latent-sde-anomaly-detection concept as it offers a robust, reusable inductive bias for time-series modeling. I also approved the open question regarding the use of latent tori, as it addresses a core limitation in capturing complex multi-periodic dynamics, which is a significant research frontier in generative time-series modeling. No datasets were approved as none were presented as novel or central benchmarks distinct from standard evaluation sets.

### Approved Concepts
- Latent Stochastic Differential Equations for Anomaly Detection: The paper positions latent SDEs as a novel, effective inductive bias specifically for handling irregularities and sparsity in multivariate time series anomaly detection.

### Approved Open Questions
- Latent Torus for Multi-Periodic Dynamics: This addresses a fundamental limitation in representing complex, multi-period cyclical dynamics common in industrial monitoring which currently lack effective inductive bias in standard SDE frameworks.

## Links

- [Abstract](https://arxiv.org/abs/2606.18898)
- [PDF](https://arxiv.org/pdf/2606.18898)

