---
# CSL-compatible fields
title: "Biarchetype analysis for univariate functional data. An application to macroeconomic financial time series"
author:
  - literal: "Aleix Alcacer"
  - literal: "Rafael Benı́tez"
  - literal: "Vicente J. Bolós"
  - literal: "Irene Epifanio"
issued:
  date-parts:
    - [2026, 6, 14]
url: "https://arxiv.org/abs/2606.15881"

# Custom fields
paper_id: "2606.15881"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "biarchetype-analysis"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:25:31Z"
created_at: "2026-06-17T09:25:31Z"
---

# Biarchetype analysis for univariate functional data. An application to macroeconomic financial time series

**Authors**: Aleix Alcacer, Rafael Benı́tez, Vicente J. Bolós, Irene Epifanio
**Date**: 2026-06-14
**Paper ID**: [openalex:2606.15881](https://arxiv.org/abs/2606.15881)

## Summary

This paper introduces biarchetype analysis as an unsupervised framework for univariate functional data, enabling the simultaneous decomposition of both instances and time points into mixtures of extreme, representative patterns. Unlike traditional biclustering, which relies on average-based centroids, this method leverages extreme archetypes to provide a more intuitive and interpretable structural analysis. The methodology is evaluated on European government bond yield data from 2001-2025, successfully uncovering meaningful temporal regimes and distinct geographical archetypes.

## Key Contributions

- Introduces biarchetype analysis for univariate functional data to jointly identify representative structures in cross-sectional and temporal dimensions.
- Provides a highly interpretable alternative to biclustering by representing data as convex combinations of extreme patterns rather than average centroids.
- Demonstrates the efficacy of the framework by identifying significant time regimes and country archetypes in 2001-2025 European government bond yield data.

## Open Questions & Future Work

- [[automated-k-c-selection-biarchetype-analysis]]

## Key Concepts

- [[biarchetype-analysis]]: An unsupervised learning approach for univariate functional data that represents observations as mixtures of extreme archetypal patterns across both cases and time dimensions.

## Archivist Review

I approved the concept 'Biarchetype analysis' for its methodological novelty in functional data analysis, providing an interpretable alternative to biclustering. I also approved the open question regarding automated parameter selection, as it addresses a key practical bottleneck for the framework's reliability and reproducibility. No datasets were approved as none were presented that meet the specific requirement for a reusable, named, and centrally documented benchmark dataset.

### Approved Concepts
- Biarchetype analysis: Provides a novel, interpretable alternative to biclustering for functional data by identifying extreme, representative patterns across both instances and temporal dimensions.

### Approved Open Questions
- Automated Selection of Biarchetype Parameters: The choice of hyperparameters dictates model complexity and interpretability, making automated selection essential for preventing overfitting and ensuring consistent analysis.

## Links

- [Abstract](https://arxiv.org/abs/2606.15881)
- [PDF](https://arxiv.org/pdf/2606.15881)

