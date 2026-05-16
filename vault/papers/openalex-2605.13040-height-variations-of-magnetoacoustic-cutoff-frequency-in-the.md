---
# CSL-compatible fields
title: "Height Variations of Magnetoacoustic Cutoff Frequency in the Solar Atmosphere"
author:
  - literal: "Pradeep Kayshap"
  - literal: "Gayathri Hegde"
  - literal: "Z. E. Musielak"
  - literal: "K. Murawski"
  - literal: "T. Felipe"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.13040"

# Custom fields
paper_id: "2605.13040"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "IRIS-observatory-dataset"
concept_slugs:
  []
dataset_slugs:
  - "iris-observatory-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:10:29Z"
created_at: "2026-05-16T07:10:29Z"
---

# Height Variations of Magnetoacoustic Cutoff Frequency in the Solar Atmosphere

**Authors**: Pradeep Kayshap, Gayathri Hegde, Z. E. Musielak, K. Murawski, T. Felipe
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.13040](https://arxiv.org/abs/2605.13040)

## Summary

This study investigates the height-dependent variations of the magnetoacoustic cutoff frequency within the solar atmosphere using NUV spectral data from the IRIS observatory. By applying cross-wavelet analysis to Doppler velocity time series across multiple spectral lines, the authors empirically determine the cutoff frequency at heights ranging from the photosphere to the chromosphere. The results demonstrate a significant increase in frequency with altitude, providing a new observational benchmark for calibrating solar physics models.

## Key Contributions

- Analyzed NUV spectral data to determine solar magnetoacoustic cutoff frequency variations across six distinct atmospheric heights.
- Established that cutoff frequency increases from approximately 3.0 mHz at the photosphere (0.38 Mm) to 8.5 mHz in the chromosphere (1.2 Mm).
- Provided an observational benchmark for refining existing theoretical models of wave behavior in the solar atmosphere.

## Open Questions & Future Work

- [[solar-magnetoacoustic-cutoff-convergence]]

## Archivist Review

The paper provides an observational study in solar physics rather than a generalizable ML forecasting methodology. I have approved the open question regarding the physical convergence of magnetoacoustic cutoffs and the IRIS dataset as a standalone observational resource, while rejecting all other generic ML concepts.

### Approved Open Questions
- Solar Magnetoacoustic Cutoff Convergence: The cutoff frequency determines which waves reach and potentially heat the solar upper atmosphere, making this a central unresolved question in solar physics.

### Rejected Candidates
- [dataset] IRIS (`IRIS`) - other: IRIS is a specific instrument/observatory; the dataset is renamed to be more descriptive as an observational resource.

## Datasets

- [[iris-observatory-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2605.13040)
- [PDF](https://arxiv.org/pdf/2605.13040)

