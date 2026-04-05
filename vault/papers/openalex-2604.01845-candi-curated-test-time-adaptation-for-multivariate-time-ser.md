---
# CSL-compatible fields
title: "CANDI: Curated Test-Time Adaptation for Multivariate Time-Series Anomaly Detection Under Distribution Shift"
author:
  - literal: "HyunGi Kim"
  - literal: "Jisoo Mok"
  - literal: "Hyungyu Lee"
  - literal: "Juhyeon Shin"
  - literal: "Sungroh Yoon"
issued:
  date-parts:
    - [2026, 4, 2]
url: "https://arxiv.org/abs/2604.01845"

# Custom fields
paper_id: "2604.01845"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "fine-tuning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "false-positive-mining-fpm"
  - "spatiotemporally-aware-normality-adaptation-sana"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-05T06:08:42Z"
created_at: "2026-04-05T06:08:42Z"
---

# CANDI: Curated Test-Time Adaptation for Multivariate Time-Series Anomaly Detection Under Distribution Shift

**Authors**: HyunGi Kim, Jisoo Mok, Hyungyu Lee, Juhyeon Shin, Sungroh Yoon
**Date**: 2026-04-02
**Paper ID**: [openalex:2604.01845](https://arxiv.org/abs/2604.01845)

## Summary

CANDI is a test-time adaptation framework designed to maintain the performance of multivariate time-series anomaly detectors under distribution shift. By utilizing a False Positive Mining strategy, the framework selectively identifies and adapts to samples likely to be false positives while preserving core pre-trained knowledge. Additionally, the Spatiotemporally-Aware Normality Adaptation module ensures that model updates remain informed by the inherent structural dependencies of the data. Experimental results show that CANDI improves AUROC by up to 14% compared to baseline methods while requiring fewer adaptation samples.

## Key Contributions

- Proposes CANDI, a test-time adaptation framework for multivariate time-series anomaly detection that preserves pre-trained knowledge while mitigating distribution shift effects.
- Introduces a False Positive Mining (FPM) strategy to curate high-quality adaptation samples using anomaly scores and latent similarity.
- Develops a Spatiotemporally-Aware Normality Adaptation (SANA) module for plug-and-play, structurally-informed model updates, achieving up to 14% improvement in AUROC under distribution shift.

## Key Concepts

- [[false-positive-mining-fpm]]: A strategy for selecting robust samples for test-time adaptation by filtering based on anomaly scores and latent similarity.
- [[spatiotemporally-aware-normality-adaptation-sana]]: A module for performing structurally-informed model updates in time-series models during test-time adaptation by exploiting spatiotemporal dependencies.

## Archivist Review

I have approved the core methodological components of the CANDI framework. FPM and SANA represent reusable strategies for improving model robustness during test-time adaptation in time-series anomaly detection, which aligns with the skill-specific focus on adaptation and structural inductive bias. No additional open questions or datasets met the strict threshold for permanent documentation.

### Approved Concepts
- False Positive Mining (FPM): It provides a principled way to select reliable samples for test-time adaptation in anomaly detection by filtering out false positives, which is crucial for preventing model degradation.
- Spatiotemporally-Aware Normality Adaptation (SANA): It enables model updates that explicitly consider the spatial and temporal structural relationships in multivariate time series data during test-time adaptation.

## Links

- [Abstract](https://arxiv.org/abs/2604.01845)
- [PDF](https://arxiv.org/pdf/2604.01845)

