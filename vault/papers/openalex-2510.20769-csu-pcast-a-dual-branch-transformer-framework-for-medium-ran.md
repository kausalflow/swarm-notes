---
# CSL-compatible fields
title: "CSU-PCAST: a dual-branch transformer framework for medium-range ensemble precipitation forecasting"
author:
  - literal: "Tianyi Xiong"
  - literal: "Haonan Chen"
  - literal: "Kelly Mahoney"
  - literal: "Jingyin Tang"
  - literal: "Tim Smith"
  - literal: "Janice Bytheway"
issued:
  date-parts:
    - [2026, 7, 7]
url: "https://arxiv.org/abs/2510.20769"

# Custom fields
paper_id: "2510.20769"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
architectures:
  - "encoder-decoder"
datasets:
  - "ERA5"
  - "IMERG"
concept_slugs:
  - "csu-pcast"
dataset_slugs:
  - "era5"
  - "imerg"
skill: "TimeSeriesSkill"
processed_at: "2026-07-10T08:15:18Z"
created_at: "2026-07-10T08:15:18Z"
---

# CSU-PCAST: a dual-branch transformer framework for medium-range ensemble precipitation forecasting

**Authors**: Tianyi Xiong, Haonan Chen, Kelly Mahoney, Jingyin Tang, Tim Smith, Janice Bytheway
**Date**: 2026-07-07
**Paper ID**: [openalex:2510.20769](https://arxiv.org/abs/2510.20769)

## Summary

CSU-PCAST is a dual-branch transformer-based ensemble forecasting framework designed for medium-range, global 6-hour precipitation prediction. By leveraging a Swin Transformer backbone, periodic padding, and stochastic noise conditioning, the model generates 30-member autoregressive forecasts up to 15 days in advance. Evaluations against the GEFS operational ensemble demonstrate significant improvements in short-lead deterministic skill, bias reduction, and probabilistic reliability for precipitation extremes.

## Key Contributions

- Developed CSU-PCAST, a deep learning ensemble framework that uses a dual-branch decoder to predict both 6-h total precipitation and atmospheric state variables.
- Achieved improved short-lead deterministic skill (higher CSI, lower RMSE) compared to the GEFS operational ensemble during the first several forecast days in 2023.
- Demonstrated reduced systemic wet bias for light precipitation and improved Brier Skill Scores, with enhanced spatial structure and exceedance-probability guidance for extreme events like the Sanba precipitation case.

## Limitations

Both the CSU-PCAST and GEFS systems remain underdispersive, and further research is required to improve high-end precipitation intensity and ensemble calibration.

## Open Questions & Future Work

- [[mitigating-precipitation-smoothing-in-dl-models]]

## Key Concepts

- [[csu-pcast]]: A dual-branch transformer-based ensemble forecasting framework for global 6-h precipitation prediction that combines atmospheric state modeling with stochastic noise conditioning.

## Archivist Review

I have approved the core architecture (CSU-PCAST) as it represents a significant dual-branch approach to atmospheric ensemble forecasting. The open question regarding precipitation smoothing is highly relevant as it captures the fundamental trade-off between regression-based stability and the representation of localized high-intensity weather features. Datasets ERA5 and IMERG were approved as they are standard, central benchmarks in the field of meteorological deep learning.

### Approved Concepts
- CSU-PCAST: It provides a specialized dual-branch transformer architecture that integrates atmospheric state prediction with precipitation forecasting for medium-range ensemble members.

### Approved Open Questions
- Mitigating precipitation smoothing in DL models: Addressing this smoothing issue is critical for improving the utility of deep learning weather models for high-impact hydrometeorological event forecasting, where precise spatial structure and peak intensity are often more important than aggregate statistical performance.

## Datasets

- [[era5]]
- [[imerg]]

## Links

- [Abstract](https://arxiv.org/abs/2510.20769)
- [PDF](https://arxiv.org/pdf/2510.20769)

