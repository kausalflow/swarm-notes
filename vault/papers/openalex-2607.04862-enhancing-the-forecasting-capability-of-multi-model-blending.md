---
# CSL-compatible fields
title: "Enhancing the Forecasting Capability of Multi-Model Blending Algorithms for Extreme Precipitation via Joint Use of Station and Gridded Observations"
author:
  - literal: "Yu Wang"
  - literal: "Yong Cao"
  - literal: "Kan Dai"
  - literal: "Yue SHEN"
  - literal: "Xiaoqing Zeng"
  - literal: "R C Zhao"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2607.04862"

# Custom fields
paper_id: "2607.04862"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "deep-learning"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "station-grid-joint-supervision-mechanism"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:18:14Z"
created_at: "2026-07-09T08:18:14Z"
---

# Enhancing the Forecasting Capability of Multi-Model Blending Algorithms for Extreme Precipitation via Joint Use of Station and Gridded Observations

**Authors**: Yu Wang, Yong Cao, Kan Dai, Yue SHEN, Xiaoqing Zeng, R C Zhao
**Date**: 2026-07-06
**Paper ID**: [openalex:2607.04862](https://arxiv.org/abs/2607.04862)

## Summary

This paper presents a two-stage U-Net architecture for blending six numerical weather prediction (NWP) models to improve extreme precipitation forecasting. By implementing a novel station-grid joint supervision mechanism, the framework incorporates point-based station observations into the loss function to effectively mitigate NWP spatial displacement and intensity smoothing. Evaluation on 2025 flood season data shows significant improvements, with a 38.4% increase in threat scores for heavy rainstorms and superior handling of extreme events compared to operational products.

## Key Contributions

- Proposes a two-stage U-Net framework (probability classification followed by value reconstruction) to blend multiple NWP model outputs for precipitation forecasting.
- Introduces a station-grid joint supervision mechanism that yields a 38.4% TS improvement for rainstorms (>50 mm) over the best baseline NWP.
- Achieves TS > 0.1 for extreme events (>100 mm) by correcting systematic NWP displacement and intensity underestimation.

## Key Concepts

- [[station-grid-joint-supervision-mechanism]]: A training loss integration strategy that uses both point-based station observations and grid-based forecasts to constrain the spatial structure and intensity of extreme precipitation predictions.

## Archivist Review

I approved the 'station-grid joint supervision mechanism' as a distinct, reusable methodology for reconciling multi-scale observational and gridded data in spatiotemporal forecasting. I rejected the dataset because it is a localized observational set rather than a benchmark repository. No open questions were approved as the paper focuses on a specific engineering solution for precipitation blending without identifying broader, unresolved research gaps.

### Approved Concepts
- station-grid joint supervision mechanism: Addresses the systemic bias in extreme weather forecasting by combining sparse station data with grid-based NWP outputs to preserve peak intensity and improve spatial alignment.

### Rejected Candidates
- [dataset] 2025 flood season China station dataset (`2025-flood-season-china-station-dataset`) - paper_local: This is a localized, proprietary observational dataset rather than a standardized, widely reusable benchmark.

## Links

- [Abstract](https://arxiv.org/abs/2607.04862)
- [PDF](https://arxiv.org/pdf/2607.04862)

