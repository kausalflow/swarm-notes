---
# CSL-compatible fields
title: "Foundations of Practical Quantum Advantage in Quantum-Informed Machine Learning for Predicting Chaos"
author:
  - literal: "Maida Wang"
  - literal: "Xiao Xue"
  - literal: "Minh Chung"
  - literal: "Peter V. Coveney"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.13422"

# Custom fields
paper_id: "2606.13422"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  - "quantum-statistical-priors-q-priors"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:38:52Z"
created_at: "2026-06-14T08:38:52Z"
---

# Foundations of Practical Quantum Advantage in Quantum-Informed Machine Learning for Predicting Chaos

**Authors**: Maida Wang, Xiao Xue, Minh Chung, Peter V. Coveney
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.13422](https://arxiv.org/abs/2606.13422)

## Summary

This paper provides a theoretical foundation and practical implementation of quantum-informed machine learning for predicting chaotic dynamical systems. The authors introduce k-indexed Quantum Statistical Priors (Q-Priors) to store complex spatial correlations using quantum superposition and entanglement, achieving a provable complexity advantage for state extraction using two-copy joint measurements. Empirical validation on superconducting hardware and a weather forecasting case study using ERA5 data demonstrate significant performance improvements in long-horizon rollout stability.

## Key Contributions

- Established a formal two-stage quantum-classical separation in copy-measurement complexity for Pauli functional estimation in chaotic systems.
- Proposed Q-Priors, a novel quantum representation for compact storage of high-order non-factorisable spatial correlations.
- Demonstrated 10-39% improvements in anomaly-correlation skill for medium-range weather forecasting on the ERA5 dataset compared to classical Koopman rollouts.

## Open Questions & Future Work

- [[end-to-end-qiml-advantage]]
- [[higher-order-q-priors]]

## Key Concepts

- [[quantum-statistical-priors-q-priors]]: A family of higher-order quantum priors that encode k-point marginals of invariant measures to facilitate efficient chaotic system prediction.

## Archivist Review

I have approved the Q-Priors concept as it is a novel, reusable mechanism for embedding dynamical systems into quantum representations. The two open questions were approved as they define substantial bottlenecks regarding hardware-software co-design and the representational power of the proposed quantum priors. ERA5 was rejected as a dataset because it is already present in the vault.

### Approved Concepts
- Quantum Statistical Priors (Q-Priors): Central mechanism proposed for encoding chaotic dynamical system states into quantum states.

### Approved Open Questions
- Demonstrating End-to-End QIML Advantage: This is the primary bottleneck to transitioning from a theoretical/simulation-based advantage to a verified practical utility in real-world scientific applications.
- Exploring Higher-Order Q-Priors: This addresses the representational limits of current pairwise (k=2) models and provides a path to leveraging the full expressive power of the quantum Hilbert space for complex physical systems.

## Links

- [Abstract](https://arxiv.org/abs/2606.13422)
- [PDF](https://arxiv.org/pdf/2606.13422)

