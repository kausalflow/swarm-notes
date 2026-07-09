---
# CSL-compatible fields
title: "Differentially private federated learning for localized control of infectious disease dynamics"
author:
  - literal: "Raouf Kerkouche"
  - literal: "Henrik Zunker"
  - literal: "Mario Fritz"
  - literal: "Martin J. Kühn"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2509.14024"

# Custom fields
paper_id: "2509.14024"
paper_source: "openalex"
domain: "medicine"
tags:
  - "federated-learning"
  - "differential-privacy"
  - "time-series"
  - "forecasting"
  - "privacy"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:18:31Z"
created_at: "2026-07-09T08:18:31Z"
---

# Differentially private federated learning for localized control of infectious disease dynamics

**Authors**: Raouf Kerkouche, Henrik Zunker, Mario Fritz, Martin J. Kühn
**Date**: 2026-07-06
**Paper ID**: [openalex:2509.14024](https://arxiv.org/abs/2509.14024)

## Summary

This study addresses the conflict between the need for localized infectious disease forecasting and data privacy constraints by employing a federated learning framework with client-level differential privacy. By training a shared multilayer perceptron across German health authorities, the approach enables accurate case count predictions without centralizing sensitive patient data. Results demonstrate that moderate privacy budgets preserve model utility, yielding performance metrics comparable to non-private baselines during significant pandemic phases.

## Key Contributions

- Demonstrates that client-level differentially private federated learning can provide useful COVID-19 case count forecasts at the county level without centralizing sensitive raw data.
- Evaluates the utility-privacy trade-off on real-world COVID-19 data across two epidemic phases (November 2020 and March 2022), showing competitive performance (MAPE of 0.16-0.20) at moderate epsilon values.
- Establishes a practical, privacy-preserving collaborative framework for local health authorities to improve forecasting accuracy using data pooled across multiple regions.

## Open Questions & Future Work

- [[privacy-utility-tradeoff-in-epidemic-fl]]
- [[community-scale-disease-forecasting-benchmarks]]

## Archivist Review

The paper applies established federated learning and differential privacy techniques to epidemiological forecasting. While the application is socially useful, the methodological contributions are incremental, so no new concepts or datasets were approved. Two open questions were refined to capture the broader research challenges regarding the privacy-utility tradeoff and the necessity of community-scale benchmarks for decentralized forecasting.

### Approved Open Questions
- Privacy-Utility Tradeoff in FL: As public health authorities increasingly rely on data-driven interventions, establishing robust, privacy-preserving collaborative forecasting frameworks is essential for reliable decision support.
- Community-Scale Disease Benchmarks: Establishing benchmarks for community-scale forecasting is vital for determining the scalability and real-world utility of federated learning in decentralized public health management.

### Rejected Candidates
- [open_question] Optimizing DP-FL for Epidemics (`dp-fl-optimization-epidemic-forecasting`) - duplicate_existing: Redundant with the newly refined privacy-utility tradeoff question which is more broadly applicable.
- [open_question] Community-Level Data Validation Needs (`community-level-data-validation-needs`) - duplicate_existing: Redundant with the newly refined community-scale benchmarks question.

## Links

- [Abstract](https://arxiv.org/abs/2509.14024)
- [PDF](https://arxiv.org/pdf/2509.14024)

