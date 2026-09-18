---
# CSL-compatible fields
title: "Every Fixed Metric Has a Blind Spot: A Learned Atmospheric Critic for Scoring Forecast Realism"
author:
  - literal: "Younes Elberkennou"
  - literal: "Dmitri Demler"
  - literal: "Thierry Meier"
  - literal: "Luca Rispoli"
  - literal: "Fanny Lehmann"
  - literal: "Joel Oskarsson"
issued:
  date-parts:
    - [2026, 9, 16]
url: "https://arxiv.org/abs/2609.18381"

# Custom fields
paper_id: "2609.18381"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  - "era5"
concept_slugs:
  - "learned-atmospheric-critic"
dataset_slugs:
  - "era5"
skill: "TimeSeriesSkill"
processed_at: "2026-09-18T09:17:29Z"
created_at: "2026-09-18T09:17:29Z"
---

# Every Fixed Metric Has a Blind Spot: A Learned Atmospheric Critic for Scoring Forecast Realism

**Authors**: Younes Elberkennou, Dmitri Demler, Thierry Meier, Luca Rispoli, Fanny Lehmann, Joel Oskarsson
**Date**: 2026-09-16
**Paper ID**: [openalex:2609.18381](https://arxiv.org/abs/2609.18381)

## Summary

Machine learning weather forecasting models often suffer from unphysical spatial artifacts like blurring and periodic irregularities, which fixed evaluation metrics fail to detect due to predetermined representations. To address this, the authors propose a learned atmospheric critic that trains a discriminator to separate reference weather data from model outputs, yielding a divergence-like realism score. Evaluated on synthetic corruptions of ERA5 reanalysis data and real weather models, the learned critic successfully identifies and ranks severities where fixed metrics fail, while revealing that numerical models generally achieve higher realism than machine learning models.

## Key Contributions

- Proposes a learned atmospheric critic framework that trains a discriminator to detect unphysical spatial artifacts and provide divergence-like realism scores for weather forecasts.
- Demonstrates that the learned critic successfully identifies synthetic corruptions and ranks their severity across ERA5 reanalysis data, whereas existing fixed metrics fail on at least one corruption.
- Evaluates real weather models, showing that realism scores degrade with longer lead times and consistently rank numerical models higher than machine learning models.

## Open Questions & Future Work

- [[transferrable-learned-atmospheric-critics-limitation]]

## Key Concepts

- [[learned-atmospheric-critic]]: A discriminator-based realism scoring mechanism that learns to separate weather model outputs from reference data to detect unphysical spatial artifacts.

## Archivist Review

Approved the core learned atmospheric critic concept and its open question concerning cross-model transferability, along with the ERA5 dataset central to the evaluation. Applied strict scarcity and quality filters to avoid paper-local artifacts.

### Approved Concepts
- Learned Atmospheric Critic: Introduces a dynamic discriminator-based scoring mechanism to evaluate weather forecast realism and identify unphysical artifacts that fixed metrics miss.

### Approved Open Questions
- Transferrable Learned Atmospheric Critics: Crucial for establishing a universal, computationally efficient realism evaluation standard in weather forecasting.

## Datasets

- [[era5]]

## Links

- [Abstract](https://arxiv.org/abs/2609.18381)
- [PDF](https://arxiv.org/pdf/2609.18381)

