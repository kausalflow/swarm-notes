---
# CSL-compatible fields
title: "Learning to Program Adaptive Non-Local Observables for Machine Learning"
author:
  - literal: "Yu-Ting Lee"
  - literal: "Samuel Yen-Chi Chen"
  - literal: "Hua-an Tseng"
issued:
  date-parts:
    - [2026, 9, 16]
url: "https://arxiv.org/abs/2609.18655"

# Custom fields
paper_id: "2609.18655"
paper_source: "openalex"
domain: "time-series"
tags:
  - "reinforcement-learning"
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adaptive-non-local-observables"
  - "qfwp-ano"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-18T09:17:34Z"
created_at: "2026-09-18T09:17:34Z"
---

# Learning to Program Adaptive Non-Local Observables for Machine Learning

**Authors**: Yu-Ting Lee, Samuel Yen-Chi Chen, Hua-an Tseng
**Date**: 2026-09-16
**Paper ID**: [openalex:2609.18655](https://arxiv.org/abs/2609.18655)

## Summary

Quantum neural networks built from variational quantum circuits (VQCs) are often limited by static local measurements, while existing adaptive non-local observables (ANO) learn only input-invariant static observables. To overcome this, the authors propose QFWP-ANO, an architecture utilizing a classical hypernetwork to dynamically program VQC parameters and multi-qubit non-local observables conditioned on individual inputs. Evaluated on multivariate time-series forecasting across four ETT datasets and reinforcement learning tasks, QFWP-ANO consistently outperforms static ANO-based and conventional strong baselines.

## Key Contributions

- Proposes QFWP-ANO, a novel architecture that employs a classical hypernetwork to dynamically program VQC parameters and/or non-local observables conditioned on each input.
- Achieves the lowest MSE in 16 of 20 settings and second-lowest in the remaining 4 across four ETT multivariate time-series forecasting datasets, outperforming static ANO-based and strong baselines.
- Consistently surpasses standard ANO-VQCs on reinforcement learning tasks, establishing input-conditioned ANO as an effective approach for enhancing quantum neural networks.

## Key Concepts

- [[adaptive-non-local-observables]]: A method that dynamically programs variational quantum circuit parameters and multi-qubit measurements conditioned on each input using a classical hypernetwork.
- [[qfwp-ano]]: A novel quantum neural network architecture that employs a classical hypernetwork to dynamically program circuit parameters and multi-qubit observables per input.

## Archivist Review

Evaluated candidates against the stringent vault standards for time series and quantum machine learning. Approved the core architectural concepts 'Adaptive Non-Local Observables' and 'QFWP-ANO' as they represent a distinct methodological innovation in hypernetwork-guided quantum measurements. No datasets or open questions met the bar for permanent notes.

### Approved Concepts
- Adaptive Non-Local Observables: Introduces input-conditioned adaptive non-local observables via a hypernetwork for quantum neural networks, outperforming static ANO approaches.
- QFWP-ANO: Serves as the core architecture combining hypernetworks and adaptive non-local observables for quantum neural networks.

## Links

- [Abstract](https://arxiv.org/abs/2609.18655)
- [PDF](https://arxiv.org/pdf/2609.18655)

