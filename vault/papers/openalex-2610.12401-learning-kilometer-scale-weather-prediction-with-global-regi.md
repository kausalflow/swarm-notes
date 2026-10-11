---
# CSL-compatible fields
title: "Learning Kilometer-Scale Weather Prediction with Global-Regional Alignment"
author:
  - literal: "Guowen Li"
  - literal: "Yang Liu"
  - literal: "Yujie Wang"
  - literal: "Qiuyan Sun"
  - literal: "Haoyuan Liang"
  - literal: "Juepeng Zheng"
  - literal: "Hong Cheng"
  - literal: "Haohuan Fu"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.12401"

# Custom fields
paper_id: "2610.12401"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "scalecast"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-11T11:04:54Z"
created_at: "2026-10-11T11:04:54Z"
---

# Learning Kilometer-Scale Weather Prediction with Global-Regional Alignment

**Authors**: Guowen Li, Yang Liu, Yujie Wang, Qiuyan Sun, Haoyuan Liang, Juepeng Zheng, Hong Cheng, Haohuan Fu
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.12401](https://arxiv.org/abs/2610.12401)

## Summary

The authors propose ScaleCast, a regional weather forecasting framework designed for kilometer-scale predictions that aligns and leverages pretrained global weather models without requiring task-specific retraining. The framework uses a Global-Regional Conversion module and a Global-Regional Alignment and Dynamics block to fuse large-scale guidance with local neighborhood interactions. Experiments on ERA5 and CERRA, alongside fine-tuning on HRRR, demonstrate superior performance across surface and upper-air variables as well as accurate windstorm case studies.

## Key Contributions

- Proposed ScaleCast, a kilometer-scale regional weather forecasting framework that aligns joint global and regional representations across different grids.
- Integrated multiple global forecast drivers (Pangu-Weather, GraphCast, and HRES) without specific retraining into a single trained model.
- Demonstrated robust adaptability through fine-tuning on HRRR at 3 km spacing and improved cyclone positioning and core-pressure estimates in windstorm case studies.

## Open Questions & Future Work

- [[global-regional-weather-forecasting-generalization]]

## Key Concepts

- [[scalecast]]: A regional weather forecasting framework that leverages global-regional alignment to reuse pretrained global weather models for high-resolution predictions.

## Archivist Review

Approved the overarching framework concept 'ScaleCast' and the corresponding open question on global-regional weather forecasting generalization. Adhered strictly to the scarcity policy and avoided duplicate concepts or routine datasets.

### Approved Concepts
- ScaleCast: ScaleCast is the central methodological contribution of the paper, providing a global-regional alignment framework for kilometer-scale weather prediction.

### Approved Open Questions
- Global-Regional Weather Forecasting Generalization: Understanding how to generalize data-driven weather forecasting models across varying regional domains and upstream global drivers without retraining is critical for practical, operational deployment.

## Links

- [Abstract](https://arxiv.org/abs/2610.12401)
- [PDF](https://arxiv.org/pdf/2610.12401)

