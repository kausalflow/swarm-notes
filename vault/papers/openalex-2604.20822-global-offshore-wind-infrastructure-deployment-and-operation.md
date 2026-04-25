---
# CSL-compatible fields
title: "Global Offshore Wind Infrastructure: Deployment and Operational Dynamics from Dense Sentinel-1 Time Series"
author:
  - literal: "Thorsten Hoeser"
  - literal: "Felix Bachofer"
  - literal: "Claudia Kuenzer"
issued:
  date-parts:
    - [2026, 4, 22]
url: "https://arxiv.org/abs/2604.20822"

# Custom fields
paper_id: "2604.20822"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "dataset"
  - "time-series"
  - "benchmark"
architectures:
  []
datasets:
  - "Sentinel-1 SAR Data Corpus"
concept_slugs:
  - "offshore-wind-deployment-sar-corpus"
dataset_slugs:
  - "sentinel-1-sar-data-corpus"
skill: "TimeSeriesSkill"
processed_at: "2026-04-25T06:15:12Z"
created_at: "2026-04-25T06:15:12Z"
---

# Global Offshore Wind Infrastructure: Deployment and Operational Dynamics from Dense Sentinel-1 Time Series

**Authors**: Thorsten Hoeser, Felix Bachofer, Claudia Kuenzer
**Date**: 2026-04-22
**Paper ID**: [openalex:2604.20822](https://arxiv.org/abs/2604.20822)

## Summary

This paper addresses the gap in temporally dense monitoring of global offshore wind infrastructure by introducing a comprehensive Sentinel-1 SAR time series corpus spanning 2016 to 2025. The dataset comprises over 14 million analysis-ready 1D backscatter profiles that capture construction and operational phases at high temporal resolution. The authors release this corpus alongside an expert-annotated benchmark and a rule-based baseline classifier to facilitate future research in remote sensing-based infrastructure lifecycle monitoring.

## Key Contributions

- Introduces a global Sentinel-1 SAR time series corpus covering 15,606 infrastructure locations and 14.8 million events.
- Provides an expert-annotated benchmark dataset of 553 time series with 328,657 semantic event labels for monitoring infrastructure lifecycle.
- Demonstrates baseline classifier performance (macro F1 of 0.84) for event-wise detection of deployment and operational phases.

## Open Questions & Future Work

- [[unified-spatiotemporal-offshore-monitoring]]

## Key Concepts

- [[offshore-wind-deployment-sar-corpus]]: A global SAR time series corpus of offshore wind infrastructure deployment and operational dynamics from 2016-2025.

## Archivist Review

I approved the dataset and the corpus concept due to their unique scale in remote sensing infrastructure monitoring. The open question was approved for capturing the critical limitation of current two-stage spatiotemporal monitoring paradigms in the SAR domain. No other candidates were provided.

### Approved Concepts
- Offshore Wind Deployment SAR Corpus: This is the first global-scale, temporally dense dataset for monitoring the full lifecycle of offshore wind infrastructure using SAR data.

### Approved Open Questions
- Unified Spatiotemporal Monitoring Framework: Improving early-onset detection is critical for accurate monitoring of the entire construction lifecycle, which is currently hindered by the two-stage separation of spatial detection and temporal analysis.

## Datasets

- [[sentinel-1-sar-data-corpus]]

## Links

- [Abstract](https://arxiv.org/abs/2604.20822)
- [PDF](https://arxiv.org/pdf/2604.20822)

