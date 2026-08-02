---
# CSL-compatible fields
title: "Space2Ground 2.0: A Multi-Source Dataset and Framework for Agricultural Monitoring through Fusion of Street-Level and Satellite Imagery"
author:
  - literal: "Iason Tsardanidis"
  - literal: "Alkiviadis Koukos"
  - literal: "George Choumos"
  - literal: "Vasileios Sitokontantinou"
  - literal: "Charalampos Kontoes"
  - literal: "Charalampos Kontoes"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2607.28247"

# Custom fields
paper_id: "2607.28247"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "multimodal"
  - "vision-language-model"
  - "remote-sensing"
  - "dataset"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  - "space2ground-2.0"
concept_slugs:
  []
dataset_slugs:
  - "space2ground-20"
skill: "TimeSeriesSkill"
processed_at: "2026-08-02T07:27:20Z"
created_at: "2026-08-02T07:27:20Z"
---

# Space2Ground 2.0: A Multi-Source Dataset and Framework for Agricultural Monitoring through Fusion of Street-Level and Satellite Imagery

**Authors**: Iason Tsardanidis, Alkiviadis Koukos, George Choumos, Vasileios Sitokontantinou, Charalampos Kontoes, Charalampos Kontoes
**Date**: 2026-07-30
**Paper ID**: [openalex:2607.28247](https://arxiv.org/abs/2607.28247)

## Summary

Space2Ground 2.0 is a multimodal framework and dataset that integrates Sentinel-1 SAR and Sentinel-2 satellite time series with geo-tagged crowdsourced street-level imagery for agricultural monitoring. Using an automated pipeline for semantic filtering, image quality assessment, and viewpoint-based parcel association, the authors transform raw crowdsourced photos into curated, parcel-linked observations. Experiments in crop classification demonstrate that combining ground-level visual details with overhead satellite perspectives significantly improves agricultural monitoring accuracy.

## Key Contributions

- Introduces Space2Ground 2.0, a multi-source dataset and framework combining Sentinel-1 SAR, Sentinel-2 multispectral time series, and crowdsourced street-level imagery from Mapillary for agricultural monitoring.
- Develops an automated processing pipeline featuring semantic filtering, quality assessment, and viewpoint-based parcel association to curate over 46,000 analysis-ready images linked to 8,581 parcels.
- Demonstrates through parcel-level crop classification experiments that integrating street-level visual data with satellite time series significantly enhances predictive performance compared to satellite observations alone.

## Open Questions & Future Work

- [[weakly-supervised-agricultural-labeling]]

## Archivist Review

Approved the primary dataset 'space2ground-2.0' and the open question concerning weakly supervised agricultural labeling, following strict selectivity guidelines. Rejected the concept candidate because it refers directly to the paper-specific dataset and pipeline rather than a generalized ML technique.

### Approved Open Questions
- Weakly Supervised Agricultural Labeling: Addressing label noise and reliance on administrative ground truth is critical for scaling automated agricultural monitoring systems across diverse geographical regions without manual data collection bottlenecks.

### Rejected Candidates
- [concept] Space2Ground 2.0 (`space2ground-2.0`) - not_novel: Space2Ground 2.0 is a specific multimodal dataset and collection framework rather than a reusable core machine learning concept or algorithm.

## Datasets

- [[space2ground-20]]

## Links

- [Abstract](https://arxiv.org/abs/2607.28247)
- [PDF](https://arxiv.org/pdf/2607.28247)

