---
# CSL-compatible fields
title: "Scaling Recurrence-aware Foundation Models for Clinical Records via Next-Visit Prediction"
author:
  - literal: "Haresh Rengaraj Rajamohan"
  - literal: "Xiang Gao"
  - literal: "Weicheng Zhu"
  - literal: "Shih‐Lun Huang"
  - literal: "Long Chen"
  - literal: "Gabe Schulman"
  - literal: "Huizhen Jin"
  - literal: "Shengduo Li"
  - literal: "Yixuan Wang"
  - literal: "Huidi Yang"
  - literal: "Kyunghyun Cho"
  - literal: "Cem M. Deniz"
  - literal: "Narges Razavian"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24562"

# Custom fields
paper_id: "2603.24562"
paper_source: "openalex"
domain: "time-series"
tags:
  - "language-model"
  - "pre-training"
  - "time-series"
  - "autoregressive"
  - "llm"
  - "evaluation"
  - "long-context"
  - "reasoning"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "recurrence-aware-next-visit-event-prediction"
  - "raven-foundation-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:30:12Z"
created_at: "2026-03-28T05:30:12Z"
---

# Scaling Recurrence-aware Foundation Models for Clinical Records via Next-Visit Prediction

**Authors**: Haresh Rengaraj Rajamohan, Xiang Gao, Weicheng Zhu, Shih‐Lun Huang, Long Chen, Gabe Schulman, Huizhen Jin, Shengduo Li, Yixuan Wang, Huidi Yang, Kyunghyun Cho, Cem M. Deniz, Narges Razavian
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24562](https://arxiv.org/abs/2603.24562)

## Summary

This paper introduces RAVEN, a novel generative pretraining approach for sequential Electronic Health Record (EHR) data built upon a Recurrence-Aware next-Visit Event prediction objective, aiming to adapt large-scale language model techniques to structured healthcare data. The model autoregressively generates future patient visits conditioned on history, while incorporating regularization to predict the likelihood of event recurrence versus novelty. The authors emphasize the necessity of scaling model size alongside data volume in data-constrained settings and highlight evaluation pitfalls related to repeatedly occurring clinical events. Evaluated via zero-shot disease incidence forecasting, RAVEN shows performance competitive with fully fine-tuned models and strong generalization capability to external cohorts despite mapping inconsistencies.

## Key Contributions

- Developed RAVEN, a generative pretraining strategy for sequential EHR data based on Recurrence-Aware next-Visit Event prediction.
- Identified a key pitfall in EHR foundation model evaluation where repeated event tokens inflate performance metrics without distinguishing new onsets.
- Empirically demonstrated that in data-constrained, compute-saturated regimes, increasing model size without commensurate data volume increase is suboptimal for scaling.
- Achieved zero-shot prediction performance rivaling fine-tuned Transformer models for disease incidence forecasting.
- Showed RAVEN's ability to generalize to an external patient cohort despite lossy clinical code mappings and feature coverage gaps without fine-tuning.

## Limitations

The investigation into scaling behaviors was constrained to a data-constrained, compute-saturated regime, suggesting that the optimal scaling trajectory might differ under different resource allocations. The evaluation focuses on zero-shot prediction against other models, leaving potential for comparison against fully fine-tuned state-of-the-art methods.

## Key Concepts

- [[recurrence-aware-next-visit-event-prediction]]: A pretraining objective for sequential clinical data that explicitly models the predictability of recurrent versus novel events in a patient's next visit.
- [[raven-foundation-model]]: A large language model pretrained on sequential electronic health record (EHR) data using a recurrence-aware next-visit prediction objective.

## Archivist Review

Two core concepts were approved: the novel pretraining objective, Recurrence-Aware Next-Visit Event Prediction, and the named model, RAVEN, as they represent a specific, reusable approach to sequential EHR modeling. The candidates identified as open questions were rejected because they represented paper-specific empirical findings or evaluation caveats rather than fundamental, reusable research problems. Scarcity was maintained by approving only the two most central technical contributions.

### Approved Concepts
- Recurrence-Aware Next-Visit Event Prediction: This is the core generative pretraining strategy introduced specifically for modeling sequential electronic health record (EHR) data.
- RAVEN Foundation Model: RAVEN is the named foundation model at the center of this work, trained on large-scale clinical records.

### Rejected Candidates
- [open_question] Pitfall of Inflated Metrics from Repeated Events in EHR Foundation Model Evaluation (`pitfall-inflated-metrics-repeated-events`) - paper_local: This is a specific evaluation caveat identified for EHR models, not a general, reusable open research question worthy of a top-level vault note.
- [open_question] Suboptimal Scaling Without Commensurate Data Volume Increase (`suboptimal-scaling-data-constrained-regime`) - paper_local: This is an empirical finding/limitation specific to the authors' scaling investigation, not a general, fundamental open question.
- [open_question] Generalization to External Cohorts with Lossy Mappings (`generalization-lossy-code-mappings`) - paper_local: This describes a demonstration of robustness rather than an explicit, unresolved open question about a general mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2603.24562)
- [PDF](https://arxiv.org/pdf/2603.24562)

