---
# CSL-compatible fields
title: "Quantum Weighted Moving Average for Predicting Limit Order Book Trends"
author:
  - literal: "Matthias Kamm"
  - literal: "Dinh-Long Vu"
  - literal: "Patrick Rebentrost"
  - literal: "Quantum Weighted Moving Average for Predicting Limit Order Book Trends"
issued:
  date-parts:
    - [2026, 9, 1]
url: "https://arxiv.org/abs/2609.01524"

# Custom fields
paper_id: "2609.01524"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  - "fi-2010"
concept_slugs:
  - "quantum-weighted-moving-average"
dataset_slugs:
  - "fi-2010"
skill: "TimeSeriesSkill"
processed_at: "2026-09-04T09:11:08Z"
created_at: "2026-09-04T09:11:08Z"
---

# Quantum Weighted Moving Average for Predicting Limit Order Book Trends

**Authors**: Matthias Kamm, Dinh-Long Vu, Patrick Rebentrost, Quantum Weighted Moving Average for Predicting Limit Order Book Trends
**Date**: 2026-09-01
**Paper ID**: [openalex:2609.01524](https://arxiv.org/abs/2609.01524)

## Summary

This paper introduces the quantum weighted moving average (QWMA) model for forecasting price trends from limit order book (LOB) data, combining classical feature/temporal normalization with a linear combination of unitaries-based quantum layer. Evaluated on the FI-2010 benchmark and a China A-share dataset, the hybrid approach achieves performance close to leading classical models, though no quantum advantage is demonstrated. Specializations such as an exponential moving average (EMA) variant are also explored.

## Key Contributions

- Introduced the quantum weighted moving average (QWMA) model for limit order book trend prediction, combining classical preprocessing with a linear combination of unitaries-based quantum layer.
- Evaluated QWMA on the FI-2010 benchmark dataset and a China A-share stock dataset, showing performance close to top classical models without demonstrating quantum advantage.
- Proposed specializations of the QWMA model, including a variant corresponding to the exponential moving average (EMA).

## Limitations

No evidence of quantum advantage observed compared to classical counterparts; limitations in current quantum methods and financial datasets discussed.

## Open Questions & Future Work

- [[hardware-friendly-lcu-implementations-financial-ml]]

## Key Concepts

- [[quantum-weighted-moving-average]]: A hybrid classical-quantum model that combines feature/temporal normalization with a linear combination of unitaries-based layer for financial time series forecasting.

## Archivist Review

Approved the core quantum moving average concept and the hardware-friendly LCU open question since they capture a distinct, reusable hybrid quantum-classical forecasting methodology. Approved the FI-2010 dataset as a standard benchmark for limit order book forecasting. Applied strict scarcity rules.

### Approved Concepts
- Quantum Weighted Moving Average: Central methodological innovation for predicting limit order book trends using quantum-enhanced linear combination of unitaries.

### Approved Open Questions
- Hardware-Friendly LCU Implementations for Financial ML: Crucial for reducing the circuit overhead and qubit requirements of hybrid quantum-classical financial algorithms, making them more viable on near-term NISQ and early fault-tolerant hardware.

## Datasets

- [[fi-2010]]

## Links

- [Abstract](https://arxiv.org/abs/2609.01524)
- [PDF](https://arxiv.org/pdf/2609.01524)

