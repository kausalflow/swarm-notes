---
# CSL-compatible fields
title: "Will Scaling Improve Social Simulation with LLMs?"
author:
  - literal: "Caleb Ziems"
  - literal: "William Held"
  - literal: "Su Doga Karaca"
  - literal: "David Grusky"
  - literal: "Tatsunori Hashimoto"
  - literal: "D Yang"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.02464"

# Custom fields
paper_id: "2607.02464"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "scaling-law"
  - "benchmark"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "social-simulation-fidelity-scaling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:53:12Z"
created_at: "2026-07-05T07:53:12Z"
---

# Will Scaling Improve Social Simulation with LLMs?

**Authors**: Caleb Ziems, William Held, Su Doga Karaca, David Grusky, Tatsunori Hashimoto, D Yang
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.02464](https://arxiv.org/abs/2607.02464)

## Summary

This paper investigates whether the scaling paradigm in language modeling enhances the fidelity of LLM-based social simulations. Through experiments with 85 models across fixed-compute budgets, the authors find that while most simulation tasks scale well with compute, specific sub-domains like longitudinal forecasting and tasks involving underrepresented opinions show slower improvements. Furthermore, the study identifies that scaling does not inherently resolve failures in calibrating model behavior with human cognitive biases, suggesting that simulation fidelity is not always a byproduct of general capability scaling.

## Key Contributions

- Demonstrates that social simulation performance in opinion modeling, behavioral simulation, and longitudinal forecasting exhibits strong compute scaling laws.
- Identifies that longitudinal forecasting and underrepresented opinion modeling scale significantly slower than general knowledge tasks.
- Reveals that scaling LLMs fails to improve model calibration with specific human cognitive biases like risk aversion and heuristic-based reward learning.

## Open Questions & Future Work

- [[social-simulation-fidelity-underrepresented-populations]]
- [[limitations-behavioral-simulation-scaling]]

## Key Concepts

- [[social-simulation-fidelity-scaling]]: A framework for analyzing the relationship between LLM compute scale and social simulation fidelity.

## Archivist Review

The concepts and open questions were approved because they define the limits of the current LLM scaling paradigm when applied to specialized social and behavioral science tasks. These items provide a reusable taxonomy for researchers to distinguish between tasks that scale well and those where simulation fidelity remains an unresolved architectural or data-driven bottleneck. No datasets were approved as none provided a unique, stable, or standalone contribution beyond typical web corpora.

### Approved Concepts
- Social Simulation Fidelity Scaling: Establishes the extent to which simulation accuracy is a function of compute vs. domain-specific properties, providing a framework for future research.

### Approved Open Questions
- Scaling Fidelity for Underrepresented Populations: Critical for ensuring that social simulations do not exacerbate existing societal biases or representational gaps.
- Scaling Behavioral Simulation Bottlenecks: Essential for determining the limits of LLMs as faithful simulators of complex human cognition and behavioral patterns.

## Links

- [Abstract](https://arxiv.org/abs/2607.02464)
- [PDF](https://arxiv.org/pdf/2607.02464)

