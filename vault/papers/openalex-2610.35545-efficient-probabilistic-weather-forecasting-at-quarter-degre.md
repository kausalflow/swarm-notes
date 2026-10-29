---
# CSL-compatible fields
title: "Efficient probabilistic weather forecasting at quarter-degree resolution with two-sided transport attention"
author:
  - literal: "Junu Choi"
  - literal: "Youngjoon Hong"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35545"

# Custom fields
paper_id: "2610.35545"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "transformer"
  - "attention-mechanism"
  - "multimodal"
  - "benchmark"
  - "dataset"
  - "evaluation"
architectures:
  - "encoder-only"
datasets:
  - "weatherbench2"
concept_slugs:
  - "kantorovich-attention"
dataset_slugs:
  - "weatherbench2"
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:11:00Z"
created_at: "2026-10-29T11:11:00Z"
---

# Efficient probabilistic weather forecasting at quarter-degree resolution with two-sided transport attention

**Authors**: Junu Choi, Youngjoon Hong
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35545](https://arxiv.org/abs/2610.35545)

## Summary

Astra is an efficient 0.25-degree probabilistic weather forecasting ensemble model that leverages Kantorovich Attention—a two-sided transport attention mechanism enabling token-resolution reading and writing across regions—and a self-featurised continuous ranked probability score (CRPS). Trained on eight H200 GPUs, Astra matches GenCast's CRPS on WeatherBench 2 using a fraction of the training compute while outperforming the ECMWF ensemble and GenCast across extensive evaluation combinations and operating efficiently on consumer hardware.

## Key Contributions

- Astra matches GenCast's CRPS averaged over five upper-air targets and days 1-10 on WeatherBench 2 while using only 9.8% of its hardware-normalised training compute.
- Achieves lower CRPS and ensemble-mean RMSE than the ECMWF ensemble across all 600 variable, level, and lead-time combinations.
- Enables generating 50 ensemble members in under 40 minutes on a single consumer GPU within 21 GB, requiring 39x fewer FLOPs than GenCast's implementation.

## Open Questions & Future Work

- [[scaling-transport-attention-higher-resolutions]]

## Key Concepts

- [[kantorovich-attention]]: A two-sided transport attention mechanism where each region chooses reading and writing locations at token resolution for efficient spatial modeling.

## Archivist Review

Approved Kantorovich Attention as a reusable spatial transport attention mechanism and WeatherBench 2 as a canonical benchmark dataset. The open question regarding scaling transport attention to higher resolutions was also retained. All items adhere to vault standards and criteria.

### Approved Concepts
- Kantorovich Attention: It introduces a two-sided transport attention mechanism enabling efficient token-resolution communication across regions for high-resolution weather forecasting.

### Approved Open Questions
- Scaling Transport Attention to Higher Resolutions: Scaling sparse transport attention to ultra-high resolutions is critical for capturing finer regional atmospheric dynamics and expanding the accessibility of frontier weather models.

### Rejected Candidates
- [concept] Self-featurised CRPS (`self-featurised-crps`) - subcomponent_of_broader_mechanism: Loss functions and scoring rules like CRPS variants are generally subcomponents of broader training frameworks unless established as standalone optimization frameworks.

## Datasets

- [[weatherbench2]]

## Links

- [Abstract](https://arxiv.org/abs/2610.35545)
- [PDF](https://arxiv.org/pdf/2610.35545)

