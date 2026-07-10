---
# CSL-compatible fields
title: "Observation‐Driven Correction of Numerical Weather Prediction for Marine Winds"
author:
  - literal: "Matteo Peduto"
  - literal: "Qidong Yang"
  - literal: "Jonathan Giezendanner"
  - literal: "Devis Tuia"
  - literal: "Sherrie Wang"
issued:
  date-parts:
    - [2026, 7, 7]
url: "https://arxiv.org/abs/2512.03606"

# Custom fields
paper_id: "2512.03606"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "time-series"
  - "forecasting"
architectures:
  - "transformer"
datasets:
  - "international-comprehensive-ocean-atmosphere-data-set"
concept_slugs:
  - "orca-framework"
dataset_slugs:
  - "international-comprehensive-ocean-atmosphere-data-set"
skill: "TimeSeriesSkill"
processed_at: "2026-07-10T08:15:37Z"
created_at: "2026-07-10T08:15:37Z"
---

# Observation‐Driven Correction of Numerical Weather Prediction for Marine Winds

**Authors**: Matteo Peduto, Qidong Yang, Jonathan Giezendanner, Devis Tuia, Sherrie Wang
**Date**: 2026-07-07
**Paper ID**: [openalex:2512.03606](https://arxiv.org/abs/2512.03606)

## Summary

This paper introduces ORCA, a transformer-based post-processing framework designed to correct systematic errors in global numerical weather prediction (NWP) marine wind forecasts. By treating sparse, irregular in situ observations as tokens and employing cross-attention, the model effectively fuses localized real-time data with large-scale forecast outputs. Evaluation against the International Comprehensive Ocean-Atmosphere Data Set shows significant improvements in wind speed accuracy across all 48-hour lead times, particularly along shipping routes and coastlines.

## Key Contributions

- Introduced ORCA, a transformer-based architecture that utilizes cross-attention to condition NWP outputs on sparse, heterogeneous in situ observations.
- Achieved significant wind error reduction compared to GFS, with 45% improvement at 1-hr and 13% at 48-hr lead times.
- Demonstrated a single-pass inference capability for generating both site-specific predictions and basin-scale gridded corrections for marine winds.

## Open Questions & Future Work

- [[extreme-wind-prediction-robustness]]
- [[spatial-generalization-marine-wind]]

## Key Concepts

- [[orca-framework]]: A transformer-based deep learning architecture for real-time post-processing and correction of numerical weather prediction wind forecasts using heterogeneous, sparse observation data.

## Archivist Review

I approved the ORCA framework as it represents a robust architecture for integrating irregular, sparse observational data with global model forecasts, a problem of high interest in environmental AI. I also approved the dataset and the two open questions, as they represent distinct, well-justified research bottlenecks regarding extreme event reliability and spatial generalization. The rejection of other candidates followed the directive to be scarce and avoid local implementation details.

### Approved Concepts
- Observation-informed Real-time Correction with Attention (ORCA): ORCA provides a novel post-processing framework that effectively combines sparse, irregular in situ ocean observations with global NWP model outputs to correct systemic forecast biases.

### Approved Open Questions
- Extreme Wind Forecasting Robustness: This is critical for operational applications where accurate extreme wind forecasting is necessary for safety, maritime navigation, and risk management.
- Spatial Generalization of Corrections: Ensuring models generalize to data-sparse or novel regions is foundational to the reliable global application of machine learning-based post-processing.

## Datasets

- [[international-comprehensive-ocean-atmosphere-data-set]]

## Links

- [Abstract](https://arxiv.org/abs/2512.03606)
- [PDF](https://arxiv.org/pdf/2512.03606)

