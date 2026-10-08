---
# CSL-compatible fields
title: "WaveGSSM: Graph Wave State Space Models for Propagating Spatio-Temporal Patterns"
author:
  - literal: "Junyou Zhu"
  - literal: "Fenying Cai"
  - literal: "Ping Xiong"
  - literal: "Christian Nauck"
  - literal: "Langzhou He"
  - literal: "Chao Gao"
  - literal: "J urgen Kurths"
  - literal: "Frank Hellmann"
issued:
  date-parts:
    - [2026, 10, 5]
url: "https://arxiv.org/abs/2610.06540"

# Custom fields
paper_id: "2610.06540"
paper_source: "openalex"
domain: "time-series"
tags:
  - "state-space-model"
  - "ssm"
  - "graph-neural-network"
  - "gnn"
  - "time-series"
  - "forecasting"
architectures:
  - "mamba"
datasets:
  []
concept_slugs:
  - "wavegssm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-08T11:41:37Z"
created_at: "2026-10-08T11:41:37Z"
---

# WaveGSSM: Graph Wave State Space Models for Propagating Spatio-Temporal Patterns

**Authors**: Junyou Zhu, Fenying Cai, Ping Xiong, Christian Nauck, Langzhou He, Chao Gao, J urgen Kurths, Frank Hellmann
**Date**: 2026-10-05
**Paper ID**: [openalex:2610.06540](https://arxiv.org/abs/2610.06540)

## Summary

WaveGSSM is a second-order graph state-space model designed for spatio-temporal forecasting that explicitly models pattern propagation and motion. By maintaining two coupled latent states per node representing the current pattern and its rate of change, it unifies spatial propagation and temporal evolution into a single rollout. Evaluations across four temporal-graph benchmarks and global weather forecasting show that WaveGSSM outperforms backbone-matched snapshot models while preserving large-scale atmospheric structures.

## Key Contributions

- Introduces WaveGSSM, a second-order graph state-space model maintaining two coupled latent states per node for pattern and temporal rate of change.
- Couples spatial propagation and temporal evolution within a single graph-wave transition rollout.
- Achieves best mean performance across four temporal-graph benchmarks and reduces geopotential RMSE by 20.2% on average for 1- to 5-day weather forecasts compared to snapshot models.

## Open Questions & Future Work

- [[explicit-motion-representation-spatio-temporal-graphs]]

## Key Concepts

- [[wavegssm]]: A second-order graph state-space model that maintains two coupled latent states per node to explicitly represent motion and pattern propagation in spatio-temporal forecasting.

## Archivist Review

Approved the core second-order graph state-space model (WaveGSSM) and the open question regarding explicit motion representation in spatio-temporal graph architectures, adhering strictly to scarcity and quality rules. No dataset candidates were provided in the analysis.

### Approved Concepts
- WaveGSSM: It introduces a novel second-order graph state-space model architecture that couples spatial propagation and temporal evolution using two latent states per node.

### Approved Open Questions
- Explicit Motion Representation in Spatio-Temporal Graph Models: Important for extending wave-inspired state-space models to a broader range of chaotic and propagating spatio-temporal systems.

## Links

- [Abstract](https://arxiv.org/abs/2610.06540)
- [PDF](https://arxiv.org/pdf/2610.06540)

