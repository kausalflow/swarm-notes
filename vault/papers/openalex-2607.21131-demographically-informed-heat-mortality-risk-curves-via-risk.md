---
# CSL-compatible fields
title: "Demographically-Informed Heat-Mortality Risk Curves via Risk Graph Neural Networks"
author:
  - literal: "Alex Davies"
  - literal: "Y. T. Eunice Lo"
  - literal: "Ry Zhu"
issued:
  date-parts:
    - [2026, 7, 23]
url: "https://arxiv.org/abs/2607.21131"

# Custom fields
paper_id: "2607.21131"
paper_source: "openalex"
domain: "biology"
tags:
  - "graph-neural-network"
  - "gnn"
  - "interpretablity"
  - "time-series"
  - "forecasting"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "risk-graph-neural-networks"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-26T07:30:15Z"
created_at: "2026-07-26T07:30:15Z"
---

# Demographically-Informed Heat-Mortality Risk Curves via Risk Graph Neural Networks

**Authors**: Alex Davies, Y. T. Eunice Lo, Ry Zhu
**Date**: 2026-07-23
**Paper ID**: [openalex:2607.21131](https://arxiv.org/abs/2607.21131)

## Summary

The paper introduces Risk Graph Neural Networks (RGNNs), a hierarchical GNN encoder that incorporates granular census features to optimize Distributed Lag Non-linear Model (DLNM) coefficient vectors for heat-mortality risk estimation. By combining GNNs with traditional epidemiological models, RGNNs preserve interpretable exposure-response risk curves while improving calibration. Evaluated across 10 regions of England and Wales, the proposed method maintains lower point-errors and robust uncertainty coverage during extreme heat events where standard baselines collapse.

## Key Contributions

- Proposes Risk Graph Neural Networks (RGNNs), a hierarchical graph neural network encoder that integrates granular census features to optimize Distributed Lag Non-linear Model (DLNM) coefficient vectors.
- Preserves interpretable exposure-response risk curve outputs while significantly enhancing predictive calibration across different geographic regions.
- Demonstrates superior robustness during extreme heat events, maintaining lower point-errors and near-nominal uncertainty coverage during the 2022 heatwave in England and Wales where standard DLNM baselines fail.

## Limitations

Evaluated specifically on temperature-mortality time series across 10 regions of England and Wales.

## Open Questions & Future Work

- [[transferability-of-demographic-embeddings-for-health-outcomes]]

## Key Concepts

- [[risk-graph-neural-networks]]: A hierarchical graph neural network encoder that uses granular census features to optimize Distributed Lag Non-linear Model coefficient vectors for heat-mortality risk estimation.

## Archivist Review

Approved the core method concept 'Risk Graph Neural Networks' and its associated open question regarding demographic embedding transferability, while rejecting the established standard baseline DLNM as well as paper-local geographic references.

### Approved Concepts
- Risk Graph Neural Networks: RGNN introduces a novel hierarchical GNN encoder designed to integrate granular census features into DLNM coefficient vectors for heat-mortality risk estimation.

### Approved Open Questions
- Transferability of Demographic Embeddings for Health Outcomes: Determining whether spatial demographic embeddings can transfer zero-shot or few-shot across diverse geographic regions and health outcomes is vital for scaling predictive public health infrastructure.

### Rejected Candidates
- [concept] Distributed Lag Non-linear Models (`dlnm`) - not_novel: DLNMs are standard existing statistical models in environmental epidemiology, not a new method introduced by the paper.

## Links

- [Abstract](https://arxiv.org/abs/2607.21131)
- [PDF](https://arxiv.org/pdf/2607.21131)

