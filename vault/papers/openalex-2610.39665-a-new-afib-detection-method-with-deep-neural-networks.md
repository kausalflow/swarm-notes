---
# CSL-compatible fields
title: "A New AFIB Detection Method with Deep Neural Networks"
author:
  - literal: "Sara Gjorgjieva"
  - literal: "Ana Angjelevska"
  - literal: "Dimitar Trajanov"
  - literal: "Gusev Marjan"
issued:
  date-parts:
    - [2026, 10, 29]
url: "https://arxiv.org/abs/2610.39665"

# Custom fields
paper_id: "2610.39665"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "benchmark"
  - "dataset"
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
processed_at: "2026-11-01T11:34:28Z"
created_at: "2026-11-01T11:34:28Z"
---

# A New AFIB Detection Method with Deep Neural Networks

**Authors**: Sara Gjorgjieva, Ana Angjelevska, Dimitar Trajanov, Gusev Marjan
**Date**: 2026-10-29
**Paper ID**: [openalex:2610.39665](https://arxiv.org/abs/2610.39665)

## Summary

This paper introduces a robust deep neural network approach for early atrial fibrillation (AFIB) detection using electrocardiogram (ECG) data. The authors propose a novel feature engineering technique based on successive heart rate differences (dBPM) and a cleaning method that treats unclean intervals as outliers during training. Evaluated on the MIT-BIH Arrhythmia Database and the Long-term Atrial Fibrillation Database, the best-performing model achieves an F1 score of 95.18% for binary AFIB classification, outperforming existing published methods.

## Key Contributions

- Proposes a robust AFIB detection system using deep neural networks and conventional machine learning algorithms.
- Introduces a novel feature engineering technique utilizing successive heart rate differences (dBPM) instead of traditional inter-beat intervals.
- Achieves an F1 score of 95.18% for binary atrial fibrillation classification on a benchmark dataset using a new cleaning and labeling strategy.

## Archivist Review

All candidate concepts and questions were rejected as the paper applies standard deep neural networks and conventional feature engineering techniques (dBPM) to atrial fibrillation detection without introducing a broadly reusable theoretical or architectural mechanism for the vault.

## Links

- [Abstract](https://arxiv.org/abs/2610.39665)
- [PDF](https://arxiv.org/pdf/2610.39665)

