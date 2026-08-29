---
# CSL-compatible fields
title: "Scalable Multi-GPU Simulation of 3D Multicellular Growth with RNN-Based Workload Balancing"
author:
  - literal: "Matvey Moisseyev"
  - literal: "Huijing Du"
  - literal: "DanDan Zheng"
  - literal: "Chi Zhang"
  - literal: "Hongfeng Yu"
issued:
  date-parts:
    - [2026, 8, 26]
url: "https://arxiv.org/abs/2608.25890"

# Custom fields
paper_id: "2608.25890"
paper_source: "openalex"
domain: "biology"
tags:
  - "rnn"
  - "distributed-training"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-29T11:24:02Z"
created_at: "2026-08-29T11:24:02Z"
---

# Scalable Multi-GPU Simulation of 3D Multicellular Growth with RNN-Based Workload Balancing

**Authors**: Matvey Moisseyev, Huijing Du, DanDan Zheng, Chi Zhang, Hongfeng Yu
**Date**: 2026-08-26
**Paper ID**: [openalex:2608.25890](https://arxiv.org/abs/2608.25890)

## Summary

This paper presents a scalable multi-GPU framework for 3D multicellular growth simulations based on subcellular element models, addressing the challenge of dynamically evolving spatial workloads. The authors introduce an RNN-based load-balancing controller, trained on a differentiable surrogate without execution traces, which learns residual corrections to reactive boundary-adjustment rules. Evaluations on embryonic epidermal development show that the approach reduces global workload imbalance to 3.5%, improves runtime, and drastically cuts slice migration compared to conventional static and reactive partitioning baselines.

## Key Contributions

- Introduces a scalable multi-GPU framework for 3D multicellular growth simulation integrating GPU acceleration, spatial binning, domain decomposition, and workload-aware partitioning.
- Develops an RNN-based load-balancing controller trained on a differentiable surrogate of the load-balancing loop to predict residual corrections to reactive boundary adjustments without requiring measured execution traces.
- Reduces mean global workload imbalance from 11.3% (static) to 3.5%, lowers end-to-end runtime by 9.0%, and decreases slice migration by 7.7x compared to reactive baselines.

## Archivist Review

Applied strict selectivity guidelines. The paper focuses on a multi-GPU systems engineering and simulation workload balancing framework for biological cell growth, which does not align with our machine learning/time-series forecasting knowledge vault scope. Consequently, all candidates were rejected.

### Rejected Candidates
- [concept] RNN-based load-balancing controller (`rnn-based-load-balancing-controller`) - low_impact: This is a domain-specific, systems-level load-balancing technique for multi-GPU biological simulations rather than a general time-series forecasting or neural architecture method.
- [open_question] Million-Cell Multicellular Simulation Scaling (`million-cell-multicellular-simulation-scaling`) - paper_local: This addresses paper-specific scaling limits for multi-GPU biological simulations rather than a broad, reusable machine learning or time-series research question.

## Links

- [Abstract](https://arxiv.org/abs/2608.25890)
- [PDF](https://arxiv.org/pdf/2608.25890)

