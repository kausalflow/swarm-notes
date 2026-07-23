---
# CSL-compatible fields
title: "LLMs and Agentic AI Systems for Smart Grids: A Tutorial on Architectures and Applications"
author:
  - literal: "Daniela Rojas"
  - literal: "Abdulwahab Albassam"
  - literal: "Aidan G. Leung"
  - literal: "Jett Ngo"
  - literal: "Ryan Luo"
  - literal: "Peter R. Quawas"
  - literal: "Junpyung Kim"
  - literal: "Kangkai Liang"
  - literal: "Mansi Nanavati"
  - literal: "Jonathan Mai"
  - literal: "Meng-Chi Tsai"
  - literal: "Yun-Tong Tsai"
  - literal: "Yize Chen"
  - literal: "Y Shi"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2607.18147"

# Custom fields
paper_id: "2607.18147"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "agent"
  - "autonomous-agent"
  - "tool-use"
  - "forecasting,optimization,control"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-23T07:27:26Z"
created_at: "2026-07-23T07:27:26Z"
---

# LLMs and Agentic AI Systems for Smart Grids: A Tutorial on Architectures and Applications

**Authors**: Daniela Rojas, Abdulwahab Albassam, Aidan G. Leung, Jett Ngo, Ryan Luo, Peter R. Quawas, Junpyung Kim, Kangkai Liang, Mansi Nanavati, Jonathan Mai, Meng-Chi Tsai, Yun-Tong Tsai, Yize Chen, Y Shi
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.18147](https://arxiv.org/abs/2607.18147)

## Summary

This tutorial-style paper reviews the integration of large language models and agentic AI systems into smart grids, addressing the challenge of physically infeasible model outputs by introducing a solver-grounded design principle. The authors establish that agentic systems should orchestrate workflows and utilize trusted external solvers rather than performing raw numerical computations directly. Four comprehensive case studies—covering wind forecasting, EV charging, power flow analysis, and contingency diagnosis—demonstrate that solver-grounded agents significantly outperform LLM-only baselines in accuracy and constraint satisfaction. Finally, a structured four-group evaluation framework is proposed to assess task utility, correctness, safety, and operational overhead in power systems.

## Key Contributions

- Introduces a solver-grounded design principle for LLM and agentic smart grid systems, ensuring numerical outputs originate from trusted tools and pass explicit verification.
- Reviews prompting strategies and agentic architectures for power systems across four case studies: wind power forecasting, EV charging scheduling, power flow analysis, and contingency diagnosis.
- Demonstrates quantitative improvements across case studies, including EVAgent reproducing the CVXPY optimum while reducing unmet energy by 7.5-9.5x, and GridDebugAgent reducing total contingency violations by 52.3%.
- Proposes a four-group evaluation framework spanning task utility, solver-grounded correctness, faithfulness/safe failure, and cost/latency.

## Open Questions & Future Work

- [[verifiable-repair-policies-smart-grids]]

## Archivist Review

Applied strict scarcity and reusability standards. No new concepts or datasets met the rigorous threshold for standalone vault notes, but the open question regarding verifiable repair policies for smart grids was retained as an important future research direction in grid AI systems.

### Approved Open Questions
- Verifiable Repair Policies for Smart Grids: Crucial for transitioning LLM-based grid assistants from exploratory tools to mission-critical operational systems requiring strict mathematical and physical guarantees.

### Rejected Candidates
- [open_question] Verifiable Repair Policies for Smart Grids (`verifiable-repair-policies-smart-grids`) - generic: The open question is well-motivated and explicitly stated in the paper's conclusion/future work, so it is approved.

## Links

- [Abstract](https://arxiv.org/abs/2607.18147)
- [PDF](https://arxiv.org/pdf/2607.18147)

