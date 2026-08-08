---
# CSL-compatible fields
title: "IMFACT: Counterfactual Explanations for Time Series via Intrinsic Mode Function Substitution"
author:
  - literal: "Udo Schlegel"
  - literal: "Julian Rakuschek"
  - literal: "Thomas Seidl"
  - literal: "Andreas Holzinger"
  - literal: "Tobias Schreck"
  - literal: "Javier Del Ser"
issued:
  date-parts:
    - [2026, 8, 5]
url: "https://arxiv.org/abs/2608.04777"

# Custom fields
paper_id: "2608.04777"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "explainability"
  - "interpretability"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "imfact"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-08T05:34:18Z"
created_at: "2026-08-08T05:34:18Z"
---

# IMFACT: Counterfactual Explanations for Time Series via Intrinsic Mode Function Substitution

**Authors**: Udo Schlegel, Julian Rakuschek, Thomas Seidl, Andreas Holzinger, Tobias Schreck, Javier Del Ser
**Date**: 2026-08-05
**Paper ID**: [openalex:2608.04777](https://arxiv.org/abs/2608.04777)

## Summary

IMFACT is a model-agnostic framework for generating plausible counterfactual explanations for time series classifiers by operating in the decomposition space of Empirical Mode Decomposition, avoiding the temporal structure destruction caused by raw feature perturbations. By progressively substituting Intrinsic Mode Functions (IMFs) with those of a Nearest Unlike Neighbour (NUN), the method effectively flips classifier decisions while preserving physical plausibility. Evaluations on UCR benchmarks (FaultDetectionA, FruitFlies) demonstrate that variance-based IMF selection with multi-NUN cycling achieves superior reliability, plausibility, and proximity compared to baseline techniques.

## Key Contributions

- Introduces IMFACT, a model-agnostic counterfactual explanation framework operating in the decomposition space of Empirical Mode Decomposition for time series classifiers.
- Evaluates six IMF-selection strategies and a multi-NUN cycling extension across the FaultDetectionA and FruitFlies UCR benchmark datasets.
- Demonstrates that the variance-based IMF selection strategy with three NUNs outperforms baseline techniques on reliability and plausibility metrics.

## Limitations

Evaluated specifically on two UCR benchmarks (FaultDetectionA, FruitFlies); generalizability to broader multivariate or non-oscillatory time series domains remains to be explored.

## Open Questions & Future Work

- [[multivariate-time-series-decomposition-alignment]]

## Key Concepts

- [[imfact]]: A model-agnostic framework for generating counterfactual explanations for time series classifiers by substituting Intrinsic Mode Functions obtained from Empirical Mode Decomposition.

## Archivist Review

Approved the core model-agnostic counterfactual explanation framework IMFACT and an open question regarding its multivariate extension via IMF alignment across channels. Routine dataset references and paper-local strategies were omitted.

### Approved Concepts
- IMFACT: It forms the core methodological contribution of the paper, providing a novel paradigm for generating counterfactuals via Intrinsic Mode Function substitution.

### Approved Open Questions
- Multivariate Time Series IMF Alignment: Multivariate time series are ubiquitous in real-world applications such as industrial monitoring and healthcare, making channel alignment in decomposition spaces a critical architectural hurdle.

## Links

- [Abstract](https://arxiv.org/abs/2608.04777)
- [PDF](https://arxiv.org/pdf/2608.04777)

