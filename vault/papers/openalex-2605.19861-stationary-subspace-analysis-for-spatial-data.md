---
# CSL-compatible fields
title: "Stationary subspace analysis for spatial data"
author:
  - literal: "Perttu Saarela"
  - literal: "Klaus Nordhausen"
  - literal: "Jaakko Pere"
  - literal: "Anne M. Ruiz"
issued:
  date-parts:
    - [2026, 5, 19]
url: "https://arxiv.org/abs/2605.19861"

# Custom fields
paper_id: "2605.19861"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "spatial-stationary-subspace-analysis-spssa"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-22T08:17:41Z"
created_at: "2026-05-22T08:17:41Z"
---

# Stationary subspace analysis for spatial data

**Authors**: Perttu Saarela, Klaus Nordhausen, Jaakko Pere, Anne M. Ruiz
**Date**: 2026-05-19
**Paper ID**: [openalex:2605.19861](https://arxiv.org/abs/2605.19861)

## Summary

This paper extends Stationary Subspace Analysis (SSA) to spatial data by incorporating spatial dependence into the blind source separation framework. The authors propose three estimation procedures based on first- and second-order spatial statistics, integrated via approximate joint diagonalization to handle complex nonstationarity. Additionally, they introduce a data augmentation strategy to solve the persistent challenge of determining the dimension of the nonstationary subspace. The methodology provides a robust, generalized approach for spatial signal decomposition that is also applicable to time series analysis.

## Key Contributions

- Introduced Spatial Stationary Subspace Analysis (spSSA) to decompose spatially dependent multivariate data into stationary and nonstationary components.
- Proposed three estimation procedures for the unmixing matrix based on spatial statistics, solvable via generalized eigenvalue problems.
- Developed a novel data augmentation-based approach to estimate the dimension of the nonstationary subspace, addressing a fundamental limitation in stationary subspace analysis.

## Open Questions & Future Work

- [[determining-nonstationary-subspace-dimension]]

## Key Concepts

- [[spatial-stationary-subspace-analysis-spssa]]: A blind source separation framework that decomposes spatially indexed multivariate data into stationary and nonstationary components by accounting for spatial dependence.

## Archivist Review

I approved the overarching spSSA framework as a distinct extension to classical SSA. I also approved the open question regarding subspace dimension determination, as it is a foundational, recurring problem in subspace separation models. Submodules and implementation-specific procedures were rejected as they are subordinate to the main methodology.

### Approved Concepts
- Spatial Stationary Subspace Analysis (spSSA): Extends classical Stationary Subspace Analysis (SSA) to spatial data by incorporating spatial dependence through statistical moment-based unmixing.

### Approved Open Questions
- Dimension Determination in SSA: This is a bottleneck for the practical deployment of subspace methods as it impacts the accuracy and reliability of component separation.

### Rejected Candidates
- [concept] Estimation procedures for unmixing matrix (`estimation-procedures-for-unmixing-matrix`) - subcomponent_of_broader_mechanism: These are specific estimation subcomponents (generalized eigenvalue problems) of the broader spSSA mechanism.
- [concept] Data augmentation for dimension estimation (`data-augmentation-for-dimension-estimation`) - subcomponent_of_broader_mechanism: This is a heuristic implementation technique to solve a specific problem within the framework rather than a broad, reusable algorithmic paradigm.

## Links

- [Abstract](https://arxiv.org/abs/2605.19861)
- [PDF](https://arxiv.org/pdf/2605.19861)

