---
# CSL-compatible fields
title: "CLOUDADV: Decision-Aligned Instance Sizing with Zero-Shot Foundation Models under Drift"
author:
  - literal: "J F Bell"
  - literal: "Giacomo Carfì"
  - literal: "Gerlando Gramaglia"
  - literal: "Andrea Simioni"
  - literal: "Daniele Fontani"
  - literal: "Vincenzo Lomonaco"
issued:
  date-parts:
    - [2026, 6, 30]
url: "https://arxiv.org/abs/2606.31470"

# Custom fields
paper_id: "2606.31470"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "zero-shot-learning"
  - "time-series"
  - "forecasting"
  - "cloud-computing"
architectures:
  []
datasets:
  []
concept_slugs:
  - "decision-aligned-instance-sizing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-03T07:55:28Z"
created_at: "2026-07-03T07:55:28Z"
---

# CLOUDADV: Decision-Aligned Instance Sizing with Zero-Shot Foundation Models under Drift

**Authors**: J F Bell, Giacomo Carfì, Gerlando Gramaglia, Andrea Simioni, Daniele Fontani, Vincenzo Lomonaco
**Date**: 2026-06-30
**Paper ID**: [openalex:2606.31470](https://arxiv.org/abs/2606.31470)

## Summary

CLOUDADV is an interactive advisory system designed to optimize cloud virtual machine sizing by integrating zero-shot time-series forecasting with heuristic-driven recommendation generation. The system constructs a structured decision context encompassing historical utilization, metadata, and pricing to mitigate overprovisioning under workload drift. By utilizing both offline reference LLMs and smaller production-ready models, it assesses deployment-time alignment against cost and latency constraints. The approach demonstrates significant cost savings in production environments without the operational overhead of constant model retraining.

## Key Contributions

- Introduces CLOUDADV, an advisory system for cloud instance sizing that eliminates per-tenant retraining through zero-shot foundation models.
- Achieves 52.9% simulated cost reduction on production VM workloads while maintaining low exceedance rates (≤ 1.5%).
- Demonstrates that zero-shot forecasters like Chronos-2 can produce recommendation patterns competitive with supervised baselines in drift-prone cloud environments.

## Open Questions & Future Work

- [[decision-aligned-cloud-sizing-generalization]]

## Key Concepts

- [[decision-aligned-instance-sizing]]: A framework for cloud virtual machine provisioning that leverages zero-shot time-series forecasting to generate cost-effective instance sizing recommendations.

## Archivist Review

The paper proposes a decision-focused framework for cloud sizing that effectively bridges time-series forecasting with heuristic-based recommendation systems. I approved the core concept as a reusable framework for downstream decision-centric forecasting. The open question was approved because it addresses the non-trivial challenge of guaranteeing safety and generalizability when applying zero-shot foundation models to operational infrastructure management.

### Approved Concepts
- Decision-Aligned Instance Sizing: Introduces a task-oriented framework for cloud resource optimization that bridges zero-shot forecasting with downstream decision-making under drift.

### Approved Open Questions
- Generalizing Decision-Aligned Cloud Sizing: This is critical for bridging the gap between theoretical zero-shot forecasting performance and the reliability requirements of automated, safety-critical cloud infrastructure management.

## Links

- [Abstract](https://arxiv.org/abs/2606.31470)
- [PDF](https://arxiv.org/pdf/2606.31470)

