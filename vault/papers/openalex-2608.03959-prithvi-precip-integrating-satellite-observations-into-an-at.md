---
# CSL-compatible fields
title: "Prithvi-Precip: Integrating Satellite Observations into an Atmospheric AI Foundation Model for Precipitation Forecasting"
author:
  - literal: "Simon Pfreundschuh"
  - literal: "Christian D. Kummerow"
  - literal: "Johannes Schmude"
  - literal: "Sujit Roy"
  - literal: "Rahul Ramachandran"
  - literal: "Tsengdar Lee"
  - literal: "Valentine Anantharaj"
  - literal: "Katherine H. Breen"
issued:
  date-parts:
    - [2026, 8, 4]
url: "https://arxiv.org/abs/2608.03959"

# Custom fields
paper_id: "2608.03959"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "language-model"
  - "pre-training"
  - "fine-tuning"
  - "multimodal"
  - "forecasting"
  - "autoregressive"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "prithvi-precip"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-07T06:04:29Z"
created_at: "2026-08-07T06:04:29Z"
---

# Prithvi-Precip: Integrating Satellite Observations into an Atmospheric AI Foundation Model for Precipitation Forecasting

**Authors**: Simon Pfreundschuh, Christian D. Kummerow, Johannes Schmude, Sujit Roy, Rahul Ramachandran, Tsengdar Lee, Valentine Anantharaj, Katherine H. Breen
**Date**: 2026-08-04
**Paper ID**: [openalex:2608.03959](https://arxiv.org/abs/2608.03959)

## Summary

Prithvi-Precip is a global precipitation forecasting system built by fine-tuning the Prithvi-WxC atmospheric AI foundation model using satellite-derived training targets and direct satellite observation ingestion. Evaluating against independent radar estimates, the authors demonstrate that autoregressive rollout training combined with satellite targets outperforms reanalysis-based training (MERRA-2), with direct satellite ingestion providing substantial accuracy gains in tropical and subtropical regions at short lead times.

## Key Contributions

- Developed Prithvi-Precip, a global precipitation forecasting system built on the Prithvi-WxC foundation model by integrating satellite observations and estimates.
- Demonstrated that autoregressive rollout training produces substantially more accurate precipitation forecasts than direct conditioning on forecast lead time.
- Showed that training on satellite-derived precipitation targets yields superior accuracy compared to training on MERRA-2 reanalysis fields when evaluated against radar estimates.
- Established that direct ingestion of satellite observations provides significant forecast improvements at short lead times, particularly in tropical and subtropical regions.

## Open Questions & Future Work

- [[improving-ai-precipitation-forecasting-targets-and-observations]]

## Key Concepts

- [[prithvi-precip]]: A global precipitation forecasting system that integrates satellite observations and estimates into the Prithvi-WxC atmospheric AI foundation model.

## Archivist Review

Approved the core model concept 'Prithvi-Precip' and the associated open question on improving precipitation targets and satellite ingestion, adhering strictly to scarcity and novelty guidelines. No new dataset notes were created as MERRA-2 is already in the vault and other mentions are general.

### Approved Concepts
- Prithvi-Precip: It is the core global precipitation forecasting system introduced by the paper, extending Prithvi-WxC with satellite observations and targets.

### Approved Open Questions
- Improving AI Precipitation Forecasting Targets: Addressing the quality of training targets and extending the observation ingestion mechanism are critical bottlenecks for bridging the performance gap between AI precipitation models and advanced conventional numerical weather prediction systems at longer lead times.

## Links

- [Abstract](https://arxiv.org/abs/2608.03959)
- [PDF](https://arxiv.org/pdf/2608.03959)

