---
# CSL-compatible fields
title: "Deep learning model emulators for marine biogeochemistry forecasting from days to decades"
author:
  - literal: "Jozef Skakala"
  - literal: "Ieuan Higgs"
  - literal: "David Moffat"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.27168"

# Custom fields
paper_id: "2606.27168"
paper_source: "openalex"
domain: "biology"
tags:
  - "lstm"
  - "cnn"
  - "forecasting"
  - "explainability"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "physics-informed-1d-cnn-emulator"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:16:17Z"
created_at: "2026-06-28T08:16:17Z"
---

# Deep learning model emulators for marine biogeochemistry forecasting from days to decades

**Authors**: Jozef Skakala, Ieuan Higgs, David Moffat
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.27168](https://arxiv.org/abs/2606.27168)

## Summary

This paper explores the use of LSTM and physics-informed 1D CNN architectures to emulate high-complexity marine biogeochemistry models. The emulators are shown to provide stable, computationally efficient long-term forecasts and decadal projections, outperforming the parent model's forecast skill when trained on reanalysis data. The study also introduces explainability techniques to interpret the learned dynamics and highlights the models' utility for operational forecasting and marine autonomous systems.

## Key Contributions

- Demonstrates that LSTM and physics-informed 1D CNN emulators can accurately replicate parent biogeochemical models in both 10-day forecasts and decadal projections.
- Shows that emulators trained on reanalysis data outperform the parent model in forecast skill scores for phytoplankton and zooplankton.
- Enables multi-year lead time prediction for phytoplankton Spring blooms while maintaining stability over multi-decadal intervals.
- Utilizes explainability techniques to derive insights into emergent ecosystem dynamics and identify primary drivers of emulator performance.

## Open Questions & Future Work

- [[3d-biogeochemical-emulation-scaling]]
- [[emulator-data-assimilation-integration]]

## Key Concepts

- [[physics-informed-1d-cnn-emulator]]: A deep learning architecture designed for stable, computationally efficient emulation of marine biogeochemical dynamics across decadal timescales.

## Archivist Review

I approved the core architectural concept of physics-informed 1D CNN emulators, as this represents a reusable strategy for accelerating Earth System Models. I also approved two research questions regarding scaling emulators to 3D dynamics and integrating them with operational data assimilation systems, both of which are high-level, unresolved bottlenecks in the field. No other candidates met the high bar for inclusion in the knowledge vault.

### Approved Concepts
- Physics-informed 1D CNN Emulator: Enables computationally efficient, long-term stable simulation of complex marine biogeochemical systems within a 1D water-column framework.

### Approved Open Questions
- 3D Biogeochemical Emulator Scaling: Scaling to three-dimensional systems is critical for operational relevance, as biogeochemical dynamics are inherently spatial and horizontal transport is a major factor not captured in one-dimensional test-beds.
- Emulator Data Assimilation Integration: Without integration with data assimilation, emulators cannot effectively correct for initial state biases or incorporate real-time observations, which are essential for operational forecasting reliability.

## Links

- [Abstract](https://arxiv.org/abs/2606.27168)
- [PDF](https://arxiv.org/pdf/2606.27168)

