---
# CSL-compatible fields
title: "Think Fast, Talk Smart: Partitioning Deterministic and Neural Computation for Structured Health Text Generation"
author:
  - literal: "Kai-Chen Cheng"
  - literal: "Haejun Han"
  - literal: "David Sun"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29652"

# Custom fields
paper_id: "2605.29652"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "instruction-tuning"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "think-fast-talk-smart-pipeline"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:11:38Z"
created_at: "2026-05-31T08:11:38Z"
---

# Think Fast, Talk Smart: Partitioning Deterministic and Neural Computation for Structured Health Text Generation

**Authors**: Kai-Chen Cheng, Haejun Han, David Sun
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29652](https://arxiv.org/abs/2605.29652)

## Summary

This paper explores the division of labor between deterministic computation and neural language generation for structured health text tasks. The authors introduce the 'Think Fast, Talk Smart' pipeline, which delegates recurring analysis and fact verification to deterministic code while limiting the LLM to a bounded, final-writer role. Empirical results across multiple models and sleep-health datasets demonstrate that this approach consistently outperforms traditional end-to-end LLM prompting in faithfulness, cost-efficiency, and policy adherence.

## Key Contributions

- Introduces the 'Think Fast, Talk Smart' pipeline, which separates deterministic analysis from LLM generation to improve faithfulness and lower costs in health text generation.
- Demonstrates that delegating recurring analysis to deterministic code reduces numeric errors and instruction-compliance failures compared to standard zero-shot and few-shot LLM baselines.
- Provides experimental evidence across 280 user-nights and six models showing that even small LLM interventions in deterministic pipelines, such as LLM-based ranking or interface generation, reintroduce failure modes.

## Open Questions & Future Work

- [[complex-clinical-reasoning-partitioning]]

## Key Concepts

- [[think-fast-talk-smart-pipeline]]: A structured generation pipeline that uses deterministic code for recurring analysis and a single bounded LLM call for fluent expression.

## Archivist Review

I approved the core architectural concept of partitioning deterministic and neural generation as it addresses a fundamental trade-off in high-stakes AI deployment. The open question was approved because it addresses a necessary boundary condition for this architecture—the scalability to more complex, less structured reasoning tasks. No datasets were approved as none were identified as uniquely novel or benchmark-standard for broader time-series research.

### Approved Concepts
- Think Fast, Talk Smart Pipeline: Proposes a paradigm for structured generation that strictly partitions deterministic computational logic from LLM language generation to ensure high-fidelity, cost-effective outputs in safety-critical domains.

### Approved Open Questions
- Partitioning for Complex Reasoning: This is critical because the current results are limited to descriptive health reporting; verifying whether the 'code-first' design principle scales to high-stakes clinical decision-making is necessary for determining the scope of this architecture in broader healthcare applications.

## Links

- [Abstract](https://arxiv.org/abs/2605.29652)
- [PDF](https://arxiv.org/pdf/2605.29652)

