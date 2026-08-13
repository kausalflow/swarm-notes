---
# CSL-compatible fields
title: "Impact of Terminal Noise on Polarization Rotation Vector for Sensing Applications"
author:
  - literal: "Mohammad M. Hosseini"
  - literal: "Miquel Masanas"
  - literal: "Giuseppe Paris"
  - literal: "Antonio Mecozzi"
  - literal: "Alberto Marullo"
  - literal: "Danilo Decaroli"
  - literal: "Antonio Napoli"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/2608.09384"

# Custom fields
paper_id: "2608.09384"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-13T06:10:08Z"
created_at: "2026-08-13T06:10:08Z"
---

# Impact of Terminal Noise on Polarization Rotation Vector for Sensing Applications

**Authors**: Mohammad M. Hosseini, Miquel Masanas, Giuseppe Paris, Antonio Mecozzi, Alberto Marullo, Danilo Decaroli, Antonio Napoli
**Date**: 2026-08-10
**Paper ID**: [openalex:2608.09384](https://arxiv.org/abs/2608.09384)

## Summary

This work investigates how terminal and fiber noise impact state-of-polarization sensing using coherent transponders over deployed submarine cables. By analyzing Jones-matrix time series and Power Spectral Densities from the MedNautilus link alongside laboratory back-to-back references, the authors characterize low-frequency random-walk regimes, high-frequency white-noise floors, and transponder-related harmonic artifacts. The findings reveal how terminal noise obscures stochastic polarization drift and how rotation innovation variance scales with link length.

## Key Contributions

- Investigates the impact of terminal noise on polarization rotation estimates derived from coherent transponder receiver equalizer coefficients for state-of-polarization sensing.
- Analyzes Jones-matrix time series from deployed submarine links (MedNautilus) and laboratory back-to-back references using Power Spectral Density (PSD) analysis to separate low-frequency random-walk regimes from high-frequency white-noise floors.
- Demonstrates that rotation innovation variance increases with link length while identifying transponder-related harmonic spectral artifacts in practical sensing applications.

## Open Questions & Future Work

- [[mitigation-of-terminal-noise-in-sop-sensing]]

## Archivist Review

The paper investigates terminal noise in optical submarine cables for polarization sensing. No core reusable forecasting concepts were proposed, but the open question regarding terminal noise mitigation in SOP sensing represents a specific, technically important bottleneck worth archiving.

### Approved Open Questions
- Mitigation of Terminal Noise in SOP Sensing: Terminal and hardware noise acts as a primary bottleneck preventing coherent transponder-based polarization sensing from achieving its theoretical sensitivity limit, making noise mitigation critical for reliable planetary-scale geophysical monitoring.

### Rejected Candidates
- [open_question] Mitigation of Terminal Noise in SOP Sensing (`mitigation-of-terminal-noise-in-sop-sensing`) - duplicate_existing: Duplicate or highly similar question already exists or not broadly reusable across general time-series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2608.09384)
- [PDF](https://arxiv.org/pdf/2608.09384)

