---
# CSL-compatible fields
title: "Earth-o1: A Grid-free Observation-native Atmospheric World Model"
author:
  - literal: "Junchao Gong"
  - literal: "Kaiyi Xu"
  - literal: "Wangxu Wei"
  - literal: "Siwei Tu"
  - literal: "Siwei Tu"
  - literal: "Jingyi Xu"
  - literal: "Zili Liu"
  - literal: "Hang Fan"
  - literal: "Zhiwang Zhou"
  - literal: "Tao Han"
  - literal: "Yi Xiao"
  - literal: "Xinyu Gu"
  - literal: "Zhangrui Li"
  - literal: "Wenlong Zhang"
  - literal: "Hao Chen"
  - literal: "Xiaokang Yang"
  - literal: "Yaqiang Wang"
  - literal: "Lijing Cheng"
  - literal: "Pierre Gentine"
  - literal: "Wanli Ouyang"
  - literal: "Feng Zhang"
  - literal: "Zhe-Min Tan"
  - literal: "Bowen Zhou"
  - literal: "Fenghua Ling"
  - literal: "Ben Fei"
  - literal: "Lei Bai"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.06337"

# Custom fields
paper_id: "2605.06337"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "multimodal"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "observation-native-atmospheric-world-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:22:18Z"
created_at: "2026-05-10T07:22:18Z"
---

# Earth-o1: A Grid-free Observation-native Atmospheric World Model

**Authors**: Junchao Gong, Kaiyi Xu, Wangxu Wei, Siwei Tu, Siwei Tu, Jingyi Xu, Zili Liu, Hang Fan, Zhiwang Zhou, Tao Han, Yi Xiao, Xinyu Gu, Zhangrui Li, Wenlong Zhang, Hao Chen, Xiaokang Yang, Yaqiang Wang, Lijing Cheng, Pierre Gentine, Wanli Ouyang, Feng Zhang, Zhe-Min Tan, Bowen Zhou, Fenghua Ling, Ben Fei, Lei Bai
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.06337](https://arxiv.org/abs/2605.06337)

## Summary

Earth-o1 is an observation-native atmospheric world model that eschews traditional grid-based assimilation in favor of learning continuous, 3D physical dynamics directly from ungridded sensor data. By unifying heterogeneous inputs into a grid-free field, the model provides a scalable alternative for real-time atmospheric forecasting and cross-sensor inference. Evaluations demonstrate that this data-driven approach reaches the predictive fidelity of the Integrated Forecasting System (IFS) without relying on explicit numerical solvers.

## Key Contributions

- Introduced Earth-o1, a grid-free atmospheric world model that learns physical dynamics directly from heterogeneous, ungridded observational data.
- Eliminates the computational overhead of traditional numerical solvers and data assimilation by autonomously advancing atmospheric states in continuous space-time.
- Achieves surface forecasting performance comparable to the operational Integrated Forecasting System (IFS) in hindcast evaluations.

## Open Questions & Future Work

- [[probabilistic-geophysical-simulation]]
- [[generalized-geophysical-sensor-integration]]

## Key Concepts

- [[observation-native-atmospheric-world-model]]: An atmospheric modeling paradigm that directly learns three-dimensional physical evolution from ungridded observational data without numerical solvers.

## Archivist Review

I approved the 'Observation-native Atmospheric World Model' concept as it represents a significant methodological shift in geophysical forecasting away from traditional grid-constrained solvers. I also approved two open questions concerning probabilistic extension and multimodal integration, as these address fundamental bottlenecks in the scalability and completeness of such world models. Other candidates were rejected to maintain the strict curation standards of the vault.

### Approved Concepts
- Observation-native Atmospheric World Model: It represents a fundamental shift from grid-based assimilation to continuous, observation-driven modeling for atmospheric dynamics.

### Approved Open Questions
- Probabilistic Geophysical Simulation: Atmospheric and climate predictions are inherently chaotic; incorporating uncertainty is critical for risk assessment and reliable decision-making in real-world meteorological applications.
- Generalized Geophysical Sensor Integration: A comprehensive Earth digital twin requires integrating heterogeneous geophysical data across multiple spheres to fully capture complex Earth system interactions.

## Links

- [Abstract](https://arxiv.org/abs/2605.06337)
- [PDF](https://arxiv.org/pdf/2605.06337)

