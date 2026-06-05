---
# CSL-compatible fields
title: "Validation-Gated Multi-Agent Governance for Online Adaptation of Thermal-Hydraulic Surrogate Models under Operating-Regime Shift"
author:
  - literal: "Doyeong Lim"
  - literal: "Seungyoon Lee"
  - literal: "In Cheol Bang"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2606.03321"

# Custom fields
paper_id: "2606.03321"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multi-agent"
  - "fourier-neural-operator"
  - "transformer"
  - "graph-neural-network"
  - "governance"
architectures:
  []
datasets:
  []
concept_slugs:
  - "validation-gated-multi-agent-governance"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:39:31Z"
created_at: "2026-06-05T08:39:31Z"
---

# Validation-Gated Multi-Agent Governance for Online Adaptation of Thermal-Hydraulic Surrogate Models under Operating-Regime Shift

**Authors**: Doyeong Lim, Seungyoon Lee, In Cheol Bang
**Date**: 2026-06-02
**Paper ID**: [openalex:2606.03321](https://arxiv.org/abs/2606.03321)

## Summary

This paper presents a multi-agent governance framework designed to maintain the accuracy of thermal-hydraulic surrogate models during online operating-regime shifts. By employing role-separated agents and deterministic champion-challenger gates, the system enables continuous, auditable model adaptation while preventing erratic updates in safety-critical deployments. Evaluation on experimental thermal-hydraulic loop data demonstrates that this approach significantly outperforms both static models and naive shadow learning, achieving a 19% reduction in forecast error. The method successfully transitions between different architectures, such as Fourier neural operators and Transformers, ensuring model relevance over time.

## Key Contributions

- Introduces a validation-gated multi-agent governance framework for online surrogate model adaptation in thermal-hydraulic systems.
- Demonstrates that the proposed MA-Full adaptation mode reduces forecasting MAE by 19.0% and warning-exceedance ratios by 21 percentage points compared to static models.
- Shows that deterministic champion-challenger gates enable safe, auditable model promotions between disparate architectures like Fourier neural operators, Transformers, and GNNs.

## Open Questions & Future Work

- [[safe-online-surrogate-governance]]

## Key Concepts

- [[validation-gated-multi-agent-governance]]: A framework for autonomous surrogate model evolution that employs role-separated agents and deterministic safety gates to govern model promotions.

## Archivist Review

I approved the validation-gated multi-agent governance concept as it introduces a novel, reusable pattern for governing model adaptation in safety-critical physical systems. I also approved the open question regarding safe online surrogate governance, as it captures the fundamental tension between model flexibility and safety in high-stakes industrial deployments, a recurring bottleneck in the field. No other candidates met the criteria for novelty or broader reusability.

### Approved Concepts
- Validation-Gated Multi-Agent Governance: It provides a structured, auditable mechanism for online model adaptation in safety-critical domains, addressing the failure of static surrogates under regime shifts.

### Approved Open Questions
- Safe Online Surrogate Governance: This represents a foundational bottleneck for the deployment of AI digital twins in high-stakes, safety-critical industrial applications where autonomous model evolution must be auditable and restricted.

## Links

- [Abstract](https://arxiv.org/abs/2606.03321)
- [PDF](https://arxiv.org/pdf/2606.03321)

