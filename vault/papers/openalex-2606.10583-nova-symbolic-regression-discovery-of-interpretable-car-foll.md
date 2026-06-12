---
# CSL-compatible fields
title: "NOVA: Symbolic Regression Discovery of Interpretable Car-Following and Lane-Change Models with Driver Heterogeneity"
author:
  - literal: "Ishak Abassi"
  - literal: "Nassim Ali Bouazzouni"
  - literal: "Farah Ibelaiden"
  - literal: "Nadir Farhi"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.10583"

# Custom fields
paper_id: "2606.10583"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "dataset"
  - "benchmark"
architectures:
  []
datasets:
  - "ngsim-i-80-us-101-dataset"
concept_slugs:
  - "nova-framework"
dataset_slugs:
  - "ngsim-i-80-us-101-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:55:26Z"
created_at: "2026-06-12T08:55:26Z"
---

# NOVA: Symbolic Regression Discovery of Interpretable Car-Following and Lane-Change Models with Driver Heterogeneity

**Authors**: Ishak Abassi, Nassim Ali Bouazzouni, Farah Ibelaiden, Nadir Farhi
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.10583](https://arxiv.org/abs/2606.10583)

## Summary

NOVA is an autonomous symbolic regression framework designed to extract interpretable car-following and lane-change models from high-volume trajectory data with minimal priors. Utilizing a robust, deterministic search engine, the framework identifies compact algebraic structures that align with psychophysical collision-avoidance theories. The model demonstrates high predictive accuracy on the NGSIM datasets, achieving state-of-the-art performance in both acceleration forecasting and lane-change classification.

## Key Contributions

- Introduces NOVA, a Rust-powered symbolic regression framework that identifies interpretable, compact car-following and lane-change models.
- Achieves an RMSE of 1.376 m/s^2 on trajectory data, outperforming the SR-LLM symbolic baseline by 0.135 m/s^2.
- Demonstrates zero-shot transferability across freeway sites and achieves 67.4% balanced accuracy in lane-change modeling, significantly surpassing existing baselines.

## Open Questions & Future Work

- [[overcoming-lane-change-discrimination-ceiling]]

## Key Concepts

- [[nova-framework]]: An autonomous symbolic regression framework for discovering interpretable algebraic models of driver behavior from raw trajectory data.

## Archivist Review

The paper introduces a symbolic regression framework (NOVA) that provides significant interpretability advantages in driver behavior modeling, which is a reusable methodology. I have consolidated the two mentioned datasets into a single entry to adhere to the scarcity requirement. The open question regarding the discrimination ceiling in lane-change classification is a substantial research bottleneck that warrants further tracking in the vault.

### Approved Concepts
- NOVA framework: Central framework of the paper for symbolic regression discovery of driver behavior.

### Approved Open Questions
- Overcoming lane-change discrimination ceiling: This is a clear, bounded bottleneck identified by the authors that prevents further progress in lane-change modeling using their symbolic regression approach.

### Rejected Candidates
- [dataset] NGSIM I-80 (`ngsim-i-80-dataset`) - duplicate_existing: Consolidated into a single unified dataset entry with US-101 for better vault management.
- [dataset] US-101 (`us-101-dataset`) - duplicate_existing: Consolidated into a single unified dataset entry with NGSIM I-80 for better vault management.

## Datasets

- [[ngsim-i-80-us-101-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2606.10583)
- [PDF](https://arxiv.org/pdf/2606.10583)

