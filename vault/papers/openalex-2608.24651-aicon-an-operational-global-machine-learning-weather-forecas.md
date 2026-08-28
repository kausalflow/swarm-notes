---
# CSL-compatible fields
title: "AICON: An operational global machine learning weather forecasting model"
author:
  - literal: "Tobias Goecke"
  - literal: "Marek Jacob"
  - literal: "Florian Prill"
  - literal: "Michael Denhard"
  - literal: "Felix Fundel"
  - literal: "Jan Keller"
  - literal: "Roland Potthast"
  - literal: "Hendrik Reich"
  - literal: "Britta Seegebrecht"
  - literal: "Sven Ulbrich"
  - literal: "Arianna Valmassoi"
  - literal: "Sabrina Wahl"
issued:
  date-parts:
    - [2026, 8, 25]
url: "https://arxiv.org/abs/2608.24651"

# Custom fields
paper_id: "2608.24651"
paper_source: "openalex"
domain: "time-series"
tags:
  - "graph-neural-network"
  - "gnn"
  - "attention-mechanism"
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T16:59:44Z"
created_at: "2026-08-28T16:59:44Z"
---

# AICON: An operational global machine learning weather forecasting model

**Authors**: Tobias Goecke, Marek Jacob, Florian Prill, Michael Denhard, Felix Fundel, Jan Keller, Roland Potthast, Hendrik Reich, Britta Seegebrecht, Sven Ulbrich, Arianna Valmassoi, Sabrina Wahl
**Date**: 2026-08-25
**Paper ID**: [openalex:2608.24651](https://arxiv.org/abs/2608.24651)

## Summary

AICON is an operational global machine learning weather prediction model deployed at Deutscher Wetterdienst that generates 13 km resolution forecasts using a graph neural network with graph attention. Trained on the ICON-DREAM dataset, AICON integrates an icosahedral multi-mesh derived from the native ICON grid and terrain-following vertical SLEVE coordinates. By avoiding multi-step autoregressive rollouts during training, AICON prioritizes small-scale fidelity and achieves competitive verification skill compared to traditional numerical weather prediction models.

## Key Contributions

- Introduces AICON, an operational global machine learning weather forecasting model developed at Deutscher Wetterdienst using a 13 km spatial resolution and 3-hour time step.
- Utilizes an icosahedral multi-mesh derived from the native ICON grid and terrain-following vertical SLEVE coordinates to maintain physical consistency with NWP data.
- Employs a training strategy avoiding autoregressive multi-step rollouts and long forecast horizons to preserve small-scale atmospheric features.
- Demonstrates competitive operational skill against the numerical ICON model for near-surface variables in short- to medium-range forecasting.

## Archivist Review

The paper introduces AICON, an operational machine learning weather forecasting model, but the core modeling concepts (GNNs on icosahedral grids, terrain-following coordinates) are specific implementations of existing meteorological architectures rather than universally reusable forecasting paradigms. The proposed open question is a duplicate of existing vault entries covering noise accumulation and error growth in ML weather prediction.

### Rejected Candidates
- [open_question] Noise Amplification and Instabilities in MLWP (`noise-amplification-and-instabilities-in-mlwp`) - duplicate_existing: A similar open question regarding error accumulation and noise growth in atmospheric rollout models already exists in the vault.

## Links

- [Abstract](https://arxiv.org/abs/2608.24651)
- [PDF](https://arxiv.org/pdf/2608.24651)

