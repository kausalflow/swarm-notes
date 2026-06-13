---
# CSL-compatible fields
title: "WorldReasoner: Evaluating Whether Language Model Agents Forecast Events with Valid Reasoning"
author:
  - literal: "Yizhou Chi"
  - literal: "Eric Chamoun"
  - literal: "Zifeng Ding"
  - literal: "Andreas Vlachos"
issued:
  date-parts:
    - [2026, 6, 10]
url: "https://arxiv.org/abs/2606.11816"

# Custom fields
paper_id: "2606.11816"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "reasoning"
  - "agent"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "worldreasoner-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-13T08:16:10Z"
created_at: "2026-06-13T08:16:10Z"
---

# WorldReasoner: Evaluating Whether Language Model Agents Forecast Events with Valid Reasoning

**Authors**: Yizhou Chi, Eric Chamoun, Zifeng Ding, Andreas Vlachos
**Date**: 2026-06-10
**Paper ID**: [openalex:2606.11816](https://arxiv.org/abs/2606.11816)

## Summary

WorldReasoner is a novel evaluation framework designed to assess whether language model agents perform event forecasting with valid, evidence-backed reasoning rather than just memorized facts. By restricting agents to information available before a simulated forecast date and scoring their predictions against post-resolution hindsight event graphs, the framework decomposes performance into outcome, evidence, and reasoning quality. Evaluation across six agent settings reveals that while retrieval is critical for accuracy, bridging the gap between grounded causal evidence and calibrated probability remains a significant challenge for modern LLMs.

## Key Contributions

- Introduced WorldReasoner, an evaluation framework that assesses event forecasting agents across three axes: outcome accuracy, evidence quality, and causal reasoning quality.
- Developed an agentic pipeline for generating 345 temporally valid forecasting tasks, incorporating time-stamped evidence collection and hindsight event graph construction.
- Demonstrated that while causal graph construction enhances key-event recovery, agents frequently struggle to map grounded evidence to well-calibrated outcome probabilities.

## Open Questions & Future Work

- [[calibrated-probability-conversion-bottleneck]]

## Key Concepts

- [[worldreasoner-framework]]: An evaluation framework for temporally valid event forecasting that scores predictions across outcome quality, evidence grounding, and causal reasoning.

## Archivist Review

The paper introduces a significant framework for evaluating agentic forecasting that emphasizes temporal validity and multi-faceted reasoning. The concepts and open questions were approved for their focus on the structural limitations of current LLM agents in mapping grounded evidence to reliable probabilistic output, which is a core concern for future development of reliable forecasting systems. No datasets were approved as the provided information did not establish a specific named public repository or benchmark entity beyond the framework name itself.

### Approved Concepts
- WorldReasoner Framework: It shifts event forecasting evaluation from simple outcome accuracy to multi-dimensional analysis incorporating temporal validity, evidence retrieval, and causal reasoning via hindsight graphs.

### Approved Open Questions
- Calibrated Probability Conversion Bottleneck: This disconnect between grounding and calibration limits the practical reliability of agentic systems in high-stakes forecasting tasks requiring actionable uncertainty estimates.

## Links

- [Abstract](https://arxiv.org/abs/2606.11816)
- [PDF](https://arxiv.org/pdf/2606.11816)

