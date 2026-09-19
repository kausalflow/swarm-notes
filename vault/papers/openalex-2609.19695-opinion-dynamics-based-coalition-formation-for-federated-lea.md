---
# CSL-compatible fields
title: "Opinion Dynamics-based Coalition Formation for Federated Learning in Heterogeneous IoT Systems"
author:
  - literal: "Mohammed El Hanjri"
  - literal: "Anas Abouaomar"
  - literal: "Hamidou Tembine"
  - literal: "Abdellatif Kobbane"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.19695"

# Custom fields
paper_id: "2609.19695"
paper_source: "openalex"
domain: "time-series"
tags:
  - "federated-learning"
  - "time-series"
  - "forecasting"
  - "lstm"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-19T09:04:43Z"
created_at: "2026-09-19T09:04:43Z"
---

# Opinion Dynamics-based Coalition Formation for Federated Learning in Heterogeneous IoT Systems

**Authors**: Mohammed El Hanjri, Anas Abouaomar, Hamidou Tembine, Abdellatif Kobbane
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.19695](https://arxiv.org/abs/2609.19695)

## Summary

Federated learning in heterogeneous IoT deployments like smart-city water-metering networks suffers from performance degradation when standard aggregation blends dissimilar local models. To overcome this, the authors model coalition formation as a Hegselmann-Krause bounded-confidence opinion-dynamics process operating directly on the local weights of LSTM models. Evaluated on real smart-meter water consumption data, the proposed approach yields stable coalition structures within ten inner iterations and significantly outperforms standard baselines like FedAvg, FedProx, and Per-FedAvg in forecasting accuracy.

## Key Contributions

- Proposes an opinion-dynamics-based coalition formation framework using the Hegselmann-Krause (HK) bounded-confidence process on local weights to address statistical heterogeneity in federated learning.
- Develops Euclidean-distance and cosine-similarity confidence variants for the HK interaction operating directly in the local-weight space of LSTM models.
- Achieves up to a 54% reduction in average MAE compared to FedAvg, 39% relative to FedProx, and 24% relative to Per-FedAvg on short-term water-consumption forecasting.

## Archivist Review

Applied strict selectivity standards to avoid cluttering the vault. The paper's core ideas regarding federated learning coalitions and opinion dynamics are closely tied to federated clustering literature, and the single open question regarding theoretical convergence lacks distinct standalone novelty.

### Rejected Candidates
- [open_question] Theoretical Convergence of Coalition Aggregation (`theoretical-convergence-coalition-aggregation`) - low_impact: While studying convergence is interesting, this falls under standard future work on theoretical convergence guarantees for federated learning variants.

## Links

- [Abstract](https://arxiv.org/abs/2609.19695)
- [PDF](https://arxiv.org/pdf/2609.19695)

