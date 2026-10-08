---
# CSL-compatible fields
title: "Latent Similarity Gaussian Processes: A Theory-Grounded Approach to Personalized Suicide-Risk Forecasting for Clinical Decision-Support"
author:
  - literal: "Yaniv Yacoby"
  - literal: "Weiwei Pan"
  - literal: "Hope Neveux"
  - literal: "Taylor C. McGuire"
  - literal: "Franchesca Castro-Ramirez"
  - literal: "Anushka Patel"
  - literal: "Matthew K. Nock"
  - literal: "Yaniv Yacoby"
  - literal: "Weiwei Pan"
  - literal: "Hope Neveux"
  - literal: "Taylor C. McGuire"
  - literal: "Franchesca Castro‐Ramirez"
  - literal: "Anushka Patel"
  - literal: "Matthew K. Nock"
issued:
  date-parts:
    - [2026, 10, 5]
url: "https://arxiv.org/abs/2610.06355"

# Custom fields
paper_id: "2610.06355"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "latent-similarity-gaussian-processes"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-08T11:41:24Z"
created_at: "2026-10-08T11:41:24Z"
---

# Latent Similarity Gaussian Processes: A Theory-Grounded Approach to Personalized Suicide-Risk Forecasting for Clinical Decision-Support

**Authors**: Yaniv Yacoby, Weiwei Pan, Hope Neveux, Taylor C. McGuire, Franchesca Castro-Ramirez, Anushka Patel, Matthew K. Nock, Yaniv Yacoby, Weiwei Pan, Hope Neveux, Taylor C. McGuire, Franchesca Castro‐Ramirez, Anushka Patel, Matthew K. Nock
**Date**: 2026-10-05
**Paper ID**: [openalex:2610.06355](https://arxiv.org/abs/2610.06355)

## Summary

The paper introduces Latent Similarity Gaussian Processes (LSGPs), a theory-grounded approach for personalized suicide-risk forecasting that embeds patients in a continuous latent space to jointly model similarity and forecast risk. By employing an identifiable two-channel similarity kernel and fixing a collapse vulnerability in mean-field variational inference, LSGPs generalize nomothetic, idiographic, and hierarchical modeling frameworks. Empirical evaluations on intensive longitudinal suicide data demonstrate that LSGPs outperform existing models for next-week forecasting, yielding the greatest improvements for predicting first-occurrence suicide-related events.

## Key Contributions

- Introduces Latent Similarity Gaussian Processes (LSGPs), embedding patients in a continuous latent space via an identifiable two-channel Similarity Kernel to jointly model similarity and forecast risk.
- Proves that standard mean-field variational inference collapses LSGPs to nomothetic models and provides an analytical fix.
- Demonstrates superior next-week risk forecasting performance over nomothetic, idiographic, and hierarchical baselines on intensive longitudinal suicide data, with maximal gains on first-occurrence suicide-related events.

## Open Questions & Future Work

- [[training-objectives-pac-bayes-selection]]

## Key Concepts

- [[latent-similarity-gaussian-processes]]: A Gaussian process model that embeds patients in a continuous latent space using a two-channel similarity kernel to jointly model patient similarity and forecast personalized risk.

## Archivist Review

Approved the core methodological concept (Latent Similarity Gaussian Processes) and one major open question addressing model selection under extreme class imbalance, while rejecting open-ended future work items that lack specific technical framing.

### Approved Concepts
- Latent Similarity Gaussian Processes: Central methodological contribution addressing patient heterogeneity and low base-rate forecasting via a theory-grounded Gaussian process framework.

### Approved Open Questions
- PAC-Bayes Generalization Bound Model Selection: Critical for ensuring that probabilistic models in healthcare are selected based on clinically meaningful metrics rather than uncalibrated marginal likelihoods under extreme class imbalance.

### Rejected Candidates
- [open_question] Clinical Grounding of Latent Similarity (`clinical-grounding-patient-similarity`) - low_impact: Future work direction is too application-specific and lacks formal mathematical framing.
- [open_question] Accounting for Temporal Dynamics (`temporal-dynamics-psychiatric-risk`) - low_impact: Broad future work suggestion proposing standard temporal extensions without a distinct methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.06355)
- [PDF](https://arxiv.org/pdf/2610.06355)

