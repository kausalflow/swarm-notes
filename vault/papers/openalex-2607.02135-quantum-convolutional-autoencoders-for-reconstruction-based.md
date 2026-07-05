---
# CSL-compatible fields
title: "Quantum Convolutional Autoencoders for Reconstruction-Based Anomaly Detection"
author:
  - literal: "Donovan Slabbert"
  - literal: "Francesco Petruccione"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.02135"

# Custom fields
paper_id: "2607.02135"
paper_source: "openalex"
domain: "speech"
tags:
  - "anomaly-detection"
  - "semi-supervised-learning"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "quantum-convolutional-autoencoder"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:53:23Z"
created_at: "2026-07-05T07:53:23Z"
---

# Quantum Convolutional Autoencoders for Reconstruction-Based Anomaly Detection

**Authors**: Donovan Slabbert, Francesco Petruccione
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.02135](https://arxiv.org/abs/2607.02135)

## Summary

This paper explores the adaptation of Quantum Convolutional Neural Networks (QCNNs) into a Quantum Autoencoder (QAE) framework designed for reconstruction-based anomaly detection. The authors compare two distinct architectures—one that maintains a distributed latent representation and one that utilizes an explicit bottleneck for compression—to evaluate their efficacy in reconstructing time-series features. Benchmarking against variational quantum circuits and classical baselines on an exoplanet dataset reveals that explicit bottleneck-based compression yields superior anomaly detection performance. The findings provide critical insights into the relationship between quantum latent space sizing and model capacity for anomaly detection tasks.

## Key Contributions

- Introduced a Quantum Convolutional Autoencoder (QAE) framework for anomaly detection using hierarchical and bottleneck-based circuit designs.
- Demonstrated that explicit bottleneck-based quantum latent space compression outperforms architectures retaining distributed quantum information for anomaly detection.
- Evaluated the model on a real-world exoplanet dataset, establishing a trade-off between latent space size, model capacity, and reconstruction accuracy.

## Open Questions & Future Work

- [[quantum-autoencoder-hardware-performance]]

## Key Concepts

- [[quantum-convolutional-autoencoder]]: A quantum autoencoder framework utilizing quantum convolutional layers to perform reconstruction-based anomaly detection on dimensionally reduced data.

## Archivist Review

I approved the Quantum Convolutional Autoencoder concept as it represents a core architectural novelty for hybrid quantum-classical anomaly detection. I also approved an open question regarding hardware-noise resilience for quantum autoencoders, as bridging the gap between simulation and real-world hardware is the primary bottleneck for this field. Other minor suggestions were rejected to maintain the required scarcity of the knowledge vault.

### Approved Concepts
- Quantum Convolutional Autoencoder: Central novelty: combines the hierarchical parameterization of quantum convolutional networks with the bottleneck-driven reconstruction of autoencoders for anomaly detection.

### Approved Open Questions
- Hardware-noise-resilience-for-QAE: Understanding the gap between simulated and hardware-based performance is crucial for the field of Quantum Machine Learning (QML) to move from theoretical demonstration to practical, real-world utility.

### Rejected Candidates
- [open_question] Hardware Validation of QAEs (`quantum-autoencoder-hardware-performance`) - other: Renamed to match the established slug format and to focus on the technical barrier rather than general validation.

## Links

- [Abstract](https://arxiv.org/abs/2607.02135)
- [PDF](https://arxiv.org/pdf/2607.02135)

