---
# CSL-compatible fields
title: "Scientific Validation of the SPARC4 Pipeline: Multi-band Imaging, Polarimetry, and Photometric Time Series for Improved Characterization of Transiting Exoplanets"
author:
  - literal: "Eder Martioli"
  - literal: "Vanderlei Rodrigues"
  - literal: "Julio C. N. Campagnolo"
  - literal: "F. Jablonski"
  - literal: "Ana Carolina Mattiuci"
  - literal: "F. Falkenberg"
  - literal: "Gustavo H. S. Santos"
  - literal: "Marina M. C. Mello"
  - literal: "Isabel J. Lima"
  - literal: "Filipe V. M. Monteiro"
  - literal: "Luciano Fraga"
  - literal: "Leandro de Almeida"
  - literal: "Diego Lorenzo-Oliveira"
  - literal: "Hélio D. Perottoni"
  - literal: "Laerte Andrade"
  - literal: "Wagner Schlindwein"
  - literal: "Denis Bernardes"
issued:
  date-parts:
    - [2026, 4, 7]
url: "https://arxiv.org/abs/2604.05305"

# Custom fields
paper_id: "2604.05305"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-10T06:26:19Z"
created_at: "2026-04-10T06:26:19Z"
---

# Scientific Validation of the SPARC4 Pipeline: Multi-band Imaging, Polarimetry, and Photometric Time Series for Improved Characterization of Transiting Exoplanets

**Authors**: Eder Martioli, Vanderlei Rodrigues, Julio C. N. Campagnolo, F. Jablonski, Ana Carolina Mattiuci, F. Falkenberg, Gustavo H. S. Santos, Marina M. C. Mello, Isabel J. Lima, Filipe V. M. Monteiro, Luciano Fraga, Leandro de Almeida, Diego Lorenzo-Oliveira, Hélio D. Perottoni, Laerte Andrade, Wagner Schlindwein, Denis Bernardes
**Date**: 2026-04-07
**Paper ID**: [openalex:2604.05305](https://arxiv.org/abs/2604.05305)

## Summary

The paper presents the SPARC4 Pipeline, a comprehensive data processing suite designed for the SPARC4 instrument at the Pico dos Dias Observatory to handle multi-band imaging and polarimetry. The authors demonstrate the pipeline's capability to deliver high-cadence time series with 0.02% photometric precision and ~0.02% polarimetric precision for transiting exoplanet observations. By integrating these high-precision ground-based observations with space-based TESS and K2 data via a Bayesian MCMC framework, the pipeline significantly improves the characterization of hot Jupiter physical parameters.

## Key Contributions

- Introduces the SPARC4 Pipeline, an end-to-end processing suite for multi-band photometry and polarimetry data acquired at the Pico dos Dias Observatory.
- Demonstrates 0.02% photometric precision and ~0.02% polarimetric precision for exoplanetary transits with host stars in the 10.2 < V < 13.9 magnitude range.
- Validates joint Bayesian MCMC modeling of SPARC4 and TESS/K2 data to refine physical parameters of hot Jupiters, including orbital periods and planetary radii.

## Open Questions & Future Work

- [[instrument-induced-flux-modulation-correction]]

## Archivist Review

The paper focuses on an instrument-specific data processing pipeline for astronomical observations, which is not a general-purpose forecasting or machine learning contribution. I rejected the SPARC4 Pipeline as it is domain-specific software. I approved the open question regarding flux modulation, as it addresses a fundamental challenge in high-precision time-series sensor calibration that generalizes to other observational astronomy contexts.

### Approved Open Questions
- Instrument-induced flux modulation correction: Instrumental modulation often exceeds the target signal amplitude, making automated correction protocols a fundamental requirement for the scientific validity of high-precision polarimetric time-series analysis in astronomy.

### Rejected Candidates
- [concept] SPARC4 Pipeline (`sparc4-pipeline`) - paper_local: This is a specific software tool and instrument-local pipeline, not a reusable algorithmic concept for general forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2604.05305)
- [PDF](https://arxiv.org/pdf/2604.05305)

