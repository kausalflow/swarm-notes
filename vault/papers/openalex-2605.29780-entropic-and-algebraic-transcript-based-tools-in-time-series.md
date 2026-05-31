---
# CSL-compatible fields
title: "Entropic and algebraic transcript-based tools in time series analysis"
author:
  - literal: "José M. Amigó"
  - literal: "Roberto Dale"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29780"

# Custom fields
paper_id: "2605.29780"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "information-extraction"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "similarity-distance-for-time-series"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:08:58Z"
created_at: "2026-05-31T08:08:58Z"
---

# Entropic and algebraic transcript-based tools in time series analysis

**Authors**: José M. Amigó, Roberto Dale
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29780](https://arxiv.org/abs/2605.29780)

## Summary

This paper presents a formal framework for analyzing coupled time series by mapping them to algebraic representations, specifically using symbols from finite groups such as the symmetric group. The authors utilize the concept of 'transcripts'—transitions between group elements—to develop and evaluate various entropic and algebraic tools for detecting dependencies and synchronization. A key contribution is the proposal of a similarity distance based on the mean Kendall distance, which proves more effective at identifying generalized synchronization in coupled systems than traditional entropy or divergence-based methods.

## Key Contributions

- Outlines a unified framework for analyzing coupled time series using algebraic transcripts within finite groups.
- Introduces a novel 'similarity distance' for time series, defined as the mean Kendall distance between group-valued transcript representations.
- Demonstrates that the similarity distance outperforms established tools like entropy, divergence, and statistical complexity in detecting generalized synchronization.

## Open Questions & Future Work

- [[general-group-distance-metrics]]

## Key Concepts

- [[similarity-distance-for-time-series]]: A novel similarity metric for coupled time series calculated as the mean Kendall distance between group-valued transcript representations.

## Archivist Review

The similarity distance is a distinct, domain-agnostic metric for analyzing coupled time series through algebraic transcripts, fulfilling the criteria for a reusable concept. The open question regarding group distance metrics addresses a fundamental methodological challenge in extending these algebraic tools to arbitrary finite groups, which is a critical theoretical bottleneck. No datasets were approved as none provided in the candidate list met the necessity and criticality criteria.

### Approved Concepts
- Similarity distance for time series: Introduces a new metric based on Kendall distance for measuring the similarity between coupled time series in algebraic/ordinal representations.

### Approved Open Questions
- Distance Metrics for General Groups: This is a fundamental methodological limitation for applying transcript-based tools to arbitrary groups beyond symmetric groups, as it affects the sensitivity and range of dissimilarity quantification.

## Links

- [Abstract](https://arxiv.org/abs/2605.29780)
- [PDF](https://arxiv.org/pdf/2605.29780)

