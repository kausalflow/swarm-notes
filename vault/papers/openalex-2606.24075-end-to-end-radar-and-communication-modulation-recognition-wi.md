---
# CSL-compatible fields
title: "End-to-End Radar and Communication Modulation Recognition with Neuromorphic Computing"
author:
  - literal: "Xiaohu Li"
  - literal: "Chongxiao Qu"
  - literal: "C Y Lin"
  - literal: "Chenxiao Dou"
  - literal: "Wei Hua"
issued:
  date-parts:
    - [2026, 6, 23]
url: "https://arxiv.org/abs/2606.24075"

# Custom fields
paper_id: "2606.24075"
paper_source: "openalex"
domain: "speech"
tags:
  - "transformer"
  - "attention-mechanism"
  - "spiking-neural-network"
  - "efficient-transformer"
  - "model-compression"
architectures:
  []
datasets:
  []
concept_slugs:
  - "emrformer"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-26T08:25:42Z"
created_at: "2026-06-26T08:25:42Z"
---

# End-to-End Radar and Communication Modulation Recognition with Neuromorphic Computing

**Authors**: Xiaohu Li, Chongxiao Qu, C Y Lin, Chenxiao Dou, Wei Hua
**Date**: 2026-06-23
**Paper ID**: [openalex:2606.24075](https://arxiv.org/abs/2606.24075)

## Summary

This paper introduces EMRFormer, an end-to-end spiking neural network (SNN) architecture specifically designed for energy-efficient automatic modulation recognition (AMR). By combining spike-separable CNN modules with spike-driven transformers, the model effectively extracts multi-scale temporal features from IQ waveforms while operating within the tight power constraints of neuromorphic hardware. Experimental results show that EMRFormer surpasses existing baselines in accuracy while providing significant power savings and maintaining robust performance in low signal-to-noise ratio conditions.

## Key Contributions

- Introduces EMRFormer, a spiking neural network architecture for end-to-end automatic modulation recognition.
- Achieves state-of-the-art accuracy in modulation recognition while reducing theoretical energy consumption by over 90%.
- Demonstrates real-world deployment on the KA200 neuromorphic chip with a 5x power reduction compared to traditional GPU/embedded systems.

## Open Questions & Future Work

- [[real-world-neuromorphic-validation]]

## Key Concepts

- [[emrformer]]: An end-to-end spiking transformer architecture for automatic modulation recognition using spike-driven inference.

## Archivist Review

The review prioritized the overarching neuromorphic architecture (EMRFormer) as a candidate for the vault while rejecting the submodule as an implementation detail. The open question was approved for its focus on the transition from simulated SNN benchmarks to real-world edge hardware deployment, which is a substantial bottleneck in the field.

### Approved Concepts
- EMRFormer: Central architecture for AMR that enables SNN-based modulation recognition on resource-constrained hardware.

### Approved Open Questions
- Real-world Neuromorphic System Validation: Transitioning from simulation or specific dataset evaluation to robust, real-world deployment is critical for the practical adoption of neuromorphic computing in field-deployed devices.

### Rejected Candidates
- [concept] Spike-Separable Convolutional Neural Network (SSCNN) (`spike-separable-convolutional-neural-network-sscnn`) - subcomponent_of_broader_mechanism: This is a local architectural subcomponent (a module within EMRFormer) rather than a broader, reusable mechanism for general forecasting or signal processing.

## Links

- [Abstract](https://arxiv.org/abs/2606.24075)
- [PDF](https://arxiv.org/pdf/2606.24075)

