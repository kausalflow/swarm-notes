---
# CSL-compatible fields
title: "SwissCrop25: A National Multi-Year Benchmark for Operational Crop Mapping"
author:
  - literal: "Thomas Lauber"
  - literal: "Mehmet Özgür Türkoglu"
  - literal: "Sélène Ledain"
  - literal: "Helge Aasen"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/2608.09497"

# Custom fields
paper_id: "2608.09497"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "benchmark"
  - "dataset"
  - "evaluation"
  - "vision-transformer"
  - "multimodal"
  - "time-series"
architectures:
  []
datasets:
  - "swisscrop25"
concept_slugs:
  []
dataset_slugs:
  - "swisscrop25"
skill: "TimeSeriesSkill"
processed_at: "2026-08-13T06:10:24Z"
created_at: "2026-08-13T06:10:24Z"
---

# SwissCrop25: A National Multi-Year Benchmark for Operational Crop Mapping

**Authors**: Thomas Lauber, Mehmet Özgür Türkoglu, Sélène Ledain, Helge Aasen
**Date**: 2026-08-10
**Paper ID**: [openalex:2608.09497](https://arxiv.org/abs/2608.09497)

## Summary

The paper introduces SwissCrop25, a national-scale multi-year crop mapping benchmark spanning seven growing seasons (2019-2025) that combines Sentinel-2 time series, daily temperature observations, and a fine-grained taxonomy of 73 crop types and 5 non-crop classes. Using a leave-one-year-out evaluation protocol, the authors benchmark U-TAE, TSViT, and Galileo, revealing that domain-specific models like TSViT outperform general EO foundation models and highlighting challenges related to interannual distribution shifts and in-season progression.

## Key Contributions

- Introduces SwissCrop25, a national-scale multi-year benchmark dataset for operational crop mapping spanning seven growing seasons (2019-2025).
- Defines a rigorous leave-one-year-out evaluation protocol combining cropland delineation and fine-grained crop classification across 73 crop types and 5 non-crop land cover classes.
- Evaluates representative architectures (U-TAE, TSViT, Galileo) and demonstrates that TSViT achieves superior overall performance while highlighting trade-offs between domain-specific models and EO foundation models.
- Shows that incorporating temperature-derived phenological information improves model robustness against interannual distribution shifts.

## Open Questions & Future Work

- [[interannual-generalisation-anomalies]]

## Archivist Review

Approved the SwissCrop25 dataset as a major national-scale resource and approved the open question regarding interannual climate anomalies in operational crop mapping. Rejected the concept candidate for SwissCrop25 since it is classified as a dataset.

### Approved Open Questions
- Mitigating Interannual Climate Anomalies: Understanding and bridging performance gaps during climate anomalies is critical for deploying robust, operational national agricultural monitoring systems across diverse multi-year weather patterns.

### Rejected Candidates
- [concept] SwissCrop25 (`swisscrop25`) - not_reusable: SwissCrop25 is primarily a dataset and benchmark rather than a standalone algorithmic concept or architectural component.

## Datasets

- [[swisscrop25]]

## Links

- [Abstract](https://arxiv.org/abs/2608.09497)
- [PDF](https://arxiv.org/pdf/2608.09497)

