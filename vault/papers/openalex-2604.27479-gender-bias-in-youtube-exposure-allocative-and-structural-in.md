---
# CSL-compatible fields
title: "Gender Bias in YouTube Exposure: Allocative and Structural Inequalities in Political Information Environments"
author:
  - literal: "Jipeng Tan"
  - literal: "Weifeng Zhang"
  - literal: "Ye Wu"
  - literal: "Jialin Guo"
  - literal: "Yŏng Min"
issued:
  date-parts:
    - [2026, 4, 30]
url: "https://arxiv.org/abs/2604.27479"

# Custom fields
paper_id: "2604.27479"
paper_source: "openalex"
domain: "nlp"
tags:
  - "fairness"
  - "llm"
  - "language-model"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "allocative-and-structural-bias-in-recommendation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-03T07:14:51Z"
created_at: "2026-05-03T07:14:51Z"
---

# Gender Bias in YouTube Exposure: Allocative and Structural Inequalities in Political Information Environments

**Authors**: Jipeng Tan, Weifeng Zhang, Ye Wu, Jialin Guo, Yŏng Min
**Date**: 2026-04-30
**Paper ID**: [openalex:2604.27479](https://arxiv.org/abs/2604.27479)

## Summary

This study investigates gender bias in YouTube's recommendation algorithms through a controlled social-bot field experiment comparing male-coded and female-coded profiles. The authors identify and distinguish between allocative bias, involving disparities in content issue and ideology, and structural bias, which involves disparate network clustering patterns. A collaborative-filtering model is used to confirm that these observed inequalities are inherent to current algorithmic information distribution mechanisms, reinforcing a need for robust algorithmic fairness interventions.

## Key Contributions

- Demonstrates that gender-coded profiles on YouTube receive significantly different political content recommendations, confirming the existence of both allocative and structural bias.
- Identifies that structural bias manifests as distinct, polarized clustering patterns in political information environments that perpetuate over time.
- Validates the emergence of observed systemic gender bias through a collaborative-filtering model reproduction.

## Open Questions & Future Work

- [[impact-of-structural-algorithmic-bias]]

## Key Concepts

- [[allocative-and-structural-bias-in-recommendation]]: A framework for auditing recommendation systems by decomposing algorithmic discrimination into the unequal distribution of content (allocative) and the formation of disparate informational network topologies (structural).

## Archivist Review

I approved the 'Allocative and Structural Bias' concept as a reusable framework for auditing recommendation fairness and a related open question regarding the downstream behavioral effects of such biases. I rejected 'YouTube' as a dataset candidate because it is a general platform, not a specific, controlled research dataset.

### Approved Concepts
- Allocative and Structural Bias in Recommendation: Provides a formal framework for disentangling two distinct, critical dimensions of algorithmic bias in recommender systems beyond simple exposure counts.

### Approved Open Questions
- Consequences of Structural Algorithmic Bias: Understanding the downstream effects of algorithmic structural bias is critical for assessing the actual societal impact of personalized information distribution beyond mere exposure patterns.

### Rejected Candidates
- [dataset] YouTube (`youtube`) - low_impact: YouTube is a massive, general-purpose platform and not a structured research dataset.

## Links

- [Abstract](https://arxiv.org/abs/2604.27479)
- [PDF](https://arxiv.org/pdf/2604.27479)

