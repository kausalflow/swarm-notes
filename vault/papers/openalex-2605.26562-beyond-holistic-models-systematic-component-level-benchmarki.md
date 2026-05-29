---
# CSL-compatible fields
title: "Beyond Holistic Models: Systematic Component-level Benchmarking of Deep Multivariate Time-Series Forecasting"
author:
  - literal: "Shuang Liang"
  - literal: "Chaochuan Hou"
  - literal: "Xu Yao"
  - literal: "Shiping Wang"
  - literal: "Hailiang Huang"
  - literal: "Songqiao Han"
  - literal: "Minqi Jiang"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.26562"

# Custom fields
paper_id: "2605.26562"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tscomp"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:37:16Z"
created_at: "2026-05-29T08:37:16Z"
---

# Beyond Holistic Models: Systematic Component-level Benchmarking of Deep Multivariate Time-Series Forecasting

**Authors**: Shuang Liang, Chaochuan Hou, Xu Yao, Shiping Wang, Hailiang Huang, Songqiao Han, Minqi Jiang
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.26562](https://arxiv.org/abs/2605.26562)

## Summary

This paper shifts the focus of multivariate time-series forecasting from holistic architectural design to granular, component-level analysis. The authors propose TSCOMP, a large-scale benchmarking framework that deconstructs models into discrete modules—preprocessing, encoding, architecture, and optimization—and evaluates their individual and interactive impacts. By leveraging a corpus of over 20,000 evaluations, the researchers demonstrate that automated component selection significantly outperforms complex, hand-crafted state-of-the-art models across diverse data characteristics.

## Key Contributions

- Introduces TSCOMP, a systematic benchmark for deconstructing multivariate time-series forecasting models into modular components (preprocessing, encoding, architectures, optimization).
- Establishes a performance corpus of over 20,000 model-dataset evaluations, enabling empirical analysis of component interactions and effectiveness.
- Demonstrates that automated component selection based on the corpus consistently outperforms state-of-the-art holistic architectures.

## Open Questions & Future Work

- [[llm-agent-continuous-benchmark-updating]]

## Key Concepts

- [[tscomp]]: A large-scale benchmark for deconstructing and evaluating deep multivariate time-series forecasting models at the component level.

## Archivist Review

I approved TSCOMP as it establishes a novel, systematic methodology for modular forecasting research, shifting focus from monolithic architectures to component-level interactions. The corresponding open question is approved for addressing the sustainability of benchmarking in rapidly evolving fields via automated knowledge integration. Other candidates were rejected to prioritize core methodological contributions over specific implementation metrics.

### Approved Concepts
- TSCOMP: It provides a foundational, systematic deconstruction of multivariate forecasting models into modular components, enabling data-driven automated architecture selection.

### Approved Open Questions
- Continuous Automated Benchmark Updating: This is critical for maintaining the utility of component-level benchmarks in a rapidly evolving research field where manual curation is unsustainable.

## Links

- [Abstract](https://arxiv.org/abs/2605.26562)
- [PDF](https://arxiv.org/pdf/2605.26562)

