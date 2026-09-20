---
# CSL-compatible fields
title: "One Intervention per Component is Enough: Towards Identifiability in Linear Stochastic Dynamics from Steady State"
author:
  - literal: "Saber Salehkaleybar"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.19955"

# Custom fields
paper_id: "2609.19955"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "causal-discovery"
  - "identifiability"
  - "stochastic-differential-equation"
  - "steady-state"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-20T09:30:59Z"
created_at: "2026-09-20T09:30:59Z"
---

# One Intervention per Component is Enough: Towards Identifiability in Linear Stochastic Dynamics from Steady State

**Authors**: Saber Salehkaleybar
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.19955](https://arxiv.org/abs/2609.19955)

## Summary

This paper investigates the identifiability of multivariate Ornstein-Uhlenbeck (OU) stochastic processes using steady-state observational and interventional data, bypassing the need for full time-series trajectories. The author proves that performing a single intervention per strongly connected component (SCC) of the drift graph enables generic parameter recovery up to a global scaling factor under mild connectivity and spectral conditions. To leverage this, a recursive learning algorithm and a regularized least-squares estimator are introduced, jointly minimizing steady-state mean and covariance equation residuals. Experiments confirm the effectiveness of these methods in recovering underlying OU parameters from stationary snapshot measurements.

## Key Contributions

- Proves that one intervention per strongly connected component (SCC) of the drift graph suffices to recover multivariate Ornstein-Uhlenbeck process parameters up to a global scaling factor from steady-state data.
- Develops a recursive learning algorithm that topologically orders SCCs, isolates marginal dynamics, and solves linear systems from steady-state moment equations.
- Proposes a regularized least-squares estimator that jointly minimizes steady-state mean and covariance equation residuals across observational and interventional data.

## Open Questions & Future Work

- [[genericity-proof-spectral-rank-assumptions]]

## Archivist Review

Applied a strict selection standard. No permanent concepts qualified as standalone reusable architectural primitives or foundational paradigms beyond paper-internal derivations. The open question candidate was rejected as a duplicate of an existing vault entry.

### Approved Open Questions
- Genericity of Spectral and Rank Assumptions: This is technically important because current identifiability guarantees for linear stochastic dynamical systems depend on nondegeneracy assumptions that have only been validated numerically, limiting the absolute theoretical completeness of parameter recovery frameworks.

### Rejected Candidates
- [open_question] Genericity of Spectral and Rank Assumptions (`genericity-proof-spectral-rank-assumptions`) - duplicate_existing: An open question with this slug and title already exists in the vault.

## Links

- [Abstract](https://arxiv.org/abs/2609.19955)
- [PDF](https://arxiv.org/pdf/2609.19955)

