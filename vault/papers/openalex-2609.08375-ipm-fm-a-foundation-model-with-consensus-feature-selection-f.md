---
# CSL-compatible fields
title: "IPM-FM: A Foundation Model with Consensus Feature Selection for Industrial Process Monitoring"
author:
  - literal: "Liang Cao"
  - literal: "Weide Liu"
  - literal: "Yan Qin"
  - literal: "Jun Cheng"
  - literal: "Weisi Lin"
  - literal: "R. Bhushan Gopaluni"
issued:
  date-parts:
    - [2026, 9, 8]
url: "https://arxiv.org/abs/2609.08375"

# Custom fields
paper_id: "2609.08375"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "pre-training"
  - "fine-tuning"
  - "self-supervised-learning"
  - "uncertainty-estimation"
  - "transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:17:16Z"
created_at: "2026-09-10T09:17:16Z"
---

# IPM-FM: A Foundation Model with Consensus Feature Selection for Industrial Process Monitoring

**Authors**: Liang Cao, Weide Liu, Yan Qin, Jun Cheng, Weisi Lin, R. Bhushan Gopaluni
**Date**: 2026-09-08
**Paper ID**: [openalex:2609.08375](https://arxiv.org/abs/2609.08375)

## Summary

Industrial process monitoring traditionally relies on isolated, single-task models that suffer from data inefficiency and operating drift. To address this, the authors introduce IPM-FM, a foundation model featuring self-supervised pretraining on unlabeled industrial data, task adaptation, and an uncertainty-aware prediction head. Powered by a self-supervised Informer backbone and a multi-criteria consensus feature selector, IPM-FM outperforms classical and scratch baselines on a seven-year hydrotreater dataset while delivering calibrated predictive intervals.

## Key Contributions

- Proposes IPM-FM, the first foundation model tailored for industrial process monitoring combining self-supervised pretraining, adaptation, and uncertainty calibration.
- Integrates a self-supervised Informer backbone with a multi-criteria consensus feature selector and recursive lag-feature regression.
- Achieves an RMSE of 2.99 and R2 of 0.50 on a seven-year hydrotreater dataset, outperforming classical and from-scratch baselines by 8.3% and 14.6% in RMSE.

## Archivist Review

The paper presents an industrial process monitoring foundation model combining self-supervised pretraining, feature selection, and uncertainty estimation. No concepts or open questions met the stringent criteria for standalone vault notes.

### Rejected Candidates
- [open_question] Generalizing Heads for Classification and Anomaly Detection (`generalizing-heads-classification-anomaly`) - low_impact: Future work proposing the extension of an application-specific architecture to new tasks is too incremental and paper-local.

## Links

- [Abstract](https://arxiv.org/abs/2609.08375)
- [PDF](https://arxiv.org/pdf/2609.08375)

