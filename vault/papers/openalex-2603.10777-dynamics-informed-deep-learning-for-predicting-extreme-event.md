---
# CSL-compatible fields
title: "Dynamics-informed deep learning for predicting extreme events"
author:
  - literal: "Eirini Katsidoniotaki"
  - literal: "Themistoklis P. Sapsis"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2603.10777"

# Custom fields
paper_id: "2603.10777"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:44:58Z"
created_at: "2026-10-22T09:44:58Z"
---

# Dynamics-informed deep learning for predicting extreme events

**Authors**: Eirini Katsidoniotaki, Themistoklis P. Sapsis
**Date**: 2026-10-21
**Paper ID**: [openalex:2603.10777](https://arxiv.org/abs/2603.10777)

## Summary

Predicting rare extreme events in high-dimensional chaotic systems is challenging due to limited observations and transient dynamics. This paper introduces a dynamics-informed deep learning framework that uses finite-time Lyapunov exponents (FTLE) computed via optimal time-dependent (OTD) modes as mechanism-aware precursors. Feeding these sequence precursors into a transformer model enables long-lead forecasting of extreme events in Kolmogorov flow, outperforming standard observable-based baselines.

## Key Contributions

- Proposes a fully data-driven, mechanism-aware framework for real-time forecasting of extreme events in chaotic dynamical systems using finite-time Lyapunov exponents (FTLE) as precursors.
- Introduces a reduced-order, equation-agnostic FTLE formulation restricted to an adaptively evolving subspace spanned by optimal time-dependent (OTD) modes to reduce computational costs.
- Employs a transformer-based model taking the FTLE precursor sequence as input to forecast system observables at extended lead times.
- Demonstrates substantial improvements in prediction horizons compared to baseline observable-based approaches on Kolmogorov flow turbulence.

## Links

- [Abstract](https://arxiv.org/abs/2603.10777)
- [PDF](https://arxiv.org/pdf/2603.10777)

