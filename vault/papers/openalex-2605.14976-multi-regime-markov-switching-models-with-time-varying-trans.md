---
# CSL-compatible fields
title: "Multi-regime Markov-switching models with time-varying transition probabilities: An application to U.S. Treasury yields"
author:
  - literal: "Samuel Modée"
  - literal: "Yushu Li"
  - literal: "Sjur Westgaard"
  - literal: "Stein Andreas Bethuelsen"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14976"

# Custom fields
paper_id: "2605.14976"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "multi-regime-markov-switching-tvtp-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:31:22Z"
created_at: "2026-05-17T07:31:22Z"
---

# Multi-regime Markov-switching models with time-varying transition probabilities: An application to U.S. Treasury yields

**Authors**: Samuel Modée, Yushu Li, Sjur Westgaard, Stein Andreas Bethuelsen
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14976](https://arxiv.org/abs/2605.14976)

## Summary

This paper introduces a generalized Markov-switching model with time-varying transition probabilities (TVTP), extending previous two-regime frameworks to handle K-regime dynamics with regime-specific means and variances. The authors implement the model in an open-source R package and conduct extensive Monte Carlo simulations, revealing critical insights into parameter identifiability—specifically that GAS score coefficients are often non-identifiable. Empirical results using U.S. Treasury yield data indicate that while short-horizon forecasting is robust to model misspecification, accurate regime specification remains crucial for capturing true underlying dynamics.

## Key Contributions

- Generalizes the GAS-based Markov-switching model to a K-regime specification with regime-specific means and variances.
- Demonstrates through simulation that while regime parameters are robust, GAS score coefficients exhibit non-identifiability issues.
- Identifies that one-step point forecasts are robust to TVTP misspecification, whereas filtered regime probabilities are sensitive, highlighting the importance of correct specification for regime interpretation.

## Open Questions & Future Work

- [[gas-model-identifiability-convergence]]

## Key Concepts

- [[multi-regime-markov-switching-tvtp-model]]: A generalized Markov-switching framework with time-varying transition probabilities and regime-specific parameters.

## Archivist Review

The paper is approved for its contribution to generalized Markov-switching models with time-varying transition probabilities. The concept was approved as it formalizes a distinct extension of the GAS model. The open question regarding GAS identifiability is a specific, well-documented bottleneck that is useful to track. I rejected the transition probability functional form question as it is too broad and generic for the vault.

### Approved Concepts
- Multi-regime Markov-switching TVTP model: This generalized framework allows for more flexible regime-switching behavior than standard Markov-switching models by incorporating time-varying transition probabilities.

### Approved Open Questions
- GAS model identifiability issues: The identifiability issue limits the practical application of GAS-based time-varying transition probability models, as current estimation methods frequently fail to converge or provide reliable parameter estimates for the dynamic components.

## Links

- [Abstract](https://arxiv.org/abs/2605.14976)
- [PDF](https://arxiv.org/pdf/2605.14976)

