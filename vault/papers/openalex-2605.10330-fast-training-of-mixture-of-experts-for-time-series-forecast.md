---
# CSL-compatible fields
title: "Fast Training of Mixture-of-Experts for Time Series Forecasting via Expert Loss Integration"
author:
  - literal: "Btissame El Mahtout"
  - literal: "Florian Ziel"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10330"

# Custom fields
paper_id: "2605.10330"
paper_source: "openalex"
domain: "time-series"
tags:
  - "mixture-of-experts"
  - "moe"
  - "time-series"
  - "forecasting"
  - "online-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "expert-specific-loss-integration"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:36:56Z"
created_at: "2026-05-14T07:36:56Z"
---

# Fast Training of Mixture-of-Experts for Time Series Forecasting via Expert Loss Integration

**Authors**: Btissame El Mahtout, Florian Ziel
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10330](https://arxiv.org/abs/2605.10330)

## Summary

This paper proposes an adaptive Mixture-of-Experts (MoE) framework for time series forecasting that improves expert specialization by incorporating expert-specific losses into the global training objective. To enhance training efficiency, the method employs a partial online learning strategy that allows for incremental updates to the gating mechanism and expert parameters. This approach avoids costly full-model retraining while achieving superior predictive accuracy across various energy, economic, and tourism datasets. Empirical evaluations confirm that this framework outperforms traditional statistical methods and baseline neural networks like Transformers and WaveNet.

## Key Contributions

- Introduces an expert-specific loss integration strategy that incorporates expert-level errors into the global forecasting objective to drive specialization.
- Proposes a partial online learning strategy for MoE that enables incremental parameter updates, significantly reducing the computational overhead of full retraining.
- Demonstrates state-of-the-art forecasting performance and improved training efficiency across diverse economic, tourism, and energy datasets compared to statistical baselines and standard neural architectures.

## Open Questions & Future Work

- [[optimizing-loss-balance-in-moe-forecasting]]

## Key Concepts

- [[expert-specific-loss-integration]]: A training strategy for mixture-of-experts that incorporates expert-level prediction errors into the global loss function to drive specialization.

## Archivist Review

The approved concept provides a novel approach to training mixture-of-experts by explicitly integrating expert-level objectives into the global loss function. The open question was approved to address the instability of balancing these multiple losses in forecasting, which is a known challenge in MoE architectures. I rejected the initial slug for the open question in favor of a slightly more descriptive and standardized naming convention.

### Approved Concepts
- Expert-specific loss integration: It is the central methodological novelty enabling improved expert specialization in the proposed MoE framework.

### Approved Open Questions
- Optimizing Loss Balance in MoE: Balancing global and expert-specific objectives is critical for MoE training dynamics, as poor weighting can lead to specialization instability or pathological outputs.

### Rejected Candidates
- [open_question] Optimizing Loss Balance in MoE (`moe-gamma-sensitivity-and-extreme-predictions`) - duplicate_existing: Renamed to a cleaner, more generalized slug for consistency with existing vault naming.

## Links

- [Abstract](https://arxiv.org/abs/2605.10330)
- [PDF](https://arxiv.org/pdf/2605.10330)

