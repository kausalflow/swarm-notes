---
# CSL-compatible fields
title: "Near Linear Time Approximation Schemes for Clustering of Partially Doubling Metrics"
author:
  - literal: "Anne Driemel"
  - literal: "Jan Höckendorff"
  - literal: "Ioannis Psarros"
  - literal: "Christian Sohler"
  - literal: "Di Yue"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24336"

# Custom fields
paper_id: "2603.24336"
paper_source: "openalex"
domain: "algorithm"
tags:
  - "approximation"
  - "clustering"
  - "optimization"
  - "mathematical-reasoning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "partially-doubling-metrics-clustering"
  - "partially-doubling-dimension-reduction"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:30:17Z"
created_at: "2026-03-28T05:30:17Z"
---

# Near Linear Time Approximation Schemes for Clustering of Partially Doubling Metrics

**Authors**: Anne Driemel, Jan Höckendorff, Ioannis Psarros, Christian Sohler, Di Yue
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24336](https://arxiv.org/abs/2603.24336)

## Summary

This paper extends the $(1+\epsilon)$-approximation scheme for $k$-median from purely doubling metric spaces to partially doubling metrics, where only one of the sets ($X$ of points or $Y$ of potential centers) has a bounded doubling dimension. The authors achieve near linear time complexity, $2^{2^t} \tilde O(n+m)$, where $t$ depends on the doubling dimension ($\mathrm{ddim}$) and $\epsilon$. Key technical advancements include a novel dimension reduction for the case where the center set $Y$ is doubling, and a generalization of Talwar's decomposition for when the point set $X$ is doubling. These results also yield the first near linear time approximation for $(k,\ell)$-median under discrete Fréchet distance when $\ell$ is constant, and extend to the metric facility location problem.

## Key Contributions

- Generalization of near-linear time $(1+\epsilon)$-approximation schemes for $k$-median to partially doubling metrics (where either $X$ or $Y$ is doubling).
- First near linear time approximation algorithm for $(k,\ell)$-median under discrete Fréchet distance when $\ell$ is constant.
- Introduction of a complexity reduction for time series of real values leading to results for discrete Fréchet distance.
- Development of a dimension reduction technique replacing $X$ points by sets of $Y$ points to handle doubling $Y$ set, and generalization of Talwar's decomposition for doubling $X$ set.

## Limitations

The running time is exponential in a function of the doubling dimension $t=O(\mathrm{ddim} \log \frac{\mathrm{ddim}}ε)$, which is sub-linear in $n+m$ but not fully polynomial in the dimension.

## Key Concepts

- [[partially-doubling-metrics-clustering]]: Approximation schemes for $k$-median or facility location problems where only one partition ($X$ or $Y$) of the input points possesses a bounded doubling dimension.
- [[partially-doubling-dimension-reduction]]: A novel dimension reduction technique for $k$-median where the set of centers $Y$ has bounded doubling dimension, replacing points in $X$ with sets of points in $Y$.

## Archivist Review

Two core reusable concepts were approved: the generalization of approximation schemes to partially doubling metrics, which extends a fundamental problem class, and a specific, novel dimension reduction technique introduced for the $Y$-doubling case. Other specialized results, like the Fréchet distance extension or the generalization of Talwar's decomposition, were deemed subcomponents or applications of the main algorithmic framework and thus rejected.

### Approved Concepts
- Partially Doubling Metrics Clustering: This extends the class of metrics for which near-linear time approximation schemes exist for the $k$-median problem beyond purely doubling metrics.
- Dimensionality Reduction for Partially Doubling $k$-Median: It is a specific, novel technique developed to solve the case where the centers $Y$ have bounded doubling dimension, which is non-standard.

### Rejected Candidates
- [concept] Generalization of Talwar's Decomposition (`talwars-decomposition-generalization`) - subcomponent_of_broader_mechanism: The generalization of Talwar's decomposition is a method used to solve one specific case (doubling X) and is a subcomponent of the main result, making the overall mechanism ('Partially Doubling Metrics Clustering') the primary contribution.
- [concept] Near Linear Time $(k,\\ell)$-Median under Discrete Fréchet Distance (`k-ell-median-discrete-frechet`) - subcomponent_of_broader_mechanism: This is an application/result of the core algorithmic machinery (partially doubling metrics) rather than a novel reusable mechanism itself, and the time series complexity reduction is a technique, not the result.

## Links

- [Abstract](https://arxiv.org/abs/2603.24336)
- [PDF](https://arxiv.org/pdf/2603.24336)

