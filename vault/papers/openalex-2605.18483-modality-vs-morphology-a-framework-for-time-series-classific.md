---
# CSL-compatible fields
title: "Modality vs. Morphology: A Framework for Time Series Classification for Biological Signals"
author:
  - literal: "Jordan Tschida"
  - literal: "Matthew Yohe"
  - literal: "Edward Kane"
  - literal: "Gavin Jager"
  - literal: "Emma J. Reid"
  - literal: "Tony G. Allen"
  - literal: "Mark Story"
  - literal: "Leanne Thompson"
  - literal: "Joe Hoskins"
  - literal: "Brandon Schreiber"
  - literal: "Stan Seiferth"
  - literal: "Scott Dolvin"
  - literal: "David Cornett"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.18483"

# Custom fields
paper_id: "2605.18483"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "classification"
  - "interpretability"
  - "deep-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "morphology-modality-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:30:48Z"
created_at: "2026-05-21T08:30:48Z"
---

# Modality vs. Morphology: A Framework for Time Series Classification for Biological Signals

**Authors**: Jordan Tschida, Matthew Yohe, Edward Kane, Gavin Jager, Emma J. Reid, Tony G. Allen, Mark Story, Leanne Thompson, Joe Hoskins, Brandon Schreiber, Stan Seiferth, Scott Dolvin, David Cornett
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.18483](https://arxiv.org/abs/2605.18483)

## Summary

This review paper proposes a morphology-modality framework for time series classification of biological signals, shifting the focus from modality-specific approaches to the underlying waveform dynamics. By analyzing signals such as EEG, EMG, and ECG, the authors demonstrate that success in classification depends primarily on how well model inductive biases align with the morphological features like spikes, bursts, and rhythms. The study highlights that morphology-aware design is a critical unifying principle for developing more generalizable and interpretable models in physiological signal analysis.

## Key Contributions

- Introduces a unified morphology-modality framework that maps physiological signal structures (spikes, bursts, oscillations) to optimal TSC model design.
- Demonstrates that waveform morphology, rather than the specific modality or model class, is the primary driver of classification performance and model interpretability.
- Provides a systematic analysis across diverse biological signals (EEG, EMG, ECG, PPG, and ocular signals) to explain why specific deep learning inductive biases succeed.

## Open Questions & Future Work

- [[biological-tsc-benchmarking-standardization]]
- [[morphology-aware-data-augmentation]]

## Key Concepts

- [[morphology-modality-framework]]: A framework that categorizes biological time series by waveform structure (e.g., spikes, bursts, oscillations) to inform model architectural design and inductive bias selection.

## Archivist Review

The paper presents a high-level conceptual framework for biological signal processing. I have approved the Morphology-Modality Framework as a core concept because it shifts the field toward structure-aware modeling. The two open questions address critical bottlenecks in biological time series analysis: the lack of standardized benchmarks that respect signal structure, and the need for augmentation strategies that preserve morphological validity rather than just statistical distributions.

### Approved Concepts
- Morphology-Modality Framework: It establishes a fundamental principle that shifts focus from modality-specific engineering to signal-structure-driven design.

### Approved Open Questions
- Standardized Biological TSC Benchmarks: Without such standards, it is impossible to evaluate whether model improvements are due to algorithmic innovation or idiosyncratic dataset quirks.
- Morphology-Aware Data Augmentation: As deep learning models rely increasingly on synthetic or augmented data for training, ensuring these processes maintain the signal's biological validity is a prerequisite for reliable clinical deployment.

## Links

- [Abstract](https://arxiv.org/abs/2605.18483)
- [PDF](https://arxiv.org/pdf/2605.18483)

