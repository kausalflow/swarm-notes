---
# CSL-compatible fields
title: "PROSWIN: Probabilistic Solar Wind Speed Forecasting Using Deep Distributional Regression From Solar Images"
author:
  - literal: "Daniel Collin"
  - literal: "Yuri Shprits"
  - literal: "Luca Chiarabini"
  - literal: "Stefan J. Hofmeister"
  - literal: "Nadja Klein"
  - literal: "Guillermo Gallego"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.26683"

# Custom fields
paper_id: "2609.26683"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "uncertainty-quantification"
  - "multimodal"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-25T09:55:02Z"
created_at: "2026-09-25T09:55:02Z"
---

# PROSWIN: Probabilistic Solar Wind Speed Forecasting Using Deep Distributional Regression From Solar Images

**Authors**: Daniel Collin, Yuri Shprits, Luca Chiarabini, Stefan J. Hofmeister, Nadja Klein, Guillermo Gallego
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.26683](https://arxiv.org/abs/2609.26683)

## Summary

PROSWIN is a probabilistic deep distributional regression model that forecasts hourly solar wind speed at Earth four days in advance using solar images and magnetograms. To address the failure of standard metrics in capturing dangerous high-speed solar wind streams, the authors introduce a specialized prediction score that jointly evaluates timeline and peak accuracy. Evaluated on 14 years of data, PROSWIN yields well-calibrated probabilistic forecasts and avoids the traditional trade-off between baseline timeline accuracy and peak accuracy.

## Key Contributions

- Introduces PROSWIN, a probabilistic machine learning model combining deep neural networks and distributional regression to forecast hourly solar wind speed with a four-day lead time.
- Proposes the prediction score, a novel model-selection metric that jointly rewards timeline accuracy and high-speed solar wind stream (HSS) peak accuracy.
- Achieves well-calibrated uncertainties with <1% average deviation and robust performance across a 14-year dataset, outperforming literature baselines that trade off timeline versus HSS peak accuracy.
- Demonstrates that combining the 171 Å channel with traditional 193 Å and 211 Å channels significantly enhances solar wind speed forecasting.

## Archivist Review

Evaluated the proposed concept and open question under strict filtering criteria. PROSWIN is specific to space weather application rather than a foundational ML concept, and the open question is too domain-specific to coronal mass ejections. Therefore, no new vault notes are created.

### Rejected Candidates
- [concept] PROSWIN (`proswin`) - paper_local: PROSWIN is a paper-specific model name tailored to solar wind forecasting rather than a broadly reusable methodological concept.
- [open_question] Unified HSS and CME Forecasting (`unified-hss-cme-forecasting`) - low_impact: This open question is extremely narrow and domain-specific to space weather and coronal mass ejections, lacking broader applicability across general time-series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2609.26683)
- [PDF](https://arxiv.org/pdf/2609.26683)

