---
# CSL-compatible fields
title: "GCov-based portmanteau test"
author:
  - literal: "Joann Jasiak"
  - literal: "Aryan Manafi Neyazi"
issued:
  date-parts:
    - [2026, 4, 14]
url: "https://arxiv.org/abs/2312.05373"

# Custom fields
paper_id: "2312.05373"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "gcov-portmanteau-test"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-17T06:28:58Z"
created_at: "2026-04-17T06:28:58Z"
---

# GCov-based portmanteau test

**Authors**: Joann Jasiak, Aryan Manafi Neyazi
**Date**: 2026-04-14
**Paper ID**: [openalex:2312.05373](https://arxiv.org/abs/2312.05373)

## Summary

This paper introduces a novel portmanteau test for detecting nonlinear serial dependence (NLSD) in time series, specifically designed for non-Gaussian residuals from dynamic models. The proposed method leverages Generalized Covariance (GCov) to extend testing to an infinite set of autocovariance conditions while maintaining an asymptotic χ2 distribution. To address finite-sample performance, the authors also provide a bootstrap-based version of the test. The effectiveness of this approach is validated through simulations on mixed causal-noncausal autoregressive models and applied to detect bubble-like patterns in aluminum price data.

## Key Contributions

- Introduces a generalized covariance (GCov) residual-based portmanteau test for nonlinear serial dependence, providing an asymptotic χ2 distribution for semi-parametric dynamic models.
- Extends GCov-based inference to an infinite set of nonlinear autocovariance conditions and derives asymptotic properties under local alternative hypotheses for dynamic model parameters.
- Develops a GCov bootstrap test to improve finite-sample performance and support residual diagnostics in parametrically estimated models (e.g., maximum likelihood).

## Open Questions & Future Work

- [[optimal-generator-system-selection-gcov]]

## Key Concepts

- [[gcov-portmanteau-test]]: A residual-based portmanteau test for nonlinear serial dependence in time series that uses Generalized Covariance to remain valid for non-Gaussian processes.

## Archivist Review

I approved the GCov portmanteau test as a significant extension of traditional diagnostic tools for time series, particularly for non-Gaussian settings where classical methods fail. The open question regarding the selection of generators was approved because it addresses the core computational bottleneck of the proposed framework. I rejected the initial open question candidate in favor of a renamed version that better adheres to the vault's naming standard for tracking research challenges.

### Approved Concepts
- Generalized Covariance (GCov) Portmanteau Test: It provides a theoretically sound, non-Gaussian-capable framework for detecting nonlinear serial dependence, addressing a common weakness in classical portmanteau statistics.

### Approved Open Questions
- Optimal System of Generators Selection: This bottleneck directly limits the diagnostic power and efficiency of GCov-based tests in broader applications.

### Rejected Candidates
- [open_question] Optimal System of Generators (`optimal-system-generators-gcov-test`) - other: Renamed for clarity and consistency with established vault naming conventions.

## Links

- [Abstract](https://arxiv.org/abs/2312.05373)
- [PDF](https://arxiv.org/pdf/2312.05373)

