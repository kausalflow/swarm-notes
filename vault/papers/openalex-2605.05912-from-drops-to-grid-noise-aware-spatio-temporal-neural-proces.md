---
# CSL-compatible fields
title: "From Drops to Grid: Noise-Aware Spatio-Temporal Neural Process for Rainfall Estimation"
author:
  - literal: "Rafael Pablos Sarabia"
  - literal: "Joachim Nyborg"
  - literal: "Morten Birk"
  - literal: "Ira Assent"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.05912"

# Custom fields
paper_id: "2605.05912"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "multimodal"
  - "attention-mechanism"
  - "forecasting"
  - "uncertainty-quantification"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dropstogrid"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:22:58Z"
created_at: "2026-05-10T07:22:58Z"
---

# From Drops to Grid: Noise-Aware Spatio-Temporal Neural Process for Rainfall Estimation

**Authors**: Rafael Pablos Sarabia, Joachim Nyborg, Morten Birk, Ira Assent
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.05912](https://arxiv.org/abs/2605.05912)

## Summary

DropsToGrid is a Neural Process-based framework designed to generate high-resolution, continuous rainfall maps by integrating sparse, noisy weather station data with spatial radar context. The method utilizes multi-scale feature extraction, temporal attention, and multimodal fusion to handle the localized and skewed nature of rainfall data. By producing stochastic estimates with explicit uncertainty quantification, it offers improved reliability over traditional operational and existing deep learning baselines, particularly in data-scarce and cross-regional environments.

## Key Contributions

- DropsToGrid achieves superior accuracy and uncertainty calibration in high-resolution rainfall estimation compared to operational and standard deep learning benchmarks.
- The model provides robust rainfall maps by integrating sparse, noisy station observations with spatial radar context using multi-scale feature extraction and multimodal fusion.
- Demonstrates significant generalization performance in cross-regional scenarios and low-density station settings.

## Open Questions & Future Work

- [[radar-rainfall-mapping-bottleneck]]

## Key Concepts

- [[dropstogrid]]: A Neural Process-based framework for generating dense, uncertainty-aware rainfall fields from sparse and noisy sensor observations.

## Archivist Review

Approved DropsToGrid as a specific architectural framework for spatial densification using Neural Processes. Approved the radar mapping open question as it identifies a concrete technical challenge in physical-data fusion. Rejected the second open question for being overly broad and speculative.

### Approved Concepts
- DropsToGrid: It introduces a specific Neural Process-based architectural pattern for spatiotemporal densification that is highly relevant to environmental time-series monitoring.

### Approved Open Questions
- Radar-to-Rainfall Mapping Bottlenecks: Addressing the physical misalignment between remote sensing and surface observations is essential for reliable high-resolution weather forecasting.

### Rejected Candidates
- [open_question] Broadening probabilistic data assimilation (`probabilistic-data-assimilation-framework`) - low_impact: This is a broad, vague aspiration for future model expansion rather than a specific research problem or technical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2605.05912)
- [PDF](https://arxiv.org/pdf/2605.05912)

