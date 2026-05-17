---
# CSL-compatible fields
title: "MambaRain: Multi-Scale Mamba-Attention Framework for 0-3 Hour Precipitation Nowcasting"
author:
  - literal: "Chunlei Shi"
  - literal: "Cui Wu"
  - literal: "Xiang Xu"
  - literal: "Hao Li"
  - literal: "Ni Fan"
  - literal: "Xue Han"
  - literal: "Yongchao Feng"
  - literal: "Yufeng Zhu"
  - literal: "Boyu Liu"
  - literal: "Zengliang Zang"
  - literal: "Hongbin Wang"
  - literal: "Yanlan Yang"
  - literal: "Dan Niu"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14606"

# Custom fields
paper_id: "2605.14606"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "mamba"
  - "state-space-model"
  - "ssm"
  - "attention-mechanism"
  - "self-attention"
  - "transformer"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "mambarain"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:32:23Z"
created_at: "2026-05-17T07:32:23Z"
---

# MambaRain: Multi-Scale Mamba-Attention Framework for 0-3 Hour Precipitation Nowcasting

**Authors**: Chunlei Shi, Cui Wu, Xiang Xu, Hao Li, Ni Fan, Xue Han, Yongchao Feng, Yufeng Zhu, Boyu Liu, Zengliang Zang, Hongbin Wang, Yanlan Yang, Dan Niu
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14606](https://arxiv.org/abs/2605.14606)

## Summary

MambaRain is a hybrid encoder-decoder architecture designed to overcome the limitations of deterministic precipitation nowcasting models in capturing long-range dependencies. By integrating Mamba's linear-complexity state space modeling for temporal dynamics with self-attention modules for spatial correlations, the framework significantly extends reliable forecasting from 2 to 3 hours. Additionally, a specialized spectral loss formulation reduces blurring in precipitation fields, preserving essential fine-scale motion details.

## Key Contributions

- Introduces MambaRain, a hybrid architecture combining Mamba's selective state space modeling with self-attention to improve long-range spatiotemporal precipitation forecasting.
- Extends the viable precipitation nowcasting horizon from 2 to 3 hours with significant accuracy gains compared to traditional deterministic methods.
- Proposes a spectral loss formulation to address blurring artifacts in high-resolution, chaotic precipitation predictions.

## Open Questions & Future Work

- [[nowcasting-uncertainty-and-generalization]]

## Key Concepts

- [[mambarain]]: A multi-scale encoder-decoder framework combining linear-complexity Mamba blocks for temporal dynamics and self-attention for spatial correlation modeling.

## Archivist Review

The paper introduces a hybrid architecture combining SSMs with spatial attention for spatiotemporal forecasting. I approved the framework as a concept and a broader open question regarding nowcasting uncertainty and generalization, as these represent significant technical hurdles in meteorological forecasting. Subcomponents like the specific loss function were rejected as they are implementation details rather than standalone theoretical contributions.

### Approved Concepts
- MambaRain: Represents a novel hybrid architectural paradigm for spatiotemporal forecasting that combines SSM and self-attention.

### Approved Open Questions
- Nowcasting Uncertainty and Generalization: Quantifying uncertainty is critical for high-stakes operational decision-making in disaster prevention, and generalization across diverse radar networks is a fundamental requirement for the widespread deployment of data-driven meteorological models.

### Rejected Candidates
- [concept] Spectral Loss Formulation (`mambarain-spectral-loss`) - subcomponent_of_broader_mechanism: This is a specific subcomponent/loss function enhancement that does not rise to the level of a core, reusable conceptual innovation independent of the framework.

## Links

- [Abstract](https://arxiv.org/abs/2605.14606)
- [PDF](https://arxiv.org/pdf/2605.14606)

