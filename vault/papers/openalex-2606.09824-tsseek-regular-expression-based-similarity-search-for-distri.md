---
# CSL-compatible fields
title: "TSseek: Regular Expression-Based Similarity Search for Distributed Time Series Datasets"
author:
  - literal: "Xiaoshuai Li"
  - literal: "Khalid Alnuaim"
  - literal: "Mohamed Y. Eltabakh"
  - literal: "Elke A. Rundensteiner"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2606.09824"

# Custom fields
paper_id: "2606.09824"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "semantic-search"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tsseek"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:07:14Z"
created_at: "2026-06-11T09:07:14Z"
---

# TSseek: Regular Expression-Based Similarity Search for Distributed Time Series Datasets

**Authors**: Xiaoshuai Li, Khalid Alnuaim, Mohamed Y. Eltabakh, Elke A. Rundensteiner
**Date**: 2026-06-08
**Paper ID**: [openalex:2606.09824](https://arxiv.org/abs/2606.09824)

## Summary

TSseek is a framework for regular-expression-based similarity search in distributed time series that overcomes the limitations of traditional, rigid sequence-based query methods. By representing time series as sequences of line segments and query constructs as bounding rectangles, the framework enables efficient, exact matching for complex patterns including trends and value ranges. Experimental results demonstrate that TSseek outperforms traditional approximation techniques and state-of-the-art subsequence matching engines in both accuracy and computational efficiency.

## Key Contributions

- Introduces TSseek, a novel query language enabling regular-expression-based similarity search for trends, value ranges, and wildcards in time series.
- Develops a representation technique that approximates time series as line segments and maps query constructs into bounding rectangles to facilitate exact search.
- Implements TSseek-X, a distributed spatial index that achieves significant speedups and provides exact answers compared to existing approximate (PAA/SAX) or model-based baseline methods.

## Open Questions & Future Work

- [[extending-regex-time-series-search-capabilities]]

## Key Concepts

- [[tsseek]]: A regular-expression-powered search framework that enables pattern-based similarity queries on large-scale distributed time series by mapping series to line segments and queries to bounding rectangles.

## Archivist Review

I approved the TSseek concept as it introduces a novel, reusable paradigm for time-series similarity search by reframing query patterns as geometric indices. I rejected the indexing component (TSseek-X) as it is a specific sub-component of the framework. The open question was approved for capturing the critical transition from static exact matching to dynamic/approximate retrieval.

### Approved Concepts
- TSseek: It introduces a paradigm shift from rigid sequence-based matching to flexible, pattern-based search in time series using regular expressions.

### Approved Open Questions
- Extending Regex Time Series Search: This addresses the limitation of current exact, static-focused approaches, enabling broader utility in real-time and heterogeneous streaming environments.

### Rejected Candidates
- [concept] TSseek-X (`tsseek-x`) - subcomponent_of_broader_mechanism: This is a sub-component of the broader TSseek framework.

## Links

- [Abstract](https://arxiv.org/abs/2606.09824)
- [PDF](https://arxiv.org/pdf/2606.09824)

