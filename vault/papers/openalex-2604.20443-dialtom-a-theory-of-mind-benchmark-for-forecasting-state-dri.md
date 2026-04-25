---
# CSL-compatible fields
title: "DialToM: A Theory of Mind Benchmark for Forecasting State-Driven Dialogue Trajectories"
author:
  - literal: "Neemesh Yadav"
  - literal: "Palakorn Achananuparp"
  - literal: "Jing Jiang"
  - literal: "Ee‐Peng Lim"
issued:
  date-parts:
    - [2026, 4, 22]
url: "https://arxiv.org/abs/2604.20443"

# Custom fields
paper_id: "2604.20443"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "benchmark"
  - "reasoning"
  - "evaluation"
architectures:
  []
datasets:
  - "dialtom"
concept_slugs:
  - "prospective-diagnostic-forecasting"
dataset_slugs:
  - "dialtom"
skill: "TimeSeriesSkill"
processed_at: "2026-04-25T06:15:27Z"
created_at: "2026-04-25T06:15:27Z"
---

# DialToM: A Theory of Mind Benchmark for Forecasting State-Driven Dialogue Trajectories

**Authors**: Neemesh Yadav, Palakorn Achananuparp, Jing Jiang, Ee‐Peng Lim
**Date**: 2026-04-22
**Paper ID**: [openalex:2604.20443](https://arxiv.org/abs/2604.20443)

## Summary

DialToM evaluates LLM Theory of Mind (ToM) capabilities by moving beyond literal mental state prediction to Prospective Diagnostic Forecasting. The benchmark tests whether models can predict state-consistent dialogue trajectories based on inferred mental-state profiles. Findings show that while models exhibit competence in literal ToM, most struggle to apply this information effectively to forecast complex social interactions, suggesting a reliance on spurious correlations rather than robust functional reasoning.

## Key Contributions

- Introduced DialToM, a human-verified benchmark for assessing Theory of Mind in LLMs via Prospective Diagnostic Forecasting.
- Demonstrated a reasoning asymmetry where LLMs identify mental states but fail to utilize them for accurate dialogue trajectory forecasting.
- Established that LLM-generated inferences show weak semantic similarity to human-grounded mental state attributions.

## Open Questions & Future Work

- [[llm-functional-tom-asymmetry]]

## Key Concepts

- [[prospective-diagnostic-forecasting]]: A diagnostic evaluation procedure that tests whether an agent can forecast trajectory outcomes based on inferred latent mental-state profiles.

## Archivist Review

I approved Prospective Diagnostic Forecasting as it captures the novel method proposed by the paper—evaluating trajectory consistency based on latent mental states—which is a broadly applicable mechanism for sequence forecasting. I also approved the dataset DialToM and the identified reasoning asymmetry as a critical research bottleneck in the field of LLM agent reasoning. I rejected the concept 'DialToM' to avoid redundancy, as the dataset itself is now recorded.

### Approved Concepts
- Prospective Diagnostic Forecasting: It provides a formal mechanism for testing whether inferred states have predictive power for future trajectories, moving beyond static classification of mental states.

### Approved Open Questions
- Functional vs. Literal ToM Gap: Understanding this gap is essential for determining if agents can reliably use internal state models to navigate social or complex sequential environments.

### Rejected Candidates
- [concept] DialToM (`dialtom`) - duplicate_existing: The concept describes the benchmark itself, which is already approved as a dataset; the novel method is the forecasting procedure, which is better captured by the Prospective Diagnostic Forecasting concept.

## Datasets

- [[dialtom]]

## Links

- [Abstract](https://arxiv.org/abs/2604.20443)
- [PDF](https://arxiv.org/pdf/2604.20443)

