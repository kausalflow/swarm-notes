---
# CSL-compatible fields
title: "Bayesian Synchronization of Proxy Paleorecords with Reference Chronologies"
author:
  - literal: "Marco A. Aquino‐López"
  - literal: "Francesco Muschitiello"
  - literal: "Matt Osman"
issued:
  date-parts:
    - [2026, 10, 25]
url: "https://arxiv.org/abs/2603.10218"

# Custom fields
paper_id: "2603.10218"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "uncertainty-quantification"
architectures:
  []
datasets:
  []
concept_slugs:
  - "bsync"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-27T10:06:36Z"
created_at: "2026-10-27T10:06:36Z"
---

# Bayesian Synchronization of Proxy Paleorecords with Reference Chronologies

**Authors**: Marco A. Aquino‐López, Francesco Muschitiello, Matt Osman
**Date**: 2026-10-25
**Paper ID**: [openalex:2603.10218](https://arxiv.org/abs/2603.10218)

## Summary

The authors introduce BSync, a Bayesian synchronization framework designed to align noisy proxy paleorecords with reference chronologies by framing time-warping as probabilistic inference over a monotone mapping function. By utilizing interpretable local rate parameters and deposition-time priors, BSync enforces physically plausible deformations while delivering rigorous posterior uncertainty quantification for aligned time scales. Experiments on synthetic data and real paleoclimate records demonstrate that BSync outperforms existing optimization-based alignment methods, particularly when independent age constraints are sparse.

## Key Contributions

- Introduces BSync, a Bayesian synchronization framework that treats time-series alignment as probabilistic inference over a monotone time-mapping function.
- Parametrizes the alignment transformation through interpretable local rate parameters and deposition-time priors to ensure physically plausible deformations.
- Provides joint posterior uncertainty quantification for the time-warping function and the resulting aligned time scale, outperforming optimization-based baselines under sparse independent age constraints.

## Open Questions & Future Work

- [[computational-efficiency-and-multi-record-joint-alignment]]

## Key Concepts

- [[bsync]]: A Bayesian synchronization framework for aligning proxy paleorecords to reference chronologies with formal uncertainty quantification.

## Archivist Review

Approved the core Bayesian synchronization framework 'BSync' as a reusable concept for time-series alignment and uncertainty quantification, along with a specific open question regarding its computational scaling and multi-record extension. No datasets met the strict curation bar.

### Approved Concepts
- BSync: It introduces the core methodological contribution of the paper: a Bayesian time-synchronization framework for aligning proxy paleorecords with formal uncertainty quantification.

### Approved Open Questions
- Computational Efficiency and Multi-Record Alignment: Improving computational efficiency and multi-record joint alignment capabilities is critical for scaling Bayesian proxy synchronization tools to handle large-scale paleoclimate data compilations and fully end-to-end uncertainty quantification workflows.

## Links

- [Abstract](https://arxiv.org/abs/2603.10218)
- [PDF](https://arxiv.org/pdf/2603.10218)

