---
# CSL-compatible fields
title: "Transcripts and Algebraic Distances in Time Series: Stochastic Properties and Nonparametric Dependence Tests"
author:
  - literal: "Christian H. Weiß"
  - literal: "José M. Amigó"
issued:
  date-parts:
    - [2026, 5, 25]
url: "https://arxiv.org/abs/2605.25478"

# Custom fields
paper_id: "2605.25478"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ordinal-patterns-transcripts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-28T08:37:36Z"
created_at: "2026-05-28T08:37:36Z"
---

# Transcripts and Algebraic Distances in Time Series: Stochastic Properties and Nonparametric Dependence Tests

**Authors**: Christian H. Weiß, José M. Amigó
**Date**: 2026-05-25
**Paper ID**: [openalex:2605.25478](https://arxiv.org/abs/2605.25478)

## Summary

This paper introduces a methodology for analyzing univariate time series by transforming them into sequences of transcripts or algebraic edit distances between successive ordinal patterns. The authors derive key stochastic properties for these transformations and use them to construct new nonparametric statistics for detecting serial dependence. Under the null hypothesis of independence, the asymptotic distributions of these statistics are characterized, enabling robust statistical testing. Experimental results show that these novel tests outperform traditional ordinal pattern-based approaches in power across various stochastic processes.

## Key Contributions

- Introduces the concept of 'transcripts' of ordinal patterns to quantify dependence in univariate processes.
- Establishes algebraic distances (Cayley and Kendall) between ordinal patterns to transform time series into distance sequences with derived stochastic properties.
- Develops nonparametric tests for serial dependence based on transcript-derived statistics, which demonstrate superior power compared to existing ordinal pattern-based tests.

## Open Questions & Future Work

- [[closed-form-transcript-distributions-general-processes]]
- [[multivariate-cross-transcript-analysis]]

## Key Concepts

- [[ordinal-patterns-transcripts]]: A transformation of univariate time series into sequences of transcripts based on differences between successive ordinal patterns to analyze dependence structure.

## Archivist Review

I have approved the core concept of 'Ordinal Patterns Transcripts' for its methodological novelty in symbolic time series analysis. I have also approved two open questions that directly address the theoretical scalability of this approach to more complex process classes and multivariate coupling scenarios. No datasets were approved as none were central or uniquely identified in the paper.

### Approved Concepts
- Ordinal Patterns Transcripts: Provides a novel approach to analyzing dependence structure by transforming series into sequences of transcripts derived from successive ordinal patterns.

### Approved Open Questions
- Distributions for General Processes: Generalizing these analytical distributions would enable more reliable and versatile statistical diagnostic tools for serial dependence.
- Multivariate Cross-Transcript Analysis: This extension is critical for applying algebraic dependence testing to multivariate and networked systems.

## Links

- [Abstract](https://arxiv.org/abs/2605.25478)
- [PDF](https://arxiv.org/pdf/2605.25478)

