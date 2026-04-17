---
# CSL-compatible fields
title: "CycloneMAE: A Scalable Multi-Task Learning Model for Global Tropical Cyclone Probabilistic Forecasting"
author:
  - literal: "Renlong Hang"
  - literal: "Zihao Xu"
  - literal: "Jiuwei Zhao"
  - literal: "Runling Yu"
  - literal: "Leye Cheng"
  - literal: "Qingshan Liu"
issued:
  date-parts:
    - [2026, 4, 14]
url: "https://arxiv.org/abs/2604.12180"

# Custom fields
paper_id: "2604.12180"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "multi-modal"
  - "forecasting"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "structure-aware-masked-autoencoder"
  - "discrete-probabilistic-gridding-mechanism"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-17T06:29:23Z"
created_at: "2026-04-17T06:29:23Z"
---

# CycloneMAE: A Scalable Multi-Task Learning Model for Global Tropical Cyclone Probabilistic Forecasting

**Authors**: Renlong Hang, Zihao Xu, Jiuwei Zhao, Runling Yu, Leye Cheng, Qingshan Liu
**Date**: 2026-04-14
**Paper ID**: [openalex:2604.12180](https://arxiv.org/abs/2604.12180)

## Summary

CycloneMAE is a scalable, multi-task masked autoencoder designed to address limitations in current tropical cyclone (TC) forecasting, such as high NWP computational costs and the deterministic nature of existing DL models. By utilizing a TC structure-aware encoder and a discrete probabilistic gridding mechanism, the model provides both deterministic and probabilistic forecasts from multi-modal inputs. Extensive evaluation across five global ocean basins confirms that CycloneMAE achieves superior accuracy compared to operational NWP systems in wind, pressure, and track forecasting.

## Key Contributions

- Introduces CycloneMAE, a multi-task masked autoencoder that learns transferable representations for tropical cyclone forecasting.
- Outperforms leading NWP systems on global TC pressure and wind speed benchmarks (up to 120h) and track forecasting (up to 24h).
- Demonstrates that TC forecasting relies on distinct spatiotemporal features—internal convective cores for short-term and external environmental factors for long-term prediction.

## Open Questions & Future Work

- [[integrating-global-boundary-conditions-for-forecasting]]

## Key Concepts

- [[structure-aware-masked-autoencoder]]: A masked autoencoder variant designed to incorporate physical structural priors into representation learning for atmospheric phenomena.
- [[discrete-probabilistic-gridding-mechanism]]: A technique for converting deterministic deep learning outputs into probabilistic distributions via spatial discretization.

## Archivist Review

I have approved the core architectural innovations of the paper and a specific, well-defined bottleneck in integrating multi-scale atmospheric data. The concepts were renamed slightly to be more general and reusable across other forecasting domains, ensuring they fit the vault's criteria. I rejected no candidates since the provided list was concise and high-quality, though I adjusted the open question slug to be slightly more general than just TC forecasting.

### Approved Concepts
- Structure-aware masked autoencoder: It provides a reusable architectural approach for incorporating domain-specific structural priors into masked autoencoder representations for extreme weather modeling.
- Discrete probabilistic gridding mechanism: It addresses the limitation of deterministic-only DL models by providing a structured path for simultaneous probabilistic output.

### Approved Open Questions
- Integrating global boundary conditions: Addressing the spatial scale limitation is critical for advancing the reliability of data-driven models in long-range tropical cyclone track forecasting where large-scale steering flows dominate.

## Links

- [Abstract](https://arxiv.org/abs/2604.12180)
- [PDF](https://arxiv.org/pdf/2604.12180)

