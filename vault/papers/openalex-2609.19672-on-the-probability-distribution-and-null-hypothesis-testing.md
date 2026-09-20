---
# CSL-compatible fields
title: "On the Probability Distribution and Null-hypothesis Testing of Cross-correlation for Light Curves in Active Galactic Nuclei"
author:
  - literal: "Yan-Rong Li"
  - literal: "Jian-Min Wang"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.19672"

# Custom fields
paper_id: "2609.19672"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-20T09:31:05Z"
created_at: "2026-09-20T09:31:05Z"
---

# On the Probability Distribution and Null-hypothesis Testing of Cross-correlation for Light Curves in Active Galactic Nuclei

**Authors**: Yan-Rong Li, Jian-Min Wang
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.19672](https://arxiv.org/abs/2609.19672)

## Summary

This paper addresses the lack of a proper statistical framework for assessing cross-correlation significance in active galactic nuclei (AGN) reverberation mapping. The authors leverage stochastic time series theory to show that the probability distribution of cross-correlation coefficients for independent stochastic light curves asymptotically approaches a normal distribution, with variance analytically determinable from auto-correlation functions. Through Monte Carlo simulations, they validate this property for irregularly sampled red-noise AGN light curves and introduce a fast null-hypothesis testing procedure.

## Key Contributions

- Establishes that the probability distribution of cross-correlation coefficients for independent stochastic light curves asymptotically approaches a normal distribution whose variance can be analytically estimated via auto-correlation functions.
- Validates this asymptotic normality property via Monte Carlo simulations for irregularly sampled, red-noise AGN light curves.
- Proposes a fast analytical null-hypothesis testing procedure for cross-correlation analysis in active galactic nuclei reverberation mapping.

## Limitations

The long-standing issue regarding unbiasedly recovering the auto-correlation function remains unresolved when light-curve duration is comparable to the typical variation timescale.

## Open Questions & Future Work

- [[reliable-damping-timescale-inference]]

## Archivist Review

I reviewed the paper analysis and confirmed that no standalone architectural concepts or reusable datasets meet our high threshold for vault inclusion. One open question regarding reliable damping timescale inference for short-duration time series was approved as a valuable research tracking point.

### Approved Open Questions
- Reliable Damping Timescale Inference: Accurate inference of variability parameters such as damping timescales is essential for calculating reliable variances and significance levels in null-hypothesis testing for cross-correlation.

### Rejected Candidates
- [concept] Asymptotic Normality of Cross-correlation Coefficients (`asymptotic-normality-cross-correlation`) - not_novel: Standard statistical result derived from stochastic process theory rather than a newly introduced architectural concept or algorithmic framework.

## Links

- [Abstract](https://arxiv.org/abs/2609.19672)
- [PDF](https://arxiv.org/pdf/2609.19672)

