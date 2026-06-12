---
# CSL-compatible fields
title: "Personalized Deep Learning for Short-Term Forecasting of Impending Atrial Fibrillation from Continuous Wearable ECG Signals"
author:
  - literal: "Jangwon Suh"
  - literal: "Soonil Kwon"
  - literal: "Jungmin Ko"
  - literal: "Yun Kwan Kim"
  - literal: "Hee Seok Song"
  - literal: "Eue-Keun Choi"
  - literal: "Wonjong Rhee"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.10900"

# Custom fields
paper_id: "2606.10900"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "fine-tuning"
  - "deep-learning"
  - "health-monitoring"
  - "forecasting"
  - "interpretability"
architectures:
  - "encoder-only"
datasets:
  - "icentia11k"
  - "mobicare"
concept_slugs:
  - "personalized-ecg-forecasting-framework"
dataset_slugs:
  - "icentia11k"
  - "mobicare"
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:53:48Z"
created_at: "2026-06-12T08:53:48Z"
---

# Personalized Deep Learning for Short-Term Forecasting of Impending Atrial Fibrillation from Continuous Wearable ECG Signals

**Authors**: Jangwon Suh, Soonil Kwon, Jungmin Ko, Yun Kwan Kim, Hee Seok Song, Eue-Keun Choi, Wonjong Rhee
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.10900](https://arxiv.org/abs/2606.10900)

## Summary

This paper evaluates the efficacy of personalizing global deep learning models for forecasting impending atrial fibrillation using continuous wearable ECG signals. By fine-tuning models on individual patient data across three cohorts (ICENTIA11K, IRIDIA-AF, and MobiCARE), the study demonstrates significant improvements in short-term forecasting performance compared to non-personalized global benchmarks. Feature attribution analysis confirms that the personalized models successfully capture clinically meaningful arrhythmia precursors such as premature atrial complexes.

## Key Contributions

- Demonstrated that fine-tuning a global model with patient-specific ECG data yields superior AUROC compared to global-only models (0.711 vs 0.614 on ICENTIA11K).
- Identified that the predictive benefit of model personalization scales positively with the volume of patient-specific fine-tuning data.
- Revealed through feature attribution that personalized models capture clinically relevant precursors like frequent premature atrial complexes and short supraventricular tachycardias.

## Open Questions & Future Work

- [[data-scarcity-personalized-ecg-forecasting]]

## Key Concepts

- [[personalized-ecg-forecasting-framework]]: A methodology for fine-tuning global deep learning models on patient-specific ECG streams to improve forecasting of arrhythmic events.

## Archivist Review

I approved the overarching personalization framework for ECG forecasting and the two specific named datasets used for benchmarking. The concept was renamed to be more general for broader applicability. The open question regarding data scarcity is a well-defined bottleneck for personalized healthcare AI.

### Approved Concepts
- Personalized ECG Forecasting Framework: Addresses the inherent inter-patient variability in physiological signals, providing a methodology for adapting generalized models to specific patient dynamics.

### Approved Open Questions
- Data scarcity in personalized ECG: The scarcity of labeled data is a primary bottleneck for advancing personalized healthcare AI; identifying this as a central limitation is crucial for prioritizing future community-wide efforts to build standardized, high-quality, long-term medical datasets.

### Rejected Candidates
- [concept] Personalized Deep Learning for AF Forecasting (`personalized-deep-learning-for-af-forecasting`) - duplicate_existing: Replaced by a more generalized, reusable slug 'personalized-ecg-forecasting-framework'.

## Datasets

- [[icentia11k]]
- [[mobicare]]

## Links

- [Abstract](https://arxiv.org/abs/2606.10900)
- [PDF](https://arxiv.org/pdf/2606.10900)

