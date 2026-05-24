---
# CSL-compatible fields
title: "Evolutionary Multi-Task Optimization for LLM-Guided Program Discovery"
author:
  - literal: "Halil Alperen Gozeten"
  - literal: "Xuechen Zhang"
  - literal: "Emrullah Ildız"
  - literal: "Ege Onur Taga"
  - literal: "Tara Javidi"
  - literal: "Samet Oymak"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22613"

# Custom fields
paper_id: "2605.22613"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "program-synthesis"
  - "evolutionary-algorithm"
  - "multi-task-learning"
  - "generalization"
architectures:
  []
datasets:
  - "arc"
concept_slugs:
  - "emo-sta-shared-then-adapt"
dataset_slugs:
  - "arc"
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:47:55Z"
created_at: "2026-05-24T07:47:55Z"
---

# Evolutionary Multi-Task Optimization for LLM-Guided Program Discovery

**Authors**: Halil Alperen Gozeten, Xuechen Zhang, Emrullah Ildız, Ege Onur Taga, Tara Javidi, Samet Oymak
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22613](https://arxiv.org/abs/2605.22613)

## Summary

This paper addresses the limitations of single-task LLM-guided program discovery by introducing EMO-STA (Shared-Then-Adapt), an evolutionary framework that exploits common structure across task families. EMO-STA employs a two-stage process: evolving a pool of shared candidate programs, followed by targeted adaptation to specific tasks. Empirical results across eight domains demonstrate that EMO-STA achieves superior performance and improved generalization, particularly in data-scarce scenarios, by reducing reliance on task-specific artifacts.

## Key Contributions

- Introduces EMO-STA, a two-stage framework that leverages shared evolutionary archives to improve program discovery efficiency across task families.
- Demonstrates that EMO-STA outperforms matched-compute single-task evolution across diverse domains including continuous optimization and geometric construction.
- Shows that shared evolutionary pressure acts as a regularizer, effectively mitigating overfitting in low-evidence settings like ARC tasks and time-series feature engineering.

## Open Questions & Future Work

- [[automated-multitask-grouping-llm]]

## Key Concepts

- [[emo-sta-shared-then-adapt]]: A two-stage evolutionary framework that evolves a shared archive of programs across a task family before adapting them to individual target tasks.

## Archivist Review

I approved the EMO-STA framework as it represents a robust, reusable paradigm for LLM-guided program search. The open question on automated grouping was approved to address the inherent limitation of current task-family definitions. The ARC dataset was added due to its frequent use in program discovery evaluation.

### Approved Concepts
- EMO-STA (Shared-Then-Adapt): This framework is the primary contribution, formalizing a two-stage approach to multi-task LLM-guided evolutionary program search.

### Approved Open Questions
- Automated Multitask Program Discovery: Addressing this is critical for moving beyond manually curated task families and enabling scalable, general-purpose evolutionary program discovery that can autonomously identify and exploit structural commonalities in arbitrary problem spaces.

## Datasets

- [[arc]]

## Links

- [Abstract](https://arxiv.org/abs/2605.22613)
- [PDF](https://arxiv.org/pdf/2605.22613)

