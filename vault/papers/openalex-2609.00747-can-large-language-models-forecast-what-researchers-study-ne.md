---
# CSL-compatible fields
title: "Can Large Language Models Forecast What Researchers Study Next?"
author:
  - literal: "Fenghai Li"
  - literal: "Zihan Tang"
  - literal: "Haofei Yu"
  - literal: "Yining Zhao"
  - literal: "Jiaxuan You"
issued:
  date-parts:
    - [2026, 9, 1]
url: "https://arxiv.org/abs/2609.00747"

# Custom fields
paper_id: "2609.00747"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "benchmark"
  - "evaluation"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-04T09:11:02Z"
created_at: "2026-09-04T09:11:02Z"
---

# Can Large Language Models Forecast What Researchers Study Next?

**Authors**: Fenghai Li, Zihan Tang, Haofei Yu, Yining Zhao, Jiaxuan You
**Date**: 2026-09-01
**Paper ID**: [openalex:2609.00747](https://arxiv.org/abs/2609.00747)

## Summary

This paper introduces IdeaForecastBench, a benchmark designed to evaluate whether large language models and forecasting systems can accurately predict the research ideas a scientific community will subsequently pursue. Spanning 624 rolling episodes across 52 topics, the benchmark evaluates multiple history-compression strategies across prominent LLMs and a learned Mode-Decomposition Forecaster (MDF). Findings indicate that summary-based history compression enhances forecasting metrics like Hit@5 and Precision@5, while uncovering distinct performance patterns among different model families.

## Key Contributions

- Introduces IdeaForecastBench, a benchmark comprising 624 rolling episodes across 52 topics to evaluate whether computational systems can forecast future research topics.
- Compares five history-compression strategies across multiple backbones (GPT-4.1, Qwen2.5, Qwen3.5) alongside a learned Mode-Decomposition Forecaster (MDF).
- Demonstrates that summary-based history compression improves Hit@5 and Precision@5 over direct prompting across all backbones, while revealing nuanced performance differences among models.

## Limitations

The work highlights that outcome-blind assessments show broader forecasts by certain models, but the precise contribution of breadth remains undetermined, and realizing an idea does not always mean precise anticipation.

## Open Questions & Future Work

- [[disentangling-breadth-from-anticipation-in-research-forecasting]]

## Archivist Review

We strictly adhere to the scarcity and relevance policies. The proposed concept 'IdeaForecastBench' is a benchmark/evaluation framework and is more appropriately handled via the open question regarding forecast breadth and anticipation, which captures the core methodological bottleneck of evaluating research forecasting systems.

### Approved Open Questions
- Disentangling Breadth from Anticipation in Forecasting: This question is crucial for advancing scientific forecasting benchmarks, as it addresses the fundamental validity of realization metrics and prevents models from gaming evaluation systems through overly broad or trivial statements.

### Rejected Candidates
- [concept] IdeaForecastBench (`ideaforecastbench`) - low_impact: Benchmarks and evaluation testbeds are better tracked as tasks or open questions unless they introduce a standalone algorithmic concept.

## Links

- [Abstract](https://arxiv.org/abs/2609.00747)
- [PDF](https://arxiv.org/pdf/2609.00747)

