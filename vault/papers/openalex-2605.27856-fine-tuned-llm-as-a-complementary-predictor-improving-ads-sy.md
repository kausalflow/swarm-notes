---
# CSL-compatible fields
title: "Fine-Tuned LLM as a Complementary Predictor Improving Ads System"
author:
  - literal: "Hui Yang"
  - literal: "Daiwei He"
  - literal: "Kevin Jiang"
  - literal: "박태진"
  - literal: "Kungang Li"
  - literal: "Jiajun Luo"
  - literal: "Yuying Chen"
  - literal: "Xinyi Zhang"
  - literal: "Sihan Wang"
  - literal: "Haoyu He"
  - literal: "Yu Liu"
  - literal: "Lakshmi Manoharan"
  - literal: "David Xue"
  - literal: "Shubham Barhate"
  - literal: "Runze Su"
  - literal: "Duna Zhan"
  - literal: "Ling Leng"
  - literal: "Siping Ji"
  - literal: "Jinfeng Zhuang"
  - literal: "Alice Wu"
  - literal: "Leo Lu"
  - literal: "Han Sun"
  - literal: "Zhifang Liu"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.27856"

# Custom fields
paper_id: "2605.27856"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "fine-tuning"
  - "embedding"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "llm-driven-ancillary-prediction"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:37:42Z"
created_at: "2026-05-30T07:37:42Z"
---

# Fine-Tuned LLM as a Complementary Predictor Improving Ads System

**Authors**: Hui Yang, Daiwei He, Kevin Jiang, 박태진, Kungang Li, Jiajun Luo, Yuying Chen, Xinyi Zhang, Sihan Wang, Haoyu He, Yu Liu, Lakshmi Manoharan, David Xue, Shubham Barhate, Runze Su, Duna Zhan, Ling Leng, Siping Ji, Jinfeng Zhuang, Alice Wu, Leo Lu, Han Sun, Zhifang Liu
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.27856](https://arxiv.org/abs/2605.27856)

## Summary

This paper introduces a complementary paradigm for leveraging LLMs in large-scale advertising systems by using a fine-tuned LLM as an ancillary predictor of advertisers rather than as a ranker or generator. By forecasting likely advertisers based on user profiles and history, the LLM provides valuable priors that augment traditional candidate generation and downstream ranking processes. The approach is validated within a production-scale system, demonstrating significant offline performance improvements and measurable online business impact.

## Key Contributions

- Introduces a complementary paradigm for ad recommendation where a fine-tuned LLM acts as an ancillary predictor for potential advertisers.
- Demonstrates that LLM-based ancillary predictions effectively augment existing candidate generation and ranking pipelines in large-scale production ads systems.
- Achieves measurable end-to-end business impact and offline performance gains through the efficient harness of LLM predictive capacity as informative priors.

## Open Questions & Future Work

- [[online-deployment-of-id-aligned-llm-predictors]]

## Key Concepts

- [[llm-driven-ancillary-prediction]]: A paradigm where a fine-tuned LLM serves as an ancillary predictor to provide informative priors for downstream candidate generation and ranking systems.

## Archivist Review

I approved the concept of 'LLM-driven ancillary prediction' because it captures a novel, reusable architecture for integrating LLMs into recommendation pipelines without the common bottlenecks of generative latency or ranker replacement. I also approved an open question regarding the online deployment of ID-aligned predictors, as this addresses a specific, high-stakes technical barrier in applying LLMs to production-scale recommendation systems. I renamed the concepts/questions for better abstraction and consistency.

### Approved Concepts
- LLM-driven ancillary prediction: Proposes a distinct architectural paradigm for LLM integration in recommendation systems, specifically as a side-channel source of informative priors rather than a direct ranker or generator.

### Approved Open Questions
- Online Deployment of ID-Aligned LLM Predictors: This question addresses the fundamental deployment bottleneck of aligning LLM-based predictive signals with production-scale sparse ID structures, which is critical for real-world adoption.

### Rejected Candidates
- [concept] LLM-driven advertiser prediction (`llm-driven-advertiser-prediction`) - subcomponent_of_broader_mechanism: Renamed to 'LLM-driven ancillary prediction' to reflect the broader, more reusable paradigm rather than the task-specific domain of advertisers.
- [open_question] Online Validation of SID-Enhanced Predictors (`online-validation-of-sid-enhanced-llm-predictors`) - duplicate_existing: Renamed to 'Online Deployment of ID-Aligned LLM Predictors' to provide a more descriptive and professional title.

## Links

- [Abstract](https://arxiv.org/abs/2605.27856)
- [PDF](https://arxiv.org/pdf/2605.27856)

