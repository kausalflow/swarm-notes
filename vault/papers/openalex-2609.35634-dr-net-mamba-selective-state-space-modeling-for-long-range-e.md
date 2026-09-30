---
# CSL-compatible fields
title: "DR-net-Mamba: Selective State-Space Modeling for Long-Range ECG Time-Series Denoising"
author:
  - literal: "Basile Morel"
  - literal: "Samuel Ruiperez-Campillo"
  - literal: "Andreas P. Streich"
  - literal: "Julia Elisabeth Vogt"
  - literal: "Thomas Hofmann"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.35634"

# Custom fields
paper_id: "2609.35634"
paper_source: "openalex"
domain: "biology"
tags:
  - "mamba"
  - "state-space-model"
  - "ssm"
  - "time-series"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dr-net-mamba"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:50:35Z"
created_at: "2026-09-30T10:50:35Z"
---

# DR-net-Mamba: Selective State-Space Modeling for Long-Range ECG Time-Series Denoising

**Authors**: Basile Morel, Samuel Ruiperez-Campillo, Andreas P. Streich, Julia Elisabeth Vogt, Thomas Hofmann
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.35634](https://arxiv.org/abs/2609.35634)

## Summary

This paper introduces DR-net-Mamba, a selective state-space model that integrates Mamba blocks at the convolutional bottleneck to achieve linear-complexity long-range ECG denoising. Evaluated on synthetic and real datasets across over 40 pathology classes, the model outperforms traditional convolutional, transformer, and diffusion denoisers in reconstruction fidelity and macro AUROC. The approach is particularly effective for low-SNR regimes, long sequence lengths, and context-sensitive morphological abnormalities such as ST/T-changes.

## Key Contributions

- Proposes DR-net-Mamba, integrating selective state-space blocks at a convolutional bottleneck for linear-complexity long-range ECG denoising.
- Achieves highest SNR and lowest RMSE on synthetic and real datasets, with advantages scaling for longer sequences and low-SNR regimes.
- Improves macro AUROC over all baseline denoisers across over 40 pathology classes using two independent downstream classifiers.
- Demonstrates specific morphology-dependent benefits, substantially improving ST/T-change diagnoses relying on broad, context-sensitive waveforms.

## Limitations

Calibration improvements are nuanced and classifier-dependent, with specific variants required to consistently outperform noisy baselines across diverse architectures.

## Open Questions & Future Work

- [[unsupervised-ecg-denoising-without-ground-truth]]

## Key Concepts

- [[dr-net-mamba]]: A Mamba-augmented convolutional model inserting selective state-space blocks at the bottleneck for long-range ECG time-series denoising at linear complexity.

## Archivist Review

Approved the overarching architectural concept DR-net-Mamba for its novel combination of convolutional local extraction and state-space bottlenecks, along with one specific open question concerning unsupervised ECG denoising without ground truth. No datasets were approved since none were explicitly named in the abstract.

### Approved Concepts
- DR-net-Mamba: Introduces a novel architecture combining convolutional local feature extraction and selective state-space blocks at the bottleneck for long-range ECG time-series denoising.

### Approved Open Questions
- Unsupervised ECG Denoising Without Ground Truth: Crucial for scaling physiological time-series denoising to real-world clinical datasets where clean signals are fundamentally unobservable.

## Links

- [Abstract](https://arxiv.org/abs/2609.35634)
- [PDF](https://arxiv.org/pdf/2609.35634)

