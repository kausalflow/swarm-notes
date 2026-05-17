---
# CSL-compatible fields
title: "What if Tomorrow is the World Cup Final? Counterfactual Time Series Forecasting with Textual Conditions"
author:
  - literal: "Shuqi Gu"
  - literal: "Yongxiang Zhao"
  - literal: "Baoyu Jing"
  - literal: "Kan Ren"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14422"

# Custom fields
paper_id: "2605.14422"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "llm"
architectures:
  []
datasets:
  []
concept_slugs:
  - "counterfactual-time-series-forecasting"
  - "text-attribution-mechanism"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:30:02Z"
created_at: "2026-05-17T07:30:02Z"
---

# What if Tomorrow is the World Cup Final? Counterfactual Time Series Forecasting with Textual Conditions

**Authors**: Shuqi Gu, Yongxiang Zhao, Baoyu Jing, Kan Ren
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14422](https://arxiv.org/abs/2605.14422)

## Summary

This paper addresses the challenge of adapting time series forecasting to complex, non-structured future conditions represented as text. The authors define the task of counterfactual time series forecasting, allowing models to predict sequences under hypothetical scenarios. To support this, they propose a text-attribution mechanism that explicitly differentiates between mutable and immutable factors in textual inputs, enhancing robustness. A novel evaluation framework is also provided to assess performance when ground truth data is absent, a common challenge in counterfactual forecasting.

## Key Contributions

- Introduces the task of counterfactual time series forecasting conditioned on natural language inputs.
- Develops a comprehensive evaluation framework for both factual and counterfactual time series forecasting scenarios.
- Introduces a text-attribution mechanism that improves forecasting by disentangling mutable and immutable influences from textual conditions.

## Open Questions & Future Work

- [[counterfactual-forecasting-evaluation-limitations]]

## Key Concepts

- [[counterfactual-time-series-forecasting]]: The task of generating future time series predictions conditioned on hypothetical textual descriptions of future events.
- [[text-attribution-mechanism]]: A conditioning module that separates immutable contextual facts from mutable event-driven inputs to refine time-series forecasts.

## Archivist Review

I approved the core task of counterfactual time series forecasting and the specific text-attribution mechanism as they provide a foundational approach for incorporating unstructured textual events into forecasting. The open question regarding counterfactual evaluation is highly relevant as it addresses a significant technical bottleneck in moving away from simple factual ground-truth benchmarks. I did not approve any datasets as none were explicitly identified as unique or reusable benchmarks within the provided analysis.

### Approved Concepts
- Counterfactual Time Series Forecasting: Moves beyond standard historical forecasting to allow predictive modeling under hypothetical, text-defined future scenarios.
- Text-Attribution Mechanism (Forecasting): Provides a method for disentangling static context (immutable) from dynamic scenario-specific triggers (mutable) in textual conditions.

### Approved Open Questions
- Evaluating Counterfactual Forecasting Quality: This is a central bottleneck in counterfactual forecasting; without reliable ways to evaluate performance when ground truth is absent, it is difficult to systematically improve model reliability for real-world decision-making.

## Links

- [Abstract](https://arxiv.org/abs/2605.14422)
- [PDF](https://arxiv.org/pdf/2605.14422)

