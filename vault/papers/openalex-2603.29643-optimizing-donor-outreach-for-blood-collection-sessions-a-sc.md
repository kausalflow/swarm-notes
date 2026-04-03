---
# CSL-compatible fields
title: "Optimizing Donor Outreach for Blood Collection Sessions: A Scalable Decision Support Framework"
author:
  - literal: "André Carneiro"
  - literal: "Pedro T. Monteiro"
  - literal: "Rui Henriques"
issued:
  date-parts:
    - [2026, 3, 31]
url: "https://arxiv.org/abs/2603.29643"

# Custom fields
paper_id: "2603.29643"
paper_source: "openalex"
domain: "nlp"
tags:
  - "optimization"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-03T06:07:42Z"
created_at: "2026-04-03T06:07:42Z"
---

# Optimizing Donor Outreach for Blood Collection Sessions: A Scalable Decision Support Framework

**Authors**: André Carneiro, Pedro T. Monteiro, Rui Henriques
**Date**: 2026-03-31
**Paper ID**: [openalex:2603.29643](https://arxiv.org/abs/2603.29643)

## Summary

This paper presents a scalable decision support framework for optimizing donor outreach in blood collection networks, addressing the balance between supply-demand matching and donor solicitation fatigue. The authors compare a binary integer linear programming (BILP) approach with an efficient greedy heuristic, using historical data from the Instituto Português do Sangue e da Transplantação (IPST). Results indicate that while BILP provides superior fulfillment, the greedy heuristic offers a highly performant, scalable alternative for operational planning with significant gains in computational efficiency. The framework utilizes organic attendance forecasting and quantile-based demand targets to effectively manage donor invitation planning in multi-site environments.

## Key Contributions

- Introduces an optimization framework for donor invitation scheduling that integrates eligibility, geographic convenience, blood-type demand, and safety constraints.
- Evaluates two scheduling strategies—a BILP formulation and an efficient greedy heuristic—providing a comprehensive trade-off analysis of runtime, memory, and supply-demand fulfillment.
- Demonstrates that the greedy heuristic offers a scalable alternative to exact BILP methods, with 115x faster execution and 188x lower peak memory at the cost of 3.9 percentage points lower demand fulfillment in a real-world regional setting.

## Open Questions & Future Work

- [[calibrating-participation-response-probabilities]]

## Archivist Review

The paper provides a practical application of standard optimization techniques (BILP vs. Greedy Heuristic) to blood donor management. I have rejected the specific BILP concept as it is a standard methodology rather than a reusable algorithmic contribution. I have generalized the open question about donor show-up to a broader, more impactful question about calibrating response probabilities in intervention-based scheduling.

### Approved Open Questions
- Calibrating Participation Response Probabilities: The accuracy of decision support frameworks hinges on the quality of its inputs; without calibrated response probabilities, the model risks significant efficiency loss or unmet demand.

### Rejected Candidates
- [concept] Binary Integer Linear Programming (BILP) for donor invitation scheduling (`bilp-donor-invitation-scheduling`) - not_novel: This is an application-specific formulation of standard BILP techniques, not a novel algorithmic contribution.
- [open_question] Calibrating Donor Show-up Probabilities (`calibrating-donor-show-up-probabilities`) - duplicate_existing: Redundant with the approved concept of response probability calibration; merged for a more universal scope.
- [open_question] Benchmarking Open-source Optimization Solvers (`open-source-solver-scalability`) - low_impact: Benchmarking specific solvers is a routine engineering task rather than a foundational research question.
- [open_question] Improving Geographic Data Accuracy (`improving-geographic-data-accuracy`) - other: This is a data quality issue rather than a structural algorithmic or scientific bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2603.29643)
- [PDF](https://arxiv.org/pdf/2603.29643)

