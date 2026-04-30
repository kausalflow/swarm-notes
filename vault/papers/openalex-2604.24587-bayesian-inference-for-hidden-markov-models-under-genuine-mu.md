---
# CSL-compatible fields
title: "Bayesian inference for hidden Markov models under genuine multimodality with application to ecological time series"
author:
  - literal: "Marco A. Gallegos-Herrada"
  - literal: "Vianey Leos-Barajas"
  - literal: "Jeffrey S. Rosenthal"
issued:
  date-parts:
    - [2026, 4, 27]
url: "https://arxiv.org/abs/2604.24587"

# Custom fields
paper_id: "2604.24587"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-30T07:24:12Z"
created_at: "2026-04-30T07:24:12Z"
---

# Bayesian inference for hidden Markov models under genuine multimodality with application to ecological time series

**Authors**: Marco A. Gallegos-Herrada, Vianey Leos-Barajas, Jeffrey S. Rosenthal
**Date**: 2026-04-27
**Paper ID**: [openalex:2604.24587](https://arxiv.org/abs/2604.24587)

## Summary

This paper addresses the difficulty of Bayesian inference in hidden Markov models (HMMs) caused by multimodality in the likelihood and posterior distributions. The authors reveal standard pitfalls when applying the parallel tempering (PT) algorithm to HMMs and propose remediations alongside new non-informative priors for better posterior exploration. Their approach is validated on real-world ecological time series, specifically modeling blue whale dive patterns and the influence of sound stimuli on animal behavior.

## Key Contributions

- Identifies and addresses implementation pitfalls in the parallel tempering algorithm for HMMs that cause poor exploration of complex, multimodal posterior distributions.
- Introduces new non-informative prior distributions specifically designed to improve posterior distribution exploration in Bayesian HMMs.
- Demonstrates the framework's effectiveness through analysis of blue whale dive behavior using 3-state HMMs, including models with behavioral covariates.

## Open Questions & Future Work

- [[optimal-swap-acceptance-rate-hmm]]
- [[hmm-multimodality-validation-diagnostics]]

## Archivist Review

The paper provides a focused analysis on the technical challenges of Bayesian inference in hidden Markov models (HMMs) when facing genuine multimodality. I approved the two proposed open questions as they address fundamental, non-trivial bottlenecks in HMM inference and validation that transcend the specific application to whale movement data. No concepts were approved as the improvements mentioned, while useful, are specific refinements to existing algorithms rather than novel architectural or methodological frameworks.

### Approved Open Questions
- Optimal swap rate for HMMs: Efficient exploration of multimodal posteriors in HMMs is highly sensitive to the temperature schedule; establishing a theoretically grounded optimal swap rate would improve the consistency and computational efficiency of Bayesian inference for these models.
- Validating HMM posterior multimodality: Without clear diagnostic tools, practitioners risk over-interpreting minor modes, leading to potentially biased or misleading biological and scientific conclusions based on spurious local maxima.

## Links

- [Abstract](https://arxiv.org/abs/2604.24587)
- [PDF](https://arxiv.org/pdf/2604.24587)

