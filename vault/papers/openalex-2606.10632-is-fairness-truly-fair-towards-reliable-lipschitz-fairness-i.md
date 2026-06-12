---
# CSL-compatible fields
title: "Is Fairness Truly Fair? Towards Reliable Lipschitz Fairness in Multi-Task Learning via Fixed-δ Alignment"
author:
  - literal: "Junbo Ding"
  - literal: "Xin Zang"
  - literal: "Chenchen Pan"
  - literal: "Donghao Song"
  - literal: "Jiaxin Zhu"
  - literal: "Danhuai Guo"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.10632"

# Custom fields
paper_id: "2606.10632"
paper_source: "openalex"
domain: "nlp"
tags:
  - "fairness"
  - "multitask-learning"
  - "robustness"
  - "evaluation"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fixed-delta-auditing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:55:19Z"
created_at: "2026-06-12T08:55:19Z"
---

# Is Fairness Truly Fair? Towards Reliable Lipschitz Fairness in Multi-Task Learning via Fixed-δ Alignment

**Authors**: Junbo Ding, Xin Zang, Chenchen Pan, Donghao Song, Jiaxin Zhu, Danhuai Guo
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.10632](https://arxiv.org/abs/2606.10632)

## Summary

This paper addresses the problem of 'threshold confounding' in Lipschitz fairness evaluation, where variations in representation scales between different multi-task learning models make fairness comparisons inconsistent. The authors introduce ReLiF, a framework that enforces a fixed-δ threshold for evaluation to ensure semantic consistency and uses a violation-rate feedback controller to balance fairness regularization with task utility. Experiments demonstrate that this approach reveals significant utility-fairness trade-offs and provides a more reliable fairness assessment compared to standard method-dependent auditing protocols.

## Key Contributions

- Identified the phenomenon of 'threshold confounding' in multi-task learning fairness evaluation, where method-induced representation scales distort performance comparisons.
- Proposed ReLiF, a reliability-aware framework using a shared fixed-δ tolerance for auditing and a violation-rate feedback controller for stable training.
- Demonstrated that fixed-δ auditing exposes genuine utility-fairness trade-offs often obscured by model-dependent threshold metrics in clinical time-series and computer vision tasks.

## Open Questions & Future Work

- [[cross-domain-semantic-tolerance-standardization]]

## Key Concepts

- [[fixed-delta-auditing]]: A semantically consistent fairness auditing protocol that uses a shared reference tolerance to ensure comparable evaluation across different models in multi-task learning.

## Archivist Review

The paper makes a clear contribution to fairness auditing by highlighting threshold confounding and proposing a decoupled, fixed-threshold approach. I have approved Fixed-δ Auditing as a reusable evaluation methodology and the associated open question regarding cross-domain standardization. Other candidates were not proposed, and I have remained selective per the instructions.

### Approved Concepts
- Fixed-δ Auditing: Addresses the fundamental issue of threshold confounding where varying representation scales distort fairness evaluations in multi-task learning.

### Approved Open Questions
- Cross-domain Semantic Tolerance Standardization: Without a cross-domain standard for semantic tolerance, comparing fairness across different datasets remains difficult, limiting the scalability of Lipschitz fairness auditing.

## Links

- [Abstract](https://arxiv.org/abs/2606.10632)
- [PDF](https://arxiv.org/pdf/2606.10632)

