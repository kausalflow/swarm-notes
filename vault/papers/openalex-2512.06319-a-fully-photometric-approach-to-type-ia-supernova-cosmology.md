---
# CSL-compatible fields
title: "A Fully Photometric Approach to Type Ia Supernova Cosmology in the LSST Era: Host-galaxy Redshifts and Supernova Classification"
author:
  - literal: "Ayan Mitra"
  - literal: "Richard Kessler"
  - literal: "Rui Chen"
  - literal: "Alex Gagliano"
  - literal: "Matthew Grayling"
  - literal: "Surhud More"
  - literal: "Gautham Narayan"
  - literal: "Helen Qu"
  - literal: "Srinivasan Raghunathan"
  - literal: "Alex I. Malz"
  - literal: "Michelle Lochner"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2512.06319"

# Custom fields
paper_id: "2512.06319"
paper_source: "openalex"
domain: "computer-vision"
tags:
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
processed_at: "2026-07-22T07:30:23Z"
created_at: "2026-07-22T07:30:23Z"
---

# A Fully Photometric Approach to Type Ia Supernova Cosmology in the LSST Era: Host-galaxy Redshifts and Supernova Classification

**Authors**: Ayan Mitra, Richard Kessler, Rui Chen, Alex Gagliano, Matthew Grayling, Surhud More, Gautham Narayan, Helen Qu, Srinivasan Raghunathan, Alex I. Malz, Michelle Lochner
**Date**: 2026-07-20
**Paper ID**: [openalex:2512.06319](https://arxiv.org/abs/2512.06319)

## Summary

This paper develops a fully photometric cosmology pipeline for Type Ia supernovae in anticipation of the Vera C. Rubin Observatory's LSST, combining joint photometric redshift fitting, neural-network classification, and Bayesian bias corrections. Evaluating the pipeline on extensive simulations of ~6000 events across Deep Drilling Fields and low-redshift samples, the approach yields a dark energy figure of merit of ~150, outperforming previous surveys while exposing subtle systematic biases that require future development.

## Key Contributions

- Presents a fully photometric cosmological analysis framework for Type Ia supernovae tailored for the Vera C. Rubin Observatory's LSST era using simulations with realistic contamination, mis-associations, and transient-host correlations.
- Integrates joint SN and host photometric redshift fitting, a neural-network-based photometric classifier (SCNN), and Bayesian bias correction methodology to build a bias-corrected Hubble diagram and full covariance matrices.
- Achieves a cosmological figure of merit (FoM) of approximately 150 on a simulated sample of ~6000 events for wCDM and w0waCDM models, significantly outperforming DES-SN5YR (FoM = 54), while identifying small but significant systematic biases across 25 independent samples.

## Limitations

Averages analysis results over 25 independent samples and uncovers small but significant biases that highlight the need for further methodological refinement and testing.

## Open Questions & Future Work

- [[photometric-snia-cosmology-residual-biases]]

## Archivist Review

I applied strict selectivity filters, approving only the critical open question regarding residual systematic biases in fully photometric Type Ia supernova cosmology pipelines while rejecting domain-specific simulation pipeline components as non-reusable for general ML vault notes.

### Approved Open Questions
- Unresolved Biases in Photometric SNIa Cosmology: Addressing these residual biases is critical for ensuring that upcoming Rubin Observatory LSST cosmology analyses achieve systematic uncertainties competitive with statistical precision without biasing dark energy constraints.

### Rejected Candidates
- [open_question] Unresolved Biases in Photometric SNIa Cosmology (`photometric-snia-cosmology-residual-biases`) - generic: Approved as a standalone open question.

## Links

- [Abstract](https://arxiv.org/abs/2512.06319)
- [PDF](https://arxiv.org/pdf/2512.06319)

