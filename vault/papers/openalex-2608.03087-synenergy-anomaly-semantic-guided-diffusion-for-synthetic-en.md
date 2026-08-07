---
# CSL-compatible fields
title: "SynEnergy: Anomaly Semantic-Guided Diffusion for Synthetic Energy Data Generation"
author:
  - literal: "Lin Jiang"
  - literal: "Dahai Yu"
  - literal: "Ravikumar Gelli"
  - literal: "Guang Wang"
issued:
  date-parts:
    - [2026, 8, 4]
url: "https://arxiv.org/abs/2608.03087"

# Custom fields
paper_id: "2608.03087"
paper_source: "openalex"
domain: "time-series"
tags:
  - "diffusion-model"
  - "time-series"
  - "graph-neural-network"
  - "anomaly-detection"
  - "robustness"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-07T06:05:04Z"
created_at: "2026-08-07T06:05:04Z"
---

# SynEnergy: Anomaly Semantic-Guided Diffusion for Synthetic Energy Data Generation

**Authors**: Lin Jiang, Dahai Yu, Ravikumar Gelli, Guang Wang
**Date**: 2026-08-04
**Paper ID**: [openalex:2608.03087](https://arxiv.org/abs/2608.03087)

## Summary

SynEnergy is a two-stage diffusion framework designed to generate realistic synthetic energy consumption data while effectively preserving sparse and localized anomalous events. The first stage, HG-ASL, extracts region-specific anomaly semantics by modeling spatial and attribute dependencies on a heterogeneous graph, while the second stage, AS-Diff, injects these semantics into the diffusion denoising process. Evaluations across four real-world energy datasets demonstrate improvements in anomaly preservation fidelity and downstream performance over multiple baselines.

## Key Contributions

- Proposes SynEnergy, a two-stage diffusion framework combining Heterogeneous Graph-based Anomaly Semantic Learning (HG-ASL) and Anomaly Semantic-guided Diffusion (AS-Diff) for synthetic energy data generation.
- Addresses the underrepresentation of sparse, localized anomalous energy consumption events caused by extreme weather, infrastructure failures, and behavioral shifts.
- Improves anomaly preservation fidelity by an average of 12.21% and downstream quality by 2.96% across four real-world datasets compared to 11 baselines.

## Archivist Review

Applied strict selection standards, rejecting paper-local model architectures like SynEnergy as paper-internal framework instances. No other concepts or open questions met the high bar for universal vault inclusion.

### Rejected Candidates
- [concept] SynEnergy (`synenergy`) - paper_local: Paper-specific model architecture and framework name without broad standalone reusability across diverse time-series tasks.

## Links

- [Abstract](https://arxiv.org/abs/2608.03087)
- [PDF](https://arxiv.org/pdf/2608.03087)

