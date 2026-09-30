---
# CSL-compatible fields
title: "Domain Generalization under Sampling Pattern Shifts in Irregular Time Series"
author:
  - literal: "Changhun Kim"
  - literal: "Joohyung Lee"
  - literal: "Kwanhyung Lee"
  - literal: "Donghwee Yoon"
  - literal: "Grigorios G. Chrysos"
  - literal: "Eunho Yang"
issued:
  date-parts:
    - [2026, 9, 27]
url: "https://arxiv.org/abs/2609.33279"

# Custom fields
paper_id: "2609.33279"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "continual-learning"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "prism"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:49:50Z"
created_at: "2026-09-30T10:49:50Z"
---

# Domain Generalization under Sampling Pattern Shifts in Irregular Time Series

**Authors**: Changhun Kim, Joohyung Lee, Kwanhyung Lee, Donghwee Yoon, Grigorios G. Chrysos, Eunho Yang
**Date**: 2026-09-27
**Paper ID**: [openalex:2609.33279](https://arxiv.org/abs/2609.33279)

## Summary

This paper investigates domain generalization for irregularly sampled multivariate time series (ISMTS) under distribution shifts in observation times and sampling patterns. The authors introduce HAR-C, a controlled benchmark showing that sampling shifts induce severe performance drops and shortcut learning that standard domain generalization methods fail to handle. To address this, they propose PRISM, a framework that learns complementary feature-centric and sampling-centric representations without task labels before robust supervised training. Extensive experiments validate that PRISM achieves superior robustness to unseen sampling shifts.

## Key Contributions

- Introduced HAR-C, the first controlled benchmark for evaluating sampling pattern shifts in irregularly sampled multivariate time series (ISMTS).
- Demonstrated that sampling pattern shifts alone can substantially degrade forecasting/prediction performance and induce sampling-specific shortcuts for existing domain generalization methods.
- Proposed PRISM, a domain generalization framework that learns complementary feature-centric and sampling-centric representations without task labels to mitigate brittle shortcut reliance.
- Showed through extensive experiments that PRISM consistently improves robustness to unseen sampling shifts compared to existing domain generalization baselines.

## Open Questions & Future Work

- [[handling-coupled-sampling-and-feature-shifts]]

## Key Concepts

- [[prism]]: A domain generalization framework that learns complementary feature-centric and sampling-centric representations to achieve robustness against sampling pattern shifts in irregularly sampled time series.

## Archivist Review

Approved the core PRISM domain generalization framework and the open question regarding coupled sampling and feature shifts. Rejected the local benchmark name HAR-C as a dataset following vault scarcity and naming guidelines.

### Approved Concepts
- PRISM: Core methodological contribution for domain generalization under sampling pattern shifts in irregular time series.

### Approved Open Questions
- Handling Coupled Sampling and Feature Shifts: Real-world distribution shifts rarely affect only observation patterns or feature values in isolation; handling their coupling is crucial for robust deployment in critical domains like healthcare.

### Rejected Candidates
- [dataset] HAR-C (`har-c`) - paper_local: HAR-C is a paper-internal controlled benchmark environment rather than an established standalone vault dataset.

## Links

- [Abstract](https://arxiv.org/abs/2609.33279)
- [PDF](https://arxiv.org/pdf/2609.33279)

