---
# CSL-compatible fields
title: "Prediction of chaotic dynamics from data: An introduction"
author:
  - literal: "Luca Magri"
  - literal: "Andrea Nóvoa"
  - literal: "Elise Özalp"
  - literal: "Luca Magri"
  - literal: "Andrea Nóvoa"
  - literal: "Elise Özalp"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2604.11624"

# Custom fields
paper_id: "2604.11624"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "recurrent-neural-network"
  - "lstm"
  - "rnn"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:29:10Z"
created_at: "2026-04-16T06:29:10Z"
---

# Prediction of chaotic dynamics from data: An introduction

**Authors**: Luca Magri, Andrea Nóvoa, Elise Özalp, Luca Magri, Andrea Nóvoa, Elise Özalp
**Date**: 2026-04-13
**Paper ID**: [openalex:2604.11624](https://arxiv.org/abs/2604.11624)

## Summary

This chapter provides a comprehensive, pedagogical overview of predicting chaotic systems using data-driven machine learning approaches. It bridges dynamical systems theory with deep learning architectures like Echo State Networks and LSTMs to address the challenges inherent in chaotic forecasting. The work is supported by illustrative examples from prototypical chaotic systems and accompanying online tutorials to facilitate practical implementation.

## Key Contributions

- Provides a principled integration of dynamical systems theory with machine learning for the prediction of chaotic processes.
- Examines the utility of Echo State Networks (ESNs) and LSTM networks specifically for modeling chaotic time-series dynamics.
- Offers a pedagogical framework for bridge building between theoretical chaos theory and applied time-series forecasting.

## Open Questions & Future Work

- [[stability-metrics-finite-perturbations-in-data-driven-forecasting]]

## Archivist Review

This paper serves as an educational review article and does not introduce novel technical architectures or forecasting mechanisms that warrant a permanent concept entry. However, the identified open question regarding the transition from infinitesimal Lyapunov-based stability analysis to finite-amplitude analysis in data-driven models is a central, recurring challenge in applying ML to chaotic dynamical systems, thus it is approved.

### Approved Open Questions
- Stability metrics for finite perturbations: This is a fundamental limitation in validating the reliability of neural network surrogates for chaotic dynamical systems, which often operate in finite-amplitude regimes rather than the infinitesimal linear limit.

### Rejected Candidates
- [concept] Principled integration of dynamical systems and machine learning (`principled-integration-of-dynamical-systems-and-machine-learning`) - generic: This is a high-level goal rather than a specific, reusable technical concept or methodology.
- [concept] Pedagogical framework for chaos forecasting (`pedagogical-framework-for-chaos-forecasting`) - paper_local: This describes the nature of the publication rather than a reusable technical artifact or mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2604.11624)
- [PDF](https://arxiv.org/pdf/2604.11624)

