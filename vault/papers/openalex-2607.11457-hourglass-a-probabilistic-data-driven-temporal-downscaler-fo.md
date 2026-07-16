---
# CSL-compatible fields
title: "HourGlass: A probabilistic data-driven temporal downscaler for global and regional weather forecasting"
author:
  - literal: "Magnus Sikora Ingstad"
  - literal: "Mariana C. A. Clare"
  - literal: "Olav Ersland"
  - literal: "Vera Gahlen"
  - literal: "Håvard Homleid Haugen"
  - literal: "Ophélia Miralles"
  - literal: "Even M. Nordhagen"
  - literal: "Thomas N. Nipen"
  - literal: "Ivar A. Seierstad"
  - literal: "John Bjørnar Bremnes"
  - literal: "Michael Maier-Gerber"
  - literal: "Zied Ben Bouallègue"
  - literal: "Harrison Cook"
  - literal: "Christian Lessig"
  - literal: "Gert Mertes"
  - literal: "Cathal O'Brien"
  - literal: "Florian Pinault"
  - literal: "Ana Prieto Nemesio"
  - literal: "Matthew Chantry"
issued:
  date-parts:
    - [2026, 7, 13]
url: "https://arxiv.org/abs/2607.11457"

# Custom fields
paper_id: "2607.11457"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "probabilistic-forecasting"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "hourglass-temporal-downscaler"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-16T07:14:27Z"
created_at: "2026-07-16T07:14:27Z"
---

# HourGlass: A probabilistic data-driven temporal downscaler for global and regional weather forecasting

**Authors**: Magnus Sikora Ingstad, Mariana C. A. Clare, Olav Ersland, Vera Gahlen, Håvard Homleid Haugen, Ophélia Miralles, Even M. Nordhagen, Thomas N. Nipen, Ivar A. Seierstad, John Bjørnar Bremnes, Michael Maier-Gerber, Zied Ben Bouallègue, Harrison Cook, Christian Lessig, Gert Mertes, Cathal O'Brien, Florian Pinault, Ana Prieto Nemesio, Matthew Chantry
**Date**: 2026-07-13
**Paper ID**: [openalex:2607.11457](https://arxiv.org/abs/2607.11457)

## Summary

HourGlass is a probabilistic temporal downscaling model designed to generate high-frequency hourly weather forecasts from standard 6-hourly data-driven forecasting systems. Unlike existing deterministic downscaling approaches that result in overly smooth fields, HourGlass uses CRPS-based training on forecast trajectories to preserve small-scale spatial variability and temporal consistency. Evaluations against operational global (AIFS) and regional (Bris) ensemble systems demonstrate the model's ability to maintain baseline skill while providing realistic and coherent hourly evolutions for high-impact weather events.

## Key Contributions

- Introduces HourGlass, a probabilistic temporal downscaling method that reconstructs high-resolution temporal intervals from coarse 6-hourly weather forecasts.
- Utilizes CRPS-based loss functions to achieve temporal consistency and maintain spatial variability compared to deterministic alternatives.
- Demonstrates effectiveness in both global (AIFS) and regional (Bris) forecasting contexts, maintaining baseline skill while providing superior hourly temporal coherence.

## Open Questions & Future Work

- [[underestimation-of-extreme-precipitation]]
- [[mitigating-spectral-damping-crps]]

## Key Concepts

- [[hourglass-temporal-downscaler]]: A probabilistic data-driven temporal downscaling framework that reconstructs high-frequency intermediate forecast states from low-frequency inputs while preserving spatial variability.

## Archivist Review

The HourGlass concept was approved for its contribution to temporal downscaling via CRPS-based objectives. The open questions regarding extreme precipitation bias and spectral damping in CRPS are significant, well-defined, and broadly applicable to modern probabilistic weather forecasting research. Named datasets associated with specific model runs (AIFS-Single/ENS) were rejected as they are not standard, standalone public datasets.

### Approved Concepts
- HourGlass Temporal Downscaler: Provides a novel probabilistic approach to temporal downscaling that bridges coarse-grained and high-frequency weather forecasting, avoiding the smoothing artifacts of deterministic baselines.

### Approved Open Questions
- Extreme precipitation underestimation: Extreme precipitation events are high-impact phenomena; addressing the systematic underestimation bias is essential for the reliability of operational forecasts.
- Mitigating spectral damping in CRPS: Spectral fidelity is critical for the physical consistency of weather forecasts, particularly for high-resolution variables like precipitation.

### Rejected Candidates
- [dataset] AIFS-Single (`aifs-single-dataset`) - low_impact: This is a specific model/run configuration rather than a foundational, publicly archived research dataset.
- [dataset] AIFS-ENS (`aifs-ens-dataset`) - low_impact: This is a specific model/run configuration rather than a foundational, publicly archived research dataset.

## Links

- [Abstract](https://arxiv.org/abs/2607.11457)
- [PDF](https://arxiv.org/pdf/2607.11457)

