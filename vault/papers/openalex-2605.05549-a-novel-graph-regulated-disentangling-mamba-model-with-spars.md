---
# CSL-compatible fields
title: "A Novel Graph-Regulated Disentangling Mamba Model with Sparse Tokens for Enhanced Tree Species Classification from MODIS Time Series"
author:
  - literal: "Motasem Alkayid"
  - literal: "Zhengsen Xu"
  - literal: "Saeid Taleghanidoozdoozan"
  - literal: "Yimin Zhu"
  - literal: "Megan Greenwood"
  - literal: "Quinn Ledingham"
  - literal: "Zack Dewis"
  - literal: "Mabel Heffring"
  - literal: "Naser El-Sheimy"
  - literal: "Lincoln Linlin Xu"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.05549"

# Custom fields
paper_id: "2605.05549"
paper_source: "openalex"
domain: "nlp"
tags:
  - "mamba"
  - "state-space-model"
  - "ssm"
  - "time-series"
  - "image-classification"
architectures:
  - "mamba"
datasets:
  []
concept_slugs:
  - "graph-regulated-disentangled-sparse-mamba-gds-mamba"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:21:30Z"
created_at: "2026-05-10T07:21:30Z"
---

# A Novel Graph-Regulated Disentangling Mamba Model with Sparse Tokens for Enhanced Tree Species Classification from MODIS Time Series

**Authors**: Motasem Alkayid, Zhengsen Xu, Saeid Taleghanidoozdoozan, Yimin Zhu, Megan Greenwood, Quinn Ledingham, Zack Dewis, Mabel Heffring, Naser El-Sheimy, Lincoln Linlin Xu
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.05549](https://arxiv.org/abs/2605.05549)

## Summary

This paper introduces GDS-Mamba, a novel architecture designed to enhance tree species classification from MODIS time series by disentangling complex spatial-spectral-temporal couplings. The model incorporates mini-batch graph regulation to better capture topological context and employs an adaptive sparse token mechanism to overcome correlation decay. Extensive experiments on MOD13Q1 data demonstrate that GDS-Mamba achieves superior performance compared to twelve baseline models, significantly improving classification accuracy in cross-provincial scenarios.

## Key Contributions

- Introduces GDS-Mamba, which incorporates mini-batch graph regulation to capture topological context in large-scale MODIS time series data.
- Proposes a disentangling Mamba architecture that isolates spatial patterns, spectral signatures, and temporal phenology to mitigate information coupling.
- Develops an adaptive sparse token approach to select optimal subsets of features, effectively addressing correlation decay in standard Mamba models.
- Achieved 93.94% accuracy in Alberta and 80.19% in cross-provincial evaluations, outperforming twelve state-of-the-art classification models.

## Open Questions & Future Work

- [[optimizing-graph-regulated-disentangled-mamba-architectures]]

## Key Concepts

- [[graph-regulated-disentangled-sparse-mamba-gds-mamba]]: A hybrid model combining graph-based topological modeling, disentangled representation learning for spatial-spectral-temporal features, and sparse token selection to improve classification in MODIS time series.

## Archivist Review

I approved the proposed GDS-Mamba architecture and its corresponding open question regarding the optimization of graph-regulated state-space models. I rejected the MOD13Q1 dataset as it is a standard, publicly available MODIS product commonly used in remote sensing and does not warrant a permanent entry in this vault.

### Approved Concepts
- Graph-regulated Disentangled Sparse Mamba (GDS-Mamba): Core architecture proposed to integrate topological graph regulation with disentangled feature extraction and sparse token learning.

### Approved Open Questions
- Optimizing Graph-Regulated Disentangled Mamba: This question identifies a critical bottleneck in applying state-space models to multi-dimensional remote sensing tasks, where feature disentanglement is essential for generalization.

### Rejected Candidates
- [dataset] MOD13Q1 (`mod13q1`) - not_novel: This is a widely used standard product dataset rather than a novel or research-specific collection introduced for a new task.

## Links

- [Abstract](https://arxiv.org/abs/2605.05549)
- [PDF](https://arxiv.org/pdf/2605.05549)

