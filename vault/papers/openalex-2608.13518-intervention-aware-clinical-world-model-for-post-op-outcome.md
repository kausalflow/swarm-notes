---
# CSL-compatible fields
title: "Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology"
author:
  - literal: "Yunsung Chung"
  - literal: "Yingshuo Liu"
  - literal: "Abboud F. Hassan"
  - literal: "Han Feng"
  - literal: "Mary M. Maleckar"
  - literal: "Nassir Marrouche"
  - literal: "Jihun Hamm"
issued:
  date-parts:
    - [2026, 8, 13]
url: "https://arxiv.org/abs/2608.13518"

# Custom fields
paper_id: "2608.13518"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  - "DECAAF-II"
concept_slugs:
  []
dataset_slugs:
  - "decaaf-ii"
skill: "TimeSeriesSkill"
processed_at: "2026-08-16T05:18:15Z"
created_at: "2026-08-16T05:18:15Z"
---

# Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology

**Authors**: Yunsung Chung, Yingshuo Liu, Abboud F. Hassan, Han Feng, Mary M. Maleckar, Nassir Marrouche, Jihun Hamm
**Date**: 2026-08-13
**Paper ID**: [openalex:2608.13518](https://arxiv.org/abs/2608.13518)

## Summary

The paper introduces an intervention-aware clinical world model for post-operative outcome forecasting in cardiology that captures irregular, time-ordered patient trajectories following interventions. By encoding baseline imaging into a 3D spatial latent state and updating it with asynchronous clinical events, procedural context, and physiological embeddings, the model predicts long-term recurrence risks and scar-extent evolution. Evaluated on the DECAAF-II dataset for atrial fibrillation ablation, the model demonstrates strong predictive performance and supports flexible retrospective queries without requiring follow-up imaging at inference.

## Key Contributions

- Proposes an intervention-aware clinical world model that evolves patient latent states through time-ordered post-intervention events for longitudinal outcome forecasting
- Encodes baseline imaging into a 3D spatial latent state and dynamically updates it using procedural context, static covariates, elapsed time, and peri-event physiological embeddings
- Achieves 0.756 AUROC and 0.777 AUPRC for atrial fibrillation recurrence prediction on DECAAF-II, alongside a scar-extent MAE of 2.971 percentage points without requiring follow-up MRI intensities at inference

## Archivist Review

No concepts met the high bar for permanent standalone vault notes. DECAAF-II was approved as a specific clinical dataset, while the open question was rejected as domain-local.

### Rejected Candidates
- [open_question] Causal Modeling of Post-Ablation Interventions (`causal-modeling-post-ablation-interventions`) - low_impact: The open question focuses heavily on domain-specific post-ablation interventions and external validation rather than a general technical bottleneck in time-series forecasting.

## Datasets

- [[decaaf-ii]]

## Links

- [Abstract](https://arxiv.org/abs/2608.13518)
- [PDF](https://arxiv.org/pdf/2608.13518)

