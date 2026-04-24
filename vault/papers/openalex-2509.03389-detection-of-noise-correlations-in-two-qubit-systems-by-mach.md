---
# CSL-compatible fields
title: "Detection of noise correlations in two qubit systems by machine learning"
author:
  - literal: "Dario Fasone"
  - literal: "Shreyasi Mukherjee"
  - literal: "Dario Penna"
  - literal: "Fabio Cirinnà"
  - literal: "Mauro Paternostro"
  - literal: "Elisabetta Paladino"
  - literal: "Luigi Giannelli"
  - literal: "G. Falci"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2509.03389"

# Custom fields
paper_id: "2509.03389"
paper_source: "openalex"
domain: "physics"
tags:
  - "reinforcement-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ml-assisted-quantum-noise-sensing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T07:01:23Z"
created_at: "2026-04-24T07:01:23Z"
---

# Detection of noise correlations in two qubit systems by machine learning

**Authors**: Dario Fasone, Shreyasi Mukherjee, Dario Penna, Fabio Cirinnà, Mauro Paternostro, Elisabetta Paladino, Luigi Giannelli, G. Falci
**Date**: 2026-04-21
**Paper ID**: [openalex:2509.03389](https://arxiv.org/abs/2509.03389)

## Summary

This paper proposes a machine-learning assisted quantum sensing protocol to characterize the noise environment of ultrastrongly coupled qubits. By training a shallow neural network on final transfer efficiencies from a coherent population transfer protocol, the method distinguishes between six different Markovian and non-Markovian noise models. This approach demonstrates a classification accuracy exceeding 94% while requiring minimal experimental resources compared to traditional time-series measurement methods.

## Key Contributions

- Introduces a machine-learning assisted quantum sensing protocol for classifying six classes of Markovian and non-Markovian noise in two-qubit systems.
- Achieves over 94% classification accuracy by measuring only final transfer efficiencies under three driving conditions.
- Demonstrates that shallow neural networks can effectively identify noise correlations without requiring time-series data or real-time monitoring.

## Key Concepts

- [[ml-assisted-quantum-noise-sensing]]: A quantum sensing protocol that uses machine learning to classify noise correlations in multi-qubit systems based on final transfer efficiencies.

## Archivist Review

The paper introduces a specialized sensing protocol that leverages final transfer efficiencies rather than complex time-series data to classify noise in quantum systems. This is a distinct and potentially reusable paradigm for quantum hardware characterization, justifying the approval of the proposed concept. No other candidates were provided, and the framework for noise identification is sufficiently novel to merit a permanent vault entry.

### Approved Concepts
- ML-Assisted Quantum Noise Sensing: Provides a novel framework for noise characterization in quantum systems that avoids expensive time-series measurements by utilizing transfer efficiency data from coherent protocols.

## Links

- [Abstract](https://arxiv.org/abs/2509.03389)
- [PDF](https://arxiv.org/pdf/2509.03389)

