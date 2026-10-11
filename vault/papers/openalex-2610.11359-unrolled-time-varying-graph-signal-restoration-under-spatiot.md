---
# CSL-compatible fields
title: "Unrolled Time-Varying Graph Signal Restoration under Spatiotemporal Smoothness Priors"
author:
  - literal: "Hayate Kojima"
  - literal: "Hikari Noguchi"
  - literal: "Koki Yamada"
  - literal: "Yuichi Tanaka"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.11359"

# Custom fields
paper_id: "2610.11359"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "graph-neural-network"
  - "optimization"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-11T11:05:14Z"
created_at: "2026-10-11T11:05:14Z"
---

# Unrolled Time-Varying Graph Signal Restoration under Spatiotemporal Smoothness Priors

**Authors**: Hayate Kojima, Hikari Noguchi, Koki Yamada, Yuichi Tanaka
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.11359](https://arxiv.org/abs/2610.11359)

## Summary

This paper introduces a deep algorithm unrolling (DAU) approach for restoring noisy and incomplete time-varying graph signals by leveraging spatiotemporal smoothness priors. The underlying optimization framework combines a spatial Sobolev operator with a temporal multi-tap FIR filter, which is solved by unrolling the iterative conjugate gradient method to learn parameters across iterations. Evaluated on synthetic and real-world datasets across supervised batch, online, and unsupervised batch settings, the proposed methods consistently outperform baseline techniques in their respective categories.

## Key Contributions

- Proposes time-varying graph signal restoration methods using deep algorithm unrolling (DAU) based on spatiotemporal smoothness priors.
- Formulates an optimization problem combining a spatial Sobolev operator and a temporal multi-tap FIR filter regularizer.
- Unrolls the iterative conjugate gradient method to learn regularization parameters and filter coefficients across iterations in supervised batch, supervised online, and unsupervised batch settings.
- Demonstrates via experiments on synthetic and real-world datasets that the supervised batch method achieves superior RMSE performance, while supervised online and unsupervised batch variants outperform existing methods in their respective settings.

## Archivist Review

Evaluated the paper on unrolled time-varying graph signal restoration. No concepts or open questions met the high bar for permanent standalone vault inclusion due to being overly domain-specific or incremental.

### Rejected Candidates
- [open_question] Learning Complex Temporal Priors (`learning-complex-temporal-priors-graph-signals`) - low_impact: The open question regarding learning complex temporal priors in graph signal processing is too incremental and narrow for permanent standalone vault inclusion.

## Links

- [Abstract](https://arxiv.org/abs/2610.11359)
- [PDF](https://arxiv.org/pdf/2610.11359)

