---
# CSL-compatible fields
title: "Preference Optimization Drives Monoculture in LLM Prediction Markets"
author:
  - literal: "James Begin"
  - literal: "Brendan Gho"
  - literal: "Suman Muppavarapu"
  - literal: "Tyson Tsay"
  - literal: "Atharva Mohan"
  - literal: "Afnan Shaik"
  - literal: "R K Li"
  - literal: "Vasu Sharma"
  - literal: "Archana Vaidheeswaran"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.26583"

# Custom fields
paper_id: "2606.26583"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "alignment"
  - "rlhf"
  - "multi-agent"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "direct-preference-optimization-monoculture"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:16:42Z"
created_at: "2026-06-28T08:16:42Z"
---

# Preference Optimization Drives Monoculture in LLM Prediction Markets

**Authors**: James Begin, Brendan Gho, Suman Muppavarapu, Tyson Tsay, Atharva Mohan, Afnan Shaik, R K Li, Vasu Sharma, Archana Vaidheeswaran
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.26583](https://arxiv.org/abs/2606.26583)

## Summary

This paper investigates the loss of independence among LLM agents in prediction markets when they are aligned using Direct Preference Optimization (DPO). The authors show that DPO creates a monocultural output distribution, resulting in high error correlations that negate the benefits of increasing the number of agents. Experiments across multiple model scales confirm that this behavior is a direct consequence of preference-based alignment rather than a scaling limitation. Finally, the study proposes and validates cross-model diversity as a key intervention to restore collective intelligence in AI-driven markets.

## Key Contributions

- Demonstrates that DPO-aligned LLM agents in prediction markets suffer from severe error correlation (ρ=0.70), collapsing collective forecasting power to only ~1.4 effective agents.
- Provides empirical evidence that preference optimization is the causal driver of this monoculture through controlled ablations across different scales (8B/70B models).
- Evaluates cross-model diversity as a primary mitigation strategy, which significantly reduces pairwise error correlations compared to uniform agent populations.

## Open Questions & Future Work

- [[rlhf-alignment-monoculture-comparison]]
- [[formal-derivation-neff-lmsr]]

## Key Concepts

- [[direct-preference-optimization-monoculture]]: The phenomenon where alignment training via DPO reduces diversity in LLM agent predictions, leading to highly correlated errors and diminished collective forecasting performance.

## Archivist Review

The paper identifies a critical and non-obvious failure mode in multi-agent forecasting where alignment techniques significantly reduce collective intelligence. I approved the core concept of 'Direct Preference Optimization Monoculture' and two open questions that specifically address the scope of alignment-driven correlation and the formal grounding of existing heuristic metrics in prediction markets. No datasets were approved as none were central to the paper's novel claims beyond standard evaluation environments.

### Approved Concepts
- Direct Preference Optimization Monoculture: Identifies a specific failure mode where DPO alignment significantly reduces the effective collective intelligence of multi-agent forecasting systems by inducing correlated error patterns.

### Approved Open Questions
- RLHF vs. DPO Monoculture Impacts: Distinguishing between DPO-specific artifacts and universal alignment side effects is critical for future architecture and training design in agentic multi-model systems.
- Formalizing N_eff in LMSR: Formalizing this relationship would move N_eff from a heuristic proxy to a grounded metric for evaluating the performance and robustness of agentic prediction systems.

## Links

- [Abstract](https://arxiv.org/abs/2606.26583)
- [PDF](https://arxiv.org/pdf/2606.26583)

