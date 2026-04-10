---
# CSL-compatible fields
title: "AutoSOTA: An End-to-End Automated Research System for State-of-the-Art AI Model Discovery"
author:
  - literal: "Yu Li"
  - literal: "Chenyang Shao"
  - literal: "Xinyang Liu"
  - literal: "Ruotong Zhao"
  - literal: "Peijie Liu"
  - literal: "Hongyuan Su"
  - literal: "Zhibin Chen"
  - literal: "Qinglong Yang"
  - literal: "Anjie Xu"
  - literal: "Yi Fang"
  - literal: "Qingbin Zeng"
  - literal: "Tianxing Li"
  - literal: "Jingbo Xu"
  - literal: "Fengli Xu"
  - literal: "Yong Li"
  - literal: "Tie-Yan Liu"
issued:
  date-parts:
    - [2026, 4, 7]
url: "https://arxiv.org/abs/2604.05550"

# Custom fields
paper_id: "2604.05550"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "multi-agent"
  - "agent"
  - "autonomous-agent"
  - "time-series"
  - "computer-vision"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "autosota"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-10T06:27:21Z"
created_at: "2026-04-10T06:27:21Z"
---

# AutoSOTA: An End-to-End Automated Research System for State-of-the-Art AI Model Discovery

**Authors**: Yu Li, Chenyang Shao, Xinyang Liu, Ruotong Zhao, Peijie Liu, Hongyuan Su, Zhibin Chen, Qinglong Yang, Anjie Xu, Yi Fang, Qingbin Zeng, Tianxing Li, Jingbo Xu, Fengli Xu, Yong Li, Tie-Yan Liu
**Date**: 2026-04-07
**Paper ID**: [openalex:2604.05550](https://arxiv.org/abs/2604.05550)

## Summary

AutoSOTA is a multi-agent automated research system designed to accelerate the empirical model optimization cycle by advancing published SOTA models to higher performance levels. The system employs eight specialized agents that handle tasks ranging from environment preparation and code grounding to experimental evaluation and idea generation, effectively moving beyond basic hyperparameter tuning. Evaluation across eight top-tier AI conferences demonstrates the system's ability to successfully produce 105 improved SOTA models across various domains, including LLM and time-series research. By reducing the manual experimental burden, AutoSOTA serves as a scalable infrastructure for automated research and scientific discovery.

## Key Contributions

- Introduces AutoSOTA, a multi-agent system designed to automate the full pipeline of reproducing and improving AI models from published research.
- Utilizes a three-stage framework (resource preparation, evaluation, reflection/ideation) with eight specialized agents to surpass original model performance.
- Demonstrates success by identifying 105 new SOTA models across diverse domains including LLMs, NLP, computer vision, and time series in an average of five hours per paper.

## Open Questions & Future Work

- [[automated-rubric-scalability]]

## Key Concepts

- [[autosota]]: An end-to-end multi-agent research system that automates the replication, debugging, and iterative refinement of SOTA AI models.

## Archivist Review

I have approved the AutoSOTA architecture as a novel concept in automated research infrastructure and the open question regarding the scalability of evaluation rubrics. The criteria applied focuses on the paper's contribution to high-level systemic research automation rather than domain-specific implementation details. No datasets were approved as none were central to the contribution.

### Approved Concepts
- AutoSOTA: The system introduces a multi-agent infrastructure for automating the full cycle of empirical AI research, including model replication, debugging, and architectural refinement.

### Approved Open Questions
- Automated Research Evaluation Rubrics: Scaling automated research discovery requires robust, dense, and automated feedback signals that go beyond simple 'result matching' to evaluate structural and semantic fidelity.

## Links

- [Abstract](https://arxiv.org/abs/2604.05550)
- [PDF](https://arxiv.org/pdf/2604.05550)

