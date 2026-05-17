---
# CSL-compatible fields
title: "TopoPrimer: The Missing Topological Context in Forecasting Models"
author:
  - literal: "Zara Zetlin"
  - literal: "Kayhan Moharreri"
  - literal: "Maria Safi"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.15035"

# Custom fields
paper_id: "2605.15035"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "topoprimer"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:30:30Z"
created_at: "2026-05-17T07:30:30Z"
---

# TopoPrimer: The Missing Topological Context in Forecasting Models

**Authors**: Zara Zetlin, Kayhan Moharreri, Maria Safi
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.15035](https://arxiv.org/abs/2605.15035)

## Summary

TopoPrimer is a novel framework that enhances forecasting models by incorporating global topological structure as an explicit input. Using persistent homology and spectral sheaf coordinates, the approach provides structural context that is particularly effective in cold-start scenarios and during high-volatility seasonal demand. Experimental results across multiple benchmarks and backbone models like Chronos and TimesFM show consistent accuracy improvements, confirming that topological signal is complementary to standard temporal modeling.

## Key Contributions

- Introduced TopoPrimer, a topological framework that improves forecasting accuracy by incorporating population-level structural context.
- Achieved up to 7.3% MSE reduction on the ECL benchmark when applied to foundation models like Chronos and TimesFM.
- Demonstrated that TopoPrimer mitigates performance degradation during seasonal demand spikes (staying within 10% compared to 50% for baselines) and cold-start scenarios (27% MAE reduction).

## Open Questions & Future Work

- [[multi-parameter-persistent-homology-forecasting]]

## Key Concepts

- [[topoprimer]]: A framework that integrates global topological structure—derived via persistent homology and spectral sheaf coordinates—as explicit input for forecasting models.

## Archivist Review

I approved TopoPrimer as it introduces a novel mechanism for injecting topological priors into forecasting backbones, which is a highly reusable methodological contribution. I also approved the open question regarding multi-parameter persistent homology because it addresses a fundamental limitation in the expressivity of current TDA methods for time-series forecasting. I rejected the learned filtration metrics proposal as it is a specific implementation detail rather than a broadly transformative research direction for the field.

### Approved Concepts
- TopoPrimer: It is the core contribution of the paper, introducing a framework for augmenting forecasting models with topological structural data.

### Approved Open Questions
- Multi-parameter persistent homology filtrations: Multi-parameter persistent homology is a significant advancement in TDA that could offer more nuanced geometric descriptions of complex, multi-modal data manifolds.

### Rejected Candidates
- [open_question] Learned Topological Filtration Metrics (`learned-filtration-metrics-tda`) - low_impact: This is a specific architectural optimization for TDA pipelines that falls under general future work of learning better input representations, rather than a fundamental open question in forecasting dynamics.

## Links

- [Abstract](https://arxiv.org/abs/2605.15035)
- [PDF](https://arxiv.org/pdf/2605.15035)

