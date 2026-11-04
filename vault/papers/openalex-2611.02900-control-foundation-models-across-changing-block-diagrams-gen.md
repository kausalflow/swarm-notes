---
# CSL-compatible fields
title: "Control Foundation Models across Changing Block Diagrams: Generalizing Time-Series Prediction to Dynamic Graphs"
author:
  - literal: "Yuji Okamoto"
  - literal: "K. Hoshino"
  - literal: "Masaki Inoue"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.02900"

# Custom fields
paper_id: "2611.02900"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
  - "transformer"
  - "attention-mechanism"
  - "reinforcement-learning"
  - "robustness"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "block-diagram-transformer"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-04T12:40:23Z"
created_at: "2026-11-04T12:40:23Z"
---

# Control Foundation Models across Changing Block Diagrams: Generalizing Time-Series Prediction to Dynamic Graphs

**Authors**: Yuji Okamoto, K. Hoshino, Masaki Inoue
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.02900](https://arxiv.org/abs/2611.02900)

## Summary

This paper proposes a control foundation model formulation and the Block Diagram Transformer (BDT) to handle time-series prediction across changing block diagrams and dynamic graphs. By combining temporal attention with graph neural networks that follow block-diagram connections, the model unifies response prediction and control-input generation as a masked prediction problem. Experiments show that training on diverse control data enables stabilizing unstable systems via feedback control, outperforming standard fine-tuning of existing time-series foundation models.

## Key Contributions

- Formulates a control foundation model defining a data space of dynamic graphs containing connections, signal values, and missing values.
- Implements the Block Diagram Transformer (BDT) combining time-axis attention with graph neural networks along block-diagram connections.
- Demonstrates successful stabilization of an unstable system through feedback control using control-experiment data mixing multiple settings.

## Limitations

Ongoing work applying this approach to a wider range of target systems.

## Open Questions & Future Work

- [[generalizing-control-foundation-models-across-diverse-systems]]

## Key Concepts

- [[block-diagram-transformer]]: A control foundation model architecture that combines temporal attention with graph neural networks following dynamic block-diagram connections.

## Archivist Review

The Block Diagram Transformer is approved as a central architectural concept for unifying control and forecasting via dynamic graph block diagrams. The open question regarding cross-system generalization of control foundation models was also approved due to its technical importance. No other candidates were present.

### Approved Concepts
- Block Diagram Transformer: It introduces a novel architecture combining temporal attention with graph neural networks over block diagrams to generalize time-series prediction to dynamic graphs in control systems.

### Approved Open Questions
- Generalizing Control Foundation Models across Diverse Systems: Demonstrating cross-system and cross-domain generalization is crucial for establishing the practical viability and transferability of control foundation models in diverse real-world engineering tasks.

## Links

- [Abstract](https://arxiv.org/abs/2611.02900)
- [PDF](https://arxiv.org/pdf/2611.02900)

