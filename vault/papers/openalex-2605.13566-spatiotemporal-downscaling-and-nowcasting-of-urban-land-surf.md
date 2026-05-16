---
# CSL-compatible fields
title: "Spatiotemporal downscaling and nowcasting of urban land surface temperatures with deep neural networks"
author:
  - literal: "Solomiia Kurchaba"
  - literal: "Angela Meyer"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.13566"

# Custom fields
paper_id: "2605.13566"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "cnn"
  - "lstm"
  - "benchmark"
architectures:
  - "cnn"
  - "lstm"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:10:08Z"
created_at: "2026-05-16T07:10:08Z"
---

# Spatiotemporal downscaling and nowcasting of urban land surface temperatures with deep neural networks

**Authors**: Solomiia Kurchaba, Angela Meyer
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.13566](https://arxiv.org/abs/2605.13566)

## Summary

This paper addresses the spatiotemporal trade-off in satellite-derived Land Surface Temperature (LST) products by developing a U-Net model that fuses coarse, high-frequency geostationary data with fine, low-frequency polar-orbiting observations. The resulting 1km, 15-minute resolution fields enable enhanced urban climate monitoring. Furthermore, a ConvLSTM architecture is employed to provide short-term nowcasting of these high-resolution LST fields, outperforming traditional statistical baselines with significantly lower RMSE values.

## Key Contributions

- Developed a U-Net-based spatiotemporal downscaling model to produce 1km, 15-min resolution LST fields by fusing geostationary and polar-orbiting satellite data.
- Proposed a ConvLSTM-based nowcasting model for intraday LST forecasting, achieving superior performance compared to persistence and climatological baselines.
- Demonstrated consistent accuracy with an RMSE of 1.92°C for downscaling and lead-time-dependent RMSEs of 0.57–1.15°C for nowcasting on large European city datasets.

## Open Questions & Future Work

- [[integration-of-physical-urban-variables-for-lst-modeling]]

## Archivist Review

I have rejected the proposed concepts because they describe standard applications of existing neural architectures (U-Net and ConvLSTM) to a specific domain task rather than introducing novel, reusable methodology. I approved the open question regarding the integration of physical urban variables because it addresses a fundamental, domain-specific limitation of current satellite-based thermal forecasting that warrants tracking across future research.

### Approved Open Questions
- Integrating physical urban variables: The current data-minimal approach may be reaching an accuracy ceiling in complex urban environments; assessing the feasibility of adding exogenous physical constraints is critical for advancing towards physically-informed, more robust forecasting models.

### Rejected Candidates
- [concept] Spatiotemporal downscaling model (`spatiotemporal-downscaling-of-lst-via-unet`) - not_novel: This is a standard application of a U-Net architecture to satellite imagery rather than a novel or highly reusable methodological concept.
- [concept] ConvLSTM nowcasting architecture (`convlstm-for-lst-nowcasting`) - not_novel: ConvLSTM is a widely known architecture; applying it to LST nowcasting is a direct application rather than a new architectural innovation.

## Links

- [Abstract](https://arxiv.org/abs/2605.13566)
- [PDF](https://arxiv.org/pdf/2605.13566)

