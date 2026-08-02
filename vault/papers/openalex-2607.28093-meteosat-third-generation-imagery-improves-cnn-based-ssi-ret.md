---
# CSL-compatible fields
title: "Meteosat Third Generation imagery improves CNN-based SSI retrieval"
author:
  - literal: "Gordei Pribõtkin"
  - literal: "Piia Post"
  - literal: "Velle Toll"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2607.28093"

# Custom fields
paper_id: "2607.28093"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "convolutional-neural-network"
  - "cnn"
  - "computer-vision"
  - "evaluation"
  - "benchmark"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-02T07:28:00Z"
created_at: "2026-08-02T07:28:00Z"
---

# Meteosat Third Generation imagery improves CNN-based SSI retrieval

**Authors**: Gordei Pribõtkin, Piia Post, Velle Toll
**Date**: 2026-07-30
**Paper ID**: [openalex:2607.28093](https://arxiv.org/abs/2607.28093)

## Summary

This paper investigates the benefits of the Meteosat Third Generation (MTG) satellite constellation for convolutional neural network-based Surface Solar Irradiance (SSI) retrieval by combining MTG/FCI and MSG/SEVIRI imagery. Evaluated against ground pyranometers across Estonian meteorological stations and benchmarked against the SARAH-3 product, the hybrid SEVIRI-FCI model significantly improves accuracy under overcast and cloudy conditions. However, the study reveals that higher spatial resolution alone does not resolve clear-sky performance deficiencies relative to traditional physics-based models.

## Key Contributions

- Introduced a multi-imager and multi-resolution convolutional neural network architecture combining MSG/SEVIRI and MTG/FCI satellite imagery for 10-minute Surface Solar Irradiance (SSI) retrieval.
- Demonstrated that incorporating high-resolution MTG/FCI imagery significantly reduces RMSE under overcast (8.2 W m^-2) and cloudy (5.7 W m^-2) conditions compared to SEVIRI-only models.
- Evaluated model performance against ground-based pyranometer measurements from eight Estonian meteorological stations and compared results with the physics-based SARAH-3 SSI product.

## Limitations

Higher spatial resolution alone is insufficient to address clear-sky limitations in machine-learning-based SSI retrieval, where models underperformed compared to SARAH-3.

## Archivist Review

Applied rigorous filters to reject domain-specific atmospheric retrieval questions and paper-local model comparisons. No concepts or open questions met the high standard for permanent vault storage.

### Rejected Candidates
- [open_question] Clear-sky performance shortfalls in ML-based SSI retrieval (`clear-sky-performance-optimization-in-ml-ssi-retrieval`) - low_impact: The question addresses a domain-specific evaluation observation regarding satellite-based surface solar irradiance rather than a broad, reusable time-series or ML research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.28093)
- [PDF](https://arxiv.org/pdf/2607.28093)

