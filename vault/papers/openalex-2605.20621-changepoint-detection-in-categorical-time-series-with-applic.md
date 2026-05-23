---
# CSL-compatible fields
title: "Changepoint Detection in Categorical Time Series with Application to Daily Total Cloud Cover in Canada"
author:
  - literal: "Mo Li"
  - literal: "QiQi Lu"
  - literal: "XiaoLan Wang"
issued:
  date-parts:
    - [2026, 5, 20]
url: "https://arxiv.org/abs/2605.20621"

# Custom fields
paper_id: "2605.20621"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "statistical-modeling"
architectures:
  []
datasets:
  []
concept_slugs:
  - "marginalized-transition-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-23T07:25:17Z"
created_at: "2026-05-23T07:25:17Z"
---

# Changepoint Detection in Categorical Time Series with Application to Daily Total Cloud Cover in Canada

**Authors**: Mo Li, QiQi Lu, XiaoLan Wang
**Date**: 2026-05-20
**Paper ID**: [openalex:2605.20621](https://arxiv.org/abs/2605.20621)

## Summary

This paper presents a marginalized transition model designed for detecting changepoints in periodic and serially correlated categorical time series. By moving away from annual aggregation—which often leads to data loss and overdispersion—the proposed model leverages a first-order Markov chain to maintain the integrity of daily observations. The approach includes a novel parameter estimation procedure and a maximally selected likelihood ratio test to identify structural shifts in climate data, specifically demonstrating efficacy on daily cloud cover measurements.

## Key Contributions

- Introduces a marginalized transition model for changepoint detection that retains high-frequency daily data rather than relying on annual aggregation.
- Incorporates first-order Markov chains within the model to capture serial dependence and account for category-specific changepoint dynamics.
- Derives an efficient maximum likelihood estimation procedure and a corresponding likelihood ratio test statistic to detect structural shifts in categorical sequences.

## Open Questions & Future Work

- [[multiple-changepoint-detection-extension]]

## Key Concepts

- [[marginalized-transition-model]]: A statistical modeling framework for categorical time series that handles serial dependence via a Markov transition structure to detect structural changepoints.

## Archivist Review

I approved the Marginalized Transition Model as it provides a distinct, reusable statistical framework for categorical time series that avoids information loss from aggregation. I also approved the open question regarding multiple changepoint extension, as it addresses a fundamental limitation in the AMOC framework that is highly relevant to physical science datasets. The request for asymptotic theory proof was rejected as it is a standard theoretical requirement rather than a research direction that requires independent tracking.

### Approved Concepts
- Marginalized transition model: The model provides a principled statistical approach to handling categorical time series without the information loss associated with annual aggregation, accounting for serial dependence via a Markov chain.

### Approved Open Questions
- Multiple Changepoint Detection Extension: Most climate and physical observational time series exhibit multiple discontinuities, making the AMOC assumption a primary bottleneck for real-world homogenization tasks.

### Rejected Candidates
- [open_question] Asymptotic Theory for MTM Test (`asymptotic-distribution-mtm-changepoint-test`) - low_impact: Formal asymptotic proofs of test statistics are standard theoretical requirements rather than high-level research questions likely to be tracked as distinct advancements in this vault.

## Links

- [Abstract](https://arxiv.org/abs/2605.20621)
- [PDF](https://arxiv.org/pdf/2605.20621)

