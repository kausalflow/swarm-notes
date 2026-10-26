---
# CSL-compatible fields
title: "Demographics-Informed Neural Network for Multimodal Spatiotemporal Forecasting of Urban Growth and Travel Patterns Using Satellite Imagery"
author:
  - literal: "Eugene Kofi Okrah Denteh"
  - literal: "Andrews Danyo"
  - literal: "Joshua Kofi Asamoah"
  - literal: "Blessing Agyei Kyem"
  - literal: "Armstrong Aboah"
issued:
  date-parts:
    - [2026, 10, 24]
url: "https://arxiv.org/abs/2506.12456"

# Custom fields
paper_id: "2506.12456"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "vision-language-model"
  - "forecasting"
  - "spatiotemporal"
  - "encoder-decoder"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "demographics-informed-neural-network-dinn"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-26T10:37:25Z"
created_at: "2026-10-26T10:37:25Z"
---

# Demographics-Informed Neural Network for Multimodal Spatiotemporal Forecasting of Urban Growth and Travel Patterns Using Satellite Imagery

**Authors**: Eugene Kofi Okrah Denteh, Andrews Danyo, Joshua Kofi Asamoah, Blessing Agyei Kyem, Armstrong Aboah
**Date**: 2026-10-24
**Paper ID**: [openalex:2506.12456](https://arxiv.org/abs/2506.12456)

## Summary

The Demographics-Informed Neural Network (DINN) is introduced as a deep learning framework that forecasts next-year county-level satellite imagery from historical sequences while enforcing demographic consistency through a frozen demographic predictor. Combining an encoder-decoder predictor, gated skip connections, and demographic bottleneck fusion, DINN achieves an MSE of 0.00379 and SSIM of 0.8342 on US county data (2012-2023). Furthermore, the frozen demographic encoder is successfully repurposed to estimate aggregate county-level commute-mode and vehicle-availability indicators.

## Key Contributions

- Introduces the Demographics-Informed Neural Network (DINN), combining an encoder-decoder image predictor with demographic bottleneck fusion and consistency regularization.
- Achieves an MSE of 0.00379 and SSIM of 0.8342 for satellite image prediction on US county data spanning 2012 to 2023.
- Demonstrates that frozen demographic encoders extracted from satellite imagery can effectively estimate aggregate county-level commute-mode and vehicle-availability indicators.

## Limitations

Results reflect county-level predictive associations rather than causal behavioral inference, and transfer learning shows higher accuracy for absolute counts than scale-controlled shares.

## Open Questions & Future Work

- [[incorporating-socioeconomic-context-variables]]

## Key Concepts

- [[demographics-informed-neural-network-dinn]]: A deep learning framework for spatiotemporal satellite imagery forecasting that enforces demographic consistency via a frozen demographic predictor.

## Archivist Review

Approve the core architectural concept DINN because it establishes a reusable paradigm for enforcing demographic consistency in satellite image forecasting. The open question regarding incorporating socioeconomic context variables is retained as a substantive research direction. Unnamed or general datasets like US county data are rejected to maintain strict vault standards.

### Approved Concepts
- Demographics-Informed Neural Network (DINN): DINN is the core novel architecture introduced for multimodal spatiotemporal urban growth and travel pattern forecasting.

### Approved Open Questions
- Incorporating Socioeconomic Context Variables: Addressing demographic disparities and improving minority population prediction accuracy is crucial for equitable and unbiased urban planning.

## Links

- [Abstract](https://arxiv.org/abs/2506.12456)
- [PDF](https://arxiv.org/pdf/2506.12456)

