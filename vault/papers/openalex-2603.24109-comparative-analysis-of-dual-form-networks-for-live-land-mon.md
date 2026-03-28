---
# CSL-compatible fields
title: "Comparative analysis of dual-form networks for live land monitoring using multi-modal satellite image time series"
author:
  - literal: "Iris Dumeur"
  - literal: "Jérémy Anger"
  - literal: "Gabriele Facciolo"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24109"

# Custom fields
paper_id: "2603.24109"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "attention-mechanism"
  - "multimodal"
  - "efficient-transformer"
  - "forecasting"
  - "recurrent-neural-network"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "dual-form-spectro-temporal-encoder"
  - "date-aware-temporal-adaptation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:28:55Z"
created_at: "2026-03-28T05:28:55Z"
---

# Comparative analysis of dual-form networks for live land monitoring using multi-modal satellite image time series

**Authors**: Iris Dumeur, Jérémy Anger, Gabriele Facciolo
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24109](https://arxiv.org/abs/2603.24109)

## Summary

This paper investigates efficient dual-form attention mechanisms (linear attention and retention) for multi-modal Satellite Image Time Series (SITS) analysis, aiming to overcome the computational limits of standard Transformers in live land monitoring. The authors propose temporal adaptations to these mechanisms to accurately compute token distances based on actual acquisition dates, which addresses the temporal irregularity common in SITS data. Evaluated on Sentinel-1 and Sentinel-2 data for forecasting and construction monitoring, the dual-form models matched Transformer performance while supporting efficient recurrent inference for incremental updates. The study confirms the efficacy of sensor fusion in these dual-form architectures for operational land monitoring systems.

## Key Contributions

- Developed and studied dual-form attention mechanisms (linear attention and retention) within a multi-modal encoder for efficient SITS analysis.
- Introduced temporal adaptations to dual-form mechanisms that compute token distances based on actual acquisition dates to handle temporal irregularity in SITS.
- Demonstrated that the dual-form approach achieves performance comparable to standard Transformers while enabling efficient recurrent inference for incremental processing.
- Showcased superior performance of the multimodal framework over mono-modal approaches for SITS forecasting and solar panel construction monitoring.

## Limitations

The primary evaluation uses forecasting as a proxy task, and the full complexity of operational land monitoring deployment is not fully explored.

## Key Concepts

- [[dual-form-spectro-temporal-encoder]]: An encoder architecture designed for multi-modal Satellite Image Time Series analysis using dual-form attention mechanisms to allow parallel training and recurrent inference.
- [[date-aware-temporal-adaptation]]: A technique applied to temporal attention mechanisms where token distance is calculated using precise acquisition dates instead of fixed sequence indices to handle irregular time series data.

## Archivist Review

Two core reusable mechanisms were approved: the 'Dual-Form Spectro-Temporal Encoder' for efficiently combining parallel training/recurrent inference in multi-modal time series, and the 'Date-Aware Temporal Adaptation' for robustly handling temporal irregularity by using actual acquisition dates for distance computation. These concepts address fundamental challenges in efficient and accurate time series modeling with irregularly sampled data, making them highly relevant for future work. No open questions were explicit enough to warrant a permanent entry.

### Approved Concepts
- Dual-Form Spectro-Temporal Encoder: This novel encoder structure is specifically designed to handle multi-modal SITS data by integrating dual-form attention mechanisms for efficiency.
- Date-Aware Temporal Adaptation: This adaptation directly addresses the critical issue of temporal irregularity inherent in real-world satellite imagery acquisition, making the models robust to unaligned time steps.

### Rejected Candidates
- [concept] Dual-Form Spectro-Temporal Encoder (`dual-form-spectro-temporal-encoder`) - generic: This concept is approved as it describes a specific reusable architecture that integrates dual-form efficiency with multi-modal SITS processing.
- [concept] Date-Aware Temporal Adaptation (`date-aware-temporal-adaptation`) - generic: This concept is approved as it introduces a generalizable method for handling temporal irregularity in time series using actual timestamps.

## Links

- [Abstract](https://arxiv.org/abs/2603.24109)
- [PDF](https://arxiv.org/pdf/2603.24109)

