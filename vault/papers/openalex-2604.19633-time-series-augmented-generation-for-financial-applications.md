---
# CSL-compatible fields
title: "Time Series Augmented Generation for Financial Applications"
author:
  - literal: "Anton Kolonin"
  - literal: "Alexey Glushchenko"
  - literal: "Evgeny Bochkov"
  - literal: "Abhishek Saxena"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2604.19633"

# Custom fields
paper_id: "2604.19633"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "language-model"
  - "agent"
  - "tool-use"
  - "time-series"
  - "benchmark"
  - "evaluation"
  - "finance"
architectures:
  []
datasets:
  []
concept_slugs:
  - "time-series-augmented-generation-tsag"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T06:59:14Z"
created_at: "2026-04-24T06:59:14Z"
---

# Time Series Augmented Generation for Financial Applications

**Authors**: Anton Kolonin, Alexey Glushchenko, Evgeny Bochkov, Abhishek Saxena
**Date**: 2026-04-21
**Paper ID**: [openalex:2604.19633](https://arxiv.org/abs/2604.19633)

## Summary

This paper addresses the challenge of evaluating LLM agent reasoning in quantitative financial tasks by introducing the Time Series Augmented Generation (TSAG) framework. TSAG enables LLMs to delegate complex financial calculations to verifiable external tools, thereby increasing reliability and reducing hallucinations. The authors provide a new benchmark of 100 financial questions to measure tool-use accuracy and faithfulness, offering empirical insights into the performance of state-of-the-art models in this domain.

## Key Contributions

- Introduces Time Series Augmented Generation (TSAG), an LLM agent framework for delegating quantitative financial analysis to external tools.
- Proposes a specialized benchmark with 100 financial questions focused on isolating reasoning capabilities and tool orchestration accuracy.
- Evaluates multiple SOTA agents (e.g., GPT-4o, Llama 3) to establish baseline performance on tool selection accuracy, faithfulness, and hallucination in financial contexts.

## Open Questions & Future Work

- [[multi-step-reasoning-in-financial-agents]]
- [[linguistic-robustness-for-financial-agents]]

## Key Concepts

- [[time-series-augmented-generation-tsag]]: A framework where LLM agents delegate financial time-series computations to verifiable external tools to improve reasoning and reduce hallucinations.

## Archivist Review

The paper proposes a tool-augmented framework for financial analysis. I approved the framework concept as a representative method for hybrid LLM-quantitative systems. I also approved the identified open questions regarding multi-step reasoning and linguistic robustness, as these represent major architectural and evaluation bottlenecks for agentic systems in the time-series domain.

### Approved Concepts
- Time Series Augmented Generation (TSAG): The framework provides a structured approach for integrating LLM reasoning with external tool-based computation for financial time-series analysis.

### Approved Open Questions
- Multi-step financial agent reasoning: Multi-step composition is critical for moving from simple function-calling assistants to autonomous financial research agents.
- Agent linguistic robustness evaluation: Linguistic robustness is a primary requirement for deploying reliable, user-facing AI agents in high-stakes domains like finance.

## Links

- [Abstract](https://arxiv.org/abs/2604.19633)
- [PDF](https://arxiv.org/pdf/2604.19633)

