---
# CSL-compatible fields
title: "Analysis framework for higher-order temporal correlations with applications to human heartbeats"
author:
  - literal: "Tibebe Birhanu"
  - literal: "Hang-Hyun Jo"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2512.01235"

# Custom fields
paper_id: "2512.01235"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "burst-tree-decomposition-method"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:10:13Z"
created_at: "2026-05-31T08:10:13Z"
---

# Analysis framework for higher-order temporal correlations with applications to human heartbeats

**Authors**: Tibebe Birhanu, Hang-Hyun Jo
**Date**: 2026-05-28
**Paper ID**: [openalex:2512.01235](https://arxiv.org/abs/2512.01235)

## Summary

This paper introduces a time series analysis framework that characterizes higher-order temporal correlations in event sequences by decomposing them into hierarchical 'burst trees'. By mapping consecutive burst merges at various timescales onto tree structures, the method moves beyond traditional interevent time distribution analysis. The approach utilizes novel metrics like burst complexity to extract multiscale temporal signatures, which the authors demonstrate effectively distinguish between healthy and diseased cardiac rhythms.

## Key Contributions

- Introduces a novel time series analysis framework that quantifies higher-order temporal correlations via hierarchical burst-tree decomposition.
- Defines novel diagnostic measures including burst complexity and memory coefficients for bursts extracted from tree-based representations.
- Demonstrates the capability of the framework to differentiate between healthy and pathological physiological states using heartbeat interval time series.

## Open Questions & Future Work

- [[mechanistic-interpretation-of-burst-merging-kernels]]

## Key Concepts

- [[burst-tree-decomposition-method]]: A decomposition technique that maps event sequences onto hierarchical burst trees to reveal higher-order temporal correlations across multiple timescales.

## Archivist Review

I approved the burst-tree decomposition method as a novel, reusable framework for characterizing hierarchical temporal structure in event-based data. I also approved the open question regarding the mechanistic interpretation of burst-merging kernels, as it identifies a clear gap between statistical representation and the underlying dynamical processes in physiological time series. No datasets were approved as none provided sufficient evidence of being a novel, widely-accessible benchmark.

### Approved Concepts
- Burst-tree decomposition method: It provides a fundamental shift in how temporal correlations are modeled by mapping event sequences into hierarchical trees, moving beyond simple interevent time statistics.

### Approved Open Questions
- Mechanistic interpretation of burst-merging kernels: The burst-merging kernel is the fundamental object characterizing higher-order temporal correlations. Moving beyond descriptive statistics to understanding the generative physical processes captured by these kernels is critical for moving from classification toward mechanistic diagnosis of cardiovascular diseases.

## Links

- [Abstract](https://arxiv.org/abs/2512.01235)
- [PDF](https://arxiv.org/pdf/2512.01235)

