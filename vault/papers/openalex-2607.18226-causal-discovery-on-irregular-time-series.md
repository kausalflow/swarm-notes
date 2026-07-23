---
# CSL-compatible fields
title: "Causal Discovery on Irregular Time Series"
author:
  - literal: "Martim Penim"
  - literal: "Ricardo Ribeiro Pereira"
  - literal: "Jacopo Bono"
  - literal: "Hugo Ferreira"
  - literal: "Mário A. T. Figueiredo"
  - literal: "Pedro Bizarro"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2607.18226"

# Custom fields
paper_id: "2607.18226"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
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
processed_at: "2026-07-23T07:26:32Z"
created_at: "2026-07-23T07:26:32Z"
---

# Causal Discovery on Irregular Time Series

**Authors**: Martim Penim, Ricardo Ribeiro Pereira, Jacopo Bono, Hugo Ferreira, Mário A. T. Figueiredo, Pedro Bizarro
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.18226](https://arxiv.org/abs/2607.18226)

## Summary

Causal discovery methods in temporal systems typically require regularly sampled data and fixed lag structures, rendering them ineffective for irregular event streams found in healthcare, sensor networks, and finance. To overcome this limitation, this work extends the PCMCI+ framework to support irregular time series by aggregating causal influence across predefined temporal windows. Evaluation on synthetic irregular event streams demonstrates that the proposed method reliably recovers underlying causal structures and outperforms standard PCMCI+ under varying signal-to-noise ratios.

## Key Contributions

- Proposed an extension of PCMCI+ to handle irregular time series by aggregating causal influence over predefined temporal windows rather than relying on fixed-lag dependencies.
- Evaluated the proposed method on synthetic irregular event streams with known causal structures across different signal-to-noise ratios.
- Demonstrated consistent recovery of underlying causal graphs and substantial performance improvements over standard PCMCI+ on irregularly sampled data.

## Archivist Review

Strictly applied the selection criteria, rejecting paper-local open questions about specific causal discovery extension sub-mechanisms and finding no novel reusable core concepts or datasets.

### Rejected Candidates
- [open_question] Contemporaneous and Lagged Edge Interaction (`contemporaneous-lagged-edge-interaction`) - paper_local: This is a paper-internal future work direction about specific edge estimation details in PCMCI+ extensions rather than a broad, reusable community-wide research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.18226)
- [PDF](https://arxiv.org/pdf/2607.18226)

