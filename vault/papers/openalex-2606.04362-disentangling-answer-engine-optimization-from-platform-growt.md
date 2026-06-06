---
# CSL-compatible fields
title: "Disentangling Answer Engine Optimization from Platform Growth: A Log-Based Natural Experiment on ChatGPT Referral Traffic"
author:
  - literal: "Keisuke Watanabe"
  - literal: "Kazuki Nakayashiki"
issued:
  date-parts:
    - [2026, 6, 3]
url: "https://arxiv.org/abs/2606.04362"

# Custom fields
paper_id: "2606.04362"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "nlp"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-06T07:41:02Z"
created_at: "2026-06-06T07:41:02Z"
---

# Disentangling Answer Engine Optimization from Platform Growth: A Log-Based Natural Experiment on ChatGPT Referral Traffic

**Authors**: Keisuke Watanabe, Kazuki Nakayashiki
**Date**: 2026-06-03
**Paper ID**: [openalex:2606.04362](https://arxiv.org/abs/2606.04362)

## Summary

This study investigates the causal effectiveness of Answer Engine Optimization (AEO) by decoupling it from the rapid platform growth of LLM-based answer engines like ChatGPT. Using a longitudinal field study on the glasp.co domain, the authors deploy an on-domain control design to separate intervention effects from systemic referral traffic increases. The analysis reveals that while raw referral growth is primarily driven by platform tailwinds, AEO interventions still yield a notable level increase in traffic, though headline success stories likely overstate their impact. The findings emphasize the need for rigorous causal methodologies in assessing search-related optimizations in the age of generative AI.

## Key Contributions

- Demonstrates that raw growth metrics for Answer Engine Optimization (AEO) are heavily confounded by the underlying platform growth of answer engines.
- Introduces a rigorous on-domain control methodology to isolate the causal impact of AEO interventions from platform-level traffic tailwinds.
- Finds that while AEO interventions can yield a statistically suggestive 1.82x traffic lift, raw headline growth multiples significantly overestimate the actual intervention effect.

## Open Questions & Future Work

- [[randomized-aeo-impact-assessment]]

## Archivist Review

I reviewed the paper's proposal to formalize 'Answer Engine Optimization' and the 'On-Domain Control' technique. I rejected both as concepts because the former is an industry term and the latter is a well-established quasi-experimental design principle. I approved the open question regarding randomized assessment as it addresses a core methodological bottleneck in measuring causal effects for generative-AI-driven traffic.

### Approved Open Questions
- Randomized AEO Impact Assessment: Transitioning to RCTs is essential to disentangle the causal efficacy of specific content optimization techniques from noise and platform growth, which currently threatens the validity of most AEO performance metrics.

### Rejected Candidates
- [concept] Answer Engine Optimization (AEO) (`answer-engine-optimization-aeo`) - generic: AEO is a descriptive industry term rather than a formal technical mechanism or research concept.
- [concept] On-Domain Control Methodology (`on-domain-control-methodology`) - not_novel: This is a standard application of the control-group/quasi-experimental design pattern, which is already a well-established methodological tool.

## Links

- [Abstract](https://arxiv.org/abs/2606.04362)
- [PDF](https://arxiv.org/pdf/2606.04362)

