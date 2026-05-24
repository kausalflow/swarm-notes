---
# CSL-compatible fields
title: "A Generative Adversarial Graph Neural Network for Synthetic Time Series Data"
author:
  - literal: "Marco Gregnanin"
  - literal: "Johannes De Smedt"
  - literal: "Giorgio Gnecco"
  - literal: "Maurizio Parton"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22215"

# Custom fields
paper_id: "2605.22215"
paper_source: "openalex"
domain: "time-series,finance"
tags:
  - "generative-adversarial-network"
  - "graph-neural-network"
  - "time-series"
  - "lstm"
  - "synthetic-data-augmentation"
  - "gan"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sig-graph-gan"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:45:39Z"
created_at: "2026-05-24T07:45:39Z"
---

# A Generative Adversarial Graph Neural Network for Synthetic Time Series Data

**Authors**: Marco Gregnanin, Johannes De Smedt, Giorgio Gnecco, Maurizio Parton
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22215](https://arxiv.org/abs/2605.22215)

## Summary

The paper presents Sig-Graph GAN, a novel generative model designed to synthesize complex, non-stationary financial time series. By integrating temporal signatures, LSTM-based autoregressive learning, and GNNs trained on visibility graph representations, the model effectively captures both local temporal evolution and global geometric patterns. Empirical evaluations show that this hybrid approach outperforms baseline synthetic data methods in accurately replicating the distribution of logarithmic returns across various stock markets.

## Key Contributions

- Introduces Sig-Graph GAN, a novel generative framework combining time-series signatures, LSTM architectures, and GNNs on visibility graphs to model non-stationary dynamics.
- Demonstrates that integrating geometric graph structures with autoregressive components improves the replication of complex probability distributions in financial logarithmic returns.
- Provides a robust alternative to traditional statistical models that rely on weak stationarity assumptions for synthetic time series generation.

## Open Questions & Future Work

- [[utility-and-architectural-evolution-of-synthetic-time-series-generation]]

## Key Concepts

- [[sig-graph-gan]]: A generative adversarial network that combines time-series signatures, LSTM networks, and visibility-graph-based GNNs to model non-stationary financial time series.

## Archivist Review

I approved the Sig-Graph GAN as it presents a novel hybrid architecture for synthetic time series generation. I also approved one open question concerning the practical utility and architectural refinement of such models, while rejecting the overly broad original open question candidate.

### Approved Concepts
- Sig-Graph GAN: The model is the primary contribution, proposing a unique integration of time-series signatures, autoregressive structures, and graph representations for synthetic data generation.

### Approved Open Questions
- Synthetic data utility and evolution: This highlights critical gaps in practical downstream application and architectural evolution for generative time-series models.

### Rejected Candidates
- [open_question] Future directions for synthetic time-series generation (`future-directions-for-synthetic-time-series-generation`) - other: The original candidate was too broad and listed multiple disparate tasks; it was rewritten as a more focused research question.

## Links

- [Abstract](https://arxiv.org/abs/2605.22215)
- [PDF](https://arxiv.org/pdf/2605.22215)

