---
# CSL-compatible fields
title: "Loss-Guided Pretraining Data Selection for Time-Series Foundation Models"
author:
  - literal: "Yike Li"
  - literal: "Song Shaoxu"
  - literal: "Jianmin Wang"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.37255"

# Custom fields
paper_id: "2609.37255"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "pre-training"
  - "foundation-model"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "loss-guided-pretraining-data-selection"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-01T11:15:05Z"
created_at: "2026-10-01T11:15:05Z"
---

# Loss-Guided Pretraining Data Selection for Time-Series Foundation Models

**Authors**: Yike Li, Song Shaoxu, Jianmin Wang
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.37255](https://arxiv.org/abs/2609.37255)

## Summary

Time-series foundation models are often pretrained on vast, heterogeneous data without estimating the informativeness of individual training windows. This paper introduces a static data-selection framework that scores training windows using a reference forecaster and connects normalized squared loss to optimization difficulty via per-sample gradient norms. By applying dataset-stratified selection to preserve diversity, the proposed method outperforms random selection and full-data pretraining while using fewer candidate windows. Furthermore, the authors show strong cross-scale and cross-architecture score correlations, indicating that lightweight reference models can effectively curate data for larger downstream targets.

## Key Contributions

- Introduced a static data-selection framework for time-series foundation models that scores each window using a reference forecaster.
- Connected normalized squared forecasting loss to optimization difficulty by showing it controls the per-sample gradient norm under a local Jacobian condition.
- Demonstrated that dataset-stratified selection preserves sample diversity while outperforming random selection and full-data pretraining despite retaining fewer candidate windows.
- Revealed strong cross-scale and cross-architecture score correlations, showing that a small reference model can effectively select pretraining data for larger target models.

## Open Questions & Future Work

- [[cross-architecture-rfl-transferability]]

## Key Concepts

- [[loss-guided-pretraining-data-selection]]: A static data-selection framework that scores time-series pretraining windows using a reference forecaster and dataset-stratified retention.

## Archivist Review

Approved one high-impact concept regarding loss-guided time-series pretraining data selection and one open question on cross-architecture reference loss transferability. No datasets were proposed or named.

### Approved Concepts
- Loss-Guided Pretraining Data Selection: Establishes a principled static data selection strategy for time-series foundation models based on forecasting loss and optimization difficulty.

### Approved Open Questions
- Cross-Architecture Reference Loss Transferability: Understanding cross-architecture score transferability is crucial for making pretraining data selection efficient and avoiding the need to train dedicated reference models for every new foundation model architecture.

## Links

- [Abstract](https://arxiv.org/abs/2609.37255)
- [PDF](https://arxiv.org/pdf/2609.37255)

