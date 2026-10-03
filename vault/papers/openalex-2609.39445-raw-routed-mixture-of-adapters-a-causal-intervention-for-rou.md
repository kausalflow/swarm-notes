---
# CSL-compatible fields
title: "Raw-Routed Mixture of Adapters: A Causal Intervention for Routing Collapse in Time Series Foundation Models"
author:
  - literal: "Hung Phan"
  - literal: "Thi Thu Thuy Nguyen"
  - literal: "Minh Ngoc Dinh"
  - literal: "Nhat-Quang Tran"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.39445"

# Custom fields
paper_id: "2609.39445"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "mixture-of-experts"
  - "moe"
  - "adapter"
  - "parameter-efficient-fine-tuning"
  - "peft"
  - "lora"
  - "foundation-model"
  - "robustness"
  - "forecasting"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "raw-routed-mixture-of-adapters"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:08:34Z"
created_at: "2026-10-03T10:08:34Z"
---

# Raw-Routed Mixture of Adapters: A Causal Intervention for Routing Collapse in Time Series Foundation Models

**Authors**: Hung Phan, Thi Thu Thuy Nguyen, Minh Ngoc Dinh, Nhat-Quang Tran
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.39445](https://arxiv.org/abs/2609.39445)

## Summary

This paper identifies normalization-induced routing collapse in instance-normalized time series foundation models, where pre-encoder normalization strips the statistical signals required for mixture-of-experts routing. To fix this, the authors propose Raw-Routed Mixture of Adapters (RR-MoA), a causal intervention that routes on raw pre-normalization inputs. Extensive evaluations across six backbones and an imputation task show that RR-MoA consistently outperforms standard adapters, LoRA, and even full fine-tuning.

## Key Contributions

- Identifies normalization-induced routing collapse as a failure mode in instance-normalized time series foundation models where routing entropy collapses to zero.
- Performs a mutual-information decomposition and derives a signal-ratio predicting dataset vulnerability with a Spearman rho of -0.88.
- Proposes Raw-Routed Mixture of Adapters (RR-MoA), a minimal causal intervention routing on raw pre-normalization inputs.
- Demonstrates that frozen RR-MoA outperforms full fine-tuning by 12-79% across six backbones and an imputation task.

## Limitations

Evaluated primarily on time series forecasting and imputation with frozen backbones.

## Open Questions & Future Work

- [[routing-collapse-tsfm-limitations]]

## Key Concepts

- [[raw-routed-mixture-of-adapters]]: A mixture of adapters mechanism that routes on raw pre-normalization inputs to prevent normalization-induced routing collapse in time series foundation models.

## Archivist Review

Approved the core mechanism 'Raw-Routed Mixture of Adapters' and the corresponding open question on extending routing collapse analysis and mitigation across tasks. The subcomponent candidate was rejected in accordance with policy.

### Approved Concepts
- Raw-Routed Mixture of Adapters: Introduces a causal intervention for routing collapse in instance-normalized time series foundation models by routing on raw pre-normalization inputs.

### Approved Open Questions
- Routing Collapse in TSFMs: Understanding how normalization interacts with routing decisions across different machine learning tasks and modalities is crucial for generalizable mixture-of-experts architectures.

### Rejected Candidates
- [concept] Normalization-Induced Routing Collapse (`normalization-induced-routing-collapse`) - subcomponent_of_broader_mechanism: Subcomponent of the broader mechanism and failure mode addressed by RR-MoA.

## Links

- [Abstract](https://arxiv.org/abs/2609.39445)
- [PDF](https://arxiv.org/pdf/2609.39445)

