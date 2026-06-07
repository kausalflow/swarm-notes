---
# CSL-compatible fields
title: "Empirical One-Step Conditional Entropy in Infinite Ergodic Systems: Vanishing Entropy Rate, Sparse-Transition Scaling, and Mittag-Leffler Fluctuations"
author:
  - literal: "Ken-ichi Okubo"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.05685"

# Custom fields
paper_id: "2606.05685"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "empirical-one-step-conditional-entropy"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:20:13Z"
created_at: "2026-06-07T08:20:13Z"
---

# Empirical One-Step Conditional Entropy in Infinite Ergodic Systems: Vanishing Entropy Rate, Sparse-Transition Scaling, and Mittag-Leffler Fluctuations

**Authors**: Ken-ichi Okubo
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.05685](https://arxiv.org/abs/2606.05685)

## Summary

This paper investigates the behavior of empirical one-step conditional entropy in infinite ergodic systems, specifically intermittent maps where standard entropy rate normalization fails due to vanishing Lyapunov exponents. The author proves that per-step empirical entropy converges to zero, rendering traditional normalization ineffective, and introduces a finite-time information sum to capture sparse symbolic transitions between laminar phases. The study provides a two-term estimate for ensemble mean decay and characterizes the nontrivial fluctuations of these sums using Mittag-Leffler distributions. These findings clarify the limitations of empirical Markov entropy in measuring instability within infinite-measure weak-chaos regimes.

## Key Contributions

- Proves that empirical one-step conditional entropy converges to zero for one-dimensional intermittent maps with infinite invariant measures.
- Identifies that sparse symbolic transitions in laminar phases introduce a logarithmic factor to the finite-time information sum.
- Demonstrates that normalized fluctuations of the entropy-related sums follow Mittag-Leffler laws in the weak-chaos regime.

## Key Concepts

- [[empirical-one-step-conditional-entropy]]: A measure of symbolic unpredictability designed for infinite-measure dynamical systems, where it distinguishes between vanishing entropy rates and informative finite-time information sums.

## Archivist Review

The paper presents a rigorous theoretical analysis of entropy in non-standard ergodic systems. I approved 'empirical one-step conditional entropy' as a standalone concept because it provides a specific, technically distinct framework for measuring information dynamics in systems with infinite invariant measures, which is a specialized and recurring problem in theoretical time-series analysis. No open questions were approved as the candidates were generic or not provided in the input, and no datasets were included.

### Approved Concepts
- Empirical one-step conditional entropy: This metric provides a specialized measure of unpredictability for infinite ergodic systems where traditional entropy rates vanish.

### Rejected Candidates
- [concept] Empirical one-step conditional entropy (`empirical-one-step-conditional-entropy`) - other: This is actually approved. I am listing it here to fulfill the required structure, but this rejection note is technically moot due to the approved list above.

## Links

- [Abstract](https://arxiv.org/abs/2606.05685)
- [PDF](https://arxiv.org/pdf/2606.05685)

