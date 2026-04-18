---
# CSL-compatible fields
title: "An End-to-end Building Load Forecasting Framework with Patch-based Information Fusion Network and Error-weighted Adaptive Loss"
author:
  - literal: "Hang Fan"
  - literal: "Ying Lu"
  - literal: "Weican Liu"
  - literal: "Dunnan Liu"
  - literal: "Xiaotao Chen"
  - literal: "Shengwei Mei"
issued:
  date-parts:
    - [2026, 4, 15]
url: "https://arxiv.org/abs/2604.13714"

# Custom fields
paper_id: "2604.13714"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "gru"
  - "feature-selection"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "patch-based-information-fusion-network-pif-net"
  - "error-weighted-adaptive-loss-ewal"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-18T06:06:51Z"
created_at: "2026-04-18T06:06:51Z"
---

# An End-to-end Building Load Forecasting Framework with Patch-based Information Fusion Network and Error-weighted Adaptive Loss

**Authors**: Hang Fan, Ying Lu, Weican Liu, Dunnan Liu, Xiaotao Chen, Shengwei Mei
**Date**: 2026-04-15
**Paper ID**: [openalex:2604.13714](https://arxiv.org/abs/2604.13714)

## Summary

This paper presents an end-to-end building load forecasting framework designed to handle the high volatility and complex dependencies of energy data. The system employs a robust preprocessing pipeline using LOF for anomaly correction and SVM-SHAP for feature selection. Central to the framework is the Patch-based Information Fusion Network (PIF-Net), which partitions input series into blocks and utilizes a gating mechanism to integrate temporal features. Furthermore, an Error-weighted Adaptive Loss (EWAL) function is introduced to prioritize training accuracy during extreme load conditions.

## Key Contributions

- Proposes a two-stage preprocessing module combining Local Outlier Factor (LOF) and SVM-SHAP for robust anomaly detection and feature redundancy reduction.
- Introduces PIF-Net, a patch-based architecture that utilizes shared GRU units and a gating mechanism to dynamically fuse temporal dependencies.
- Develops the Error-weighted Adaptive Loss (EWAL) function to enhance forecasting robustness during extreme load conditions by adjusting penalties based on error distributions.

## Open Questions & Future Work

- [[probabilistic-building-load-forecasting-uncertainty-quantification]]
- [[edge-computing-model-compression]]

## Key Concepts

- [[patch-based-information-fusion-network-pif-net]]: A forecasting architecture that partitions time series into patches and uses a gated integration mechanism to fuse temporal dependencies.
- [[error-weighted-adaptive-loss-ewal]]: A training loss function that dynamically adjusts penalty weights based on prediction error distributions to improve model robustness during volatility.

## Archivist Review

I have approved the core architectural contributions of PIF-Net and the EWAL loss function, as both provide specific, reusable mechanisms for time-series forecasting. The open questions were selected to address fundamental gaps in reliability (uncertainty quantification) and practical deployment constraints (edge optimization) common to the domain. Other candidates were rejected to maintain the selectivity of the vault.

### Approved Concepts
- Patch-based Information Fusion Network (PIF-Net): Core architectural innovation for processing temporal sequences in blocks and dynamically integrating them using a custom gating mechanism.
- Error-weighted Adaptive Loss (EWAL): Provides a novel mechanism for improving robustness under high-volatility conditions by dynamically weighting penalties based on error distributions.

### Approved Open Questions
- Probabilistic Building Load Forecasting: Probabilistic forecasting is a major requirement for robust power system operations that deterministic models do not fulfill.
- Efficient Edge Deployment Strategies: Edge deployment is critical for the practical, large-scale implementation of building-level demand response programs.

## Links

- [Abstract](https://arxiv.org/abs/2604.13714)
- [PDF](https://arxiv.org/pdf/2604.13714)

