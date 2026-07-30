---
# CSL-compatible fields
title: "HydroAgent: Formalizing Forecaster Expertise into Skill-Orchestrated Flood Forecasting Workflows"
author:
  - literal: "Qingyi Yang"
  - literal: "Siqian Qiu"
  - literal: "Bing Li"
  - literal: "Xu Shan"
  - literal: "Jia Feng"
  - literal: "Shunan Zhou"
  - literal: "Xudong Zhou"
  - literal: "Tiantian Xing"
  - literal: "Jiale Guo"
  - literal: "Xiaoyi Dong"
  - literal: "Gaoyu Liu"
  - literal: "Xiaohuan Liu"
  - literal: "Haiqing Pu"
  - literal: "Qingwen Deng"
  - literal: "Xun Zhang"
  - literal: "Zhongrun Xiang"
  - literal: "Haiyang Qian"
  - literal: "Ying Yan"
  - literal: "Yongkang Xu"
  - literal: "Nuo Lei"
  - literal: "Tianlong Jia"
  - literal: "Baoying Shan"
  - literal: "Carlo De Michele"
issued:
  date-parts:
    - [2026, 7, 27]
url: "https://arxiv.org/abs/2607.23983"

# Custom fields
paper_id: "2607.23983"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "agent"
  - "llm"
  - "language-model"
  - "time-series"
  - "evaluation"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "hydroagent"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-30T07:26:15Z"
created_at: "2026-07-30T07:26:15Z"
---

# HydroAgent: Formalizing Forecaster Expertise into Skill-Orchestrated Flood Forecasting Workflows

**Authors**: Qingyi Yang, Siqian Qiu, Bing Li, Xu Shan, Jia Feng, Shunan Zhou, Xudong Zhou, Tiantian Xing, Jiale Guo, Xiaoyi Dong, Gaoyu Liu, Xiaohuan Liu, Haiqing Pu, Qingwen Deng, Xun Zhang, Zhongrun Xiang, Haiyang Qian, Ying Yan, Yongkang Xu, Nuo Lei, Tianlong Jia, Baoying Shan, Carlo De Michele
**Date**: 2026-07-27
**Paper ID**: [openalex:2607.23983](https://arxiv.org/abs/2607.23983)

## Summary

Operational flood forecasting relies heavily on tacit human expertise that is difficult to formalize or audit. This paper proposes HydroAgent, a skill-orchestrated agent framework that embeds Large Language Models into model-driven flood forecasting workflows by encoding explicit expert rules to bound LLM reasoning. Evaluated in the South Yamhill River basin across 129 events, the framework successfully captures peak flows and flood volumes within tight tolerances and improves Kling-Gupta Efficiency over strong baselines, demonstrating how explicit rule boundaries can effectively guide language models in operational hydrology.

## Key Contributions

- Proposes HydroAgent, a skill-orchestrated agent framework translating tacit forecaster expertise into auditable, reproducible workflows for operational flood forecasting.
- Demonstrates that expert prior judgments capture observed peak flow and flood volume within 5% tolerance in 10 and 11 out of 14 events, with 5-fold cross-validation over 129 events yielding Pearson correlations of 0.62 and 0.84.
- Shows that guided scheme selection improves Kling-Gupta Efficiency (KGE) by 0.023-0.154 over a high-baseline scheme library (average KGE 0.890).
- Evaluates five state-of-the-art LLMs within HydroAgent, showing successful workflow execution with judgment accuracies between 40% and 80%.

## Limitations

Relies on pre-existing scheme libraries and model-driven flood simulations; evaluation is demonstrated on a single basin (South Yamhill River basin).

## Open Questions & Future Work

- [[component-wise-uncertainty-quantification-in-hybrid-forecasting]]

## Key Concepts

- [[hydroagent]]: A skill-orchestrated agent framework that embeds Large Language Models into model-driven flood forecasting workflows using explicit rule boundaries.

## Archivist Review

Approved the core framework concept 'HydroAgent' as a reusable skill-orchestrated agent paradigm for domain-specific time series forecasting, alongside its explicit open question regarding component-wise uncertainty quantification in hybrid workflows.

### Approved Concepts
- HydroAgent: HydroAgent is the central methodological contribution, formalizing tacit forecaster expertise into a skill-orchestrated agent framework for operational flood forecasting.

### Approved Open Questions
- Component-Wise Uncertainty Quantification: Essential for building trustworthy and robust AI-assisted operational forecasting systems where error sources must be transparently traced and bounded.

## Links

- [Abstract](https://arxiv.org/abs/2607.23983)
- [PDF](https://arxiv.org/pdf/2607.23983)

