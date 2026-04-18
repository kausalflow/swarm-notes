---
# CSL-compatible fields
title: "FAST: A Synergistic Framework of Attention and State-space Models for Spatiotemporal Traffic Prediction"
author:
  - literal: "Xinjin Li"
  - literal: "Jinghan Cao"
  - literal: "Mengyue Wang"
  - literal: "Yue Wu"
  - literal: "Longxiang Yan"
  - literal: "Yeyang Zhou"
  - literal: "Ziqi Sha"
  - literal: "Yu Ma"
issued:
  date-parts:
    - [2026, 4, 15]
url: "https://arxiv.org/abs/2604.13453"

# Custom fields
paper_id: "2604.13453"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "mamba"
  - "state-space-model"
  - "spatiotemporal"
architectures:
  - "mamba"
datasets:
  - "pems04"
  - "pems08"
concept_slugs:
  - "temporal-spatial-temporal-architecture"
dataset_slugs:
  - "pems04"
  - "pems08"
skill: "TimeSeriesSkill"
processed_at: "2026-04-18T06:07:12Z"
created_at: "2026-04-18T06:07:12Z"
---

# FAST: A Synergistic Framework of Attention and State-space Models for Spatiotemporal Traffic Prediction

**Authors**: Xinjin Li, Jinghan Cao, Mengyue Wang, Yue Wu, Longxiang Yan, Yeyang Zhou, Ziqi Sha, Yu Ma
**Date**: 2026-04-15
**Paper ID**: [openalex:2604.13453](https://arxiv.org/abs/2604.13453)

## Summary

FAST is a unified spatiotemporal traffic forecasting framework that balances Transformer expressiveness with Mamba efficiency. It employs a Temporal-Spatial-Temporal architecture to model long-range dependencies while maintaining linear complexity. By integrating a multi-source embedding and multi-level skip prediction, the framework effectively captures heterogeneous traffic dynamics, consistently outperforming state-of-the-art baselines across standard traffic sensor network benchmarks.

## Key Contributions

- FAST introduces a Temporal-Spatial-Temporal architecture that leverages temporal attention for pattern modeling and a Mamba-based spatial module for linear-complexity dependencies.
- A learnable multi-source spatiotemporal embedding allows the integration of historical flow, context, and node information for heterogeneous traffic representation.
- FAST achieves state-of-the-art performance on PeMS04, PeMS07, and PeMS08, providing up to 4.3% lower RMSE and 2.8% lower MAE than leading baseline architectures.

## Open Questions & Future Work

- [[adaptive-spatial-structure-modeling]]

## Key Concepts

- [[temporal-spatial-temporal-architecture]]: A hybrid architectural pattern for spatiotemporal data that sandwiches a Mamba-based spatial module between temporal attention modules.

## Archivist Review

I approved the 'Temporal-Spatial-Temporal Architecture' concept as it represents a clear, reusable architectural design pattern for combining attention and state-space models. For datasets, I selected PeMS04 and PeMS08 as representative benchmarks while rejecting PeMS07 to maintain scarcity. I approved the 'Adaptive Spatial Structure Modeling' question because it addresses a fundamental limitation in current GNN-based and static graph-based traffic forecasting models.

### Approved Concepts
- Temporal-Spatial-Temporal Architecture: It provides a novel structural hybrid design for spatiotemporal forecasting that addresses the efficiency-expressiveness trade-off between attention and state-space models.

### Approved Open Questions
- Adaptive Spatial Structure Modeling: Real-world traffic flow is inherently dynamic; a model capable of adapting its spatial dependency structure to changing conditions offers potential for improved robustness and generalization across traffic regimes.

### Rejected Candidates
- [open_question] Multivariate Multitask Forecasting for Traffic (`multivariate-multitask-forecasting`) - not_novel: Multivariate and multi-task learning are standard extensions and lack the specificity to warrant a unique bottleneck entry in the vault.

## Datasets

- [[pems04]]
- [[pems08]]

## Links

- [Abstract](https://arxiv.org/abs/2604.13453)
- [PDF](https://arxiv.org/pdf/2604.13453)

