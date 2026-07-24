---
# CSL-compatible fields
title: "Subject-Conditioned Glucose Forecasting in Type-1 Diabetes"
author:
  - literal: "Giorgia Rigamonti"
  - literal: "Mirko Paolo Barbato"
  - literal: "Davide Marelli"
  - literal: "Paolo Napoletano"
issued:
  date-parts:
    - [2026, 7, 21]
url: "https://arxiv.org/abs/2607.19006"

# Custom fields
paper_id: "2607.19006"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "subject-conditioned-glucose-prediction"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-24T07:25:09Z"
created_at: "2026-07-24T07:25:09Z"
---

# Subject-Conditioned Glucose Forecasting in Type-1 Diabetes

**Authors**: Giorgia Rigamonti, Mirko Paolo Barbato, Davide Marelli, Paolo Napoletano
**Date**: 2026-07-21
**Paper ID**: [openalex:2607.19006](https://arxiv.org/abs/2607.19006)

## Summary

Accurate blood glucose forecasting is critical for managing Type 1 Diabetes and detecting adverse glycemic events. Current methods often rely on population-level representations or implicit personalization, struggling with inter-subject variability. This paper introduces Subject-Conditioned Glucose Prediction (SCGP), a multimodal deep learning architecture that explicitly conditions predictions on a compact subject-specific representation without early fusion of heterogeneous inputs. Experiments show that SCGP improves forecasting performance and enables reliable event detection across multiple prediction horizons.

## Key Contributions

- Proposes Subject-Conditioned Glucose Prediction (SCGP), a multimodal deep learning architecture that explicitly separates subject characterization from glucose dynamics modeling.
- Avoids early fusion of heterogeneous inputs to preserve robust temporal modeling while capturing inter-subject variability.
- Demonstrates consistent forecasting performance improvements and reliable detection of adverse glycemic events across multiple prediction horizons on benchmark datasets.

## Key Concepts

- [[subject-conditioned-glucose-prediction]]: A multimodal deep learning framework for personalized blood glucose forecasting that explicitly conditions predictions on compact subject-specific representations learned from contextual information.

## Archivist Review

Approved the core methodological concept 'subject-conditioned-glucose-prediction' as a reusable approach for personalized healthcare time-series forecasting that separates subject characterization from temporal dynamics without early fusion. No datasets or open questions met the rigorous scarcity and specificity bar for standalone vault notes.

### Approved Concepts
- Subject-Conditioned Glucose Prediction: Introduces an explicit separation between subject characterization and glucose dynamics modeling via conditioning on contextual information, solving limitations of population-level representations in Type-1 Diabetes forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2607.19006)
- [PDF](https://arxiv.org/pdf/2607.19006)

