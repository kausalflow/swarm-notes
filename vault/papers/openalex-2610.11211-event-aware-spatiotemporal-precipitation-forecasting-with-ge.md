---
# CSL-compatible fields
title: "Event-Aware Spatiotemporal Precipitation Forecasting with Geographic Context and Physics-Guided Regularization"
author:
  - literal: "Yiping Hong"
  - literal: "Xinyu Wang"
  - literal: "Sameh Abdulah"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.11211"

# Custom fields
paper_id: "2610.11211"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "spatiotemporal"
  - "physics-informed"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-10T10:53:23Z"
created_at: "2026-10-10T10:53:23Z"
---

# Event-Aware Spatiotemporal Precipitation Forecasting with Geographic Context and Physics-Guided Regularization

**Authors**: Yiping Hong, Xinyu Wang, Sameh Abdulah
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.11211](https://arxiv.org/abs/2610.11211)

## Summary

This paper introduces a spatiotemporal precipitation forecasting framework designed to handle spatial heterogeneity, heavy distribution imbalance, and lead-time skill degradation. It integrates explicit geographic representations, event-aware learning modules, and weak asymmetric regularization derived from the atmospheric water budget as a physical constraint. Experiments on ERA5 datasets reveal that geographic encoding improves spatial fields, event-aware learning enhances heavy precipitation detection, and physical regularization mitigates underprediction at longer lead times.

## Key Contributions

- Developed a spatiotemporal forecasting framework combining explicit geographic representation, event-aware learning, and weak asymmetric physics-guided regularization.
- Demonstrated that event-aware learning provides consistent gains in detecting moderate and heavy precipitation events across regional, enlarged domain, and spatial subset settings.
- Showed that physics-guided regularization via the atmospheric water budget reduces systematic underprediction and improves longer lead precipitation event prediction.

## Limitations

Physical regularization shows a selective effect depending on the data regime, becoming most beneficial as data-driven accuracy degrades with lead time.

## Open Questions & Future Work

- [[precipitation-false-alarm-tradeoff]]
- [[physics-guided-regularization-extension]]

## Archivist Review

All proposed concepts were rejected as paper-local combinations or standard architectural elements, and the dataset is already present in the vault. Two distinct open questions on precipitation false alarm tradeoffs and physics-guided regularization extensions were approved as valuable long-term research directions.

### Approved Open Questions
- Balancing Event Detection and False Alarms: Balancing high-intensity event detection with false alarm rates is a persistent bottleneck in imbalanced spatiotemporal classification and regression tasks.
- Extending Physics-Guided Regularization Strategies: Extending physics-guided constraints to broader atmospheric variables improves the generalizability and robustness of hybrid data-driven physical models across different climate zones.

### Rejected Candidates
- [concept] Event-Aware Spatiotemporal Precipitation Forecasting (`event-aware-spatiotemporal-precipitation-forecasting`) - paper_local: Paper-local combination of standard components rather than a broadly reusable standalone concept.
- [dataset] ERA5 (`era5`) - duplicate_existing: Already exists in the vault under canonical naming.

## Links

- [Abstract](https://arxiv.org/abs/2610.11211)
- [PDF](https://arxiv.org/pdf/2610.11211)

