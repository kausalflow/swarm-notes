---
# CSL-compatible fields
title: "Graph-Enhanced Disease Trajectory Discovery and Temporal Endpoint Forecasting from Longitudinal Electronic Health Records"
author:
  - literal: "Jinjia Zheng"
  - literal: "Vincent S. Tseng"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.20502"

# Custom fields
paper_id: "2610.20502"
paper_source: "openalex"
domain: "medicine"
tags:
  - "transformer"
  - "attention-mechanism"
  - "healthcare"
  - "long-context"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:55:30Z"
created_at: "2026-10-17T08:55:30Z"
---

# Graph-Enhanced Disease Trajectory Discovery and Temporal Endpoint Forecasting from Longitudinal Electronic Health Records

**Authors**: Jinjia Zheng, Vincent S. Tseng
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.20502](https://arxiv.org/abs/2610.20502)

## Summary

The authors developed a leakage-controlled, graph-enhanced framework utilizing MIMIC-IV v3.1 longitudinal electronic health records to discover disease trajectories and forecast temporal endpoints. By learning train-only consecutive-admission transitions and deploying a time-aware Transformer with endpoint-specific cross-attention over 99,527 branching motifs, the approach improves micro-AUPRC and reduces long-range event-time forecasting error. However, evaluations show that branching motifs primarily provide structured long-range timing support rather than uniformly superior endpoint discrimination or survival prediction.

## Key Contributions

- Developed a leakage-controlled graph-enhanced framework using MIMIC-IV v3.1 that learns train-only consecutive-admission transitions and freezes endpoint-specific branching-motif policies.
- Demonstrated that a time-aware Transformer utilizing endpoint-specific cross-attention to retrieve patient-compatible motifs improves micro-AUPRC from 0.9330 to 0.9357 and reduces event-time MAE from 676.9 to 657.7 days.
- Revealed heterogeneous timing effects where event-time MAE worsened for short-term events within 730 days but improved by 58.9 days for long-term events occurring after 730 days.
- Established that branch conditioning reduces conditional event-time MAE by 26.9 days in an exploratory internal temporal split without improving macro C-index or integrated Brier score superiority.

## Limitations

Corrected survival evaluation over the 0-2,555-day interval did not establish macro C-index or integrated Brier score superiority over a history-only discrete-hazard model, and replacing GNN-derived scores within fixed motif identities did not improve downstream forecasting.

## Archivist Review

No candidate concepts or open questions were proposed or met the rigorous standards for permanent vault storage. The paper describes a specialized EHR pipeline using standard graph and transformer components without establishing a distinct, reusable methodology name or open question of broad theoretical import.

## Links

- [Abstract](https://arxiv.org/abs/2610.20502)
- [PDF](https://arxiv.org/pdf/2610.20502)

