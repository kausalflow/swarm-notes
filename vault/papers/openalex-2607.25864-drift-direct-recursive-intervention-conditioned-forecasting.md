---
# CSL-compatible fields
title: "DRIFT: Direct-Recursive Intervention-Conditioned Forecasting of ICU Physiological Trajectories"
author:
  - literal: "Weixin Liu"
  - literal: "Juming Xiong"
  - literal: "Congning Ni"
  - literal: "Yanfan Zhu"
  - literal: "Xingtao Lin"
  - literal: "Bradley Malin"
  - literal: "Zhijun Yin"
issued:
  date-parts:
    - [2026, 7, 28]
url: "https://arxiv.org/abs/2607.25864"

# Custom fields
paper_id: "2607.25864"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "robustness"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "drift-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-31T07:44:03Z"
created_at: "2026-07-31T07:44:03Z"
---

# DRIFT: Direct-Recursive Intervention-Conditioned Forecasting of ICU Physiological Trajectories

**Authors**: Weixin Liu, Juming Xiong, Congning Ni, Yanfan Zhu, Xingtao Lin, Bradley Malin, Zhijun Yin
**Date**: 2026-07-28
**Paper ID**: [openalex:2607.25864](https://arxiv.org/abs/2607.25864)

## Summary

The paper introduces DRIFT, a hybrid forecasting framework designed to predict ICU physiological trajectories under external treatment interventions. DRIFT combines a direct model for primary forecasting with a recursive, action-conditioned model that provides constrained corrections. Evaluated on large cohorts from MIMIC-IV and eICU-CRD, DRIFT achieves lower mean absolute error for mean arterial pressure than standard action-conditioned baselines across multiple forecast horizons and maintains robustness under checkpoint selection rules and treatment alterations.

## Key Contributions

- Introduces DRIFT, a hybrid framework combining direct forecasting with a recursive, action-conditioned correction model to handle treatment interventions in ICUs.
- Evaluated on 6,046 MIMIC-IV admissions and 8,345 eICU-CRD admissions across 8-, 24-, and 48-hour forecast horizons.
- Demonstrates reduced mean absolute error for mean arterial pressure (MAP) compared to TFT-action, with robust performance under treatment alterations and shared checkpoint rules.

## Limitations

Overall accuracy improvements on standard evaluations are modest, and treatment-sequence alterations increase error more for DRIFT than for TFT-action in certain audited windows.

## Open Questions & Future Work

- [[richer-action-representations-and-site-held-out-evaluation]]

## Key Concepts

- [[drift-framework]]: A hybrid forecasting framework combining a direct model with a recursive, action-conditioned correction model for ICU physiological trajectories.

## Archivist Review

Approved the central hybrid action-conditioned forecasting framework concept (DRIFT) and the open question regarding richer action representations and site-held-out evaluations. Rejected standard medical datasets as they are already established in the vault or redundant.

### Approved Concepts
- DRIFT: Core methodological contribution combining direct and recursive action-conditioned models for ICU physiological trajectory forecasting under treatment interventions.

### Approved Open Questions
- Richer Action Representations and Evaluation: Evaluating action-conditioned forecasting models on site-held-out or prospective cohorts is critical to verify clinical generalizability and prevent performance degradation across diverse hospital environments.

### Rejected Candidates
- [dataset] MIMIC-IV (`mimic-iv`) - duplicate_existing: MIMIC-IV and eICU-CRD are already present in the vault as mimic-iii/mimic-iv equivalents or are standard benchmark medical datasets.
- [dataset] eICU-CRD (`eicu-crd`) - duplicate_existing: Standard public healthcare dataset already tracked or covered in general ICU benchmarking categories.

## Links

- [Abstract](https://arxiv.org/abs/2607.25864)
- [PDF](https://arxiv.org/pdf/2607.25864)

