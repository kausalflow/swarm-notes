---
# CSL-compatible fields
title: "CAMASA: A CAM-based Dataset from the MASA Living Lab"
author:
  - literal: "Salvatore Iandolo"
  - literal: "Marco Savarese"
  - literal: "Gaetano Orazio Cauchi"
  - literal: "Antonio Solida"
  - literal: "Martin Klapez"
  - literal: "Maurizio Casoni"
  - literal: "Angelo Porrello"
  - literal: "Carlo Augusto Grazia"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.10641"

# Custom fields
paper_id: "2606.10641"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "autonomous-agent"
  - "time-series"
  - "dataset"
  - "benchmark"
architectures:
  []
datasets:
  - "CAMASA"
concept_slugs:
  []
dataset_slugs:
  - "camasa"
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:53:54Z"
created_at: "2026-06-12T08:53:54Z"
---

# CAMASA: A CAM-based Dataset from the MASA Living Lab

**Authors**: Salvatore Iandolo, Marco Savarese, Gaetano Orazio Cauchi, Antonio Solida, Martin Klapez, Maurizio Casoni, Angelo Porrello, Carlo Augusto Grazia
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.10641](https://arxiv.org/abs/2606.10641)

## Summary

This paper presents CAMASA, a large-scale infrastructure-based dataset collected from real-world V2X communications within the Modena Automotive Smart Area (MASA). Addressing the limitations of current sensor-centric and synthetic benchmarks, the dataset captures over 40 million Cooperative Awareness Messages (CAMs) and 2 million Decentralized Environmental Notification Messages (DENMs) under authentic urban conditions. The authors provide a comprehensive preprocessing pipeline that ensures trajectory consistency through pseudonym reconciliation and temporal normalization, making it a valuable foundation for motion forecasting, traffic simulation, and ITS Digital Twin development.

## Key Contributions

- Introduces the CAMASA dataset, comprising 40 million CAMs and 2 million DENMs across 14,000 km of reconstructed vehicle trajectories in an urban V2X environment.
- Develops a robust preprocessing pipeline for pseudonym reconciliation and temporal normalization (10 Hz) of ETSI-standard cooperative awareness messages.
- Enables advancements in trajectory prediction, microscopic traffic simulator calibration, and the development of high-fidelity Digital Twins for C-ITS applications.

## Open Questions & Future Work

- [[pseudonym-reconciliation-robustness]]

## Archivist Review

I approved the CAMASA dataset and the open question regarding pseudonym reconciliation robustness. The dataset itself is the core contribution and is better tracked as a dataset entry. The pseudonym reconciliation challenge is a substantial, reusable bottleneck for future C-ITS and V2X research.

### Approved Open Questions
- Robust Pseudonym Reconciliation Methods: Effective vehicle re-identification is fundamental for accurate trajectory prediction and traffic analysis in C-ITS, especially as privacy regulations continue to mandate frequent identifier rotations.

### Rejected Candidates
- [concept] CAMASA Dataset (`camasa-dataset`) - subcomponent_of_broader_mechanism: The dataset is more appropriately archived as a dataset entry than as a conceptual framework for trajectory prediction.

## Datasets

- [[camasa]]

## Links

- [Abstract](https://arxiv.org/abs/2606.10641)
- [PDF](https://arxiv.org/pdf/2606.10641)

