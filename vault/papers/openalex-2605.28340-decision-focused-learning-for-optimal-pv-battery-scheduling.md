---
# CSL-compatible fields
title: "Decision-focused learning for optimal PV-Battery scheduling"
author:
  - literal: "Joris Depoortere"
  - literal: "Hussain Kazmi"
  - literal: "Johan Driesen"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.28340"

# Custom fields
paper_id: "2605.28340"
paper_source: "openalex"
domain: "time-series,energy-management"
tags:
  - "forecasting"
  - "lstm"
  - "time-series"
  - "optimization"
architectures:
  - "lstm"
datasets:
  []
concept_slugs:
  - "decision-focused-learning"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:36:30Z"
created_at: "2026-05-30T07:36:30Z"
---

# Decision-focused learning for optimal PV-Battery scheduling

**Authors**: Joris Depoortere, Hussain Kazmi, Johan Driesen
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.28340](https://arxiv.org/abs/2605.28340)

## Summary

This paper addresses the mismatch between forecasting accuracy and downstream decision performance in residential PV-battery systems. The authors propose a decision-focused learning framework that integrates the optimization task directly into the training of an LSTM forecaster. Results show that prioritizing decision-related cost metrics over statistical accuracy leads to significant financial improvements for households, challenging the traditional reliance on decoupled forecasting-optimization workflows.

## Key Contributions

- Introduced a decision-focused learning framework that trains an LSTM forecaster directly on battery scheduling optimization objectives, rather than standard statistical error metrics.
- Demonstrated a 3.6% reduction in household electricity costs compared to decoupled methods, despite higher statistical forecast error.
- Showed that warm-starting the decision-focused model reduces costs by 8% and mitigates the trade-off between statistical accuracy and task performance.

## Open Questions & Future Work

- [[generalization-of-dfl-models]]
- [[dfl-grid-stability-impact]]

## Key Concepts

- [[decision-focused-learning]]: A framework that integrates prediction and optimization by training forecasters directly on downstream decision-making performance.

## Archivist Review

The decision-focused learning concept was approved as it represents a significant, reusable paradigm for bridging the gap between forecasting accuracy and decision performance. The two open questions address critical bottlenecks regarding the transferability of such models and the systemic grid-level externalities that arise when prioritizing individual-level economic optimization. Other candidates were excluded to maintain the high selectivity of the vault.

### Approved Concepts
- Decision-focused learning: It demonstrates that optimizing for downstream task performance can yield better financial outcomes than standard statistical error minimization.

### Approved Open Questions
- Generalization of DFL models: Crucial for the practical scalability and deployment of DFL in real-world energy systems where household-specific optimization parameters vary widely.
- DFL impact on grid stability: Essential for ensuring that the adoption of intelligent, decision-aware energy management systems does not compromise the operational stability of the wider electrical infrastructure.

## Links

- [Abstract](https://arxiv.org/abs/2605.28340)
- [PDF](https://arxiv.org/pdf/2605.28340)

