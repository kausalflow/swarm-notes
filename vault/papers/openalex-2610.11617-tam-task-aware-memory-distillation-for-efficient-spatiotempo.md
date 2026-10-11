---
# CSL-compatible fields
title: "TAM: Task-Aware Memory Distillation for Efficient Spatiotemporal Prediction"
author:
  - literal: "Yuqi Li"
  - literal: "Xiaoqin Feng"
  - literal: "Fan Xu"
  - literal: "Weilun Feng"
  - literal: "Chuanguang Yang"
  - literal: "Yingli Tian"
  - literal: "Hao Wu"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.11617"

# Custom fields
paper_id: "2610.11617"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "forecasting"
  - "time-series"
  - "knowledge-distillation"
  - "video-prediction"
  - "spatiotemporal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "task-aware-memory-distillation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-11T11:05:07Z"
created_at: "2026-10-11T11:05:07Z"
---

# TAM: Task-Aware Memory Distillation for Efficient Spatiotemporal Prediction

**Authors**: Yuqi Li, Xiaoqin Feng, Fan Xu, Weilun Feng, Chuanguang Yang, Yingli Tian, Hao Wu
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.11617](https://arxiv.org/abs/2610.11617)

## Summary

The authors propose TAM (Task-Aware Memory Distillation), a novel knowledge distillation framework for efficient spatiotemporal prediction that organizes a frozen teacher's knowledge into a bounded, retrievable history. By utilizing task-specific selection rules and objectives such as similarity distribution matching and residual prototype regression, TAM exploits cross-sample predictive structures without adding any inference cost to the student. Evaluations across video prediction, weather forecasting (WeatherBench), and traffic flow prediction (TaxiBJ) demonstrate consistent improvements over conventional KD baselines.

## Key Contributions

- Proposes TAM, a Task-Aware Memory Distillation framework that organizes a frozen teacher's knowledge into a bounded, retrievable history for spatiotemporal prediction.
- Introduces task-specific selection rules and complementary objectives where the student matches similarity distributions or regresses observation-conditioned residual prototypes.
- Demonstrates performance improvements across video prediction, weather forecasting, and traffic flow prediction, achieving MSE reductions of 1.86% on KittiCaltech, 1.93% on WeatherBench with a gSTA teacher, and 1.01% on TaxiBJ relative to standard KD baselines.
- Ensures zero additional student inference cost since the teacher, memory, and auxiliary adapters are used exclusively during training.

## Limitations

Future work could explore scaling the bounded retrievable history to larger sequence lengths and diverse multi-modal spatiotemporal tasks.

## Key Concepts

- [[task-aware-memory-distillation]]: A knowledge distillation framework for spatiotemporal prediction that organizes a frozen teacher's knowledge into a bounded, retrievable history.

## Archivist Review

Approved the central framework concept 'task-aware-memory-distillation' as it presents a distinct memory-based distillation mechanism for spatiotemporal prediction. No datasets or open questions met the strict standalone criteria.

### Approved Concepts
- Task-Aware Memory Distillation: Central novelty of the paper, introducing a memory-based knowledge distillation framework for spatiotemporal prediction that leverages cross-sample predictive structure.

### Rejected Candidates
- [concept] Spatiotemporal Prediction KD (`spatiotemporal-prediction-kd`) - not_reusable: Too generic and overlaps with standard distillation practices.

## Links

- [Abstract](https://arxiv.org/abs/2610.11617)
- [PDF](https://arxiv.org/pdf/2610.11617)

