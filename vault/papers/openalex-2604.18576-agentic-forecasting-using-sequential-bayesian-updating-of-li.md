---
# CSL-compatible fields
title: "Agentic Forecasting using Sequential Bayesian Updating of Linguistic Beliefs"
author:
  - literal: "Kevin Murphy"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2604.18576"

# Custom fields
paper_id: "2604.18576"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "forecasting"
  - "agent"
  - "tool-use"
  - "benchmark"
architectures:
  []
datasets:
  - "forecastbench"
concept_slugs:
  - "bayesian-linguistic-belief-state"
dataset_slugs:
  - "forecastbench"
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:55:46Z"
created_at: "2026-04-23T06:55:46Z"
---

# Agentic Forecasting using Sequential Bayesian Updating of Linguistic Beliefs

**Authors**: Kevin Murphy
**Date**: 2026-04-20
**Paper ID**: [openalex:2604.18576](https://arxiv.org/abs/2604.18576)

## Summary

BLF (Bayesian Linguistic Forecaster) is an agentic system designed for high-accuracy binary forecasting by iteratively updating a structured belief state. Unlike traditional approaches that append all retrieved evidence to the context window, BLF maintains a refined representation containing both numerical probabilities and natural-language summaries. The system further enhances performance through hierarchical multi-trial aggregation and specialized calibration techniques. Evaluations on 400 questions from the ForecastBench benchmark demonstrate that BLF outperforms leading models, with ablation studies highlighting the critical roles of its structured memory and rigorous calibration.

## Key Contributions

- Introduces BLF, an agentic forecasting system achieving SOTA performance on the ForecastBench benchmark.
- Proposes a Bayesian linguistic belief state that optimizes evidence processing by replacing exhaustive context concatenation with iterative belief updates.
- Develops a robust backtesting framework with <1.5% leakage and implements hierarchical calibration and shrinkage aggregation to improve prediction reliability.

## Open Questions & Future Work

- [[automated-forecasting-meta-controllers]]
- [[multi-format-agentic-forecasting]]

## Key Concepts

- [[bayesian-linguistic-belief-state]]: A semi-structured framework that maintains and iteratively updates numerical probabilities and natural-language evidence summaries for forecasting.

## Archivist Review

The approval focuses on the 'Bayesian Linguistic Belief State' as a novel approach to evidence management in agents. The approved open questions reflect significant architectural hurdles in automating agent policy and generalizing outcome support beyond binary classification. Standard statistical ensembling/calibration techniques were rejected as they are not novel to this specific paper.

### Approved Concepts
- Bayesian Linguistic Belief State: Addresses the bottleneck of growing context windows in agentic forecasting by formalizing a persistent, compact state for reasoning.

### Approved Open Questions
- Automated forecasting meta-controllers: Automating tool selection is critical for scaling agentic systems beyond manual, prompt-engineered pipelines.
- Generalizing forecasting outcome formats: Moving toward multi-format forecasting is necessary for practical deployment in real-world policy and economic decision-making.

### Rejected Candidates
- [concept] Hierarchical multi-trial aggregation (`hierarchical-multi-trial-aggregation`) - subcomponent_of_broader_mechanism: This is a specific ensembling strategy and not a fundamental architectural concept likely to be reused as a standalone entity.
- [concept] Hierarchical calibration (`hierarchical-calibration`) - not_novel: Platt scaling and hierarchical priors are established statistical techniques; applying them to forecasting does not constitute a new, reusable architectural concept.

## Datasets

- [[forecastbench]]

## Links

- [Abstract](https://arxiv.org/abs/2604.18576)
- [PDF](https://arxiv.org/pdf/2604.18576)

