---
# CSL-compatible fields
title: "SL-S4Wave: Self-Supervised Learning of Physiological Waveforms with Structured State Space Models"
author:
  - literal: "Feng Wu"
  - literal: "Harsh Deep"
  - literal: "E. Lehman"
  - literal: "Sanyam Kapoor"
  - literal: "Guoshuai Zhao"
  - literal: "Rahul Krishnan"
  - literal: "Gari Clifford"
  - literal: "Li-wei H. Lehman"
issued:
  date-parts:
    - [2026, 6, 18]
url: "https://arxiv.org/abs/2606.19888"

# Custom fields
paper_id: "2606.19888"
paper_source: "openalex"
domain: "medicine"
tags:
  - "self-supervised-learning"
  - "contrastive-learning"
  - "state-space-model"
  - "ssm"
  - "long-context"
  - "medicine"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sl-s4wave-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-21T08:54:29Z"
created_at: "2026-06-21T08:54:29Z"
---

# SL-S4Wave: Self-Supervised Learning of Physiological Waveforms with Structured State Space Models

**Authors**: Feng Wu, Harsh Deep, E. Lehman, Sanyam Kapoor, Guoshuai Zhao, Rahul Krishnan, Gari Clifford, Li-wei H. Lehman
**Date**: 2026-06-18
**Paper ID**: [openalex:2606.19888](https://arxiv.org/abs/2606.19888)

## Summary

SL-S4Wave is a self-supervised learning framework designed for high-resolution, long-sequence medical waveforms like ECG and EEG. By leveraging a structured state space model (S4) encoder augmented with multiscale global convolution subkernels, the model effectively captures both fine-grained local dynamics and long-range dependencies. The framework utilizes contrastive learning to extract noise-invariant representations, achieving superior performance on arrhythmia detection and cross-domain EEG tasks even with limited labeled data.

## Key Contributions

- Introduces SL-S4Wave, a self-supervised framework integrating contrastive learning with a structured state space model encoder using multiscale subkernels.
- Demonstrates superior arrhythmia detection performance compared to supervised and self-supervised baselines, while maintaining high robustness to noise and long-range dependencies.
- Shows strong label efficiency by achieving competitive performance with significantly fewer labeled examples and demonstrates effective transfer learning on both ECG and EEG tasks.

## Open Questions & Future Work

- [[ssm-clinical-reliability-uncertainty]]

## Key Concepts

- [[sl-s4wave-framework]]: A self-supervised learning framework for physiological waveforms that combines contrastive learning with a structured state space model encoder utilizing multiscale subkernels.

## Archivist Review

The SL-S4Wave framework represents a significant and reusable approach for high-resolution, long-sequence physiological signals, justifying the creation of a concept note. The proposed open question addresses critical barriers—reliability, uncertainty, and foundation model capability—that are essential for the advancement of clinical time series modeling. I have adjusted the concept name for clarity and kept the open question title concise while ensuring the description remains objective.

### Approved Concepts
- SL-S4Wave Framework: It provides a novel architecture specifically tailored for long-range dependency modeling in high-resolution, noisy physiological time series by integrating structured state space models with contrastive learning.

### Approved Open Questions
- SSM Clinical Reliability and Uncertainty: This is critical for transitioning SSM-based time series models from research prototypes to robust, reliable tools in real-world clinical decision support where model calibration and generalizability are paramount.

## Links

- [Abstract](https://arxiv.org/abs/2606.19888)
- [PDF](https://arxiv.org/pdf/2606.19888)

