---
# CSL-compatible fields
title: "Earth observation embeddings are effective sub-grid descriptors for probabilistic weather downscaling"
author:
  - literal: "Pedro Sousa"
  - literal: "Will Tebbutt"
  - literal: "Sadiq Jaffer"
  - literal: "Robin Young"
  - literal: "Anil Madhavapeddy"
  - literal: "Richard E. Turner"
issued:
  date-parts:
    - [2026, 8, 12]
url: "https://arxiv.org/abs/2608.12271"

# Custom fields
paper_id: "2608.12271"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "spatial-temporal"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-15T05:15:33Z"
created_at: "2026-08-15T05:15:33Z"
---

# Earth observation embeddings are effective sub-grid descriptors for probabilistic weather downscaling

**Authors**: Pedro Sousa, Will Tebbutt, Sadiq Jaffer, Robin Young, Anil Madhavapeddy, Richard E. Turner
**Date**: 2026-08-12
**Paper ID**: [openalex:2608.12271](https://arxiv.org/abs/2608.12271)

## Summary

This paper investigates whether Earth observation foundation model embeddings can serve as effective sub-grid surface descriptors for probabilistic weather downscaling. By augmenting a conditional neural process with compressed patches of TESSERA embeddings, the approach improves continuous ranked probability score (CRPS) skill by 11.5% for 2m temperature and 6.2% for 10m wind speed across five climatically diverse regions. The results demonstrate that long-timescale surface representations successfully capture local atmospheric departures for instantaneous weather prediction, generalizing robustly to AI-based forecasts and stations with no historical data.

## Key Contributions

- Proposes augmenting convolutional conditional neural processes with TESSERA Earth observation embeddings for probabilistic weather downscaling, improving CRPS by 11.5% for 2m temperature and 6.2% for 10m wind speed.
- Demonstrates that long-timescale surface embeddings effectively capture sub-grid atmospheric departures across five climatically diverse regions on stations held out in space and time.
- Shows persistence of improvements when switching coarse inputs from ERA5 reanalysis to Aurora AI forecasts and when predicting at stations with zero historical data.

## Limitations

None explicitly stated in the abstract.

## Archivist Review

The paper introduces an interesting application of Earth observation embeddings for weather downscaling, but the proposed concept (TESSERA embeddings) is too tied to a specific foundation model feature source rather than a reusable architectural contribution, and the open question is standard incremental future work.

### Rejected Candidates
- [concept] TESSERA embeddings (`tessera-embeddings`) - not_reusable: TESSERA embeddings are a specific proprietary foundation model descriptor dataset/feature set tailored to this paper's specific pipeline rather than a widely reusable general architectural or methodological paradigm.
- [open_question] EO Embeddings Beyond Temperature and Wind (`eo-embeddings-beyond-temperature-wind`) - low_impact: Extending a specific modality of earth-observation embeddings to other meteorological variables is an incremental domain extension rather than a fundamental open theoretical problem.

## Links

- [Abstract](https://arxiv.org/abs/2608.12271)
- [PDF](https://arxiv.org/pdf/2608.12271)

