---
# CSL-compatible fields
title: "Physics-Enhanced Deep Learning for Proactive Thermal Runaway Forecasting in Li-Ion Batteries"
author:
  - literal: "Salman Khan"
  - literal: "Muhammad Zunair Zamir"
  - literal: "Syed Sajid Ullah"
  - literal: "Jie Li"
issued:
  date-parts:
    - [2026, 4, 22]
url: "https://arxiv.org/abs/2604.20175"

# Custom fields
paper_id: "2604.20175"
paper_source: "openalex"
domain: "time-series"
tags:
  - "lstm"
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "physics-informed-long-short-term-memory-pi-lstm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-25T06:15:38Z"
created_at: "2026-04-25T06:15:38Z"
---

# Physics-Enhanced Deep Learning for Proactive Thermal Runaway Forecasting in Li-Ion Batteries

**Authors**: Salman Khan, Muhammad Zunair Zamir, Syed Sajid Ullah, Jie Li
**Date**: 2026-04-22
**Paper ID**: [openalex:2604.20175](https://arxiv.org/abs/2604.20175)

## Summary

This paper presents a Physics-Informed Long Short-Term Memory (PI-LSTM) framework designed to predict thermal runaway in lithium-ion batteries by incorporating heat transfer equations into the training loss. By enforcing thermodynamic constraints on temperature evolution, the model addresses the physical inconsistency common in pure data-driven approaches like standard LSTMs. Experimental results across thirteen battery datasets confirm that the proposed PI-LSTM achieves significant reductions in forecasting error and maintains physical validity, enabling more reliable real-time thermal management.

## Key Contributions

- Introduced a Physics-Informed LSTM (PI-LSTM) framework that embeds heat transfer physics into the loss function to enforce thermodynamic consistency.
- Achieved an 81.9% reduction in RMSE and 81.3% reduction in MAE for temperature evolution forecasting compared to standard LSTM baselines.
- Demonstrated superior generalization and elimination of non-physical oscillations across thirteen diverse lithium-ion battery operating conditions.

## Open Questions & Future Work

- [[multidimensional-hybrid-battery-thermal-forecasting]]

## Key Concepts

- [[physics-informed-long-short-term-memory-pi-lstm]]: A neural network framework that integrates thermodynamic differential equations into the loss function of an LSTM for physically consistent time-series forecasting.

## Archivist Review

The paper is approved for the PI-LSTM concept, which represents a clear methodological integration of physical constraints into recurrent neural networks. The open question is approved because it addresses the inherent limitations of 1D physical models in complex battery management scenarios. No specific datasets were named in the paper, so none could be approved.

### Approved Concepts
- Physics-Informed Long Short-Term Memory (PI-LSTM): It serves as the core methodological contribution, bridging the gap between data-driven LSTM networks and physics-based models for thermal forecasting.

### Approved Open Questions
- Multidimensional Hybrid Thermal Forecasting: Current models often simplify thermal dynamics to 1D representations, which may fail to capture the complex, spatially distributed thermal gradients and coupled electrochemical-thermal failure mechanisms present during real-world thermal runaway.

## Links

- [Abstract](https://arxiv.org/abs/2604.20175)
- [PDF](https://arxiv.org/pdf/2604.20175)

