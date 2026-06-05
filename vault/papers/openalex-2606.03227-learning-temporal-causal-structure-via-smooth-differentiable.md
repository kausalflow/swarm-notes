---
# CSL-compatible fields
title: "Learning Temporal Causal Structure via Smooth Differentiable Optimization"
author:
  - literal: "Tong Zhao"
  - literal: "Ce Guo"
  - literal: "Wayne Luk"
  - literal: "Emil Lupu"
  - literal: "Ray Dipojjwal"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2606.03227"

# Custom fields
paper_id: "2606.03227"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "causal-discovery"
  - "optimization"
architectures:
  []
datasets:
  []
concept_slugs:
  - "triangularized-svar-parameterization"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:39:13Z"
created_at: "2026-06-05T08:39:13Z"
---

# Learning Temporal Causal Structure via Smooth Differentiable Optimization

**Authors**: Tong Zhao, Ce Guo, Wayne Luk, Emil Lupu, Ray Dipojjwal
**Date**: 2026-06-02
**Paper ID**: [openalex:2606.03227](https://arxiv.org/abs/2606.03227)

## Summary

Causal discovery in multivariate time series is hindered by the computational cost of enforcing acyclicity for instantaneous effects. The authors introduce a novel method that learns a differentiable variable permutation using the Gumbel-Sinkhorn operator to triangularize the instantaneous coefficient matrix of an SVAR model. This formulation replaces hard algebraic constraints with a valid parameterization, allowing for efficient, unified gradient-based optimization. The approach consistently outperforms competitive baselines in both discovery accuracy and computational efficiency across multiple benchmarks.

## Key Contributions

- Proposes a differentiable approach to causal discovery by learning a Gumbel-Sinkhorn based variable permutation to triangularize the instantaneous coefficient matrix.
- Converts hard acyclicity constraints into a parameterization, enabling unified gradient-based optimization for SVAR models.
- Achieves state-of-the-art causal discovery performance and up to 6x speedup on large-scale time-series benchmarks compared to existing baselines.

## Open Questions & Future Work

- [[optimal-lag-selection-strategies-in-causal-discovery]]
- [[adaptive-sparsity-regularization-for-causal-discovery]]

## Key Concepts

- [[triangularized-svar-parameterization]]: A parameterization method that enforces acyclicity in SVAR models by learning a differentiable variable permutation for triangular matrix decomposition.

## Archivist Review

I approved the triangularized SVAR parameterization concept because it provides a reusable, differentiable approach to a fundamental constraint in causal structural learning. I also approved two open questions concerning lag selection and adaptive regularization for causal discovery, as these represent substantial, widely applicable challenges in the field. I rejected the generic original title for the second open question to ensure consistency with the existing vault's naming conventions.

### Approved Concepts
- Triangularized SVAR Parameterization: It eliminates the need for complex, computationally expensive acyclicity constraints by parameterizing the instantaneous structure to be naturally acyclic via a learned triangular form.

### Approved Open Questions
- Optimal Causal Lag Selection: Choosing the correct maximum lag is critical for both the accuracy of recovering causal structures and the computational efficiency of the discovery process.
- Adaptive Sparsity Regularization: Fixed thresholds often fail to perform robustly, leading to either poor recall of genuine causal links or the retention of numerous false positives.

### Rejected Candidates
- [open_question] Adaptive Sparsity Regularization (`adaptive-sparsity-regularization`) - duplicate_existing: This is a duplicate of a more descriptive, uniquely named candidate approved in the final selection process.

## Links

- [Abstract](https://arxiv.org/abs/2606.03227)
- [PDF](https://arxiv.org/pdf/2606.03227)

