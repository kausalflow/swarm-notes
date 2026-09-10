---
# CSL-compatible fields
title: "Improving Multivariate Time Series Classification with Class-Wise Training and Model Aggregation"
author:
  - literal: "Mouhamadou Mansour Lo"
  - literal: "Gildąs Morvan"
  - literal: "Mathieu Rossi"
  - literal: "Fabrice Morganti"
  - literal: "David Mercier"
issued:
  date-parts:
    - [2026, 9, 7]
url: "https://arxiv.org/abs/2609.07493"

# Custom fields
paper_id: "2609.07493"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "classification"
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
processed_at: "2026-09-10T09:15:58Z"
created_at: "2026-09-10T09:15:58Z"
---

# Improving Multivariate Time Series Classification with Class-Wise Training and Model Aggregation

**Authors**: Mouhamadou Mansour Lo, Gildąs Morvan, Mathieu Rossi, Fabrice Morganti, David Mercier
**Date**: 2026-09-07
**Paper ID**: [openalex:2609.07493](https://arxiv.org/abs/2609.07493)

## Summary

This paper introduces a class-wise dimension selection framework for Multivariate Time Series Classification (MTSC) that independently identifies informative channels for each class, trains dedicated models, and fuses them for final prediction. By focusing on class-specific feature representations and reducing the impact of noisy dimensions, the approach enhances classification performance and interpretability, especially in high-dimensional settings when paired with random kernel methods like MiniRocket.

## Key Contributions

- Proposes a class-wise dimension (channel) selection framework for multivariate time series classification that independently identifies informative dimensions for each class.
- Implements a dedicated learning process per class followed by a fusion stage for final prediction to reduce the influence of noisy or non-informative dimensions.
- Demonstrates improved representation quality and classification performance, particularly in high-dimensional settings, when integrated with random kernel-based baselines like MiniRocket.

## Limitations

Evaluated primarily using MiniRocket as a baseline method; broader applicability across diverse neural architectures requires further investigation.

## Archivist Review

Strictly followed the review policy by enforcing zero concept approvals due to a lack of universally reusable novel methods and rejecting the boilerplate future work open question as low impact.

### Rejected Candidates
- [open_question] Class-Wise MTSC Framework Extensions and ChannelScorer Adaptation (`class-wise-mtsc-framework-extensions-and-channel-scorer-adaptation`) - low_impact: Standard future work proposing framework extensions to other baselines and architectural variants without specifying a deep unresolved theoretical limitation.

## Links

- [Abstract](https://arxiv.org/abs/2609.07493)
- [PDF](https://arxiv.org/pdf/2609.07493)

