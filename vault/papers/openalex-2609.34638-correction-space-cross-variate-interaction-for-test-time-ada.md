---
# CSL-compatible fields
title: "Correction-space Cross-variate Interaction for Test-time Adaptation in Time Series Forecasting"
author:
  - literal: "Yuanyuan Deng"
  - literal: "Mykola Pechenizkiy"
  - literal: "Songgaojun Deng"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.34638"

# Custom fields
paper_id: "2609.34638"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "continual-learning"
  - "robustness"
  - "adaptation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:48:40Z"
created_at: "2026-09-30T10:48:40Z"
---

# Correction-space Cross-variate Interaction for Test-time Adaptation in Time Series Forecasting

**Authors**: Yuanyuan Deng, Mykola Pechenizkiy, Songgaojun Deng
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.34638](https://arxiv.org/abs/2609.34638)

## Summary

Test-time adaptation in multivariate time-series forecasting often struggles with cross-variate interactions because coupling variates through backbone predictions can propagate uncorrected errors. To address this, the authors propose CoRe, which shifts cross-variate interaction into the correction space by refining adapter corrections instead of raw predictions. CoRe utilizes Shared-anchor Correction Refinement and input-conditioned spectral gating to achieve substantial MSE reductions across multiple benchmarks with minimal overhead.

## Key Contributions

- Proposes CoRe (Correction-space Interaction Refinement) for multivariate time-series forecasting test-time adaptation, performing cross-variate interaction in the correction space rather than on predictions to prevent error propagation.
- Introduces Shared-anchor Correction Refinement (SCR) to combine variate-specific corrections with a shared anchor via a parameter-efficient bottleneck.
- Implements input-conditioned spectral gating to adaptively modulate refinement from the current input window.
- Reduces MSE by 25.82% on average over backbones and 10.57% over the state-of-the-art TSF-TTA method across seven backbones, six datasets, and four prediction horizons.

## Open Questions & Future Work

- [[extension-to-foundation-models-and-irregular-delays]]

## Archivist Review

Approved one explicit open question regarding foundation model and irregular delay extensions in test-time adaptation. Rejected CoRe and its sub-modules as paper-local methodological contributions since the vault already covers general test-time adaptation and forecasting adaptation paradigms.

### Approved Open Questions
- Extension to Foundation Models and Irregular Delays: Important for broadening the practical applicability of test-time adaptation techniques to modern large-scale time series foundation models and irregular streaming protocols.

### Rejected Candidates
- [concept] CoRe (Correction-space Interaction Refinement) (`core`) - subcomponent_of_broader_mechanism: The core method CoRe is a specific architectural framework for test-time adaptation, but the vault already contains broad methodologies for time series test-time adaptation and error mitigation, making this a paper-local method implementation rather than a foundational concept.
- [concept] Shared-anchor Correction Refinement (SCR) (`shared-anchor-correction-refinement-scr`) - subcomponent_of_broader_mechanism: This is a specific sub-module/component of the CoRe framework rather than an independent foundational concept.

## Links

- [Abstract](https://arxiv.org/abs/2609.34638)
- [PDF](https://arxiv.org/pdf/2609.34638)

