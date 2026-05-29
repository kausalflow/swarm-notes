---
# CSL-compatible fields
title: "EpiCurveBench: Evaluating VLMs on Epidemic Curve Digitization"
author:
  - literal: "Thomas Berkane"
  - literal: "Maimuna S. Majumder"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.27195"

# Custom fields
paper_id: "2605.27195"
paper_source: "openalex"
domain: "nlp"
tags:
  - "multimodal"
  - "vision-language-model"
  - "benchmark"
  - "dataset"
  - "evaluation"
  - "time-series"
architectures:
  []
datasets:
  - "EpiCurveBench"
concept_slugs:
  - "epicurvesimilarity-ecs"
dataset_slugs:
  - "epicurvebench"
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:39:19Z"
created_at: "2026-05-29T08:39:19Z"
---

# EpiCurveBench: Evaluating VLMs on Epidemic Curve Digitization

**Authors**: Thomas Berkane, Maimuna S. Majumder
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.27195](https://arxiv.org/abs/2605.27195)

## Summary

The authors introduce EpiCurveBench, a benchmark of 1,000 public-health epidemic curve images, to address the saturation and limitations of existing chart-extraction benchmarks. To improve evaluation, they propose EpiCurveSimilarity (ECS), a dynamic programming metric that better captures temporal alignment and structural fidelity than standard key-value or DTW metrics. The study reveals that even frontier VLMs exhibit significant performance gaps on this task, suggesting that standard benchmarks for chart-to-data extraction do not adequately measure temporal reasoning or high-fidelity time-series reconstruction.

## Key Contributions

- Introduced EpiCurveBench, a new benchmark of 1,000 real-world epidemic curve images for evaluating chart-to-data extraction.
- Proposed EpiCurveSimilarity (ECS), a dynamic programming-based metric that outperforms key-value metrics and DTW in capturing temporal alignment and error correlation in epidemiology tasks.
- Demonstrated that frontier VLMs struggle with specialized epidemic curve extraction, achieving only 52.3% ECS despite high performance on generic chart benchmarks.

## Open Questions & Future Work

- [[vlm-chart-digitization-precision-limitations]]

## Key Concepts

- [[epicurvesimilarity-ecs]]: A dynamic programming-based evaluation metric for time-series extraction that balances temporal shift tolerance with proportional penalties for gaps.

## Archivist Review

I approved EpiCurveSimilarity (ECS) and EpiCurveBench as they provide a necessary, domain-agnostic framework for evaluating time-series extraction that corrects for the limitations of traditional key-value or DTW-based evaluation. The open question was reframed to focus on the specific structural bottlenecks (precision and truncation) in VLM chart-to-data pipelines rather than generic improvement goals. Other candidates were not proposed or were deemed redundant.

### Approved Concepts
- EpiCurveSimilarity (ECS): It provides a more structurally faithful evaluation of extracted time-series compared to unordered key-value metrics or standard DTW.

### Approved Open Questions
- VLM Chart Digitization Limitations: This addresses the gap between performance on generic chart benchmarks and task-specific utility in high-impact domains like public health.

## Datasets

- [[epicurvebench]]

## Links

- [Abstract](https://arxiv.org/abs/2605.27195)
- [PDF](https://arxiv.org/pdf/2605.27195)

