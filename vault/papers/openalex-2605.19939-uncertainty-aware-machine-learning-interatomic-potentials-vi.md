---
# CSL-compatible fields
title: "Uncertainty-aware Machine Learning Interatomic Potentials via Learned Functional Perturbations"
author:
  - literal: "Olga Zaghen"
  - literal: "Maksim Zhdanov"
  - literal: "Dario Coscia"
  - literal: "David R. Wessels"
  - literal: "Erik J. Bekkers"
issued:
  date-parts:
    - [2026, 5, 19]
url: "https://arxiv.org/abs/2605.19939"

# Custom fields
paper_id: "2605.19939"
paper_source: "openalex"
domain: "chemistry"
tags:
  - "uncertainty-quantification"
  - "graph-neural-network"
  - "fine-tuning"
  - "chemistry"
architectures:
  []
datasets:
  []
concept_slugs:
  - "learned-functional-perturbations-uq"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-22T08:17:54Z"
created_at: "2026-05-22T08:17:54Z"
---

# Uncertainty-aware Machine Learning Interatomic Potentials via Learned Functional Perturbations

**Authors**: Olga Zaghen, Maksim Zhdanov, Dario Coscia, David R. Wessels, Erik J. Bekkers
**Date**: 2026-05-19
**Paper ID**: [openalex:2605.19939](https://arxiv.org/abs/2605.19939)

## Summary

This paper addresses the need for robust uncertainty quantification in Machine Learning Interatomic Potentials (MLIPs) without the overhead of ensemble methods. The authors propose converting deterministic models into probabilistic ones by applying learned functional perturbations, optimized end-to-end using the Continuous Ranked Probability Score (CRPS). The method is validated on equivariant GNNs and fine-tuned foundation models, showing significant improvements in CRPS and uncertainty calibration over state-of-the-art Bayesian baselines.

## Key Contributions

- Introduces a non-ensemble uncertainty quantification method for MLIPs using learned functional perturbations and CRPS-based end-to-end training.
- P-EGNN achieves 19-32% improvement in CRPS on the N-body charged particle benchmark compared to the Bayesian MLIP baseline BLIP.
- P-Orb demonstrates superior uncertainty calibration on the silica dataset, increasing the Spearman correlation between predicted uncertainty and actual error from 0.75 to 0.84.

## Open Questions & Future Work

- [[energy-force-loss-balancing-mlip]]

## Key Concepts

- [[learned-functional-perturbations-uq]]: A technique to transform deterministic machine learning models into probabilistic ones by applying and training functional perturbations using the CRPS scoring rule.

## Archivist Review

Approved the core mechanism of learned functional perturbations as a reusable UQ technique. Also approved the energy-force loss balancing as a significant and trackable open question in multi-task MLIP training. Rejected Orb-v3 as it is a specific model foundation rather than a general-purpose benchmark dataset.

### Approved Concepts
- Learned Functional Perturbations for Uncertainty Quantification: This is the core methodological contribution, offering an alternative to ensemble or variational inference-based UQ methods in ML interatomic potentials.

### Approved Open Questions
- Energy-force loss balancing instability: Loss balancing is a fundamental issue in multitask training of MLIPs; failing to resolve it leads to inconsistent results and sensitivity to hyperparameter choices, hindering the robustness of learned models.

## Links

- [Abstract](https://arxiv.org/abs/2605.19939)
- [PDF](https://arxiv.org/pdf/2605.19939)

