---
# CSL-compatible fields
title: "Beyond average warming: Two-sample inference for dense-sparse functional data reveals changes in intraday temperature patterns"
author:
  - literal: "Kevin Wilk"
  - literal: "Hajo Holzmann"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.27335"

# Custom fields
paper_id: "2605.27335"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "statistical-inference"
  - "functional-data-analysis"
architectures:
  []
datasets:
  []
concept_slugs:
  - "two-sample-inference-for-dense-sparse-functional-data"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:39:28Z"
created_at: "2026-05-29T08:39:28Z"
---

# Beyond average warming: Two-sample inference for dense-sparse functional data reveals changes in intraday temperature patterns

**Authors**: Kevin Wilk, Hajo Holzmann
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.27335](https://arxiv.org/abs/2605.27335)

## Summary

This paper addresses the statistical challenge of comparing temperature patterns between modern, high-resolution sensor data and coarser historical records. The authors propose a two-sample inference framework that handles functional data with mixed sampling densities, enabling valid statistical comparisons despite resolution discrepancies. By deriving estimators with optimal convergence rates and establishing a functional central limit theorem, they provide a rigorous method for constructing uniform confidence bands. Empirical application to German weather station data demonstrates that climate change influences intraday thermal dynamics rather than just raising mean temperatures.

## Key Contributions

- Developed two-sample inference procedures for functional data that account for mixed dense-sparse sampling resolutions.
- Derived estimators of mean function differences achieving optimal convergence rates in the supremum norm.
- Established a functional central limit theorem and multiplier bootstrap methods for constructing uniform confidence bands.
- Demonstrated that climate change has significantly altered intraday temperature patterns in Germany, showing non-uniform warming throughout the day.

## Open Questions & Future Work

- [[inference-for-functional-operators]]

## Key Concepts

- [[two-sample-inference-for-dense-sparse-functional-data]]: A statistical inference framework for comparing functional mean functions when one sample is densely recorded and the other is sparsely recorded.

## Archivist Review

The paper contributes a specialized statistical framework for the common real-world problem of comparing functional data across different sampling resolutions. I approved the core inferential framework and one open question regarding higher-order operators, as these are theoretically significant contributions to functional data analysis. A secondary question about computational efficiency was rejected as it pertains to general computational optimization rather than a structural limitation of the framework itself.

### Approved Concepts
- Two-sample inference for dense-sparse functional data: Addresses the fundamental statistical challenge of comparing functional datasets with inconsistent sampling frequencies, a common problem in longitudinal and environmental sciences.

### Approved Open Questions
- Inference for functional operators: Understanding changes in the distribution and variability of functional processes, not just their centers, is essential for a complete picture in applications like climate change.

### Rejected Candidates
- [open_question] Efficient computation for FDA inference (`efficient-two-sample-inference-fda`) - low_impact: The bottleneck mentioned is a standard computational concern rather than a fundamental scientific limitation of the functional data analysis framework.

## Links

- [Abstract](https://arxiv.org/abs/2605.27335)
- [PDF](https://arxiv.org/pdf/2605.27335)

