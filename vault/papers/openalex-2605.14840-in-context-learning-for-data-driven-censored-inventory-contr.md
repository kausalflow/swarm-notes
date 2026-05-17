---
# CSL-compatible fields
title: "In-Context Learning for Data-Driven Censored Inventory Control"
author:
  - literal: "Sohom Mukherjee"
  - literal: "Anh-Duy Pham"
  - literal: "Richard Pibernik"
  - literal: "Yunbei Xu"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14840"

# Custom fields
paper_id: "2605.14840"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "in-context-learning"
  - "autoregressive"
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  - "superstore-dataset"
concept_slugs:
  - "in-context-generative-posterior-sampling-icgps"
dataset_slugs:
  - "superstore-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:32:32Z"
created_at: "2026-05-17T07:32:32Z"
---

# In-Context Learning for Data-Driven Censored Inventory Control

**Authors**: Sohom Mukherjee, Anh-Duy Pham, Richard Pibernik, Yunbei Xu
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14840](https://arxiv.org/abs/2605.14840)

## Summary

This paper addresses censored inventory control (R-NV) by proposing In-context Generative Posterior Sampling (ICGPS), a framework that leverages meta-trained generative models to perform decision-making via autoregressive completion of latent demand. By reducing censored feedback to bandit convex optimization, the authors prove that ICGPS attains sublinear Bayesian regret bounds tied to predictive completion quality. Empirical results using the ChronosFlow instantiation demonstrate significant robustness to prior mismatch and distribution shift compared to parametric Thompson sampling and UCB baselines, particularly under heavy censoring.

## Key Contributions

- Proposes In-context Generative Posterior Sampling (ICGPS), a plug-in framework for operational decision-making that addresses decision-dependent censoring by learning completions of latent demand.
- Provides theoretical regret bounds for ICGPS, demonstrating that online performance is controlled by offline censored predictive mismatch.
- Instantiates ICGPS with ChronosFlow, achieving robust inventory control performance that outperforms traditional TS and UCB baselines under prior mismatch and heavy censoring.

## Open Questions & Future Work

- [[identifiability-in-censored-inventory-control]]

## Key Concepts

- [[in-context-generative-posterior-sampling-icgps]]: A decision-making framework that uses meta-trained autoregressive generative models to perform posterior sampling for latent variables in censored environments.

## Archivist Review

I approved the ICGPS framework and the open question regarding censored identifiability as they provide a rigorous bridge between generative forecasting and decision-making under uncertainty. The SuperStore dataset is approved as a key standard for inventory control experiments. Other candidates were not submitted, so no further rejections were necessary.

### Approved Concepts
- In-context Generative Posterior Sampling (ICGPS): Introduces a novel framework for decision-making under censoring by leveraging in-context learning to generate posterior samples for latent demand.

### Approved Open Questions
- Identifiability in censored inventory control: Understanding the gap between offline predictive fit and online regret is fundamental for the reliability of data-driven operational decision-making where data is intrinsically missing.

## Datasets

- [[superstore-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2605.14840)
- [PDF](https://arxiv.org/pdf/2605.14840)

