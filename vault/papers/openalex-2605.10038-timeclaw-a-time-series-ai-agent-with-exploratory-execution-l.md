---
# CSL-compatible fields
title: "TimeClaw: A Time-Series AI Agent with Exploratory Execution Learning"
author:
  - literal: "Hangchen Liu"
  - literal: "Dongyuan Li"
  - literal: "Renhe Jiang"
  - literal: "Jiewen Deng"
  - literal: "Weiwei Ye"
  - literal: "Yoshihide Sekimoto"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10038"

# Custom fields
paper_id: "2605.10038"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "time-series"
  - "forecasting"
  - "agent"
  - "tool-use"
  - "reasoning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "timeclaw"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:37:14Z"
created_at: "2026-05-14T07:37:14Z"
---

# TimeClaw: A Time-Series AI Agent with Exploratory Execution Learning

**Authors**: Hangchen Liu, Dongyuan Li, Renhe Jiang, Jiewen Deng, Weiwei Ye, Yoshihide Sekimoto
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10038](https://arxiv.org/abs/2605.10038)

## Summary

TimeClaw is an exploratory execution learning framework designed to enhance LLM-based time series agents by distilling trial-and-error experiences into reusable hierarchical knowledge. Unlike standard execution-centric agents, it employs a four-stage loop to refine tool-use procedures and numerical accuracy without requiring online test-time adaptation. The framework prevents tool-prior collapse through task-aware tool dropout and metric-supervised learning, enabling consistent improvements in complex forecasting and reasoning scenarios.

## Key Contributions

- Introduces TimeClaw, an exploratory execution learning framework that utilizes a four-stage loop (Explore, Compare, Distill, and Reinject) to turn agentic experiences into reusable knowledge.
- Implements metric-supervised exploratory execution learning and task-aware tool dropout to prevent tool-prior collapse in numeric time series tasks.
- Demonstrates consistent performance gains over baseline models across 17 finance and weather-related time series forecasting and reasoning tasks.

## Open Questions & Future Work

- [[optimizing-execution-quality-without-differentiable-feedback]]

## Key Concepts

- [[timeclaw]]: An exploratory execution learning framework for time series analysis that distills multi-stage tool-use experiences into reusable hierarchical knowledge.

## Archivist Review

Approved the core TimeClaw framework concept as it introduces a reusable architectural loop for agentic time-series reasoning. The open question regarding optimizing execution quality without differentiable feedback was approved as it directly addresses a central bottleneck in the paper's claimed transition from execution-centric to experience-distilling agents. The exploration/exploitation question was rejected as being too generic to standard reinforcement learning.

### Approved Concepts
- TimeClaw: Introduces a novel framework to improve LLM-based time series reasoning by distilling exploratory experiences into reusable knowledge.

### Approved Open Questions
- Optimizing Execution Quality Without Differentiable Feedback: This is central to the transition from stateless, execution-centric agents to systems capable of long-term improvement through experience, which is currently hindered by the inability to backpropagate through discrete tool-use branches.

### Rejected Candidates
- [open_question] Automated Balance of Exploration and Exploitation in Agents (`automated-balance-of-exploration-and-exploitation-in-agents`) - generic: While important, this is a general RL/agent bottleneck rather than being specific to the time-series forecasting domain or the structural advancements introduced by this paper.

## Links

- [Abstract](https://arxiv.org/abs/2605.10038)
- [PDF](https://arxiv.org/pdf/2605.10038)

