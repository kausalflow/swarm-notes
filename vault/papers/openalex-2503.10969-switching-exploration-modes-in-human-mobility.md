---
# CSL-compatible fields
title: "Switching exploration modes in human mobility"
author:
  - literal: "Lu Zhong"
  - literal: "Lei Dong"
  - literal: "Qi Wang"
  - literal: "Chaoming Song"
  - literal: "Jianxi Gao"
issued:
  date-parts:
    - [2026, 6, 24]
url: "https://arxiv.org/abs/2503.10969"

# Custom fields
paper_id: "2503.10969"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "graph-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "switch-mechanism-mobility"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-26T08:26:34Z"
created_at: "2026-06-26T08:26:34Z"
---

# Switching exploration modes in human mobility

**Authors**: Lu Zhong, Lei Dong, Qi Wang, Chaoming Song, Jianxi Gao
**Date**: 2026-06-24
**Paper ID**: [openalex:2503.10969](https://arxiv.org/abs/2503.10969)

## Summary

This paper investigates human mobility networks, demonstrating that movement behaviors differ significantly between intra-module and inter-module spatial scales. To address this, the authors introduce a switch mechanism that distinguishes between these two exploration modes, mirroring biological movement patterns. By incorporating this mechanism into a generative mobility model, the approach successfully replicates complex network-level structures alongside individual movement statistics, offering a unified explanation for polycentric human mobility.

## Key Contributions

- Identified polycentric and modular structures in human mobility networks that challenge uniform mobility dynamics assumptions.
- Proposed a 'switch mechanism' to model distinct intra-module and inter-module exploration modes.
- Achieved simultaneous reproduction of individual-level mobility statistics and emergent network-level properties like modularity and long-range travel.

## Open Questions & Future Work

- [[robustness-of-mode-switching-mechanisms]]

## Key Concepts

- [[switch-mechanism-mobility]]: A generative mobility modeling approach that distinguishes between intra-module and inter-module exploration modes to replicate polycentric and modular network structures.

## Archivist Review

I approved the 'Switch Mechanism' as it represents a novel, reusable temporal-spatial inductive bias for mobility modeling. The open question was reformulated to focus specifically on the robustness of these switching dynamics under non-stationary conditions, which is a key bottleneck in epidemiological and urban forecasting. No datasets were proposed by the authors, so none were approved.

### Approved Concepts
- Switch Mechanism (Mobility): It provides a mechanistic approach to modeling scale-dependent human movement dynamics that challenges uniform mobility assumptions.

### Approved Open Questions
- Robustness of Mode Switching Mechanisms: Determining if structural mobility priors are robust to environmental and societal shifts is critical for epidemic forecasting and reliable urban planning.

### Rejected Candidates
- [open_question] Refining Switch Mechanism Applicability (`refining-switch-mechanism-applicability`) - other: The proposed question is too broad and boilerplate compared to the more specific robustness inquiry formulated.

## Links

- [Abstract](https://arxiv.org/abs/2503.10969)
- [PDF](https://arxiv.org/pdf/2503.10969)

