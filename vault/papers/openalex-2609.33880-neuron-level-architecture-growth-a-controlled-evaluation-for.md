---
# CSL-compatible fields
title: "Neuron-Level Architecture Growth: A Controlled Evaluation for EEG Time-Series Decoding"
author:
  - literal: "Adam Mounir"
  - literal: "Stella Douka"
  - literal: "Arnault Hubert Caillet"
  - literal: "Bruno Aristimunha"
  - literal: "Sylvain Chevallier"
  - literal: "Stella Douka"
issued:
  date-parts:
    - [2026, 9, 27]
url: "https://arxiv.org/abs/2609.33880"

# Custom fields
paper_id: "2609.33880"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "neural-architecture-search"
  - "model-compression"
  - "benchmark"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:50:01Z"
created_at: "2026-09-30T10:50:01Z"
---

# Neuron-Level Architecture Growth: A Controlled Evaluation for EEG Time-Series Decoding

**Authors**: Adam Mounir, Stella Douka, Arnault Hubert Caillet, Bruno Aristimunha, Sylvain Chevallier, Stella Douka
**Date**: 2026-09-27
**Paper ID**: [openalex:2609.33880](https://arxiv.org/abs/2609.33880)

## Summary

This paper investigates neuron-level architecture growth for convolutional EEG decoders, evaluating whether dynamically adding neurons during training improves performance compared to fixed-width reference models. Tested across three convolutional backbones on 12 motor-imagery datasets under three protocols, the results show that growing ShallowFBCSPNet outperforms its reference by 2.9 points with fewer parameters, whereas Deep4Net requires adaptation that hinders fair comparison. The findings indicate that growth success relies heavily on the selection mechanism's ability to rank candidate neurons via singular value decomposition thresholds.

## Key Contributions

- Evaluated neuron-level architecture growth methods across three convolutional backbones and 12 motor-imagery EEG datasets under three protocols.
- Showed that growing ShallowFBCSPNet achieves a 2.9-point improvement over its fixed-width reference model while utilizing only 0.57x the parameter count.
- Demonstrated that growth efficacy heavily depends on the selection criterion's ability to rank candidate neurons using singular value decomposition thresholds.

## Limitations

Deep4Net growing models exhibited decreased accuracy and required structural adaptations that hindered faithful comparison.

## Open Questions & Future Work

- [[deep-network-architecture-growth-pooling]]

## Archivist Review

Approved the open question regarding network architecture growth for deeper models with pooling layers, as it addresses a fundamental limitation in dynamic network expansion. Rejected the concept candidate because it is too paper-local and tied specifically to EEG decoder growth.

### Approved Open Questions
- Growth Methods for Deep Networks: Extending growth techniques to deeper networks with pooling layers is critical for understanding whether architectural growth can benefit deep architectures as effectively as shallow ones across diverse time-series decoding tasks.

### Rejected Candidates
- [concept] Neuron-Level Architecture Growth for EEG Decoding (`neuron-level-architecture-growth-eeg`) - paper_local: Too paper-local and specific to the evaluation of shallow CNN decoders on motor-imagery EEG datasets.

## Links

- [Abstract](https://arxiv.org/abs/2609.33880)
- [PDF](https://arxiv.org/pdf/2609.33880)

