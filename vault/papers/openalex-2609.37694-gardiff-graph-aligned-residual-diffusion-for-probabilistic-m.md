---
# CSL-compatible fields
title: "GARDiff: Graph-Aligned Residual Diffusion for Probabilistic Multivariate Time-Series Forecasting"
author:
  - literal: "Rui Han"
  - literal: "Min Yang"
  - literal: "Xu Zhang"
  - literal: "Xinghao Yang"
  - literal: "Wei Liu"
  - literal: "Yongshun Gong"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.37694"

# Custom fields
paper_id: "2609.37694"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
  - "probabilistic-forecasting"
  - "uncertainty-calibration"
architectures:
  []
datasets:
  []
concept_slugs:
  - "graph-aligned-residual-diffusion"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-01T11:14:47Z"
created_at: "2026-10-01T11:14:47Z"
---

# GARDiff: Graph-Aligned Residual Diffusion for Probabilistic Multivariate Time-Series Forecasting

**Authors**: Rui Han, Min Yang, Xu Zhang, Xinghao Yang, Wei Liu, Yongshun Gong
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.37694](https://arxiv.org/abs/2609.37694)

## Summary

GARDiff is a novel graph-aligned residual diffusion framework for probabilistic multivariate time-series forecasting that resolves the deterministic-to-residual structural alignment problem. While decoupled diffusion separates forecasting into deterministic and stochastic residual steps, directly using deterministic graphs introduces edge-level misalignments. GARDiff addresses this via uncertainty-aware structural refinement and timestep-aware edge sparsification, evolving graph conditions dynamically during reverse diffusion. Extensive experiments across six benchmarks demonstrate superior probabilistic forecasting and uncertainty calibration.

## Key Contributions

- Proposes GARDiff, a novel graph-aligned residual diffusion framework that resolves the deterministic-to-residual structural alignment problem in decoupled diffusion forecasting.
- Introduces uncertainty-aware structural refinement to distinguish high- and low-uncertainty regions during residual generation.
- Performs timestep-aware edge sparsification during reverse diffusion to evolve graph conditions from global dependency aggregation to localized residual refinement.
- Demonstrates consistent performance and uncertainty calibration improvements across six real-world benchmarks over strong baselines.

## Key Concepts

- [[graph-aligned-residual-diffusion]]: A probabilistic multivariate time-series forecasting framework that resolves deterministic-to-residual structural misalignment through uncertainty-aware and timestep-aware graph refinement.

## Archivist Review

Approved the primary methodological contribution, Graph-Aligned Residual Diffusion, as it provides a reusable approach for dynamically aligning dependency graphs during decoupled diffusion forecasting. Rejected the analytical problem statement candidate as it is subsumed by the main mechanism and better archived together.

### Approved Concepts
- Graph-Aligned Residual Diffusion: Introduces a novel framework to address the deterministic-to-residual structural alignment problem in decoupled diffusion forecasting by progressively adapting dependency graphs via uncertainty-aware structural refinement and timestep-aware edge sparsification.

### Rejected Candidates
- [concept] Deterministic-to-Residual Structural Alignment Problem (`deterministic-to-residual-structural-alignment`) - subcomponent_of_broader_mechanism: This is an analytical observation and problem statement identified by the paper rather than a distinct reusable method or architecture, making it better suited as a finding within the concept note or open question rather than an independent technique.

## Links

- [Abstract](https://arxiv.org/abs/2609.37694)
- [PDF](https://arxiv.org/pdf/2609.37694)

