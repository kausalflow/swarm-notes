---
# CSL-compatible fields
title: "Disentangling Damage from Operational Variability: A Label-Free Self-Supervised Representation Learning Framework for Output-Only Structural Damage Identification"
author:
  - literal: "Xudong Jian"
  - literal: "Charikleia Stoura"
  - literal: "Simon Scandella"
  - literal: "Eleni Chatzi"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2604.19658"

# Custom fields
paper_id: "2604.19658"
paper_source: "openalex"
domain: "time-series"
tags:
  - "self-supervised-learning"
  - "time-series"
  - "anomaly-detection"
  - "embedding"
architectures:
  []
datasets:
  []
concept_slugs:
  - "vicreg-disentangled-structural-monitoring"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T07:01:50Z"
created_at: "2026-04-24T07:01:50Z"
---

# Disentangling Damage from Operational Variability: A Label-Free Self-Supervised Representation Learning Framework for Output-Only Structural Damage Identification

**Authors**: Xudong Jian, Charikleia Stoura, Simon Scandella, Eleni Chatzi
**Date**: 2026-04-21
**Paper ID**: [openalex:2604.19658](https://arxiv.org/abs/2604.19658)

## Summary

This paper introduces a label-free, self-supervised representation learning framework designed to solve the challenge of distinguishing structural damage from confounding operational and environmental variability in vibration-based health monitoring. By utilizing an autoencoder with dual latent spaces constrained by Variance-Invariance-Covariance Regularization (VICReg) and frequency-domain alignment, the model effectively disentangles damage-related characteristics from nuisance factors. The end-to-end framework requires no prior data on damage or external conditions and provides robust performance for both damage detection and quantification across real-world civil and mechanical infrastructure datasets.

## Key Contributions

- Proposes a self-supervised, label-free autoencoder framework that uses dual latent representations to isolate damage signatures from environmental and operational noise.
- Implements a VICReg-based invariance regularization and frequency-domain constraint to ensure learned representations are robust to non-damage-related vibration variations.
- Demonstrates strong generalization and effective damage detection/quantification on real-world vibration datasets from bridge and gearbox monitoring systems.

## Open Questions & Future Work

- [[improving-sensitivity-to-weak-damage]]
- [[reliable-structural-damage-quantification]]

## Key Concepts

- [[vicreg-disentangled-structural-monitoring]]: A self-supervised learning framework that uses VICReg and frequency-domain constraints to extract damage-sensitive, nuisance-invariant features for structural health monitoring.

## Archivist Review

I have approved the core disentanglement framework as a reusable concept because it successfully adapts VICReg for latent factor separation in time-series monitoring. I also approved two research questions that identify critical bottlenecks in sensitivity and quantification, which are persistent challenges in structural health monitoring. Datasets were rejected as they are not unique or named benchmarks suited for the long-term vault.

### Approved Concepts
- VICReg-based Disentangled Structural Monitoring: The paper introduces a novel application of VICReg in a dual-latent autoencoder architecture specifically to disentangle environmental/operational variability from damage-related vibration features.

### Approved Open Questions
- Improving Sensitivity to Weak Damage: Improving sensitivity to subtle structural changes is critical for the practical deployment of structural health monitoring, as early-stage damage often presents with weak signal signatures that can be easily obscured.
- Reliable Structural Damage Quantification: Reliable damage quantification is essential for informed decision-making regarding structural maintenance and service life extension, moving beyond simple detection towards actionable condition assessment.

## Links

- [Abstract](https://arxiv.org/abs/2604.19658)
- [PDF](https://arxiv.org/pdf/2604.19658)

