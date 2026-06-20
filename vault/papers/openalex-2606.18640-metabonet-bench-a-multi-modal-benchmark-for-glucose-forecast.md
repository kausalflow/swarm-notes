---
# CSL-compatible fields
title: "MetaboNet-Bench: A Multi-modal Benchmark for Glucose Forecasting in Type 1 Diabetes"
author:
  - literal: "Nathaniel Jeffries"
  - literal: "M. Wolff"
  - literal: "Sam Royston"
  - literal: "Elizabeth Healey"
  - literal: "Caleb Mayer"
  - literal: "David Klonoff"
  - literal: "M Snyder"
  - literal: "Tao Wang"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.18640"

# Custom fields
paper_id: "2606.18640"
paper_source: "openalex"
domain: "medicine"
tags:
  - "multimodal"
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "metabonet-bench"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:17:20Z"
created_at: "2026-06-20T08:17:20Z"
---

# MetaboNet-Bench: A Multi-modal Benchmark for Glucose Forecasting in Type 1 Diabetes

**Authors**: Nathaniel Jeffries, M. Wolff, Sam Royston, Elizabeth Healey, Caleb Mayer, David Klonoff, M Snyder, Tao Wang
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.18640](https://arxiv.org/abs/2606.18640)

## Summary

MetaboNet-Bench addresses the lack of standardized evaluation frameworks for glucose forecasting in type 1 diabetes by providing an extensible, multimodal benchmark. The framework incorporates essential clinical signals including continuous glucose monitoring (CGM) data, insulin dosing, and carbohydrate intake. By evaluating multiple model architectures, the authors demonstrate that the performance gains from additional modalities are conditioned on model complexity and reveal key performance gaps in existing algorithms.

## Key Contributions

- Introduces MetaboNet-Bench, an extensible open-source framework for standardizing multimodal glucose forecasting evaluation in type 1 diabetes.
- Enables benchmarking of models utilizing CGM, insulin dosing, and carbohydrate intake, addressing limitations of single-modality CGM approaches.
- Demonstrates that the efficacy of integrating multimodal clinical data is highly dependent on the complexity of the underlying model architecture.

## Open Questions & Future Work

- [[clinical-metric-standardization-glucose-forecasting]]
- [[multimodal-data-integration-challenges]]

## Key Concepts

- [[metabonet-bench]]: A multimodal benchmark for glucose forecasting incorporating CGM, insulin, and carbohydrate intake data.

## Archivist Review

Approved MetaboNet-Bench as a domain-specific evaluation framework central to the paper's contribution. The two open questions were approved for addressing critical gaps in clinical safety metrics and the integration of broader physiological modalities, respectively, which are significant bottlenecks in medical time-series forecasting.

### Approved Concepts
- MetaboNet-Bench: It fills a critical gap in standardized, multimodal evaluation for glycemic control in type 1 diabetes.

### Approved Open Questions
- Clinical Evaluation Metric Standardization: Standardizing clinically sensitive metrics is crucial for ensuring that models designed for AID systems are safe for extreme glucose states, rather than just accurate on average.
- Integration of Broader Data Modalities: Expanding the feature set beyond simple insulin and carbohydrate logs is necessary to account for the complex physiological factors that drive glycemic variability in real-world environments.

## Links

- [Abstract](https://arxiv.org/abs/2606.18640)
- [PDF](https://arxiv.org/pdf/2606.18640)

