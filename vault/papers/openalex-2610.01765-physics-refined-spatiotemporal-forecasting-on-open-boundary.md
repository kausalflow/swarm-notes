---
# CSL-compatible fields
title: "Physics-Refined Spatiotemporal Forecasting on Open-Boundary Hydrologic Graphs"
author:
  - literal: "Haoyang Jiang"
  - literal: "Zhengui Wang"
  - literal: "Shenghan Gao"
  - literal: "Y. Joseph Zhang"
  - literal: "Xingquan Zhu"
  - literal: "Yi He"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2610.01765"

# Custom fields
paper_id: "2610.01765"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
  - "gnn"
  - "robustness"
  - "long-context"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:49:12Z"
created_at: "2026-10-04T10:49:12Z"
---

# Physics-Refined Spatiotemporal Forecasting on Open-Boundary Hydrologic Graphs

**Authors**: Haoyang Jiang, Zhengui Wang, Shenghan Gao, Y. Joseph Zhang, Xingquan Zhu, Yi He
**Date**: 2026-10-01
**Paper ID**: [openalex:2610.01765](https://arxiv.org/abs/2610.01765)

## Summary

This paper addresses open-boundary instability in hydrologic graph forecasting, where unobserved external fluxes compound errors during autoregressive rollout. The authors propose a computing framework that learns ghost node proxies to approximate unavailable boundary inputs while employing dual physics refiners for local consistency and global stability. Evaluated on two real-world hydrologic graphs, the approach demonstrates superior prediction accuracy and long-horizon stability compared to existing learning-based and physics-informed models.

## Key Contributions

- Dissects open-boundary hydrologic forecasting instability caused by unobserved exterior fluxes during autoregressive rollout
- Proposes a computing framework that learns ghost node proxies to approximate unavailable external boundary forcing
- Introduces a dual physics refiner combining local consistency alignment with a physics-guided graph neural operator for long-horizon stability

## Archivist Review

The paper proposes an open-boundary hydrologic forecasting framework using ghost node proxies and physics refiners. No concepts or open questions met the strict novelty and reusability standards for permanent vault notes.

### Rejected Candidates
- [open_question] Abrupt Forcing and Uncertainty Forecasting (`abrupt-external-forcing-uncertainty-forecasting`) - weak_evidence: Generic future work on extreme events and uncertainty estimation that does not establish a specific, reusable theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.01765)
- [PDF](https://arxiv.org/pdf/2610.01765)

