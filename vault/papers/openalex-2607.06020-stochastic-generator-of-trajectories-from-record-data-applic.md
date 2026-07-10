---
# CSL-compatible fields
title: "Stochastic generator of trajectories from record data: application to the fluctuations of a glacier's frontal position from a sample of moraines"
author:
  - literal: "Megret Maud"
  - literal: "Mike Pereira"
  - literal: "Nicolas Eckert"
  - literal: "Naveau Philippe"
  - literal: "Jomelli Vincent"
issued:
  date-parts:
    - [2026, 7, 7]
url: "https://arxiv.org/abs/2607.06020"

# Custom fields
paper_id: "2607.06020"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "stochastic-modeling"
  - "non-stationary"
architectures:
  []
datasets:
  []
concept_slugs:
  - "brownian-stochastic-trajectory-reconstruction-from-records"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-10T08:15:58Z"
created_at: "2026-07-10T08:15:58Z"
---

# Stochastic generator of trajectories from record data: application to the fluctuations of a glacier's frontal position from a sample of moraines

**Authors**: Megret Maud, Mike Pereira, Nicolas Eckert, Naveau Philippe, Jomelli Vincent
**Date**: 2026-07-07
**Paper ID**: [openalex:2607.06020](https://arxiv.org/abs/2607.06020)

## Summary

This paper presents a statistical method for reconstructing entire non-stationary time series from sparse sequences of record values, where observations only consist of new maximums. The approach utilizes a Brownian stochastic simulator, with hyperparameters optimized via a Neural-Based Inference procedure. The method is applied to reconstruct the frontal position dynamics of glaciers from moraine evidence, offering a powerful tool for analyzing long-term climate trends where only historical extreme records are available.

## Key Contributions

- Introduces a Brownian stochastic simulator to reconstruct complete non-stationary time series using only record-value data.
- Develops an NBI-based hyperparameter tuning procedure for the stochastic generator, validated on historical glaciological data.
- Demonstrates the method's effectiveness on the Glacier des Bossons dataset, providing a scalable approach for long-term climate impact assessment.

## Key Concepts

- [[brownian-stochastic-trajectory-reconstruction-from-records]]: A method to reconstruct non-stationary time series from a sequence of record values using a Brownian stochastic simulator.

## Archivist Review

The paper introduces a novel approach for reconstructing continuous time series from incomplete, extreme-value records, which addresses a specific data-sparsity bottleneck in climate and historical science. I approved the core reconstruction mechanism as it represents a reusable and distinct statistical methodology for time series modeling. No datasets or open questions were sufficiently novel or central to merit addition to the vault.

### Approved Concepts
- Brownian stochastic trajectory reconstruction from records: Provides a systematic approach to reconstructing full time series from extreme observations, which is highly relevant for historical data analysis.

## Links

- [Abstract](https://arxiv.org/abs/2607.06020)
- [PDF](https://arxiv.org/pdf/2607.06020)

