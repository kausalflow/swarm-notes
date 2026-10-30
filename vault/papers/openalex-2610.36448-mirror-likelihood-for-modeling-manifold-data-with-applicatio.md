---
# CSL-compatible fields
title: "Mirror Likelihood for Modeling Manifold Data with Application on Correlation Time Series"
author:
  - literal: "Luis Hasenauer"
  - literal: "Arkaprava Roy"
  - literal: "Leo L. Duan"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.36448"

# Custom fields
paper_id: "2610.36448"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "uncertainty-quantification"
  - "bayesian"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-30T11:04:52Z"
created_at: "2026-10-30T11:04:52Z"
---

# Mirror Likelihood for Modeling Manifold Data with Application on Correlation Time Series

**Authors**: Luis Hasenauer, Arkaprava Roy, Leo L. Duan
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.36448](https://arxiv.org/abs/2610.36448)

## Summary

The paper introduces mirror likelihood, a novel extrinsic framework for modeling manifold-valued data by treating the data as the Fenchel mirror map of a nearly unconstrained latent variable modeled by a canonical distribution. This augmented Bayesian framework avoids intractable normalization constants while enabling principled uncertainty quantification and flexible model extensions. The utility of the method is demonstrated on high-dimensional, rank-deficient correlation time series from neuroimaging data.

## Key Contributions

- Proposes mirror likelihood, an augmented likelihood framework for manifold-valued data utilizing the Fenchel mirror map to connect a nearly unconstrained latent variable with a canonical distribution.
- Develops a Bayesian implementation that provides a generative model interpretation, avoids intractable normalization constants, and supports principled uncertainty quantification.
- Demonstrates empirical utility on high-dimensional correlation time series involving rank-deficient correlation matrices in neuroimaging applications.

## Open Questions & Future Work

- [[learning-unknown-manifold-support-mirror-likelihood]]

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 0 concept(s), 1 open question(s), and 0 dataset(s), with 1 rejected candidate note(s).

### Approved Open Questions
- Learning Unknown Manifold Support: Extending manifold-based models to learn or adapt to unknown supports is crucial for handling real-world noisy data where the precise manifold constraint is misspecified or missing.

### Rejected Candidates
- [concept] Mirror Likelihood (`mirror-likelihood`) - not_reusable: While novel to the paper, the specific 'mirror likelihood' framing is a paper-local formulation of Fenchel conjugate latent transformations for manifold data that is not yet established as a recurring standalone concept in time series forecasting or broader machine learning literature.

## Links

- [Abstract](https://arxiv.org/abs/2610.36448)
- [PDF](https://arxiv.org/pdf/2610.36448)

