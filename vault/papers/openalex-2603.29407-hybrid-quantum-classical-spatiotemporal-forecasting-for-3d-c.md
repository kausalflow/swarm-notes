---
# CSL-compatible fields
title: "Hybrid Quantum-Classical Spatiotemporal Forecasting for 3D Cloud Fields"
author:
  - literal: "Fu Wang"
  - literal: "Qifeng Lu"
  - literal: "Xinyu Long"
  - literal: "Meng Zhang"
  - literal: "Xiaofei Yang"
  - literal: "Weijia Cao"
  - literal: "Xiaowen Chu"
issued:
  date-parts:
    - [2026, 3, 31]
url: "https://arxiv.org/abs/2603.29407"

# Custom fields
paper_id: "2603.29407"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "hybrid-quantum-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hybrid-quantum-classical-spatiotemporal-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-03T06:06:59Z"
created_at: "2026-04-03T06:06:59Z"
---

# Hybrid Quantum-Classical Spatiotemporal Forecasting for 3D Cloud Fields

**Authors**: Fu Wang, Qifeng Lu, Xinyu Long, Meng Zhang, Xiaofei Yang, Weijia Cao, Xiaowen Chu
**Date**: 2026-03-31
**Paper ID**: [openalex:2603.29407](https://arxiv.org/abs/2603.29407)

## Summary

QENO is a hybrid quantum-classical spatiotemporal forecasting framework designed to address the challenges of capturing nonlocal dependencies and multiscale dynamics in 3D cloud fields. The model employs a classical encoder, a topology-aware quantum enhancement block for latent space modeling, and a dynamic fusion unit to integrate temporal features. Empirical evaluations on the CMA-MESO dataset demonstrate that QENO outperforms established spatiotemporal baselines while maintaining computational efficiency in 3D volume reconstruction.

## Key Contributions

- Introduces QENO, a hybrid quantum-classical forecasting framework that models 3D cloud field dynamics by capturing nonlocal couplings in latent space.
- Integrates a topology-aware quantum enhancement block and a dynamic fusion temporal unit to preserve fine structural details often lost by classical locality-biased models.
- Demonstrates superior performance over state-of-the-art baselines like Earthformer and PredRNN++ on the CMA-MESO 3D cloud field benchmark across multiple metrics including MSE, RMSE, and SSIM.

## Open Questions & Future Work

- [[quantum-simulation-overhead-meteorology]]

## Key Concepts

- [[hybrid-quantum-classical-spatiotemporal-forecasting]]: A spatiotemporal forecasting framework that leverages quantum-inspired topology-aware blocks within a classical neural architecture to model nonlocal dependencies in high-dimensional data.

## Archivist Review

I approved the hybrid quantum-classical concept as it represents an emerging architectural design pattern for complex spatiotemporal modeling, and the open question regarding quantum simulation overhead as it captures a fundamental scalability constraint for this paradigm. I rejected the CMA-MESO dataset as it is a domain-specific benchmark that does not meet the threshold for permanent archival status.

### Approved Concepts
- Hybrid Quantum-Classical Spatiotemporal Forecasting: Represents a novel paradigm for incorporating quantum-inspired latent space modeling to capture long-range, nonlocal interactions in 3D physical fields.

### Approved Open Questions
- Quantum simulation overhead bottleneck: Addressing the simulation bottleneck is essential for determining whether these hybrid architectures can provide practical, scalable advantages over purely classical deep learning models in high-throughput production environments.

### Rejected Candidates
- [dataset] CMA-MESO (`CMA-MESO`) - low_impact: Routine benchmark dataset specific to this study; does not warrant a permanent entry in the central repository.

## Links

- [Abstract](https://arxiv.org/abs/2603.29407)
- [PDF](https://arxiv.org/pdf/2603.29407)

