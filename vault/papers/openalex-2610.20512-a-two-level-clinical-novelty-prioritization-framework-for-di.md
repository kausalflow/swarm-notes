---
# CSL-compatible fields
title: "A Two-Level Clinical Novelty Prioritization Framework for Disease Trajectories Discovered from Longitudinal Electronic Health Records"
author:
  - literal: "Jinjia Zheng"
  - literal: "Vincent S. Tseng"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.20512"

# Custom fields
paper_id: "2610.20512"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
  - "embedding"
  - "semantic-search"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:55:50Z"
created_at: "2026-10-17T08:55:50Z"
---

# A Two-Level Clinical Novelty Prioritization Framework for Disease Trajectories Discovered from Longitudinal Electronic Health Records

**Authors**: Jinjia Zheng, Vincent S. Tseng
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.20512](https://arxiv.org/abs/2610.20512)

## Summary

This paper presents a two-level framework for prioritizing clinical disease trajectories discovered from longitudinal electronic health records by combining semantic sparsity against PubMed literature with reliability-adjusted clinical metrics. Evaluated on the MIMIC-IV v3.1 dataset, the proposed approach identifies high-semantic trajectory subgroups that improve forecasting performance (reducing MAE and sMAPE), while extensive robustness checks validate the stability of the prioritization pipeline.

## Key Contributions

- Introduced a two-level clinical novelty prioritization framework to evaluate semantic sparsity and reliability-adjusted clinical priority for graph-based disease trajectory motifs discovered from longitudinal EHRs.
- Demonstrated that branch-enhanced forecasting on a frozen high-semantic subgroup reduced conditional event-time MAE by 20.1 days and sMAPE by 2.37 percentage points on MIMIC-IV data.
- Conducted comprehensive robustness analyses across encoders, neighbor counts, templates, and reference databases, showing that broad trajectory ordering is more stable than hard top-k membership.

## Limitations

Semantic-dose analysis did not support a monotonic relationship between score and forecasting benefit after endpoint and token-count adjustment.

## Archivist Review

The paper presents a two-level clinical novelty prioritization framework for disease trajectories discovered from longitudinal electronic health records. Since no candidate concepts or open questions were supplied in the analysis input, and following our strict review policy to maintain high vault standards without inventing unprompted candidates, all lists are returned empty.

## Links

- [Abstract](https://arxiv.org/abs/2610.20512)
- [PDF](https://arxiv.org/pdf/2610.20512)

