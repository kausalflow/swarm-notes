---
# CSL-compatible fields
title: "Kolab: Benchmarking Human-Agent Collaboration in Long-Horizon Workflows"
author:
  - literal: "Shirley Anugrah Hayati"
  - literal: "Patricia Anugrah Setiani"
  - literal: "Ruizi Wang"
  - literal: "Zhouyi Li"
  - literal: "Khánh Chi Lê"
  - literal: "Youngjun Lee"
  - literal: "Dongyeop Kang"
issued:
  date-parts:
    - [2026, 10, 15]
url: "https://arxiv.org/abs/2610.21109"

# Custom fields
paper_id: "2610.21109"
paper_source: "openalex"
domain: "nlp"
tags:
  - "agent"
  - "autonomous-agent"
  - "benchmark"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  - "kolab"
concept_slugs:
  []
dataset_slugs:
  - "kolab"
skill: "TimeSeriesSkill"
processed_at: "2026-10-18T09:14:02Z"
created_at: "2026-10-18T09:14:02Z"
---

# Kolab: Benchmarking Human-Agent Collaboration in Long-Horizon Workflows

**Authors**: Shirley Anugrah Hayati, Patricia Anugrah Setiani, Ruizi Wang, Zhouyi Li, Khánh Chi Lê, Youngjun Lee, Dongyeop Kang
**Date**: 2026-10-15
**Paper ID**: [openalex:2610.21109](https://arxiv.org/abs/2610.21109)

## Summary

The paper introduces Kolab, a comprehensive dataset and benchmark for studying human-agent collaboration in long-horizon professional workflows, derived from over 115 hours of screen recordings across 40 occupations. Kolab evaluates models on two tasks: forecasting how professionals utilize agent contributions and verifying collaboration quality and satisfaction judgments. Experiments show that current frontier models struggle significantly with these tasks, overestimating collaboration and failing to distinguish between high- and low-quality interactions.

## Key Contributions

- Introduces Kolab, a dataset of 115+ hours of screen recordings of 50 professionals collaborating with agents across 40 occupations on long-horizon professional workflows.
- Operationalizes two novel tasks for human-agent collaboration: forecasting how professionals use agent contributions, and verifying their judgments of collaboration satisfaction and output quality.
- Demonstrates that frontier models significantly overestimate collaboration with experts and struggle to distinguish between high- and low-quality collaboration.

## Limitations

Frontier models fail to accurately predict human adoption and satisfaction in long-horizon workflows, indicating that current architectures lack true understanding of collaborative dynamics.

## Open Questions & Future Work

- [[improving-long-horizon-human-agent-collaboration-understanding]]

## Archivist Review

Applied high selectivity standards, approving only the core benchmark dataset 'Kolab' and the explicit open research question on modeling long-horizon human-agent collaboration dynamics, while rejecting any concepts due to the absence of novel reusable modeling components.

### Approved Open Questions
- Improving Long-Horizon Human-Agent Collaboration Understanding: This direction addresses a fundamental limitation in current frontier models—their inability to accurately forecast human adoption and evaluate collaboration quality in long-horizon professional workflows—which is critical for deploying reliable collaborative agents.

### Rejected Candidates
- [concept] Improving Long-Horizon Human-Agent Collaboration Understanding (`improving-long-horizon-human-agent-collaboration-understanding`) - other: This candidate is an open question, not a standalone concept or methodology.

## Datasets

- [[kolab]]

## Links

- [Abstract](https://arxiv.org/abs/2610.21109)
- [PDF](https://arxiv.org/pdf/2610.21109)

