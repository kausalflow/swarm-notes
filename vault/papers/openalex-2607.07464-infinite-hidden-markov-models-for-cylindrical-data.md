---
# CSL-compatible fields
title: "Infinite hidden Markov models for cylindrical data"
author:
  - literal: "Federico P. Cortese"
  - literal: "Luca Rossini"
issued:
  date-parts:
    - [2026, 7, 8]
url: "https://arxiv.org/abs/2607.07464"

# Custom fields
paper_id: "2607.07464"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "statistical-model"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-11T07:05:46Z"
created_at: "2026-07-11T07:05:46Z"
---

# Infinite hidden Markov models for cylindrical data

**Authors**: Federico P. Cortese, Luca Rossini
**Date**: 2026-07-08
**Paper ID**: [openalex:2607.07464](https://arxiv.org/abs/2607.07464)

## Summary

This paper introduces an infinite hidden Markov model tailored for cylindrical time series, which combine circular and linear data components. The model employs von Mises-Gamma emission distributions to effectively account for circular-linear dependencies within the state-space framework. Posterior inference is facilitated by a beam sampler that balances exact conjugate updates with approximate sampling strategies, showing strong performance in both simulation and real-world application scenarios.

## Key Contributions

- Introduces an infinite hidden Markov model (iHMM) specifically designed for cylindrical data types.
- Utilizes von Mises-Gamma distributions as emission probabilities to capture circular-linear dependencies.
- Develops a beam sampler for efficient posterior inference by integrating conjugate updates with approximate sampling techniques.

## Open Questions & Future Work

- [[cylindrical-time-series-dependence-persistence]]

## Archivist Review

I have rejected the model-specific and distribution-specific proposals as they are either standard statistical techniques or overly tied to the specific HMM implementation. I approved the open question regarding cylindrical data modeling because it explicitly highlights the limitation of state persistence in HMMs and points toward a higher-level methodological transition to semi-Markov models.

### Approved Open Questions
- Cylindrical data modeling enhancements: Improving the handling of component correlation and state duration dynamics is critical for extending HMM-based approaches to more realistic, complex environmental and biological signals.

### Rejected Candidates
- [concept] Infinite hidden Markov models for cylindrical data (`infinite-hidden-markov-models-for-cylindrical-data`) - not_reusable: This is a specific model instantiation rather than a general methodology or architectural innovation suitable for a permanent concept note.
- [concept] Von Mises-Gamma emissions (`von-mises-gamma-emissions`) - subcomponent_of_broader_mechanism: This is a statistical probability distribution choice rather than a reusable forecasting concept or mechanism.
- [concept] Beam sampler for iHMM (`beam-sampler-for-ihmm`) - not_novel: This is a specific MCMC inference algorithm which is standard in the HMM literature and not a novel methodology.

## Links

- [Abstract](https://arxiv.org/abs/2607.07464)
- [PDF](https://arxiv.org/pdf/2607.07464)

