---
# CSL-compatible fields
title: "Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data"
author:
  - literal: "Yinyu Huang"
  - literal: "Yilin Zhang"
  - literal: "Sofia Michopoulou"
  - literal: "Christopher Kipps"
  - literal: "Rahman Attar"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2606.09671"

# Custom fields
paper_id: "2606.09671"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "interpretability"
architectures:
  []
datasets:
  - "alzheimers-disease-neuroimaging-initiative"
concept_slugs:
  - "transition-based-digital-twin-modelling"
dataset_slugs:
  - "alzheimers-disease-neuroimaging-initiative"
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:07:56Z"
created_at: "2026-06-11T09:07:56Z"
---

# Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data

**Authors**: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
**Date**: 2026-06-08
**Paper ID**: [openalex:2606.09671](https://arxiv.org/abs/2606.09671)

## Summary

This paper proposes a personalised digital twin framework to address the challenges of sparse and irregular longitudinal data in Alzheimer's disease progression. By integrating local transition modelling between adjacent visits with sequence-based trajectory forecasting, the method achieves improved predictive accuracy and robust uncertainty quantification compared to standard cohort-level approaches. Evaluations using the ADNI dataset confirm that transition-based modelling is particularly well-suited for sparse data, offering a more data-efficient alternative to purely sequence-based predictive architectures.

## Key Contributions

- Introduced a personalised digital twin framework for AD progression that combines local transition modelling and sequence-based trajectory analysis.
- Demonstrated that transition-based modelling of adjacent longitudinal visits provides superior data efficiency and accuracy over sequence-based branches for sparse AD data.
- Enabled uncertainty-aware, scenario-based 'what-if' trajectory forecasting for personalised disease monitoring in clinical settings.

## Open Questions & Future Work

- [[causal-inference-digital-twins]]

## Key Concepts

- [[transition-based-digital-twin-modelling]]: A modelling strategy that captures clinical transitions between adjacent longitudinal visits as a data-efficient alternative to holistic sequence modelling for digital twins.

## Archivist Review

The paper provides a compelling methodological argument for transition-based modelling as a data-efficient alternative to sequence-based models for sparse clinical data, which is a clear and reusable contribution. I approved the concept and the question regarding causal inference in digital twins, as the latter highlights a critical gap in current observational modelling frameworks. I standardized the dataset name to align with the existing vault entry.

### Approved Concepts
- Transition-Based Digital Twin Modelling: This concept introduces a shift from holistic sequence-based forecasting to transition-based modelling specifically for sparse, irregular clinical time-series, which is a novel methodological approach in digital twin formulations.

### Approved Open Questions
- Causal Inference in Digital Twins: Moving from observational to causal scenario analysis is critical for clinical decision support, as it would allow clinicians to better understand the potential impact of different treatment paths on patient outcomes.

## Datasets

- [[alzheimers-disease-neuroimaging-initiative]]

## Links

- [Abstract](https://arxiv.org/abs/2606.09671)
- [PDF](https://arxiv.org/pdf/2606.09671)

