---
# CSL-compatible fields
title: "Dynamical Parameters: An Interpretability Framework for Time-Series Foundation Models"
author:
  - literal: "Kang Yang"
  - literal: "Gaofeng Dong"
  - literal: "Liying Han"
  - literal: "Mani B. Srivastava"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.34316"

# Custom fields
paper_id: "2609.34316"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "interpretability"
  - "explainability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dynamical-parameters"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:48:48Z"
created_at: "2026-09-30T10:48:48Z"
---

# Dynamical Parameters: An Interpretability Framework for Time-Series Foundation Models

**Authors**: Kang Yang, Gaofeng Dong, Liying Han, Mani B. Srivastava
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.34316](https://arxiv.org/abs/2609.34316)

## Summary

This paper investigates the interpretability gap in time-series foundation models, revealing that while dynamical properties (like trend slope and oscillation frequency) are highly accessible in hidden states, models often fail to reflect these changes in their forecasts. The authors introduce 'Dynamical Parameters' and causal geometry to show that input interventions frequently move hidden states in directions misaligned with what is required for the correct forecast response.

## Key Contributions

- Formalizes dynamical parameters (trend slope, oscillation frequency, autoregressive dependence) to study time-series foundation model interpretability.
- Evaluates nine frozen time-series foundation models across thirteen laws, revealing a major gap between high representation accessibility (median > 0.95) and low forecast response (median 0.46).
- Introduces causal geometry to explain the accessibility-response gap by showing that parameter interventions frequently move hidden states in directions misaligned with the required forecast response.

## Open Questions & Future Work

- [[extending-tsfm-dynamical-interpretability]]

## Key Concepts

- [[dynamical-parameters]]: Formalized properties of time-series dynamics, such as trend slope and frequency, used to study interpretability and representation accessibility in foundation models.

## Archivist Review

Approved the central interpretability concept 'dynamical-parameters' and the core open question regarding extending TSFM dynamical interpretability, as they meet the vault's high bar for reusability, novelty, and conceptual independence.

### Approved Concepts
- Dynamical Parameters: Introduces a novel framework to formalize and measure hidden-state dynamical properties in time-series foundation models.

### Approved Open Questions
- Extending TSFM Dynamical Interpretability: Bridging the gap between internal parameter representation and external forecast expression is central to making time-series foundation models trustworthy and controllable for downstream decision-making.

## Links

- [Abstract](https://arxiv.org/abs/2609.34316)
- [PDF](https://arxiv.org/pdf/2609.34316)

