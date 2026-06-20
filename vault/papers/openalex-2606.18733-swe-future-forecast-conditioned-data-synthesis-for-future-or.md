---
# CSL-compatible fields
title: "SWE-Future: Forecast-Conditioned Data Synthesis for Future-Oriented Software Engineering Agents"
author:
  - literal: "Qiao Zhao"
  - literal: "JianYing Qu"
  - literal: "Jun Zhang"
  - literal: "Yehua Yang"
  - literal: "Hanwen Du"
  - literal: "Zhongkai Sun"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.18733"

# Custom fields
paper_id: "2606.18733"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "code-generation"
  - "benchmark"
  - "autonomous-agent"
architectures:
  []
datasets:
  []
concept_slugs:
  - "forecast-conditioned-data-synthesis"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:18:15Z"
created_at: "2026-06-20T08:18:15Z"
---

# SWE-Future: Forecast-Conditioned Data Synthesis for Future-Oriented Software Engineering Agents

**Authors**: Qiao Zhao, JianYing Qu, Jun Zhang, Yehua Yang, Hanwen Du, Zhongkai Sun
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.18733](https://arxiv.org/abs/2606.18733)

## Summary

SWE-Future addresses data contamination in coding-agent benchmarks by generating future-oriented tasks based on repository-evolution forecasts rather than historical replay. The method uses repository data up to a snapshot time to predict upcoming feature, bugfix, and refactoring needs, which are then used as signals for synthetic task creation. Retrospective validation confirms the forecasting accuracy, demonstrating that these generated tasks align closely with real repository evolution while avoiding pre-training data overlap.

## Key Contributions

- Introduces SWE-Future, a forecast-conditioned data synthesis approach that generates realistic coding tasks without replaying historical pull requests.
- Validates the forecasting methodology retrospectively across 80 repositories, achieving 58.1% relevance to future-work semantic task families.
- Provides a 200-task coding-agent benchmark derived from repository-evolution signals rather than direct history leakage.

## Open Questions & Future Work

- [[improving-forecast-conditioned-synthesis]]

## Key Concepts

- [[forecast-conditioned-data-synthesis]]: A data generation methodology for software engineering benchmarks that synthesizes future tasks based on predicted repository evolution.

## Archivist Review

I have approved 'Forecast-Conditioned Data Synthesis' as a concept because it represents a reusable methodological innovation for generating uncontaminated benchmarks. The open question 'Improving Forecast-Conditioned Data Synthesis' was approved to capture the significant research challenges remaining in refining repository-evolution forecasting and synthetic test fidelity. Other specific implementation labels were rejected to maintain the high-level focus of the vault.

### Approved Concepts
- Forecast-Conditioned Data Synthesis: It provides a methodological framework to generate synthetic benchmarks that avoid historical data contamination by relying on predictive repository-evolution signals rather than direct replay.

### Approved Open Questions
- Improving Forecast-Conditioned Data Synthesis: The reliability of coding-agent benchmarks depends on their ability to simulate authentic future project needs without replaying known historical pull requests.

### Rejected Candidates
- [concept] SWE-Future (`swe-future`) - subcomponent_of_broader_mechanism: This is a specific implementation of the more general concept 'Forecast-Conditioned Data Synthesis', which I have approved instead.

## Links

- [Abstract](https://arxiv.org/abs/2606.18733)
- [PDF](https://arxiv.org/pdf/2606.18733)

