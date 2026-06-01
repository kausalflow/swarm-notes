---
# CSL-compatible fields
title: "Forecasting generative amplification"
author:
  - literal: "Henning Bahl"
  - literal: "Sascha Diefenbacher"
  - literal: "Nina Elmer"
  - literal: "Tilman Plehn"
  - literal: "Jonas Spinner"
issued:
  date-parts:
    - [2026, 5, 29]
url: "https://arxiv.org/abs/2509.08048"

# Custom fields
paper_id: "2509.08048"
paper_source: "openalex"
domain: "physics"
tags:
  - "generative-adversarial-network"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "averaging-amplification"
  - "differential-amplification"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-01T10:10:29Z"
created_at: "2026-06-01T10:10:29Z"
---

# Forecasting generative amplification

**Authors**: Henning Bahl, Sascha Diefenbacher, Nina Elmer, Tilman Plehn, Jonas Spinner
**Date**: 2026-05-29
**Paper ID**: [openalex:2509.08048](https://arxiv.org/abs/2509.08048)

## Summary

This paper addresses the statistical challenges of using generative networks for large-scale LHC simulations. It proposes two novel methods—averaging amplification and differential amplification—to evaluate the precision and amplification factors of generative models without requiring massive holdout datasets. These techniques allow researchers to verify the statistical integrity of generated events in specific phase-space regions, facilitating more efficient simulation beyond training set sizes.

## Key Contributions

- Introduces 'Averaging amplification', a technique using Bayesian networks or ensembling to estimate generative model precision via phase-space integrals.
- Introduces 'Differential amplification', a hypothesis-testing approach to quantify amplification factors without resolution loss.
- Demonstrates that generative amplification is viable in specific phase-space regions for state-of-the-art LHC event generators.

## Open Questions & Future Work

- [[unification-of-amplification-metrics]]

## Key Concepts

- [[averaging-amplification]]: An estimation method for generative amplification that utilizes Bayesian networks or ensembling to compute the precision of integrals over phase-space volumes.
- [[differential-amplification]]: A method for quantifying generative amplification factors using hypothesis testing that avoids resolution loss.

## Archivist Review

I approved the two core estimation methods, averaging amplification and differential amplification, as they constitute a distinct framework for validating generative scientific simulations without holdout data. I also approved the open question regarding the unification of these metrics, as it identifies a central challenge in standardizing generative uncertainty quantification for physical systems. The remaining candidate was rejected as a meta-analysis category.

### Approved Concepts
- Averaging amplification: Provides a method to estimate generative amplification factors without requiring massive holdout datasets by leveraging integral precision.
- Differential amplification: Enables quantification of generative amplification through hypothesis testing, avoiding the resolution loss typically associated with traditional binning or evaluation methods.

### Approved Open Questions
- Unification of amplification metrics: As generative networks replace classical simulation chains, the lack of a standardized, reliable metric for amplification introduces unknown systematic uncertainties into collider physics analyses. Tracking this allows for the development of benchmarks to trust simulated data at the HL-LHC.

## Links

- [Abstract](https://arxiv.org/abs/2509.08048)
- [PDF](https://arxiv.org/pdf/2509.08048)

