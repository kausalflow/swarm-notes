---
# CSL-compatible fields
title: "Solar Energetic Particle Forecasting With Multi‐Task Deep Learning: SEPNET"
author:
  - literal: "Yian Yu"
  - literal: "Yang Chen"
  - literal: "Lulu Zhao"
  - literal: "Kathryn Whitman"
  - literal: "W. B. Manchester"
  - literal: "T. I. Gombosi"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2512.12786"

# Custom fields
paper_id: "2512.12786"
paper_source: "openalex"
domain: "time-series"
tags:
  - "language-model"
  - "time-series"
  - "forecasting"
  - "transformer"
  - "lstm"
  - "multimodal"
  - "benchmark"
architectures:
  - "transformer"
  - "lstm"
datasets:
  - "sepval"
concept_slugs:
  []
dataset_slugs:
  - "sepval"
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:46:36Z"
created_at: "2026-05-24T07:46:36Z"
---

# Solar Energetic Particle Forecasting With Multi‐Task Deep Learning: SEPNET

**Authors**: Yian Yu, Yang Chen, Lulu Zhao, Kathryn Whitman, W. B. Manchester, T. I. Gombosi
**Date**: 2026-05-21
**Paper ID**: [openalex:2512.12786](https://arxiv.org/abs/2512.12786)

## Summary

SEPNET is a multi-task deep learning framework designed to forecast solar energetic particle (SEP) events by jointly predicting solar flares, coronal mass ejections, and SEP occurrences. By integrating LSTM and transformer architectures, the model effectively captures temporal and contextual dependencies from solar flare properties, CME data, and SHARP magnetic field parameters. Rigorous evaluation on the SEPVAL dataset confirms that SEPNET significantly improves detection rates and skill scores compared to state-of-the-art models and traditional machine learning baselines, establishing it as a robust tool for real-time space weather operations.

## Key Contributions

- Introduces SEPNET, a multi-task deep learning framework for the joint prediction of solar flares, coronal mass ejections, and solar energetic particle (SEP) events.
- Demonstrates that integrating SHARP magnetic field parameters with LSTM and transformer architectures improves SEP detection rates and predictive skill scores.
- Outperforms existing state-of-the-art pre-eruptive SEP prediction models and classical machine learning baselines on the SEPVAL benchmark.

## Open Questions & Future Work

- [[reducing-false-alarms-sep-forecasting]]
- [[predicting-sep-intensity-and-duration]]

## Archivist Review

I approved the SEPVAL dataset as it is a specialized benchmark for space weather forecasting, and I refined two open questions focused on the shift from binary classification to intensity prediction and the critical challenge of false alarms in class-imbalanced space weather data. I did not approve SEPNET as a concept because it represents a specific model architecture instance rather than a broader, reusable forecasting mechanism.

### Approved Open Questions
- Reducing SEP False Alarms: High false alarm rates reduce trust and operational efficiency in real-time safety-critical space weather applications.
- Predicting SEP Intensity and Duration: Intensity and duration estimates are critical for assessing the actual severity of radiation impacts on space infrastructure and human safety.

## Datasets

- [[sepval]]

## Links

- [Abstract](https://arxiv.org/abs/2512.12786)
- [PDF](https://arxiv.org/pdf/2512.12786)

