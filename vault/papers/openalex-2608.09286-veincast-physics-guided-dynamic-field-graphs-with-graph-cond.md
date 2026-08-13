---
# CSL-compatible fields
title: "VeinCast: Physics-Guided Dynamic Field Graphs with Graph-Conditioned Fusion for Global Medium-Range Weather Forecasting"
author:
  - literal: "Zhisheng Chen"
  - literal: "Jinhan Li"
  - literal: "Yuxuan Li"
  - literal: "Yuan Gao"
  - literal: "Hao Wu"
  - literal: "Zheng Lu"
  - literal: "Jinlong Du"
  - literal: "Kun Wang"
  - literal: "Bo An"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/2608.09286"

# Custom fields
paper_id: "2608.09286"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
  - "attention-mechanism"
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
processed_at: "2026-08-13T06:09:28Z"
created_at: "2026-08-13T06:09:28Z"
---

# VeinCast: Physics-Guided Dynamic Field Graphs with Graph-Conditioned Fusion for Global Medium-Range Weather Forecasting

**Authors**: Zhisheng Chen, Jinhan Li, Yuxuan Li, Yuan Gao, Hao Wu, Zheng Lu, Jinlong Du, Kun Wang, Bo An
**Date**: 2026-08-10
**Paper ID**: [openalex:2608.09286](https://arxiv.org/abs/2608.09286)

## Summary

VeinCast is a physics-guided dynamic field graph and graph-conditioned fusion framework designed for global medium-range weather forecasting across 69 surface and upper-air fields. It integrates predefined atmospheric relations with state-dependent residual edges and graph-conditioned latent fusion to effectively model complex atmospheric interactions. Evaluated on the 1.5-degree ERA5 benchmark, VeinCast demonstrates competitive long-range forecasting performance up to 14 days compared to state-of-the-art models.

## Key Contributions

- Introduces VeinCast, a physics-guided dynamic field graph and graph-conditioned fusion framework for joint forecasting of 69 surface and upper-air fields up to 14 days ahead.
- Combines predefined atmospheric relations with state-dependent Top-K residual edges within a Physics-Guided Dynamic Field Graph to adapt Earth-window attention.
- Implements Graph-Conditioned Latent Fusion using graph context and source-node centrality for robust field-to-latent aggregation with bounded feedback.
- Achieves competitive forecasting performance against established global weather models including FuXi, Pangu-Weather, GraphCast, FengWu, and ARROW on the 1.5 degree ERA5 benchmark.

## Archivist Review

Enforced strict scarcity and vault cleanliness by rejecting paper-local architectural models and standard resolution-scaling future work.

### Rejected Candidates
- [concept] VeinCast (`veincast`) - paper_local: Model-specific system architecture notes are generally rejected unless they represent broadly reusable standalone algorithms or methodological primitives.
- [open_question] Higher-Resolution and Probabilistic Forecasting (`higher-resolution-probabilistic-weather-forecasting`) - low_impact: Standard future work calling for higher-resolution and probabilistic extensions of a specific weather model is too generic and paper-local.

## Links

- [Abstract](https://arxiv.org/abs/2608.09286)
- [PDF](https://arxiv.org/pdf/2608.09286)

