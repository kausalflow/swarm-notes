---
# CSL-compatible fields
title: "Toto 2.0: Time Series Forecasting Enters the Scaling Era"
author:
  - literal: "Emaad Khwaja"
  - literal: "Chris Lettieri"
  - literal: "Gerald Woo"
  - literal: "Eden Belouadah"
  - literal: "Marc Cenac"
  - literal: "Guillaume Jarry"
  - literal: "Enguerrand Paquin"
  - literal: "Xunyi Zhao"
  - literal: "Viktoriya Zhukov"
  - literal: "Othmane Abou-Amal"
  - literal: "Chenghao Liu"
  - literal: "Ameet Talwalkar"
  - literal: "D.B.D. Asker"
issued:
  date-parts:
    - [2026, 5, 19]
url: "https://arxiv.org/abs/2605.20119"

# Custom fields
paper_id: "2605.20119"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "language-model"
  - "benchmark"
  - "dataset"
  - "scaling-law"
architectures:
  []
datasets:
  []
concept_slugs:
  - "u-mup-hyperparameter-transfer-pipeline"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-22T08:16:30Z"
created_at: "2026-05-22T08:16:30Z"
---

# Toto 2.0: Time Series Forecasting Enters the Scaling Era

**Authors**: Emaad Khwaja, Chris Lettieri, Gerald Woo, Eden Belouadah, Marc Cenac, Guillaume Jarry, Enguerrand Paquin, Xunyi Zhao, Viktoriya Zhukov, Othmane Abou-Amal, Chenghao Liu, Ameet Talwalkar, D.B.D. Asker
**Date**: 2026-05-19
**Paper ID**: [openalex:2605.20119](https://arxiv.org/abs/2605.20119)

## Summary

Toto 2.0 introduces a family of open-weights time series foundation models that demonstrate robust scaling behavior from 4M to 2.5B parameters. By implementing a unified training recipe and the u-muP hyperparameter transfer pipeline, the models achieve superior forecasting performance across diverse benchmarks. The findings confirm the scalability of time series models, providing a foundation for large-scale observational forecasting.

## Key Contributions

- Toto 2.0 demonstrates reliable forecast-quality improvements across parameter scales from 4M to 2.5B, empirically validating scaling laws for time series foundation models.
- The Toto 2.0 model family establishes a new state-of-the-art performance across three distinct forecasting benchmarks: BOOM, GIFT-Eval, and TIME.
- Introduces a robust training recipe and the u-muP hyperparameter transfer pipeline to ensure stable convergence and performance across different model sizes.

## Open Questions & Future Work

- [[tsfm-long-horizon-stability]]
- [[principled-tsfm-data-curation]]

## Key Concepts

- [[u-mup-hyperparameter-transfer-pipeline]]: A hyperparameter transfer framework designed to facilitate consistent scaling behavior for time series foundation models.

## Archivist Review

I approved the scaling hyperparameter pipeline as it is a core methodological contribution enabling the paper's main claim about scaling foundation models. I also approved two high-level open questions that characterize the current limitations of TSFMs regarding long-horizon stability and the need for more systematic data curation. Routine benchmarking datasets were rejected as they do not constitute standalone knowledge assets.

### Approved Concepts
- u-muP Hyperparameter Transfer Pipeline: This pipeline is central to the paper's claimed scaling effectiveness, ensuring stable model performance across a wide range of parameter sizes.

### Approved Open Questions
- TSFM Long-Horizon Stability: Bridging this gap is necessary for the adoption of TSFMs in mission-critical applications where long-horizon stability is essential.
- Principled TSFM Data Curation: Standardized data curation is a critical bottleneck for the predictable scaling of time series foundation models.

### Rejected Candidates
- [dataset] BOOM Observability Benchmark (`BOOM`) - not_novel: Routine benchmarking dataset; insufficient evidence for long-term vault inclusion.
- [dataset] GIFT-Eval Benchmark (`GIFT-Eval`) - not_novel: Routine benchmarking dataset; insufficient evidence for long-term vault inclusion.
- [dataset] TIME Benchmark (`TIME`) - not_novel: Routine benchmarking dataset; insufficient evidence for long-term vault inclusion.

## Links

- [Abstract](https://arxiv.org/abs/2605.20119)
- [PDF](https://arxiv.org/pdf/2605.20119)

