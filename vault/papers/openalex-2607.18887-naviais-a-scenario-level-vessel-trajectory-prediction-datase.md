---
# CSL-compatible fields
title: "NaviAIS: A Scenario-Level Vessel Trajectory Prediction Dataset withVectorized Lane Priors and the NaviLane Forecasting Framework"
author:
  - literal: "Yuan Gui"
  - literal: "Hongchen Luo"
  - literal: "Liqi Qu"
  - literal: "Longyue Fu"
  - literal: "Jiao Wang"
issued:
  date-parts:
    - [2026, 7, 21]
url: "https://arxiv.org/abs/2607.18887"

# Custom fields
paper_id: "2607.18887"
paper_source: "openalex"
domain: "time-series"
tags:
  - "dataset"
  - "forecasting"
architectures:
  []
datasets:
  - "NaviAIS"
concept_slugs:
  []
dataset_slugs:
  - "naviais"
skill: "TimeSeriesSkill"
processed_at: "2026-07-24T07:25:06Z"
created_at: "2026-07-24T07:25:06Z"
---

# NaviAIS: A Scenario-Level Vessel Trajectory Prediction Dataset withVectorized Lane Priors and the NaviLane Forecasting Framework

**Authors**: Yuan Gui, Hongchen Luo, Liqi Qu, Longyue Fu, Jiao Wang
**Date**: 2026-07-21
**Paper ID**: [openalex:2607.18887](https://arxiv.org/abs/2607.18887)

## Summary

Vessel trajectory prediction in maritime environments often suffers from unstructured raw AIS data and a lack of navigable waterway priors. To overcome this, the authors introduce NaviAIS, a standardized scenario-level dataset featuring vectorized lane priors and structured map representations. Built on this dataset, they propose NaviLane, a hierarchical macro-action framework that combines trajectory-map joint encoding, discrete macro-action generation, residual refinement, and a consequence-aware evaluator. Experiments confirm that NaviLane outperforms representative baselines in both single-modal and multimodal settings.

## Key Contributions

- Introduces NaviAIS, a standardized scenario-level vessel trajectory prediction dataset providing vectorized lane priors, lane graphs, and rasterized navigable maps.
- Proposes NaviLane, a hierarchical macro-action framework featuring trajectory-map joint encoding, a discrete macro-action codebook, residual refinement, and consequence-aware evaluation.
- Demonstrates through experiments that NaviLane outperforms representative baselines in both single-modal and multimodal vessel trajectory prediction settings.

## Archivist Review

The NaviAIS dataset is approved as a reusable standalone benchmark resource for maritime trajectory prediction, while the proposed concept and open question were rejected as domain-specific and narrow.

### Rejected Candidates
- [open_question] Generalization to Unseen Maritime Regions (`generalization-of-map-aware-vessel-trajectory-prediction-to-unseen-maritime-regions`) - low_impact: The open question focuses on regional generalization and chart annotations specific to maritime trajectory prediction, which is too narrow and domain-specific for permanent vault retention.

## Datasets

- [[naviais]]

## Links

- [Abstract](https://arxiv.org/abs/2607.18887)
- [PDF](https://arxiv.org/pdf/2607.18887)

