---
# CSL-compatible fields
title: "Minimax Optimality and Spectral Routing for Majority-Vote Ensembles under Markov Dependence"
author:
  - literal: "Ibne Farabi Shihab"
  - literal: "Sanjeda Akter"
  - literal: "Anuj Sharma"
issued:
  date-parts:
    - [2026, 4, 15]
url: "https://arxiv.org/abs/2604.13414"

# Custom fields
paper_id: "2604.13414"
paper_source: "openalex"
domain: "nlp"
tags:
  - "ensemble-learning"
  - "time-series"
  - "reinforcement-learning"
  - "markov-chain"
  - "theory"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adaptive-spectral-routing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-18T06:07:03Z"
created_at: "2026-04-18T06:07:03Z"
---

# Minimax Optimality and Spectral Routing for Majority-Vote Ensembles under Markov Dependence

**Authors**: Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma
**Date**: 2026-04-15
**Paper ID**: [openalex:2604.13414](https://arxiv.org/abs/2604.13414)

## Summary

This paper examines the performance degradation of majority-vote ensembles when training data exhibits Markov dependence, a common scenario in time-series and reinforcement learning. The authors derive a minimax lower bound for classification risk that scales with the mixing time of the underlying process and demonstrate that standard uniform bagging is suboptimal. To close this gap, they propose an adaptive spectral routing algorithm that uses the empirical Fiedler eigenvector to optimally partition training data, achieving the theoretical minimax rate without requiring prior knowledge of mixing times. Empirical results across synthetic chains, spatial grids, and Atari DQN ensembles confirm the effectiveness of this approach.

## Key Contributions

- Established a minimax lower bound of Ω(√Tmix/n) for excess classification risk under stationary, reversible, geometrically ergodic Markovian dependence.
- Proved that standard uniform bagging suffers from a Ω(Tmix/√n) excess risk on AR(1) witness subclasses, revealing a significant 1/√Tmix algorithmic gap.
- Introduced Adaptive Spectral Routing, which achieves the minimax rate O(√Tmix/n) by partitioning data via the empirical Fiedler eigenvector of a dependency graph.

## Open Questions & Future Work

- [[finite-width-rl-ensemble-covariance]]

## Key Concepts

- [[adaptive-spectral-routing]]: A data partitioning technique that uses the empirical Fiedler eigenvector of a dependency graph to optimize ensemble majority voting under correlated data conditions.

## Archivist Review

I approved the Adaptive Spectral Routing concept as it provides a novel, principled approach to ensemble training on dependent data that is likely to be reused. I approved the open question on finite-width RL ensemble covariance because it highlights a clear, substantial theoretical gap between current idealized theory and the practical application of ensembles in non-stationary reinforcement learning. I rejected the UCR archive as it is a broad collection and not a specific, standalone dataset.

### Approved Concepts
- Adaptive Spectral Routing: It addresses a fundamental algorithmic gap in majority-vote ensembles under Markovian data dependence by using spectral graph properties to achieve minimax optimality.

### Approved Open Questions
- Finite-width RL Ensemble Covariance: Deep RL models operate in the finite-width regime with non-stationary targets, making this a critical bottleneck for understanding ensemble stability in practical applications.

### Rejected Candidates
- [dataset] UCR archive (`ucr-archive`) - other: The UCR archive is a massive, widely-used collection of datasets rather than a single specific named dataset, violating the archival policy of targeting critical, specific research datasets.

## Links

- [Abstract](https://arxiv.org/abs/2604.13414)
- [PDF](https://arxiv.org/pdf/2604.13414)

