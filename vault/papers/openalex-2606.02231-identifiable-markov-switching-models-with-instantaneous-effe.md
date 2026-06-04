---
# CSL-compatible fields
title: "Identifiable Markov Switching Models with Instantaneous Effects and Exponential Families"
author:
  - literal: "Roel Hulsman"
  - literal: "Carles Balsells-Rodas"
  - literal: "Sara Magliacane"
issued:
  date-parts:
    - [2026, 6, 1]
url: "https://arxiv.org/abs/2606.02231"

# Custom fields
paper_id: "2606.02231"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "causal-inference"
architectures:
  []
datasets:
  []
concept_slugs:
  - "flowmsm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-04T08:43:46Z"
created_at: "2026-06-04T08:43:46Z"
---

# Identifiable Markov Switching Models with Instantaneous Effects and Exponential Families

**Authors**: Roel Hulsman, Carles Balsells-Rodas, Sara Magliacane
**Date**: 2026-06-01
**Paper ID**: [openalex:2606.02231](https://arxiv.org/abs/2606.02231)

## Summary

This paper addresses the problem of identifying latent regimes and causal structures in non-stationary time series exhibiting nonlinear, non-Gaussian dynamics and instantaneous effects. The authors provide theoretical identifiability conditions for Markov Switching Models (MSM) incorporating temporal regime dependencies and variables from the exponential family. They introduce FlowMSM, a regime detection framework that functions as a wrapper for stationary causal discovery methods to enable the analysis of non-stationary processes. Performance is validated through experiments on both synthetic and real-world financial economics datasets.

## Key Contributions

- Establishes formal identifiability conditions for latent regimes and causal structures in Markov Switching Models with nonlinear lagged and instantaneous effects.
- Introduces FlowMSM, a modular framework for regime detection that facilitates causal discovery in non-stationary, non-Gaussian temporal data.
- Demonstrates that the proposed theory and method effectively identify regimes and causal dependencies on synthetic benchmarks and financial economics data.

## Open Questions & Future Work

- [[observation-dependent-regimes-msm]]
- [[identifiability-relaxed-noise-assumptions]]

## Key Concepts

- [[flowmsm]]: A modular framework for detecting latent regimes in non-stationary time series that enables the application of stationary causal discovery methods to non-stationary data.

## Archivist Review

The paper provides a significant theoretical contribution to causal discovery in non-stationary settings via MSMs. The FlowMSM framework is approved as it offers a reusable, modular strategy for regime detection. The two open questions are approved as they address fundamental theoretical bottlenecks—observation dependency and strict noise/function requirements—that restrict the generalizability of causal discovery models. No datasets were approved as they were generic financial benchmarks.

### Approved Concepts
- FlowMSM: FlowMSM provides a novel framework for detecting latent regimes in non-stationary time series, addressing the challenge of simultaneous instantaneous effects and regime-dependent causal structure recovery.

### Approved Open Questions
- Observation-dependent MSMs identification: This is a fundamental limitation in the applicability of MSMs to many physical and economic systems where observation-driven regime transitions are common.
- Identifiability under relaxed assumptions: Moving beyond these strict assumptions is crucial to validating the framework in environments where noise distributions are not strictly exponential and systems may not be real-analytic.

## Links

- [Abstract](https://arxiv.org/abs/2606.02231)
- [PDF](https://arxiv.org/pdf/2606.02231)

