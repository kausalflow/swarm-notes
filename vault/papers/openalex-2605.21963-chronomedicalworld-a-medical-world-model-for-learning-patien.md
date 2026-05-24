---
# CSL-compatible fields
title: "ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data"
author:
  - literal: "Jiangyuan Wang"
  - literal: "Xuyong Chen"
  - literal: "Junwei He"
  - literal: "Xu Xu"
  - literal: "Shasha Xie"
  - literal: "Fuman Han"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.21963"

# Custom fields
paper_id: "2605.21963"
paper_source: "openalex"
domain: "medicine"
tags:
  - "llm"
  - "time-series"
  - "multimodal"
  - "forecasting"
  - "language-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "action-conditioned-latent-world-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:48:23Z"
created_at: "2026-05-24T07:48:23Z"
---

# ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data

**Authors**: Jiangyuan Wang, Xuyong Chen, Junwei He, Xu Xu, Shasha Xie, Fuman Han
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.21963](https://arxiv.org/abs/2605.21963)

## Summary

ChronoMedicalWorld Model (CMWM) is an action-conditioned latent world-model framework developed to address the limitations of discriminative EHR models and drifting LLMs in long-horizon clinical simulation. The model integrates structured clinical interventions with free-text communications using a joint-embedding encoder and a recurrent latent transition module. Training is guided by a novel six-term objective function that enforces both physiological shape priors and multi-step rollout stability. Results on a CKD patient cohort demonstrate that CMWM effectively outperforms GPT-5.5 baselines in forecasting eGFR trajectories, particularly when leveraging conversational intervention data.

## Key Contributions

- Proposes CMWM, an action-conditioned latent world-model framework for longitudinal patient trajectory forecasting.
- Introduces a multi-term training objective incorporating physiology-aware shape priors (slope, continuity, and large-jump penalty).
- Implements a closed-loop rollout-prefix protocol that aligns training dynamics with multi-step inference error.
- Achieves a -7.28% reduction in MAE compared to GPT-5.5 baselines on a 2,232-patient chronic kidney disease (CKD) cohort.

## Open Questions & Future Work

- [[architectural-specialization-vs-clinical-fine-tuning]]
- [[causal-inference-in-latent-clinical-forecasting]]

## Key Concepts

- [[action-conditioned-latent-world-model]]: A framework for forecasting time-series trajectories that conditions latent state transitions on both structured and unstructured exogenous intervention inputs.

## Archivist Review

The paper is approved for its advancement of clinical world models that bridge structured clinical data and unstructured communication. Concepts and questions were refined to be more generalizable and aligned with existing archival standards by moving away from paper-specific nomenclature and toward structural research questions.

### Approved Concepts
- Action-conditioned Latent World Model: Provides a specialized architectural paradigm for longitudinal clinical modeling that addresses drift in standard language-based forecasting models.

### Approved Open Questions
- Architectural Specialization vs Fine-tuning: This question addresses the fundamental trade-off between architectural domain adaptation and model-scale fine-tuning in high-stakes clinical forecasting.
- Causal Inference in Clinical Forecasting: Distinguishing causal impact from correlation is required for any clinical forecasting system intended to guide, rather than merely track, patient outcomes.

### Rejected Candidates
- [concept] ChronoMedicalWorld Model (CMWM) (`chronomedicalworld-model-cmwm`) - paper_local: This is a paper-specific model name; the underlying approach is more generally captured as an action-conditioned latent world model.
- [open_question] LLM Fine-tuning vs. World Models (`llm-clinical-fine-tuning-vs-world-models`) - duplicate_existing: Replaced with a more formal and reusable title.
- [open_question] Causal Inference in World Models (`integrating-causal-inference-clinical-world-models`) - duplicate_existing: Replaced with a more formal and reusable title.

## Links

- [Abstract](https://arxiv.org/abs/2605.21963)
- [PDF](https://arxiv.org/pdf/2605.21963)

