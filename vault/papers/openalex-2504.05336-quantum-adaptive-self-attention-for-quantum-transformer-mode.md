---
# CSL-compatible fields
title: "Quantum Adaptive Self-Attention for Quantum Transformer Models"
author:
  - literal: "Chi‐Sheng Chen"
  - literal: "En-Jui Kuo"
issued:
  date-parts:
    - [2026, 7, 15]
url: "https://arxiv.org/abs/2504.05336"

# Custom fields
paper_id: "2504.05336"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "attention-mechanism"
  - "self-attention"
  - "quantum-computing"
  - "time-series"
  - "forecasting"
  - "hybrid-model"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "quantum-adaptive-self-attention-qasa"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-18T06:52:43Z"
created_at: "2026-07-18T06:52:43Z"
---

# Quantum Adaptive Self-Attention for Quantum Transformer Models

**Authors**: Chi‐Sheng Chen, En-Jui Kuo
**Date**: 2026-07-15
**Paper ID**: [openalex:2504.05336](https://arxiv.org/abs/2504.05336)

## Summary

This paper introduces Quantum Adaptive Self-Attention (QASA), a hybrid Transformer that integrates minimal quantum computation by replacing the value projection of an encoder layer with a parameterized quantum circuit (PQC). With only 36 trainable quantum parameters, QASA achieves significant improvements on chaotic and trend-heavy time-series data while outperforming larger quantum baselines like QLSTM and QnnFormer. The authors propose an architectural parsimony principle, demonstrating that strategic placement of a single quantum layer is more effective than increasing the count of quantum layers. Finally, the work provides a practical taxonomy for identifying tasks where quantum enhancement offers genuine performance advantages.

## Key Contributions

- Proposes Quantum Adaptive Self-Attention (QASA), a hybrid Transformer that replaces the value projection in an encoder layer with a PQC using only 36 trainable parameters.
- Demonstrates a 6.0% MAE reduction on the ETTh1 benchmark and superior performance on chaotic and trend-dominated signal tasks compared to QLSTM and QnnFormer.
- Establishes an 'architectural parsimony principle,' showing that a single, optimally placed quantum layer outperforms multi-layer quantum configurations in time-series tasks.
- Identifies a clear performance taxonomy: quantum layers provide gains on chaotic/noisy/trend-heavy signals, whereas classical transformers remain superior for clean periodic waveforms.

## Open Questions & Future Work

- [[adaptive-quantum-hybrid-selection]]

## Key Concepts

- [[quantum-adaptive-self-attention-qasa]]: A hybrid Transformer architecture that replaces standard value projections with a parameterized quantum circuit for efficient, task-specific quantum enhancement.

## Archivist Review

The approved concept represents a novel, parameter-efficient approach to hybrid quantum-classical Transformers, while the approved open question addresses the foundational problem of task-conditional suitability for quantum substrates in forecasting. The rejected open question was identified as a general quantum complexity problem rather than a contribution to the specific domain of time-series forecasting.

### Approved Concepts
- Quantum Adaptive Self-Attention (QASA): Introduces a minimal, task-conditional quantum integration strategy for hybrid Transformer models that optimizes performance per parameter.

### Approved Open Questions
- Adaptive Hybrid Quantum Selection: Crucial for avoiding the development of quantum architectures that perform well only due to unintentional classical bottlenecks rather than genuine quantum advantages.

### Rejected Candidates
- [open_question] Quantum Attention Gradient Complexity (`quantum-attention-gradient-complexity`) - other: This is a theoretical quantum complexity question rather than a practical temporal forecasting bottleneck or mechanism question.

## Links

- [Abstract](https://arxiv.org/abs/2504.05336)
- [PDF](https://arxiv.org/pdf/2504.05336)

