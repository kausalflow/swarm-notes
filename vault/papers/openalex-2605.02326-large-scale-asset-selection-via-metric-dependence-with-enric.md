---
# CSL-compatible fields
title: "Large-Scale Asset Selection via Metric Dependence with Enriched High Frequency Information"
author:
  - literal: "Yangzhou Chen"
  - literal: "Shuaida He"
  - literal: "Xin Chen"
issued:
  date-parts:
    - [2026, 5, 4]
url: "https://arxiv.org/abs/2605.02326"

# Custom fields
paper_id: "2605.02326"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "metric-dependence-screening"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-07T07:38:33Z"
created_at: "2026-05-07T07:38:33Z"
---

# Large-Scale Asset Selection via Metric Dependence with Enriched High Frequency Information

**Authors**: Yangzhou Chen, Shuaida He, Xin Chen
**Date**: 2026-05-04
**Paper ID**: [openalex:2605.02326](https://arxiv.org/abs/2605.02326)

## Summary

This paper introduces Metric Dependence Screening (MDS), a novel asset selection framework designed to handle large-scale portfolio construction by incorporating intraday risk dynamics as object-valued point-curve data. By representing assets through a weighted product metric that captures both returns and within-day risk, MDS provides a robust, two-stage procedure that significantly reduces estimation error in high-dimensional settings. Theoretical guarantees for consistency are established, and experiments on a large-scale Chinese A-share dataset confirm that MDS consistently improves out-of-sample portfolio performance compared to traditional scalar-based selection rules.

## Key Contributions

- Introduced Metric Dependence Screening (MDS), a methodology for asset selection using point-curve object data that integrates intraday risk dynamics.
- Proved concentration, sure selection, and rank consistency guarantees for MDS under ultrahigh dimensionality and alpha-mixing dependence.
- Empirically demonstrated that MDS outperforms standard return-based and scalar-based selection benchmarks on a universe of 2,938 stocks using 5-minute frequency data.

## Open Questions & Future Work

- [[alternative-high-frequency-risk-signatures]]
- [[empirical-pipeline-with-constraints]]

## Key Concepts

- [[metric-dependence-screening]]: An asset selection procedure that uses object-valued data (point-curves) to capture both returns and intraday risk dynamics for large-scale portfolio construction.

## Archivist Review

The paper introduces a well-defined statistical screening methodology (MDS) that moves beyond simple returns to include intraday risk curves, which is a reusable concept. The approved open questions address the critical need for evaluating the framework's robustness against alternative risk signatures and practical market frictions. Routine datasets were excluded in line with the scarcity policy.

### Approved Concepts
- Metric Dependence Screening: Central asset selection procedure proposed for handling high-dimensional, intraday risk-aware portfolio construction.

### Approved Open Questions
- Alternative High-Frequency Risk Signatures: Identifying more informative risk signatures could significantly improve the quality of the asset universe passed to portfolio optimizers.
- Empirical Pipeline with Constraints: These considerations determine whether theoretical performance gains remain viable in actual trading environments.

## Links

- [Abstract](https://arxiv.org/abs/2605.02326)
- [PDF](https://arxiv.org/pdf/2605.02326)

