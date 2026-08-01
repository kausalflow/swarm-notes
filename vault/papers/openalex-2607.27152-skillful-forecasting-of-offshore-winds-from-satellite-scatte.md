---
# CSL-compatible fields
title: "Skillful forecasting of offshore winds from satellite scatterometer constellations"
author:
  - literal: "Francesco Pinto"
  - literal: "Luca Lanzilao"
  - literal: "Paco Lopez Dekker"
  - literal: "Angela Meyer"
issued:
  date-parts:
    - [2026, 7, 29]
url: "https://arxiv.org/abs/2607.27152"

# Custom fields
paper_id: "2607.27152"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "recurrent-neural-network"
  - "lstm"
  - "multimodal"
architectures:
  - "lstm"
datasets:
  []
concept_slugs:
  - "windcastnet"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-01T07:23:02Z"
created_at: "2026-08-01T07:23:02Z"
---

# Skillful forecasting of offshore winds from satellite scatterometer constellations

**Authors**: Francesco Pinto, Luca Lanzilao, Paco Lopez Dekker, Angela Meyer
**Date**: 2026-07-29
**Paper ID**: [openalex:2607.27152](https://arxiv.org/abs/2607.27152)

## Summary

The authors present WindCastNet, a satellite-based nowcasting framework that predicts offshore wind speed and direction from irregularly sampled, asynchronous satellite scatterometer constellations. Utilizing a partial convolutional long short-term memory network with encoded spatial observation masks and continuous temporal representations, WindCastNet achieves significant error reductions compared to operational NWP models and persistence over the North Sea at short lead times.

## Key Contributions

- Introduces WindCastNet, the first satellite-based nowcasting framework for offshore wind speed and direction utilizing scatterometer constellations.
- Employs a partial convolutional LSTM network to process spatiotemporally irregular, asynchronous microwave radar observations from international satellite scatterometers.
- Achieves a 23% and 7% reduction in root-mean-square error relative to the HARMONIE MEPS model at 1 and 2 h lead times over the North Sea.

## Limitations

Forecast skill decreases under strong-wind conditions and spatially non-uniform flow.

## Open Questions & Future Work

- [[domain-extension-boundary-condition-modeling]]

## Key Concepts

- [[windcastnet]]: A satellite-based nowcasting framework for offshore wind speed and direction that learns from spatiotemporally irregular scatterometer observations using partial convolutional LSTMs.

## Archivist Review

Approved the central framework concept WindCastNet for processing irregular scatterometer observations and the open question regarding boundary conditions for regional wind nowcasting. All other routine evaluations and geographical regions were filtered out to maintain strict vault standards.

### Approved Concepts
- WindCastNet: It introduces the first satellite-based nowcasting framework for offshore wind speed and direction using scatterometer constellations.

### Approved Open Questions
- Domain Extension and Boundary Conditions: Crucial for improving nowcasting accuracy during non-uniform or highly dynamic synoptic events where large-scale weather systems propagate across regional boundaries.

## Links

- [Abstract](https://arxiv.org/abs/2607.27152)
- [PDF](https://arxiv.org/pdf/2607.27152)

