---
# CSL-compatible fields
title: "SafeDivertor: Faithful Divertor Heat Flux Reconstruction from Macroscopic Plasma State Signals via Time-Frequency Prior Exploitation"
author:
  - literal: "Hao Si"
  - literal: "Zehua Chen"
  - literal: "Qingquan Yang"
  - literal: "Xiao Wang"
  - literal: "Dengdi Sun"
  - literal: "Wanli Lyu"
  - literal: "Gaoting Chen"
  - literal: "Guosheng Xu"
  - literal: "Hang Su"
  - literal: "Jin Tang"
  - literal: "Jun Zhu"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2608.05669"

# Custom fields
paper_id: "2608.05669"
paper_source: "openalex"
domain: "physics"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "benchmark"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  - "divmps2hf"
concept_slugs:
  - "safedivertor"
dataset_slugs:
  - "divmps2hf"
skill: "TimeSeriesSkill"
processed_at: "2026-08-09T05:41:38Z"
created_at: "2026-08-09T05:41:38Z"
---

# SafeDivertor: Faithful Divertor Heat Flux Reconstruction from Macroscopic Plasma State Signals via Time-Frequency Prior Exploitation

**Authors**: Hao Si, Zehua Chen, Qingquan Yang, Xiao Wang, Dengdi Sun, Wanli Lyu, Gaoting Chen, Guosheng Xu, Hang Su, Jin Tang, Jun Zhu
**Date**: 2026-08-06
**Paper ID**: [openalex:2608.05669](https://arxiv.org/abs/2608.05669)

## Summary

This paper introduces SafeDivertor, an online-oriented signal-based framework for faithful divertor heat-flux reconstruction from macroscopic plasma state signals in magnetic-confinement fusion devices, overcoming the limitations of conventional post-discharge infrared inversion. To support this task, the authors construct DivMPS2HF, a multi-source discharge benchmark dataset. SafeDivertor incorporates physical prior-aware initialization, input perturbation, spectral-aware reconstruction optimization, and progressive training to effectively capture transient dynamics and handle heterogeneous signals. Experiments on DivMPS2HF show that SafeDivertor outperforms existing time-series baselines across all evaluated metrics.

## Key Contributions

- Introduces an online-oriented signal-based reconstruction paradigm that directly maps multi-source macroscopic plasma-state signals to time-resolved radial divertor heat-flux profiles.
- Constructs DivMPS2HF, a comprehensive multi-source discharge dataset and benchmark for signal-based divertor heat-flux reconstruction.
- Proposes SafeDivertor, integrating physical prior-aware initialization, input perturbation, spectral-aware reconstruction optimization, and progressive training.
- Demonstrates superior performance across all five metrics on DivMPS2HF compared to existing time-series baselines.

## Limitations

Limited to the specific magnetic-confinement fusion device and multi-source plasma-state signals available in the DivMPS2HF benchmark.

## Open Questions & Future Work

- [[cross-scenario-generalization-heat-flux]]

## Key Concepts

- [[safedivertor]]: A task-driven framework for online divertor heat-flux reconstruction from macroscopic plasma state signals using time-frequency priors.

## Archivist Review

Approved the core SafeDivertor framework note and the associated DivMPS2HF dataset, along with the cross-scenario generalization open question for fusion heat flux reconstruction. Applied strict scarcity and quality filters to avoid paper-local subcomponents.

### Approved Concepts
- SafeDivertor: Introduces a novel online-oriented signal-based reconstruction paradigm and framework for divertor heat-flux reconstruction from macroscopic plasma state signals in magnetic-confinement fusion devices.

### Approved Open Questions
- Cross-Scenario Generalization for Heat Flux Reconstruction: Crucial for transitioning machine-learning-based divertor monitoring systems from offline benchmarks to reliable online control tools in burning-plasma devices.

## Datasets

- [[divmps2hf]]

## Links

- [Abstract](https://arxiv.org/abs/2608.05669)
- [PDF](https://arxiv.org/pdf/2608.05669)

