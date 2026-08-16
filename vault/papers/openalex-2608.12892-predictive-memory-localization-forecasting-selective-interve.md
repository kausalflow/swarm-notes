---
# CSL-compatible fields
title: "Predictive Memory Localization: Forecasting Selective Intervention Paths from Internal Signals"
author:
  - literal: "Jinhao Jing"
  - literal: "Tian Zeyu"
  - literal: "Lucas Qingyang Fang"
  - literal: "Zhisheng Chen"
  - literal: "Shuang Chen"
  - literal: "Yuhao Luo"
  - literal: "Qiannian ZhAO"
  - literal: "Qiannian Zhao"
issued:
  date-parts:
    - [2026, 8, 13]
url: "https://arxiv.org/abs/2608.12892"

# Custom fields
paper_id: "2608.12892"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "interpretability"
  - "robustness"
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
processed_at: "2026-08-16T05:18:11Z"
created_at: "2026-08-16T05:18:11Z"
---

# Predictive Memory Localization: Forecasting Selective Intervention Paths from Internal Signals

**Authors**: Jinhao Jing, Tian Zeyu, Lucas Qingyang Fang, Zhisheng Chen, Shuang Chen, Yuhao Luo, Qiannian ZhAO, Qiannian Zhao
**Date**: 2026-08-13
**Paper ID**: [openalex:2608.12892](https://arxiv.org/abs/2608.12892)

## Summary

Activation steering often lacks guarantees about selective operating regimes when localizing representations. This paper introduces Predictive Memory Localization (PML), which treats measured-grid intervention paths as predictive targets to separate random target movement from semantic damage. Through extensive evaluation on nine datasets and fourteen domains, the authors show that low-dose causal responses can reliably forecast selective outcomes at stronger interventions, enabling risk-aware intervention selection.

## Key Contributions

- Introduces Predictive Memory Localization (PML), a framework that treats measured-grid intervention paths as predictive objects to forecast selective operating regimes for activation steering.
- Demonstrates through a large-scale frozen study across 3,000 records, 9 datasets, and 14 domains that low-dose causal responses at strength |α|=0.1 reliably predict margin-level outcomes at disjoint strengths (|α| in {0.25, 0.5}).
- Shows that a predictor-driven selector improves utility, reduces semantic-neighbor damage, and avoids dense-scan evaluations, achieving 0.801-0.828 macro AUROC on held-out records across residual-norm-matched base models.

## Archivist Review

The paper focuses on activation steering and internal representation localization in language models, which falls under LLM interpretability and steering rather than time series forecasting or fundamental temporal modeling mechanisms. No concepts or open questions met the strict reusability and methodological novelty thresholds for the vault.

### Rejected Candidates
- [open_question] Independent Validation and Collateral Damage Resolution (`independent-validation-collateral-damage-resolution`) - low_impact: The question is a boilerplate future work request for independent validation and empirical auditing rather than a precise methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.12892)
- [PDF](https://arxiv.org/pdf/2608.12892)

