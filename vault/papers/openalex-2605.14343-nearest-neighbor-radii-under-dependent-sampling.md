---
# CSL-compatible fields
title: "Nearest-Neighbor Radii under Dependent Sampling"
author:
  - literal: "Yuanyuan Gao"
  - literal: "Yilong Hou"
  - literal: "Zhexiao Lin"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14343"

# Custom fields
paper_id: "2605.14343"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "benchmarks"
architectures:
  []
datasets:
  []
concept_slugs:
  - "nearest-neighbor-radii-under-dependent-sampling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:31:38Z"
created_at: "2026-05-17T07:31:38Z"
---

# Nearest-Neighbor Radii under Dependent Sampling

**Authors**: Yuanyuan Gao, Yilong Hou, Zhexiao Lin
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14343](https://arxiv.org/abs/2605.14343)

## Summary

This paper provides a theoretical analysis of nearest-neighbor radii when observations are sampled dependently, departing from the classical assumption of independent sampling. The authors prove almost sure convergence under polynomial mixing and non-asymptotic moment bounds under geometric mixing, showing that the results scale with the local intrinsic dimension of the data. The study confirms that nearest-neighbor geometry remains statistically informative even in the presence of strong mixing dependence, offering new insights for high-dimensional dependent data applications.

## Key Contributions

- Establishes distribution-free almost sure convergence for nearest-neighbor radii under polynomial mixing conditions.
- Derives sharp non-asymptotic moment bounds for geometric mixing, demonstrating that complexity scales with local intrinsic dimension rather than ambient dimension.
- Validates theoretical findings through synthetic experiments and real-world time-series benchmarks to show robustness of neighbor-based geometry in dependent settings.

## Open Questions & Future Work

- [[uniform-convergence-nn-dependent-data]]

## Key Concepts

- [[nearest-neighbor-radii-under-dependent-sampling]]: A theoretical characterization of nearest-neighbor geometry under strong mixing dependent sampling conditions.

## Archivist Review

The paper offers a valuable theoretical expansion of nearest-neighbor geometry to dependent data settings. I approved the concept for its foundational nature in non-i.i.d. analysis and the open question for its necessity in establishing global consistency bounds for time-series and dependent-data ML models. No datasets were approved as they were mentioned only in a general benchmarking context.

### Approved Concepts
- Nearest-neighbor radii under dependent sampling: Provides a theoretical foundation for nearest-neighbor geometry under non-i.i.d. conditions, crucial for validating ML methods on time-series and spatio-temporal data.

### Approved Open Questions
- Uniform convergence for NN radii: Uniform convergence is a core prerequisite for establishing global consistency and risk bounds for nonparametric machine learning estimators operating on dependent data sequences.

## Links

- [Abstract](https://arxiv.org/abs/2605.14343)
- [PDF](https://arxiv.org/pdf/2605.14343)

