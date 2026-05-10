---
# CSL-compatible fields
title: "A Topological Sorting Criterion for Random Causal Directed Acyclic Graphs"
author:
  - literal: "Alexander G. Reisach"
  - literal: "Antoine Chambaz"
  - literal: "Gilles Blanchard"
  - literal: "Sebastian Weichwald"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.06288"

# Custom fields
paper_id: "2605.06288"
paper_source: "openalex"
domain: "nlp"
tags:
  - "causal-discovery"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "relative-based-topological-sorting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:22:32Z"
created_at: "2026-05-10T07:22:32Z"
---

# A Topological Sorting Criterion for Random Causal Directed Acyclic Graphs

**Authors**: Alexander G. Reisach, Antoine Chambaz, Gilles Blanchard, Sebastian Weichwald
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.06288](https://arxiv.org/abs/2605.06288)

## Summary

This paper investigates the properties of random directed acyclic graphs (DAGs) commonly used in causal discovery benchmarks, identifying that the number of reachable nodes—termed relatives—increases monotonically along the causal order. The authors demonstrate that this property allows for causal order recovery by simply sorting nodes based on their estimated number of relatives. They argue that this bias significantly affects the reliability of current evaluation practices and propose the use of time-series DAGs as a more robust alternative for benchmarking causal discovery algorithms.

## Key Contributions

- Proves that in random DAGs, the number of nodes reachable via open paths increases monotonically along the causal order.
- Introduces a topological sorting criterion based on the estimated number of reachable relatives to recover the underlying causal order.
- Identifies that existing synthetic evaluation settings often rely on properties where this sorting criterion acts as an excellent proxy for ground-truth order.
- Proposes time-series DAGs as a more robust alternative for evaluating causal discovery algorithms compared to standard random DAG models.

## Key Concepts

- [[relative-based-topological-sorting]]: A method for causal order recovery in directed acyclic graphs based on sorting nodes by their estimated number of reachable nodes (relatives).

## Archivist Review

I have approved the Relative-based Topological Sorting concept as it identifies a critical structural shortcut in widely used causal discovery evaluation practices, which is highly relevant for benchmarking integrity. I rejected the proposal for using time-series DAGs as a concept because it functions more as a recommendation for future data practices than a distinct, reusable architectural or algorithmic mechanism.

### Approved Concepts
- Relative-based Topological Sorting: Reveals a significant structural bias in common synthetic DAG benchmarks by showing that simple reachability counts are sufficient to recover ground-truth causal orders.

### Rejected Candidates
- [concept] Time-series DAGs as benchmarking alternative (`time-series-dags-as-benchmarking-alternative`) - not_reusable: This is a proposal for a new benchmark type rather than a reusable methodological mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2605.06288)
- [PDF](https://arxiv.org/pdf/2605.06288)

