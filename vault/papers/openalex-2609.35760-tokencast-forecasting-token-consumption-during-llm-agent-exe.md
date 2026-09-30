---
# CSL-compatible fields
title: "TokenCast: Forecasting Token Consumption During LLM Agent Execution"
author:
  - literal: "Chaoqian Ouyang"
  - literal: "Ling Yue"
  - literal: "Libin Zheng"
  - literal: "Huanghui Guo"
  - literal: "S Xu"
  - literal: "Yishu Wang"
  - literal: "Ran Li"
  - literal: "Jian Yin"
  - literal: "Shaowu Pan"
  - literal: "Shimin Di"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.35760"

# Custom fields
paper_id: "2609.35760"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "agent"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  - "swe-bench Verified"
concept_slugs:
  []
dataset_slugs:
  - "swe-bench-verified"
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:50:45Z"
created_at: "2026-09-30T10:50:45Z"
---

# TokenCast: Forecasting Token Consumption During LLM Agent Execution

**Authors**: Chaoqian Ouyang, Ling Yue, Libin Zheng, Huanghui Guo, S Xu, Yishu Wang, Ran Li, Jian Yin, Shaowu Pan, Shimin Di
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.35760](https://arxiv.org/abs/2609.35760)

## Summary

TokenCast is a forecasting framework designed to predict token consumption during the execution of large language model (LLM) agents, where context growth and tool feedback cause significant variance across runs. By learning composable cost representations for execution segments, TokenCast models cumulative input costs and context inflation without incurring extra LLM calls. Evaluated across multiple task suites and agent models, TokenCast significantly improves prediction accuracy over existing baselines and enables efficient budget control.

## Key Contributions

- Proposes TokenCast, a composable cost representation framework for forecasting token consumption during LLM agent execution without requiring additional LLM calls.
- Achieves an average 14.5% reduction in mean absolute error against the strongest comparators across 4 task suites and 6 agent models over 96 evaluated combinations.
- Demonstrates in offline budget-control replay that TokenCast consumes 21.3% fewer tokens on average than a fixed-budget policy while maintaining matched trace completion.

## Open Questions & Future Work

- [[runtime-budget-managed-agent-execution]]

## Archivist Review

Strictly adhered to scarcity guidelines by approving only the primary benchmark dataset and the explicit future work direction on runtime budget management, while rejecting the paper-specific framework name as a concept to keep the knowledge vault clean and generalizable.

### Approved Open Questions
- Runtime Budget-Managed Agent Execution: Transitioning from passive token consumption forecasting and offline budget replay to online, real-time agent execution steering is crucial for practical deployment in cost-sensitive production environments.

### Rejected Candidates
- [concept] TokenCast (`tokencast`) - low_impact: TokenCast is the name of the paper's overarching application framework/system rather than a standalone generalizable forecasting method or architecture component.

## Datasets

- [[swe-bench-verified]]

## Links

- [Abstract](https://arxiv.org/abs/2609.35760)
- [PDF](https://arxiv.org/pdf/2609.35760)

