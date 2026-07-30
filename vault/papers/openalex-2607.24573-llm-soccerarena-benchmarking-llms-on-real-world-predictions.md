---
# CSL-compatible fields
title: "LLM-SoccerArena: Benchmarking LLMs on Real-World Predictions in Sports"
author:
  - literal: "J. Schröder"
  - literal: "Jonas Schweisthal"
  - literal: "Oliver Müller"
  - literal: "Markus Weinmann"
  - literal: "Stefan Feuerriegel"
issued:
  date-parts:
    - [2026, 7, 27]
url: "https://arxiv.org/abs/2607.24573"

# Custom fields
paper_id: "2607.24573"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "benchmark"
  - "evaluation"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-30T07:26:51Z"
created_at: "2026-07-30T07:26:51Z"
---

# LLM-SoccerArena: Benchmarking LLMs on Real-World Predictions in Sports

**Authors**: J. Schröder, Jonas Schweisthal, Oliver Müller, Markus Weinmann, Stefan Feuerriegel
**Date**: 2026-07-27
**Paper ID**: [openalex:2607.24573](https://arxiv.org/abs/2607.24573)

## Summary

LLM-SoccerArena is introduced as a prospective live benchmarking platform to evaluate how large language models forecast real-world sports events under uncertainty. Using a factorial design varying model versions, information access, prompting strategies, and forecast horizons, the authors evaluate seven LLMs across 104 matches and tournament questions during the 2026 FIFA World Cup. The results show that live benchmarking provides novel empirical insights into model performance, such as finding that web access yields only marginal improvements in Brier score.

## Key Contributions

- Introduces LLM-SoccerArena, a prospective live benchmark that evaluates LLM forecasting of real-world sports events before outcomes are known.
- Provides a factorial benchmark design varying model versions, information access, prompting strategies, and forecast horizons.
- Demonstrates the benchmark via a large-scale evaluation of the 2026 FIFA World Cup across 104 matches and 15 tournament questions.

## Limitations

Evaluations are currently focused on soccer tournaments; further validation across other domains is needed.

## Open Questions & Future Work

- [[prospective-llm-forecasting-architectures-and-leagues]]

## Archivist Review

Approved the open question on prospective LLM forecasting architectures and leagues as it addresses unresolved bottlenecks in real-time benchmark evaluation and dynamic information synthesis. Rejected local benchmark datasets and non-reusable application-specific components.

### Approved Open Questions
- Prospective Forecasting Architectures and Leagues: Extending live prospective benchmarks across diverse sports leagues and refining agentic tool use and prompting strategies are crucial for understanding the limits and robustness of LLM-based forecasting in dynamic real-world environments.

### Rejected Candidates
- [dataset] LLM-SoccerArena (`llm-soccerarena`) - paper_local: Domain-specific benchmarking platform / evaluation framework rather than a general standardized open ML dataset or reusable benchmark archive.

## Links

- [Abstract](https://arxiv.org/abs/2607.24573)
- [PDF](https://arxiv.org/pdf/2607.24573)

