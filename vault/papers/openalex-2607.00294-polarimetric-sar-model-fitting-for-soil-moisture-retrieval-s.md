---
# CSL-compatible fields
title: "Polarimetric SAR Model Fitting for Soil Moisture Retrieval: Study of PALSAR-2 data over a Heterogeneous Mine Environment in Finland"
author:
  - literal: "Oleg Antropov"
  - literal: "Alireza Hamedianfar"
  - literal: "Matthieu Molinier"
  - literal: "Ulla Salmela"
  - literal: "Hanna Kukkula"
  - literal: "Lauri Seitsonen"
  - literal: "Pauliina Liwata-Kenttälä"
  - literal: "Maarit Middleton"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.00294"

# Custom fields
paper_id: "2607.00294"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "polarimetric-soil-moisture-index-smi-t3"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:37:11Z"
created_at: "2026-07-04T07:37:11Z"
---

# Polarimetric SAR Model Fitting for Soil Moisture Retrieval: Study of PALSAR-2 data over a Heterogeneous Mine Environment in Finland

**Authors**: Oleg Antropov, Alireza Hamedianfar, Matthieu Molinier, Ulla Salmela, Hanna Kukkula, Lauri Seitsonen, Pauliina Liwata-Kenttälä, Maarit Middleton
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.00294](https://arxiv.org/abs/2607.00294)

## Summary

This study explores physical model-based approaches for retrieving surface soil moisture from PALSAR-2 quad-pol SAR data over a complex mining site in Finland. The authors propose a generalized polarimetric soil moisture index (SMI) derived from the [T3] coherency matrix, which effectively incorporates temporal backscatter dynamics. The results demonstrate that sediment-specific calibration and dB-based polarimetric projections are essential for accurate retrieval, achieving an R² of 0.67. Findings suggest that physics-based semi-empirical models remain competitive with, or superior to, black-box machine learning models in data-scarce environments.

## Key Contributions

- Proposes a generalization of the TU Wien SMI for polarimetric [T3] coherency matrices, enabling improved surface soil moisture (SSM) estimation in heterogeneous mining environments.
- Demonstrates that dB-based projections of polarimetric features consistently outperform linear or trace-normalized representations for retrieval tasks.
- Establishes that sediment-specific calibration is critical for achieving high accuracy in SSM retrieval, significantly outperforming global model fitting.

## Open Questions & Future Work

- [[generalizing-ssm-retrieval-models-in-heterogeneous-environments]]

## Key Concepts

- [[polarimetric-soil-moisture-index-smi-t3]]: A generalization of time-series soil moisture index (SMI) retrieval methods applied to polarimetric coherency matrix [T3] representations.

## Archivist Review

I approved the proposed Polarimetric Soil Moisture Index (SMI[T3]) as it offers a specific, generalized approach for extending temporal geophysical indices to polarimetric SAR data. I also approved the open question regarding the generalization of SSM retrieval models, as it addresses a significant technical bottleneck in the application of SAR-based monitoring to complex, non-agricultural environments. The dataset PALSAR-2 was rejected as it refers to a sensor rather than a distinct, citable dataset.

### Approved Concepts
- Polarimetric Soil Moisture Index (SMI[T3]): Generalizes standard temporal SMI metrics to higher-dimensional polarimetric feature spaces for enhanced soil moisture estimation.

### Approved Open Questions
- Generalizing SSM Retrieval Models: Improving the transferability of SAR-based soil moisture retrieval is critical for operational monitoring of heterogeneous engineered landscapes where ground truth data is scarce.

### Rejected Candidates
- [dataset] PALSAR-2 (`palsar-2`) - other: This is a satellite sensor instrument model, not a specific reusable dataset release.

## Links

- [Abstract](https://arxiv.org/abs/2607.00294)
- [PDF](https://arxiv.org/pdf/2607.00294)

