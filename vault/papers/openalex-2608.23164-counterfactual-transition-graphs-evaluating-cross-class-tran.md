---
# CSL-compatible fields
title: "Counterfactual Transition Graphs: Evaluating Cross-Class Transition Quality"
author:
  - literal: "Syed Muhammad Hamza Zaidi"
  - literal: "Szymon Bobek"
  - literal: "Grzegorz J. Nalepa"
  - literal: "Myra Spiliopoulou"
issued:
  date-parts:
    - [2026, 8, 24]
url: "https://arxiv.org/abs/2608.23164"

# Custom fields
paper_id: "2608.23164"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "interpretability"
  - "explainability"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "counterfactual-transition-graph"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-27T15:59:08Z"
created_at: "2026-08-27T15:59:08Z"
---

# Counterfactual Transition Graphs: Evaluating Cross-Class Transition Quality

**Authors**: Syed Muhammad Hamza Zaidi, Szymon Bobek, Grzegorz J. Nalepa, Myra Spiliopoulou
**Date**: 2026-08-24
**Paper ID**: [openalex:2608.23164](https://arxiv.org/abs/2608.23164)

## Summary

The paper introduces Counterfactual Transition Graphs (CGT), a structural diagnostic framework where classes are nodes and edge weights represent counterfactual transition reliability. Applied to a six-class hand-movement task, CGT reveals that counterfactual reachability diverges from classifier accuracy, exposing how replacement-based and gradient-based counterfactual explainers interact with data manifolds and rigid classification boundaries.

## Key Contributions

- Proposed Counterfactual Transition Graphs (CGT) to evaluate cross-class transition quality and CF reliability for time-series classifiers.
- Demonstrated that counterfactual reachability does not align with classifier accuracy and can run counter to it (Spearman rho = -0.37).
- Juxtaposed replacement-based CFs (stay on-manifold and fail on rigid boundaries) with gradient-based CFs (step off the data manifold to reach any class).

## Limitations

Evaluated on a specific six-class hand-movement task.

## Open Questions & Future Work

- [[transfer-to-other-domains]]

## Key Concepts

- [[counterfactual-transition-graph]]: A graph-based diagnostic framework where nodes represent classes and edge weights denote counterfactual transition reliability between class prototypes.

## Archivist Review

Approved the foundational Counterfactual Transition Graph concept and the cross-domain transfer question, while rejecting the local prototype retrieval subcomponent and routine hyperparameter sensitivity work.

### Approved Concepts
- Counterfactual Transition Graph: Introduces a novel structural diagnostic tool for evaluating cross-class counterfactual transitions and reliability in time-series classifiers.

### Approved Open Questions
- Transfer to Other Domains: Crucial for establishing whether global counterfactual transition topologies reveal universal properties of time series classifiers or remain domain-specific artifacts.

### Rejected Candidates
- [concept] Proximity-Aware Retrieval Sweep (`proximity-aware-retrieval-sweep`) - subcomponent_of_broader_mechanism: A minor algorithmic component used for retrieving prototypes rather than a standalone conceptual paradigm.
- [open_question] Sensitivity Analysis of Hyperparameters (`sensitivity-analysis-hyperparameters`) - not_reusable: Routine hyperparameter tuning and sensitivity analysis future work that lacks a specific conceptual bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.23164)
- [PDF](https://arxiv.org/pdf/2608.23164)

