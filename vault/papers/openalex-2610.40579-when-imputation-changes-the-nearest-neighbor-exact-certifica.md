---
# CSL-compatible fields
title: "When Imputation Changes the Nearest Neighbor: Exact Certification of Similarity Retrieval for Incomplete Sensor Time Series"
author:
  - literal: "Jianru Shen"
issued:
  date-parts:
    - [2026, 10, 29]
url: "https://arxiv.org/abs/2610.40579"

# Custom fields
paper_id: "2610.40579"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "semantic-search"
  - "robustness"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-01T11:33:17Z"
created_at: "2026-11-01T11:33:17Z"
---

# When Imputation Changes the Nearest Neighbor: Exact Certification of Similarity Retrieval for Incomplete Sensor Time Series

**Authors**: Jianru Shen
**Date**: 2026-10-29
**Paper ID**: [openalex:2610.40579](https://arxiv.org/abs/2610.40579)

## Summary

This paper addresses the problem of nearest-neighbour similarity search for incomplete sensor time series, where missing values require imputation that heavily alters retrieval outcomes. The author introduces exact certification methods—including pairwise certificates, candidate bounds, and label stability certificates—that hold uniformly over all admissible completions within a feature box. By establishing a finite reduction to critical values and an interval dynamic programme combined with a fast quadratic-time bounding layer, the approach efficiently guarantees retrieval robustness without relying on fragile heuristic imputations. Experiments on traffic sensor collections show that conventional linear interpolation frequently changes nearest neighbours, whereas the proposed exact framework reliably certifies stability while outperforming unoptimized search.

## Key Contributions

- Proposes pairwise certificates, guaranteed candidate sets, and label stability certificates for similarity retrieval on incomplete sensor time series under admissible query completions within a feature box.
- Develops a finite reduction to critical values and an exact interval dynamic programme for computing worst-case ranking gaps beyond the separable $L_1$ end.
- Introduces a quadratic-time fast layer with valid bounds, feasible witnesses, and an exact tightness criterion, achieving 82-110x speedups over the dynamic program alone.
- Demonstrates on traffic-sensor datasets that linear interpolation alters nearest-neighbour outcomes in 15 to 33 percent of queries, highlighting the sensitivity of uncertified imputation.

## Open Questions & Future Work

- [[incomplete-galleries-certified-retrieval]]

## Archivist Review

No new concepts met the strict novelty and reusability requirements as standalone vault notes. The open question on incomplete galleries is retained as it addresses a substantive limitation in certified retrieval.

### Approved Open Questions
- Certified Retrieval with Incomplete Galleries: Real-world databases routinely feature missing values in both queries and historical galleries, making single-sided completeness a major bottleneck for scalable deployment.

## Links

- [Abstract](https://arxiv.org/abs/2610.40579)
- [PDF](https://arxiv.org/pdf/2610.40579)

