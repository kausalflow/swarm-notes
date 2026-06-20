---
# CSL-compatible fields
title: "ROSA-TFormer: A Radar-Optical Sensor-Aware Temporal Transformer for Pinus sylvestris Plantation Classification in Northern Shaanxi Using GEE-Derived Sentinel-1/2 Time Series"
author:
  - literal: "Nengbo Zhang"
  - literal: "Chang sheng"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.19204"

# Custom fields
paper_id: "2606.19204"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "transformer"
  - "multimodal"
  - "time-series"
  - "attention-mechanism"
  - "remote-sensing"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sensor-aware-temporal-fusion-architecture"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:17:48Z"
created_at: "2026-06-20T08:17:48Z"
---

# ROSA-TFormer: A Radar-Optical Sensor-Aware Temporal Transformer for Pinus sylvestris Plantation Classification in Northern Shaanxi Using GEE-Derived Sentinel-1/2 Time Series

**Authors**: Nengbo Zhang, Chang sheng
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.19204](https://arxiv.org/abs/2606.19204)

## Summary

ROSA-TFormer is a novel transformer-based architecture designed for the classification of Pinus sylvestris plantations by fusing radar (Sentinel-1) and optical (Sentinel-2) time-series data. The model employs a dual-branch embedding structure complemented by a sensor-aware gating mechanism to adaptively integrate multi-source seasonal features. Experimental results on the HalfMonth-dataBig dataset demonstrate that the model significantly outperforms traditional methods in classification accuracy. The study highlights the efficacy of integrating sensor-specific temporal representations for ecological monitoring.

## Key Contributions

- Proposes ROSA-TFormer, a novel sensor-aware temporal transformer for fusing Sentinel-1 (SAR) and Sentinel-2 (optical) time-series data.
- Introduces a sensor-aware gating mechanism and temporal attention pooling to effectively capture seasonal variations in vegetation patterns.
- Achieves 99.67% overall accuracy and 98.91% F1 score for Pinus sylvestris classification on the HalfMonth-dataBig dataset.

## Open Questions & Future Work

- [[point-to-wall-mapping-validation-gap]]

## Key Concepts

- [[sensor-aware-temporal-fusion-architecture]]: A transformer-based temporal fusion design that utilizes branch-specific feature embedding and sensor-aware gating to adaptively combine multi-source observational data.

## Archivist Review

I have approved the sensor-aware temporal fusion architecture as a reusable concept, as it generalizes the model's design for integrating heterogeneous remote sensing sources. I also approved the point-to-wall mapping validation gap, which correctly identifies a significant bottleneck in real-world application of point-based classification models. Other candidates were rejected as they were too specific to the paper's domain or local naming conventions.

### Approved Concepts
- Sensor-aware temporal fusion architecture: This architecture provides a modular approach to fusing heterogeneous time-series data (radar/optical) with gating mechanisms, which is a common challenge in remote sensing and earth observation forecasting.

### Approved Open Questions
- Point-to-wall mapping validation gap: This identifies a fundamental operational gap between proof-of-concept models and the utility of models in real-world large-scale environmental monitoring projects.

### Rejected Candidates
- [concept] ROSA-TFormer (`rosa-tformer`) - paper_local: The name is specific to the paper, while the architectural mechanism (sensor-aware gating for multi-source fusion) is better represented by a broader concept.
- [open_question] Species-specific conifer classification (`species-specific-conifer-classification`) - low_impact: This is a domain-specific ecological question rather than an ML methodology or time-series forecasting bottleneck.
- [dataset] HalfMonth-dataBig (`HalfMonth-dataBig`) - paper_local: This is a local experimental dataset subset not intended for broad research reuse.

## Links

- [Abstract](https://arxiv.org/abs/2606.19204)
- [PDF](https://arxiv.org/pdf/2606.19204)

