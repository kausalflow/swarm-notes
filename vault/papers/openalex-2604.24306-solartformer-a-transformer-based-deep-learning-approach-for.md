---
# CSL-compatible fields
title: "SolarTformer: A Transformer Based Deep Learning Approach for Short Term Solar Power Forecasting"
author:
  - literal: "Ankan Basu"
  - literal: "J.C. Roy"
  - literal: "Aditya Datta"
  - literal: "Prayas Sanyal"
  - literal: "Sumanta Banerjee"
issued:
  date-parts:
    - [2026, 4, 27]
url: "https://arxiv.org/abs/2604.24306"

# Custom fields
paper_id: "2604.24306"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "self-attention"
  - "time-series"
  - "forecasting"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "metadata-conditioned-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-30T07:24:20Z"
created_at: "2026-04-30T07:24:20Z"
---

# SolarTformer: A Transformer Based Deep Learning Approach for Short Term Solar Power Forecasting

**Authors**: Ankan Basu, J.C. Roy, Aditya Datta, Prayas Sanyal, Sumanta Banerjee
**Date**: 2026-04-27
**Paper ID**: [openalex:2604.24306](https://arxiv.org/abs/2604.24306)

## Summary

SolarTformer is a transformer-inspired deep learning model designed for short-term solar power forecasting using meteorological inputs. By leveraging self-attention, the model effectively captures the temporal dynamics and spatial variability inherent in solar irradiance. Furthermore, the inclusion of station-specific metadata allows the model to generalize across heterogeneous power stations and varying seasonal configurations. Experimental results confirm that the approach offers significant improvements over existing baselines, maintaining high robustness under fluctuating weather conditions.

## Key Contributions

- Introduces SolarTformer, an attention-based architecture that utilizes self-attention to capture complex temporal and spatial dependencies in solar irradiance.
- Demonstrates that incorporating station-specific metadata (e.g., location, panel configuration) enables the model to generalize effectively across diverse power stations and seasonal conditions.
- Achieves superior forecasting accuracy compared to existing models on both clear and cloudy days, enhancing robustness for renewable energy management.

## Open Questions & Future Work

- [[efficient-transformer-deployment-on-edge-devices]]
- [[robustness-to-extreme-weather-events]]

## Key Concepts

- [[metadata-conditioned-forecasting]]: A strategy for improving forecasting generalizability by incorporating site-specific or system-specific static metadata alongside temporal features.

## Archivist Review

I approved 'Metadata-Conditioned Forecasting' to capture the paper's key architectural contribution in a reusable, domain-agnostic way. I also approved two open questions concerning edge-efficiency and extreme-event robustness, renaming them for better consistency with the existing vault. SolarTformer itself was rejected as a paper-local implementation name.

### Approved Concepts
- Metadata-Conditioned Forecasting: Integrating static metadata into temporal forecasting pipelines is a recurring challenge for domain-specific generalization (e.g., renewable energy, healthcare).

### Approved Open Questions
- Efficient Transformer Edge Deployment: Enabling complex temporal models to operate on edge hardware is essential for decentralized energy management and real-time inference in remote locations.
- Extreme Weather Robustness: Reliable forecasting during extreme events is critical for grid stability and the prevention of system-wide failures.

### Rejected Candidates
- [concept] SolarTformer (`solartformer`) - paper_local: The model name is specific to this study and lacks broader, abstract utility as a general methodology; metadata-conditioned forecasting captures the contribution more effectively.
- [open_question] Efficient Transformer Deployment on Edge (`transformer-efficiency-edge-deployment`) - duplicate_existing: Redundant to the newly created and better-named equivalent slug.
- [open_question] Robustness to Extreme Weather Events (`generalization-extreme-weather-forecasting`) - duplicate_existing: Redundant to the newly created and better-named equivalent slug.

## Links

- [Abstract](https://arxiv.org/abs/2604.24306)
- [PDF](https://arxiv.org/pdf/2604.24306)

