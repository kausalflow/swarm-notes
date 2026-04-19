---
# CSL-compatible fields
title: "Assessing the Potential of Masked Autoencoder Foundation Models in Predicting Downhole Metrics from Surface Drilling Data"
author:
  - literal: "Aleksander Berezowski"
  - literal: "Hassan Hassanzadeh"
  - literal: "Gouri Ginde"
issued:
  date-parts:
    - [2026, 4, 16]
url: "https://arxiv.org/abs/2604.15169"

# Custom fields
paper_id: "2604.15169"
paper_source: "openalex"
domain: "time-series,nlp"
tags:
  - "time-series"
  - "pre-training"
  - "self-supervised-learning"
  - "lstm"
  - "llm"
architectures:
  []
datasets:
  []
concept_slugs:
  - "masked-autoencoder-foundation-models"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-19T06:24:26Z"
created_at: "2026-04-19T06:24:26Z"
---

# Assessing the Potential of Masked Autoencoder Foundation Models in Predicting Downhole Metrics from Surface Drilling Data

**Authors**: Aleksander Berezowski, Hassan Hassanzadeh, Gouri Ginde
**Date**: 2026-04-16
**Paper ID**: [openalex:2604.15169](https://arxiv.org/abs/2604.15169)

## Summary

This systematic mapping study evaluates the potential of Masked Autoencoder Foundation Models (MAEFMs) for predicting critical downhole drilling metrics using surface sensor data. The research synthesizes findings from thirteen papers, noting a reliance on traditional architectures like LSTMs and ANNs that often struggle with the scarcity of labeled downhole data. The authors propose that MAEFMs, via self-supervised pre-training, provide a promising path to improve multi-task prediction and generalization across different drilling environments. This work serves as a foundational roadmap for future empirical investigations into foundation models for drilling analytics.

## Key Contributions

- Systematic mapping study synthesizing thirteen papers (2015-2025) on predicting downhole metrics from surface drilling sensors.
- Categorization of eight commonly collected surface drilling metrics and seven target downhole metrics for standardization.
- Identified Masked Autoencoder Foundation Models (MAEFMs) as a high-potential, unexplored architectural direction compared to traditional ANN and LSTM baselines.

## Key Concepts

- [[masked-autoencoder-foundation-models]]: The use of self-supervised Masked Autoencoder Foundation Models to leverage large amounts of unlabeled sensor data for downstream forecasting tasks.

## Archivist Review

I approved 'Masked Autoencoder Foundation Models' as a general architectural concept, as it is a significant and reusable paradigm in time-series forecasting. The specific candidate 'MAEFMs in Drilling Analytics' was rejected in favor of this broader, more reusable concept. No datasets or open questions were approved as the paper is a survey mapping existing literature rather than presenting novel technical contributions.

### Approved Concepts
- Masked Autoencoder Foundation Models (MAEFMs): This represents a potential paradigm shift for sensor-heavy industrial forecasting by leveraging self-supervised pre-training to address data scarcity.

### Rejected Candidates
- [concept] Masked Autoencoder Foundation Models (MAEFMs) in Drilling Analytics (`maefm-drilling-analytics`) - subcomponent_of_broader_mechanism: This is a specific application of a broader architecture; the overarching architecture is more reusable.

## Links

- [Abstract](https://arxiv.org/abs/2604.15169)
- [PDF](https://arxiv.org/pdf/2604.15169)

