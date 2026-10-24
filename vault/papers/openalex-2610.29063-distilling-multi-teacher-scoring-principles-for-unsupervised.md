---
# CSL-compatible fields
title: "Distilling Multi-Teacher Scoring Principles for Unsupervised Time Series Anomaly Detection"
author:
  - literal: "조동찬"
  - literal: "JiHo Han"
  - literal: "Juwon Hwang"
  - literal: "Changhee Min"
  - literal: "Minsang Kim"
  - literal: "Namsoon Jung"
  - literal: "Dongchan Cho"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2610.29063"

# Custom fields
paper_id: "2610.29063"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "knowledge-distillation"
  - "time-series"
  - "benchmark"
  - "zero-shot-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-24T09:11:52Z"
created_at: "2026-10-24T09:11:52Z"
---

# Distilling Multi-Teacher Scoring Principles for Unsupervised Time Series Anomaly Detection

**Authors**: 조동찬, JiHo Han, Juwon Hwang, Changhee Min, Minsang Kim, Namsoon Jung, Dongchan Cho
**Date**: 2026-10-21
**Paper ID**: [openalex:2610.29063](https://arxiv.org/abs/2610.29063)

## Summary

This paper proposes AnoMix, an unsupervised multi-teacher knowledge distillation framework designed to combine diverse anomaly scoring principles into a single lightweight time series anomaly detector. By introducing a ranking-distillation objective called CoRank, the method converts score gaps from multiple frozen teacher models into robust pairwise supervision via teacher consensus, avoiding the need for anomaly labels. Experiments across seven benchmark datasets show that the compact student model outperforms individual teachers and static ensembles while maintaining low inference and maintenance costs, and exhibits strong zero-shot transfer performance.

## Key Contributions

- Proposes AnoMix, an unsupervised multi-teacher distillation framework for time series anomaly detection that compresses heterogeneous scoring principles into a single lightweight student (<80k parameters).
- Introduces CoRank, a multi-teacher ranking-distillation objective that leverages teacher consensus to convert score gaps into pairwise supervision without requiring anomaly labels.
- Demonstrates superiority across seven benchmark datasets over individual detectors and static score ensembles, along with strong zero-shot transfer capabilities to unseen datasets.

## Archivist Review

Applied rigorous standards: no concepts met the strict novelty and reusability threshold for standalone architecture/mechanism notes, and the single proposed open question was rejected as a standard multi-teacher failure mode rather than a major broad research bottleneck.

### Rejected Candidates
- [open_question] Mitigating Correlated Teacher Failures (`mitigating-correlated-teacher-failures-tsad`) - low_impact: The question addresses standard teacher-student distillation failure modes without introducing a distinct, broadly reusable bottleneck or methodological formulation.

## Links

- [Abstract](https://arxiv.org/abs/2610.29063)
- [PDF](https://arxiv.org/pdf/2610.29063)

