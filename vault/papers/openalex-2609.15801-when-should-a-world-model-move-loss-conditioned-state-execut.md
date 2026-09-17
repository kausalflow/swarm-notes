---
# CSL-compatible fields
title: "When Should a World Model Move? Loss-Conditioned State Execution"
author:
  - literal: "Jintao Xu"
  - literal: "Zhengyu Chen"
  - literal: "Ben Zhang"
  - literal: "Yongzhi Qi"
  - literal: "Jianshen Zhang"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.15801"

# Custom fields
paper_id: "2609.15801"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "robustness"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "loss-conditioned-state-execution"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:45:16Z"
created_at: "2026-09-17T09:45:16Z"
---

# When Should a World Model Move? Loss-Conditioned State Execution

**Authors**: Jintao Xu, Zhengyu Chen, Ben Zhang, Yongzhi Qi, Jianshen Zhang
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.15801](https://arxiv.org/abs/2609.15801)

## Summary

The paper introduces loss-conditioned state execution, a model-agnostic method that decides whether a world model should execute a proposal or retain its current state by evaluating groupwise bounded-loss gain on independent calibration units. The authors formalize state movability to show that predictive informativeness or occurrence ranking alone is insufficient for deciding state updates. Experiments on the M4 Monthly dataset and JD.com inventory benchmarks demonstrate that the approach achieves favorable loss reduction and balances certification against coverage.

## Key Contributions

- Introduces loss-conditioned state execution, a model-agnostic method that decides whether to execute a world model's proposal or retain the current state based on loss reduction.
- Formalizes state movability as the existence of a loss-reducing feasible correction, distinct from predictive informativeness or occurrence ranking.
- Demonstrates on 28,684 M4 Monthly series that the method achieves superior bounded loss (0.588) compared to persistence (0.599) and always executing proposals (0.621).

## Key Concepts

- [[loss-conditioned-state-execution]]: A model-agnostic method that decides whether to execute a world model's proposal or retain the current state based on groupwise bounded-loss gain.

## Archivist Review

Approved the primary methodological concept 'Loss-Conditioned State Execution' as it provides a distinct, reusable framework for deciding selective state updates based on loss reduction rather than mere predictive informativeness. Rejected the open question as routine future work.

### Approved Concepts
- Loss-Conditioned State Execution: Central method introduced in the paper to decide whether a world model should update its state based on loss reduction rather than predictive informativeness alone.

### Rejected Candidates
- [open_question] Recursive Rollouts and Online Recalibration (`recursive-rollouts-online-recalibration`) - low_impact: The open question is broad future work focusing on multi-step rollouts without presenting an independent bottleneck or foundational open problem.

## Links

- [Abstract](https://arxiv.org/abs/2609.15801)
- [PDF](https://arxiv.org/pdf/2609.15801)

