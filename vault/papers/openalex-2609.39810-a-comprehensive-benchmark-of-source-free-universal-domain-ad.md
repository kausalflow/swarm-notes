---
# CSL-compatible fields
title: "A Comprehensive Benchmark of Source-Free Universal Domain Adaptation on Time Series Representations"
author:
  - literal: "Romain Mussard"
  - literal: "Fannia Pacheco"
  - literal: "Maxime Bérar"
  - literal: "Paul Honeiné"
  - literal: "Gilles Gasso"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.39810"

# Custom fields
paper_id: "2609.39810"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "benchmark"
  - "evaluation"
  - "pre-training"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:08:16Z"
created_at: "2026-10-03T10:08:16Z"
---

# A Comprehensive Benchmark of Source-Free Universal Domain Adaptation on Time Series Representations

**Authors**: Romain Mussard, Fannia Pacheco, Maxime Bérar, Paul Honeiné, Gilles Gasso
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.39810](https://arxiv.org/abs/2609.39810)

## Summary

This paper introduces the first comprehensive benchmark for Source-Free Universal Domain Adaptation (SF-UniDA) on time series representations, filling a gap previously dominated by image domain research. The authors evaluate pretrained time series foundation models alongside classical backbones and uncover a critical sensitivity issue regarding unknown-sample rejection thresholds across existing methods. To mitigate this, they propose a plug-in auto-thresholding module applicable to any SF-UniDA framework, providing new empirical insights on three public time series datasets.

## Key Contributions

- Presents the first comprehensive benchmark for Source-Free Universal Domain Adaptation (SF-UniDA) on time series data, addressing label-set mismatches without source data access.
- Conducts the first systematic evaluation of pretrained time series foundation models as feature extractors for domain adaptation.
- Identifies the extreme sensitivity of unknown-sample rejection inference thresholds in existing SF-UniDA methods and proposes a robust plug-in auto-thresholding module.
- Demonstrates through experiments on standard time series benchmarks that foundation models do not systematically outperform classical backbones, highlighting the need for time series-specific SF-UniDA strategies.

## Limitations

Existing SF-UniDA methods and foundation models struggle with unknown-sample rejection sensitivity on time series, indicating that specialized domain adaptation frameworks for time series remain an open challenge.

## Open Questions & Future Work

- [[time-series-specific-sf-unida]]

## Archivist Review

Applied rigorous standards: no reusable novel forecasting concepts or specific named datasets met the strict inclusion criteria, but the open question regarding time-series-specific source-free universal domain adaptation addresses a genuine foundational gap highlighted by the paper.

### Approved Open Questions
- Time-Series-Specific SF-UniDA Approaches: Crucial for advancing domain adaptation in temporal data modalities without relying on source data privacy violations or poorly calibrated vision-based heuristics.

### Rejected Candidates
- [open_question] Time-Series-Specific SF-UniDA Approaches (`time-series-specific-sf-unida`) - generic: The question is appropriately scoped and retained.

## Links

- [Abstract](https://arxiv.org/abs/2609.39810)
- [PDF](https://arxiv.org/pdf/2609.39810)

