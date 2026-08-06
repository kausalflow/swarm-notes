---
# CSL-compatible fields
title: "Leveraging AI for fine-grained food safety risk forecasting in sparse data conditions"
author:
  - literal: "Dongqi Wang"
  - literal: "Weiwei Chen"
  - literal: "Han Zhou"
  - literal: "Weihua Zhou"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.01767"

# Custom fields
paper_id: "2608.01767"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
  - "pre-training"
  - "semi-supervised-learning"
  - "robustness"
  - "evaluation"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:32:09Z"
created_at: "2026-08-06T07:32:09Z"
---

# Leveraging AI for fine-grained food safety risk forecasting in sparse data conditions

**Authors**: Dongqi Wang, Weiwei Chen, Han Zhou, Weihua Zhou
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.01767](https://arxiv.org/abs/2608.01767)

## Summary

This paper proposes a Transformer-based framework for forecasting fine-grained, city-level food safety risks under sparse data conditions by integrating over 11 million inspection records with supplemental socioeconomic and environmental indicators. To address data scarcity, the authors introduce a three-stage pretraining design leveraging Wilson interval partial supervision and semi-supervised label refinement. Evaluations against baselines and a real-world field experiment with the Zhejiang Provincial Administration for Market Regulation confirm significant improvements in threat detection rates and inspection resource allocation efficiency.

## Key Contributions

- Proposes a Transformer-based framework for fine-grained, city-level food safety risk forecasting that integrates over 11 million inspection records with demographic, economic, and environmental indicators.
- Introduces a three-stage pretraining design utilizing partial supervision via the Wilson interval and semi-supervised label refinement to handle sparse regional sampling data.
- Demonstrates superior risk detection performance over baselines and validates the approach via a field experiment with the Zhejiang Provincial Administration for Market Regulation, showing improved inspection efficiency and higher threat detection rates.

## Limitations

Reliance on sparse regional data requires sophisticated semi-supervised label refinement and Wilson interval confidence modeling; inspectors exhibit threshold-based heuristics that may require customized decision-support interfaces.

## Open Questions & Future Work

- [[human-ai-collaboration-threshold-heuristics-food-safety]]

## Archivist Review

Reviewed the candidate open question regarding human-AI decision thresholds, which represents a substantive unresolved methodological and operational challenge in deploying predictive models in regulatory workflows, and approved it while rejecting the paper-local concept.

### Approved Open Questions
- Human-AI Collaboration Threshold Heuristics: Understanding and mitigating human cognitive biases in AI-assisted decision-making is critical for bridging the gap between predictive accuracy and actual operational efficiency in public policy and resource allocation.

### Rejected Candidates
- [concept] Wilson Interval Partial Supervision (`wilson-interval-partial-supervision`) - subcomponent_of_broader_mechanism: Subcomponent of a specific application-level training pipeline rather than a widely reusable general forecasting mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2608.01767)
- [PDF](https://arxiv.org/pdf/2608.01767)

