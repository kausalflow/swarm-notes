---
# CSL-compatible fields
title: "An Evidential Reasoning Approach for Aerial Target Classification and Intent Prediction"
author:
  - literal: "Tenzing Thiley Bhutia"
  - literal: "Subash Kumaraguru"
  - literal: "Devaprakash Muniraj"
issued:
  date-parts:
    - [2026, 7, 16]
url: "https://arxiv.org/abs/2607.14606"

# Custom fields
paper_id: "2607.14606"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "uncertainty-quantification"
architectures:
  []
datasets:
  []
concept_slugs:
  - "evidential-reasoning-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-19T07:24:34Z"
created_at: "2026-07-19T07:24:34Z"
---

# An Evidential Reasoning Approach for Aerial Target Classification and Intent Prediction

**Authors**: Tenzing Thiley Bhutia, Subash Kumaraguru, Devaprakash Muniraj
**Date**: 2026-07-16
**Paper ID**: [openalex:2607.14606](https://arxiv.org/abs/2607.14606)

## Summary

This paper addresses the challenge of rapid aerial target classification and intent prediction in high-stakes combat environments where full time-series data is unavailable. The authors propose an evidential reasoning framework that aggregates predictions from short sequential sub-samples to manage uncertainty, allowing for timely decision-making. By combining belief propagation with rule-based intent inference, the method effectively handles partial data and reduces false assessments. The approach is evaluated using a custom-generated aerial target dataset, outperforming the need for long-duration data requirements in traditional models.

## Key Contributions

- Introduces an integrated classification and intent prediction approach that processes short sequential sub-samples for rapid response in combat scenarios.
- Implements an evidential reasoning framework to propagate beliefs and manage uncertainty from partial time-series data.
- Demonstrates the method's effectiveness on a custom aerial target dataset, achieving 88% accuracy for target classification and 93% for intent prediction.

## Open Questions & Future Work

- [[multi-target-deception-inference]]
- [[online-learning-threat-adaptation]]

## Key Concepts

- [[evidential-reasoning-framework]]: A belief-propagation-based framework for combining classifier outputs across temporal sub-samples to manage uncertainty under partial observation.

## Archivist Review

I approved the Evidential Reasoning Framework concept as it provides a generalizable, non-Bayesian approach for uncertainty aggregation in time-series classification. I also approved two open questions concerning multi-target/deceptive inference and online learning for adaptation, as these address significant bottlenecks in the reliability of tactical AI systems. No datasets were approved as the custom dataset mentioned lacks a formal name and independent utility beyond this specific case study.

### Approved Concepts
- Evidential Reasoning Framework: It provides a principled mechanism for uncertainty-aware aggregation of sequential sub-sample predictions, which is critical for high-stakes, short-duration time series classification.

### Approved Open Questions
- Multi-Target and Deceptive Inference: Generalizing these systems to multi-target and deceptive scenarios is essential for operational relevance, as real-world aerial combat rarely involves isolated, non-deceptive targets.
- Online Learning for Adaptation: Static models are prone to performance degradation when encountering environmental shifts or non-stationary threat tactics, making online adaptation a key requirement for long-term reliability.

## Links

- [Abstract](https://arxiv.org/abs/2607.14606)
- [PDF](https://arxiv.org/pdf/2607.14606)

