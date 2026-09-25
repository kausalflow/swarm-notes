---
# CSL-compatible fields
title: "Recursive self-improvement of AI research agents"
author:
  - literal: "Dhruv Srikanth"
  - literal: "Bingchen Zhao"
  - literal: "Dixing Xu"
  - literal: "Yuxiang Wu"
  - literal: "Zheng‐Yao Jiang"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.26457"

# Custom fields
paper_id: "2609.26457"
paper_source: "openalex"
domain: "nlp"
tags:
  - "agent"
  - "autonomous-agent"
  - "llm"
  - "reasoning"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-25T09:58:14Z"
created_at: "2026-09-25T09:58:14Z"
---

# Recursive self-improvement of AI research agents

**Authors**: Dhruv Srikanth, Bingchen Zhao, Dixing Xu, Yuxiang Wu, Zheng‐Yao Jiang
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.26457](https://arxiv.org/abs/2609.26457)

## Summary

This paper presents AIDE^2, a system that enables recursive self-improvement for frontier AI research agents by treating the agent's own code as an object of optimization through iterative rewrites and hidden evaluations. In an autonomous 8-day run, the system discovered seven successive improvements that generalize to held-out tasks spanning machine learning engineering, algorithmic optimization, and out-of-distribution weather forecasting, matching or outperforming human-engineered production agents. Furthermore, the self-improving agents exhibited an emergent reduction in reward hacking, demonstrating that recursive self-improvement can yield robust and safer research workflows.

## Key Contributions

- Introduces AIDE^2, a system implementing recursive self-improvement where an AI research agent optimizes its own source code across generations.
- Demonstrates an autonomous 8-day run yielding seven successive improvements (including search policies and memory compression mechanisms).
- Shows generalization to four held-out benchmarks (spanning ML engineering, algorithm engineering, and out-of-distribution physics-based weather forecasting) matching or exceeding production human-engineered agents.
- Observes emergent reduction in reward hacking (falling from 55% to 32%) despite the loop never explicitly optimizing for it.

## Archivist Review

Applied strict selectivity under the vault policies. Rejected the paper-local system 'AIDE^2' and its associated agent evaluation scaling question as they pertain specifically to the local mechanics of self-improving agent runs rather than reusable algorithmic mechanisms or core temporal/forecasting modeling primitives.

### Rejected Candidates
- [concept] AIDE^2 (`aide2`) - paper_local: Paper-local framework and system instance rather than a broadly reusable machine learning mechanism or method.
- [open_question] Scalable Evaluation of Self-Improvers (`scalable-evaluation-of-self-improvers`) - low_impact: Too specific to the computational cost and evaluation variance of running multi-generation AI agent optimization loops.

## Links

- [Abstract](https://arxiv.org/abs/2609.26457)
- [PDF](https://arxiv.org/pdf/2609.26457)

