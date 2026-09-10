---
# CSL-compatible fields
title: "Neptune: An AI model for Global Ocean Subseasonal Prediction"
author:
  - literal: "D Donno"
  - literal: "Italo Epicoco"
  - literal: "Massimo Cafaro"
  - literal: "Gabriele Accarino"
  - literal: "Mohammad M. Amirian"
  - literal: "Viviana Acquaviva"
  - literal: "Paola Nassisi"
  - literal: "Doroteaciro Iovino"
  - literal: "Annalisa Bracco"
  - literal: "Simona Masina"
  - literal: "Pierre Gentine"
issued:
  date-parts:
    - [2026, 9, 8]
url: "https://arxiv.org/abs/2609.08606"

# Custom fields
paper_id: "2609.08606"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "fourier-neural-operator"
architectures:
  []
datasets:
  []
concept_slugs:
  - "neptune-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:18:07Z"
created_at: "2026-09-10T09:18:07Z"
---

# Neptune: An AI model for Global Ocean Subseasonal Prediction

**Authors**: D Donno, Italo Epicoco, Massimo Cafaro, Gabriele Accarino, Mohammad M. Amirian, Viviana Acquaviva, Paola Nassisi, Doroteaciro Iovino, Annalisa Bracco, Simona Masina, Pierre Gentine
**Date**: 2026-09-08
**Paper ID**: [openalex:2609.08606](https://arxiv.org/abs/2609.08606)

## Summary

This paper introduces Neptune, an end-to-end data-driven framework for global ocean and sea-ice emulation tailored for subseasonal-to-seasonal (S2S) timescales up to 60 days. Combining Convolutional Neural Networks and Spherical Fourier Neural Operators, Neptune models various ocean state variables (temperature, salinity, currents, sea ice) at 1° (Neptune-1) and 0.25° (Neptune-025) resolutions under prescribed atmospheric fields. Evaluated across statistical metrics, physical coherency tests, and climate indices, Neptune successfully captures complex ocean dynamics while maintaining stability over long timescales.

## Key Contributions

- Proposes Neptune, an end-to-end data-driven framework combining CNNs and Spherical Fourier Neural Operators (SFNOs) for global ocean and sea-ice subseasonal-to-seasonal emulation up to 60 days.
- Introduces two model variants, Neptune-1 and Neptune-025, operating at 1° and 0.25° resolutions respectively, forced by prescribed daily atmospheric fields.
- Demonstrates robust long-term stability and spatio-temporal accuracy across standard statistical metrics (RMSE, CRPS, ACC), physical coherency metrics (Ocean Heat Content, EKE), and climate indices (ENSO, IOD).

## Open Questions & Future Work

- [[fully-coupled-s2s-emulator]]

## Key Concepts

- [[neptune-framework]]: An end-to-end data-driven framework combining CNNs and Spherical Fourier Neural Operators for global ocean and sea-ice subseasonal-to-seasonal emulation up to 60 days.

## Archivist Review

Approved the primary model framework concept and the future fully coupled S2S emulator open question while maintaining strict scarcity and rejecting established architectural components like SFNO.

### Approved Concepts
- Neptune Framework: Central novelty of the paper, representing a data-driven framework combining CNNs and SFNOs for global ocean and sea-ice subseasonal prediction.

### Approved Open Questions
- Fully Coupled S2S Emulators: Coupled atmosphere-ocean feedback is crucial for accurate multi-week and seasonal climate prediction, as uncoupled emulators rely on prescribed atmospheric forcing and miss critical two-way interactions.

### Rejected Candidates
- [concept] Spherical Fourier Neural Operators (SFNO) (`spherical-fourier-neural-operators-sfno`) - not_novel: SFNO is an existing neural operator architecture rather than a novel concept introduced by this paper.

## Links

- [Abstract](https://arxiv.org/abs/2609.08606)
- [PDF](https://arxiv.org/pdf/2609.08606)

