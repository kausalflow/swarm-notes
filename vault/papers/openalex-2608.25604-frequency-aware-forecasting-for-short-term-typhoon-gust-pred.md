---
# CSL-compatible fields
title: "Frequency-aware forecasting for short-term typhoon gust prediction"
author:
  - literal: "Xuefei Wang"
  - literal: "Tingyi Liu"
  - literal: "Heng Zhang"
  - literal: "Shengjun Zhang"
issued:
  date-parts:
    - [2026, 8, 26]
url: "https://arxiv.org/abs/2608.25604"

# Custom fields
paper_id: "2608.25604"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "wdanet"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T16:59:39Z"
created_at: "2026-08-28T16:59:39Z"
---

# Frequency-aware forecasting for short-term typhoon gust prediction

**Authors**: Xuefei Wang, Tingyi Liu, Heng Zhang, Shengjun Zhang
**Date**: 2026-08-26
**Paper ID**: [openalex:2608.25604](https://arxiv.org/abs/2608.25604)

## Summary

This paper proposes WDANet, a frequency-aware forecasting framework for short-term typhoon gust prediction that uses stationary wavelet decomposition and a Feature-wise Linear Modulation (FiLM) strategy within a dual-branch encoder-decoder architecture. By modeling trend and fluctuation components separately, WDANet outperforms ECMWF-HRES within the first 6 hours of a 24-hour horizon and accurately captures gust peaks during extreme wind events.

## Key Contributions

- Proposed WDANet, a frequency-aware forecasting framework combining stationary wavelet decomposition and FiLM for short-term typhoon gust prediction.
- Demonstrated superior short lead time performance across a 24-h forecasting horizon, achieving higher prediction accuracy than ECMWF-HRES within the first 6 h.
- Achieved best RMSE and MAE performance during extreme wind events by accurately capturing gust peaks.

## Limitations

Evaluated specifically on offshore regions of the Western Pacific in China; generalization to other geographical regions and storm types remains to be explored.

## Open Questions & Future Work

- [[extreme-wind-gust-peak-reconstruction]]

## Key Concepts

- [[wdanet]]: A frequency-aware forecasting framework combining stationary wavelet decomposition and FiLM with a dual-branch encoder-decoder for typhoon gust prediction.

## Archivist Review

Applied high selectivity, approving only the core framework concept (WDANet) and the specific open question regarding extreme wind gust peak reconstruction, while ensuring no low-value metadata or routine datasets were admitted.

### Approved Concepts
- WDANet: Serves as the core proposed model integrating stationary wavelet decomposition and FiLM for separated trend and fluctuation modeling in typhoon gust prediction.

### Approved Open Questions
- Extreme Wind Gust Peak Reconstruction: Accurate reconstruction of peak gusts is critical for structural safety and wind turbine fatigue mitigation under severe typhoon conditions.

## Links

- [Abstract](https://arxiv.org/abs/2608.25604)
- [PDF](https://arxiv.org/pdf/2608.25604)

