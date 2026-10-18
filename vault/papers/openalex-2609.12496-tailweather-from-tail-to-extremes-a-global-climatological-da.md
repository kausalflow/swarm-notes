---
# CSL-compatible fields
title: "TailWeather: from tail to extremes, a global climatological dataset for machine-learning weather forecasting"
author:
  - literal: "Zhi-Song Liu"
  - literal: "Michael Boy"
  - literal: "Risto Makkonen"
issued:
  date-parts:
    - [2026, 10, 16]
url: "https://arxiv.org/abs/2609.12496"

# Custom fields
paper_id: "2609.12496"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "benchmark"
  - "dataset"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  - "tailweather"
concept_slugs:
  []
dataset_slugs:
  - "tailweather"
skill: "TimeSeriesSkill"
processed_at: "2026-10-18T09:13:12Z"
created_at: "2026-10-18T09:13:12Z"
---

# TailWeather: from tail to extremes, a global climatological dataset for machine-learning weather forecasting

**Authors**: Zhi-Song Liu, Michael Boy, Risto Makkonen
**Date**: 2026-10-16
**Paper ID**: [openalex:2609.12496](https://arxiv.org/abs/2609.12496)

## Summary

TailWeather is a global, land-only 0.25° climatological dataset derived from ERA5 (1981–2022) that labels extreme weather events—including heatwaves, cold waves, heavy precipitation, extreme wind, and drought—with ordinal severity tiers and intensity scores. Evaluations using this dataset reveal that leading AI weather forecasting models, while exhibiting high average skill, struggle significantly when predicting extreme tail events like heatwaves and extreme winds. This work establishes a reusable benchmark for assessing and improving machine learning models on high-impact meteorological extremes.

## Key Contributions

- Introduces TailWeather, a global, land-only 0.25° dataset of climatological tail events covering 1981–2022 derived from ERA5.
- Provides daily labels for heatwaves, cold waves, heavy precipitation, and extreme wind, alongside monthly meteorological drought labels with ordinal severity tiers and intensity scores.
- Demonstrates that leading AI weather prediction systems experience significant drops in critical success index when evaluating extreme tail events compared to standard average skill metrics.

## Limitations

Climatological tails do not perfectly equate to disaster impacts, and 80.1% of the world's land population lives in areas where disaster catalogs are too sparse for local verification.

## Open Questions & Future Work

- [[reconciling-pointwise-accuracy-and-extreme-event-detection]]

## Archivist Review

The dataset 'TailWeather' is approved as a core resource for evaluating machine learning weather extremes. The open question regarding reconciling pointwise accuracy and extreme detection is also approved because it captures a fundamental unresolved tension in weather forecasting models. Concepts were rejected to maintain strict vault standards since the primary contribution is a dataset benchmark.

### Approved Open Questions
- Reconciling Pointwise Accuracy and Extreme Detection: Resolving this trade-off is critical for developing trustworthy AI weather prediction systems that excel in both routine forecasting and disaster early warning.

### Rejected Candidates
- [concept] TailWeather (`tailweather`) - not_novel: TailWeather is primarily a dataset contribution rather than an algorithmic concept, and is best captured as an approved dataset.

## Datasets

- [[tailweather]]

## Links

- [Abstract](https://arxiv.org/abs/2609.12496)
- [PDF](https://arxiv.org/pdf/2609.12496)

