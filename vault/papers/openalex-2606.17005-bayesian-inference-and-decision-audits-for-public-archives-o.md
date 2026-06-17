---
# CSL-compatible fields
title: "Bayesian Inference and Decision Audits for Public Archives of Frontier AI Evaluations"
author:
  - literal: "Yanan Long"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.17005"

# Custom fields
paper_id: "2606.17005"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "benchmark"
  - "evaluation"
  - "robustness"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "archive-and-adjudication-protocol"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:27:06Z"
created_at: "2026-06-17T09:27:06Z"
---

# Bayesian Inference and Decision Audits for Public Archives of Frontier AI Evaluations

**Authors**: Yanan Long
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.17005](https://arxiv.org/abs/2606.17005)

## Summary

This paper addresses the limitations of treating AI evaluation leaderboards as static, terminal snapshots by modeling the underlying longitudinal data as a selective time series. By framing evaluation archives as a Bayesian inference problem, the author shows that reporting conventions significantly distort perceived progress, leading to divergent interpretations of performance trajectories. The study further introduces a formal audit protocol that reconstructs evaluation histories, enabling the verification of claims and the identification of artifacts resulting from benchmark revisions and observation regimes.

## Key Contributions

- Formulates public AI evaluation archives as a Bayesian inference problem, demonstrating that terminal-only leaderboard snapshots are insufficient for characterizing performance growth.
- Identifies that standard frontier models fail synthetic recovery and uncertainty calibration when benchmark reporting rules and missingness are not accounted for.
- Introduces an archive-and-adjudication protocol that reconstructs evaluation histories to establish verified performance timing boundaries and audit the validity of frontier AI claims.

## Open Questions & Future Work

- [[metadata-requirements-for-longitudinal-agentic-benchmarking]]

## Key Concepts

- [[archive-and-adjudication-protocol]]: A formal protocol that reconstructs evaluation history from sparse leaderboard data to verify performance claims and detect reporting bias.

## Archivist Review

I approved the archive-and-adjudication protocol as it introduces a novel, rigorous methodology for auditing evaluation leaderboards as time series, which is highly reusable as leaderboards become central to frontier claims. The open question regarding metadata requirements addresses a critical, non-boilerplate bottleneck identified by the paper for achieving reproducible, long-term performance tracking of AI agents. Other potential candidates were rejected for being overly tied to specific paper examples or representing standard ML research practices rather than foundational concepts.

### Approved Concepts
- Archive-and-Adjudication Protocol: Provides a structured, formal approach for verifying AI performance claims by treating evaluation leaderboards as longitudinal time series rather than static snapshots, a critical shift for frontier model auditing.

### Approved Open Questions
- Metadata requirements for longitudinal agentic benchmarking: This is critical for moving from terminal snapshots to robust temporal evaluation of agentic systems, as current public archives lack the necessary metadata for reproducible longitudinal frontier analysis.

## Links

- [Abstract](https://arxiv.org/abs/2606.17005)
- [PDF](https://arxiv.org/pdf/2606.17005)

