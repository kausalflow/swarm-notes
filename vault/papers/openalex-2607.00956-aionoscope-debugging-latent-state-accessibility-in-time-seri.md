---
# CSL-compatible fields
title: "Aionoscope: Debugging Latent-State Accessibility in Time-Series Representations"
author:
  - literal: "Alexander Chemeris"
  - literal: "Ming Jin"
  - literal: "Randall Balestriero"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.00956"

# Custom fields
paper_id: "2607.00956"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "interpretability"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "aionoscope"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:35:37Z"
created_at: "2026-07-04T07:35:37Z"
---

# Aionoscope: Debugging Latent-State Accessibility in Time-Series Representations

**Authors**: Alexander Chemeris, Ming Jin, Randall Balestriero
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.00956](https://arxiv.org/abs/2607.00956)

## Summary

Time-series models are often evaluated on end-task performance, which fails to reveal whether their latent representations capture essential process dynamics like phase or frequency. This paper introduces Aionoscope, a generator-based diagnostic framework that separates process generation from observation to probe latent-state accessibility using synthetic data with precise ground-truth labels. Experimental evaluation across 37 model-plus-adapter systems reveals that while models often successfully represent coarse categorical regimes, they systematically struggle to recover fine-grained dense process states. Aionoscope effectively identifies this representation failure, surfacing latent-state gaps that traditional forecasting metrics overlook.

## Key Contributions

- Introduces Aionoscope, a generator-based framework for probing latent-state accessibility in frozen time-series representations.
- Demonstrates a significant performance gap between coarse-grained regime classification and fine-grained state recovery (e.g., phase/frequency) across 37 tested models.
- Establishes a common diagnostic protocol using Primitive Process Mixtures and pooled linear probes to identify failure modes where models capture signal identity while masking underlying dense process dynamics.

## Open Questions & Future Work

- [[time-series-representation-diagnostics-robustness]]

## Key Concepts

- [[aionoscope]]: A generator-based diagnostic framework for evaluating the accessibility of dense and categorical latent states in frozen time-series representations.

## Archivist Review

Aionoscope is approved as a novel framework for auditing the latent-state transparency of time-series models, distinct from standard predictive benchmarks. The open question is approved for highlighting the fundamental methodological challenge of distinguishing representation failure from probe-limitation in temporal diagnostic tasks.

### Approved Concepts
- Aionoscope: Addresses the critical problem of latent state accessibility in time-series representations by distinguishing between coarse-grained and fine-grained feature recovery.

### Approved Open Questions
- Robustness of representation diagnostics: This question is central to validating the reliability and scope of representation-audit frameworks, ensuring that findings about information masking are robust to the chosen diagnostic protocol.

## Links

- [Abstract](https://arxiv.org/abs/2607.00956)
- [PDF](https://arxiv.org/pdf/2607.00956)

