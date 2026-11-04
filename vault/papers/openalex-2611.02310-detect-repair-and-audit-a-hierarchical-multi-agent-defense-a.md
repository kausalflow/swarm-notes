---
# CSL-compatible fields
title: "Detect, Repair and Audit: A Hierarchical Multi-Agent Defense Against Adversarial Attacks in Energy Forecasting"
author:
  - literal: "Zewei Shi"
  - literal: "Ruoxi Sun"
  - literal: "Minhui Xue"
  - literal: "Feng Liu"
  - literal: "Hua Ma"
  - literal: "Xingliang Yuan"
  - literal: "Surya Nepal"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.02310"

# Custom fields
paper_id: "2611.02310"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "language-model"
  - "reinforcement-learning"
  - "multi-agent"
  - "robustness"
  - "adversarial-examples"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-04T12:40:56Z"
created_at: "2026-11-04T12:40:56Z"
---

# Detect, Repair and Audit: A Hierarchical Multi-Agent Defense Against Adversarial Attacks in Energy Forecasting

**Authors**: Zewei Shi, Ruoxi Sun, Minhui Xue, Feng Liu, Hua Ma, Xingliang Yuan, Surya Nepal
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.02310](https://arxiv.org/abs/2611.02310)

## Summary

This paper introduces a hierarchical multi-agent defense mechanism against adversarial attacks in Time-Series Large Language Models used for electricity-demand forecasting. Drawing from energy regulatory standards, the framework implements a Multi-Agent Reinforcement Learning detector and signal repair at local control centers, alongside an evidence-grounded LLM auditing agent for Virtual Power Plants. Experimental results demonstrate high detection F1 scores, significant reductions in input Relative Squared Error, and compliance with strict real-time latency budgets.

## Key Contributions

- Proposes a hierarchical multi-agent defense framework for energy forecasting encompassing local control centers and audit-critical Virtual Power Plants (VPPs).
- Develops a Multi-Agent Reinforcement Learning detector and clean-reference-calibrated signal repair that reduces adversarial-to-clean RSE by up to 83% while operating within local-center latency budgets.
- Deploys an evidence-grounded LLM auditing agent with human-in-the-loop validation, achieving an F1 score above 0.91 for detection across evaluated dataset-attack pairs.

## Archivist Review

Applied strict reusability and selectivity criteria. No concepts or open questions met the threshold for permanent vault storage.

### Rejected Candidates
- [open_question] Robustness Under Distributional Data Drift (`distributional-data-drift-robustness-energy-forecasting`) - low_impact: The open question regarding robustness under distributional drift in energy forecasting is too broad and standard across anomaly detection domains.

## Links

- [Abstract](https://arxiv.org/abs/2611.02310)
- [PDF](https://arxiv.org/pdf/2611.02310)

