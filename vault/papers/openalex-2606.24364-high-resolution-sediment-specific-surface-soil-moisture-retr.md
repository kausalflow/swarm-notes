---
# CSL-compatible fields
title: "High Resolution Sediment-Specific Surface Soil Moisture Retrieval Using Sentinel-1 Time Series and Auxiliary Data"
author:
  - literal: "Alireza Hamedianfar"
  - literal: "Oleg Antropov"
  - literal: "Matthieu Molinier"
  - literal: "Ulla Salmela"
  - literal: "Hanna Kukkula"
  - literal: "Lauri Seitsonen"
  - literal: "Pauliina Liwata-Kenttälä"
  - literal: "Maarit Middleton"
issued:
  date-parts:
    - [2026, 6, 23]
url: "https://arxiv.org/abs/2606.24364"

# Custom fields
paper_id: "2606.24364"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "machine-translation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-26T08:25:14Z"
created_at: "2026-06-26T08:25:14Z"
---

# High Resolution Sediment-Specific Surface Soil Moisture Retrieval Using Sentinel-1 Time Series and Auxiliary Data

**Authors**: Alireza Hamedianfar, Oleg Antropov, Matthieu Molinier, Ulla Salmela, Hanna Kukkula, Lauri Seitsonen, Pauliina Liwata-Kenttälä, Maarit Middleton
**Date**: 2026-06-23
**Paper ID**: [openalex:2606.24364](https://arxiv.org/abs/2606.24364)

## Summary

This study addresses high-resolution surface soil moisture monitoring at a mining site by evaluating multiple machine learning models using integrated SAR and optical imagery. The authors develop sediment-specific retrieval models, demonstrating that tree-based ensemble methods effectively leverage complex multi-source data including backscatter and topography. Results highlight that incorporating sediment texture information provides performance gains, particularly in clay and organic soil environments compared to gravel-rich zones.

## Key Contributions

- Introduces a sediment-specific soil moisture retrieval methodology using multi-sensor SAR (Sentinel-1) and optical (Sentinel-2) data.
- Achieves high-accuracy soil moisture estimation with RMSE of 0.037-0.050 m^3/m^3 and R^2 up to 0.90 in a mining quarry environment.
- Demonstrates that tree-based ensemble models (LightGBM, RF, XGBoost) outperform linear baselines for soil moisture prediction in complex mining site geologies.

## Open Questions & Future Work

- [[physical-interpretability-ssm-ml-models]]

## Archivist Review

The paper describes a standard application of existing tree-based ensemble methods to multi-modal remote sensing data for a site-specific task. It lacks a generalizable methodological contribution that would warrant a permanent concept note. The open question regarding physical interpretability in remote sensing is substantial and relevant to broader challenges in the field.

### Approved Open Questions
- Improving Physical Interpretability in SSM Models: Standard machine learning approaches in remote sensing often suffer from overfitting to local training data. Addressing this through physical constraints or foundation models is critical for creating scalable, operational monitoring systems that can function in unseen or varied geographical settings.

### Rejected Candidates
- [concept] Sediment-specific soil moisture retrieval methodology (`sediment-specific-retrieval-methodology`) - not_novel: This is a task-specific application of standard regression models rather than a reusable methodological innovation.

## Links

- [Abstract](https://arxiv.org/abs/2606.24364)
- [PDF](https://arxiv.org/pdf/2606.24364)

