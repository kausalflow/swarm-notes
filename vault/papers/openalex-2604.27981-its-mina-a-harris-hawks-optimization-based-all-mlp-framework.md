---
# CSL-compatible fields
title: "ITS-Mina: A Harris Hawks Optimization-Based All-MLP Framework with Iterative Refinement and External Attention for Multivariate Time Series Forecasting"
author:
  - literal: "Pourya Zamanvaziri"
  - literal: "Amirhossein Sadr"
  - literal: "Aida Pakniyat"
  - literal: "Dara Rahmati"
issued:
  date-parts:
    - [2026, 4, 30]
url: "https://arxiv.org/abs/2604.27981"

# Custom fields
paper_id: "2604.27981"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "benchmark"
  - "efficient-transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  - "iterative-residual-mixer-stack"
  - "external-attention-memory-units"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-03T07:13:59Z"
created_at: "2026-05-03T07:13:59Z"
---

# ITS-Mina: A Harris Hawks Optimization-Based All-MLP Framework with Iterative Refinement and External Attention for Multivariate Time Series Forecasting

**Authors**: Pourya Zamanvaziri, Amirhossein Sadr, Aida Pakniyat, Dara Rahmati
**Date**: 2026-04-30
**Paper ID**: [openalex:2604.27981](https://arxiv.org/abs/2604.27981)

## Summary

ITS-Mina is an all-MLP architecture designed for multivariate time series forecasting that emphasizes computational efficiency and long-range dependency modeling. The framework utilizes iterative refinement with shared-parameter residual stacks to deepen representational capacity and an external attention module to achieve linear-time global dependency capture. Additionally, it incorporates Harris Hawks Optimization to automatically tune regularization parameters, yielding state-of-the-art performance across six benchmark datasets.

## Key Contributions

- Introduces ITS-Mina, an all-MLP framework that outperforms eleven baseline models on six standard benchmarks.
- Proposes an iterative refinement mechanism using a shared-parameter residual mixer to improve temporal representation learning without increasing total parameter count.
- Implements an external attention module with learnable memory units to capture global dependencies with linear computational complexity.
- Utilizes a Harris Hawks Optimization (HHO) algorithm for automated, dataset-specific dropout rate tuning to enhance model regularization.

## Open Questions & Future Work

- [[adaptive-halting-for-iterative-refinement]]

## Key Concepts

- [[iterative-residual-mixer-stack]]: A weight-tied residual block architecture that allows MLP-based models to increase depth and representational capacity without increasing the total number of trainable parameters.
- [[external-attention-memory-units]]: An attention mechanism that utilizes global learnable memory units to capture long-range dependencies with linear computational complexity.

## Archivist Review

I approved two modular architectural concepts—iterative residual mixing and external attention memory—because they represent general design patterns for efficient forecasting that transcend the specific architecture proposed. I also approved the adaptive halting research question as a meaningful direction for optimizing iterative computational models. The main framework name and the generic request for auxiliary features were rejected as they are either too implementation-specific or too broad in scope.

### Approved Concepts
- Iterative Residual Mixer Stack: This represents a specific weight-tying architectural pattern for deepening MLP-based forecasting models without parameter scaling, which is a reusable architectural paradigm.
- External Attention Memory Units: Provides a linear-complexity alternative to standard quadratic self-attention using learnable memory, which is highly reusable in efficient transformer and MLP-based forecasting architectures.

### Approved Open Questions
- Adaptive halting for refinement: Static computational depth in iterative refinement models often leads to inefficiency; dynamic halting is a critical research direction for balancing accuracy with real-time requirements.

### Rejected Candidates
- [concept] ITS-Mina (`its-mina`) - subcomponent_of_broader_mechanism: ITS-Mina is a specific architecture implementation; the framework's components (iterative residual mixer and external attention) are more broadly reusable as concepts.
- [open_question] Integrating auxiliary features (`auxiliary-feature-integration-time-series`) - not_novel: Integrating exogenous covariates is a generic task in multivariate time series forecasting rather than a novel, deep unresolved research question unique to this methodology.

## Links

- [Abstract](https://arxiv.org/abs/2604.27981)
- [PDF](https://arxiv.org/pdf/2604.27981)

