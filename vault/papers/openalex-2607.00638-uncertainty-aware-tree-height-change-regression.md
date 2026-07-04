---
# CSL-compatible fields
title: "Uncertainty-aware tree height change regression"
author:
  - literal: "Max Gaber"
  - literal: "Dimitri Gominski"
  - literal: "Jaime C. Revenga"
  - literal: "Stefan Oehmcke"
  - literal: "Rasmus Fensholt"
  - literal: "Martin Brandt"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.00638"

# Custom fields
paper_id: "2607.00638"
paper_source: "openalex"
domain: "computer-vision, biology"
tags:
  - "vision-language-model"
  - "vlm"
  - "fine-tuning"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "Canopy Height Change (CHC) dataset"
concept_slugs:
  - "uncertainty-aware-change-regression"
dataset_slugs:
  - "canopy-height-change-chc-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:37:24Z"
created_at: "2026-07-04T07:37:24Z"
---

# Uncertainty-aware tree height change regression

**Authors**: Max Gaber, Dimitri Gominski, Jaime C. Revenga, Stefan Oehmcke, Rasmus Fensholt, Martin Brandt
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.00638](https://arxiv.org/abs/2607.00638)

## Summary

This paper addresses the limitations of binary change detection in forestry by introducing the uncertainty-aware change regression task. The authors provide the Canopy Height Change (CHC) dataset, which offers high-resolution (3m) continuous canopy height differences along with spatially resolved uncertainty labels. By pairing this dataset with PlanetScope time-series imagery, the authors propose and evaluate fine-tuning strategies to enable Geospatial Foundation Models (GFMs) to estimate continuous environmental changes effectively.

## Key Contributions

- Introduces the Canopy Height Change (CHC) dataset, a 3-meter resolution benchmark for continuous canopy height difference estimation over 10,598 km² of Spain.
- Formulates the task of uncertainty-aware change regression and proposes corresponding evaluation metrics and fine-tuning strategies for Geospatial Foundation Models (GFMs).
- Benchmarks state-of-the-art GFMs on the CHC dataset, providing insights into model performance and remaining challenges for continuous vegetation change estimation.

## Open Questions & Future Work

- [[gfm-pixel-level-regression-gap]]

## Key Concepts

- [[uncertainty-aware-change-regression]]: A regression task for estimating continuous changes in environmental variables while quantifying associated label uncertainty.

## Archivist Review

The paper introduces a significant shift from binary change detection to continuous, uncertainty-aware regression for environmental monitoring. The proposed task and the accompanying dataset are central to the paper's contribution and provide a reusable framework for evaluating GFM performance on fine-grained spatial tasks. The open question regarding the regression capability of GFMs is a critical, unresolved challenge in current remote sensing research.

### Approved Concepts
- Uncertainty-aware change regression: It shifts the task of canopy height monitoring from discrete change detection to a continuous regression framework that explicitly accounts for label uncertainty.

### Approved Open Questions
- GFM performance on regression tasks: This is a foundational problem in the field of remote sensing, as the utility of large-scale foundation models is currently constrained by their inability to reliably handle high-precision regression tasks essential for ecological monitoring.

## Datasets

- [[canopy-height-change-chc-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2607.00638)
- [PDF](https://arxiv.org/pdf/2607.00638)

