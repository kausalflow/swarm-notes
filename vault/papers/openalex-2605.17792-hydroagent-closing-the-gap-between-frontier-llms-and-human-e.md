---
# CSL-compatible fields
title: "HydroAgent: Closing the Gap Between Frontier LLMs and Human Experts in Hydrologic Model Calibration via Simulator-Grounded RL"
author:
  - literal: "Zhi Li"
  - literal: "Songkun Yan"
  - literal: "Jie Cao"
  - literal: "Mofan Zhang"
  - literal: "Anjiang Wei"
  - literal: "J.-M. Yoo"
  - literal: "Yang Hong"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.17792"

# Custom fields
paper_id: "2605.17792"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "fine-tuning"
  - "reinforcement-learning"
  - "agent"
  - "autonomous-agent"
  - "earth-system-science"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hydroagent"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:36:39Z"
created_at: "2026-05-21T08:36:39Z"
---

# HydroAgent: Closing the Gap Between Frontier LLMs and Human Experts in Hydrologic Model Calibration via Simulator-Grounded RL

**Authors**: Zhi Li, Songkun Yan, Jie Cao, Mofan Zhang, Anjiang Wei, J.-M. Yoo, Yang Hong
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.17792](https://arxiv.org/abs/2605.17792)

## Summary

This paper investigates the efficacy of frontier LLM agents in calibrating the CREST distributed hydrologic model, finding a significant performance gap compared to human experts. To address this, the authors introduce HydroAgent, which utilizes supervised fine-tuning on expert trajectories and reinforcement learning with simulation feedback (RLSF) for domain-specific grounding. The results show that this domain-tuned approach outperforms larger generic models in hydrologic model parameter estimation, offering a more efficient and physically faithful solution for Earth system science.

## Key Contributions

- Benchmarked nine frontier LLMs on hydrologic model calibration, demonstrating that existing capability tiers struggle to match human expert performance due to poor domain grounding.
- Introduced HydroAgent, a 4B parameter model fine-tuned on expert trajectories using Group-Relative Policy Optimization with simulator feedback (RLSF).
- Demonstrated that domain-tuned models with simulator-in-the-loop RL are more compute-efficient and physically faithful than scaling generic frontier LLMs for physical science applications.

## Open Questions & Future Work

- [[global-generalization-hydrologic-agents]]
- [[multi-modal-critics-scientific-calibration]]

## Key Concepts

- [[hydroagent]]: A domain-specific LLM agent calibrated via simulator-grounded reinforcement learning for hydrologic model parameter optimization.

## Archivist Review

Approved HydroAgent as a framework for simulator-grounded RL in scientific calibration, and two open questions regarding cross-regime generalization and the shift from scalar to vision-based rewards. I rejected the CREST dataset because it is a specific domain model rather than a general-purpose benchmark repository.

### Approved Concepts
- HydroAgent: Represents a novel paradigm for automating complex physical model calibration by grounding LLM agents in domain simulators via reinforcement learning.

### Approved Open Questions
- Generalization of Hydrologic Agents: This question is critical for establishing whether small, domain-tuned models are truly scalable solutions for operational hydrology or if their effectiveness is restricted to the specific geographic regions used during training.
- Multi-modal Critics for Calibration: Replacing narrow, scalar rewards with richer, multi-modal feedback could solve persistent bottlenecks in physical simulator calibration where single-metric optimization often leads to suboptimal results.

## Links

- [Abstract](https://arxiv.org/abs/2605.17792)
- [PDF](https://arxiv.org/pdf/2605.17792)

