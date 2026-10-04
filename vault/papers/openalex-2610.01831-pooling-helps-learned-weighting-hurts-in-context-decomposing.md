---
# CSL-compatible fields
title: "Pooling Helps, Learned Weighting Hurts In-Context: Decomposing Group Attention"
author:
  - literal: "Michael Fore"
  - literal: "James Mason Inder"
  - literal: "Mrishika Nair"
  - literal: "Praneetha Vaddamanu"
  - literal: "Sharlina Keshava"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2610.01831"

# Custom fields
paper_id: "2610.01831"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multivariate"
  - "in-context-learning"
  - "attention-mechanism"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:49:22Z"
created_at: "2026-10-04T10:49:22Z"
---

# Pooling Helps, Learned Weighting Hurts In-Context: Decomposing Group Attention

**Authors**: Michael Fore, James Mason Inder, Mrishika Nair, Praneetha Vaddamanu, Sharlina Keshava
**Date**: 2026-10-01
**Paper ID**: [openalex:2610.01831](https://arxiv.org/abs/2610.01831)

## Summary

This paper analyzes the group attention mechanism from Chronos-2 by decomposing it into query/key weight-deciding pathways and value/output summary projection pathways. Through inference-time editing of the attention matrix, the authors reveal that uniform pooling consistently benefits multivariate and in-context learning (ICL) forecasting, whereas learned Q/K weighting frequently degrades ICL performance. Consequently, replacing learned weights with uniform pooling in the first attention block improves all tested ICL configurations.

## Key Contributions

- Decomposes group attention into V/O (weighted summary projection) and Q/K (weight-deciding) pathways to evaluate cross-variate attention in time series forecasting.
- Demonstrates that uniform pooling outperforms learned Q/K weighting across the majority of sensor-network configurations.
- Shows that learned Q/K weighting materially degrades in-context learning (ICL) performance on sensor networks, whereas uniforming attention in the first block alone consistently improves ICL configurations.

## Limitations

Tested primarily on sensor-network configurations for multivariate and in-context learning forecasting regimes.

## Open Questions & Future Work

- [[learned-weighting-degradation-mechanisms]]

## Archivist Review

Applied strict scarcity and novelty filters. The proposed open question on learned weighting degradation explicitly captures an unresolved analytical bottleneck regarding depth-dependent failures and rank collapse in time series models, while concepts were rejected as paper-local analysis.

### Approved Open Questions
- Mechanisms of Learned Weighting Degradation: Understanding why learned weighting degrades in-context group attention is crucial for designing robust time series foundation models that can handle both multivariate and in-context forecasting without manual intervention.

### Rejected Candidates
- [concept] Group Attention Decomposition (`group-attention-decomposition`) - paper_local: Too paper-local and specific to the internal analysis of Chronos-2 group attention pathways.

## Links

- [Abstract](https://arxiv.org/abs/2610.01831)
- [PDF](https://arxiv.org/pdf/2610.01831)

