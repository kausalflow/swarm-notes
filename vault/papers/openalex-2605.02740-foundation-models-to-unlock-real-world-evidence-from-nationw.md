---
# CSL-compatible fields
title: "Foundation Models to Unlock Real-World Evidence from Nationwide Medical Claims"
author:
  - literal: "Fan Ma"
  - literal: "Yuntian Liu"
  - literal: "Xiang Lan"
  - literal: "Weipeng Zhou"
  - literal: "Jun Ni"
  - literal: "Mauro Giuffrè"
  - literal: "Lingfei Qian"
  - literal: "Xueqing Peng"
  - literal: "Yujia Zhou"
  - literal: "Ruey-Ling Weng"
  - literal: "Huan He"
  - literal: "Lu Li"
  - literal: "Qingyu Chen"
  - literal: "Andrew Loza"
  - literal: "Laila Rasmy"
  - literal: "Degui Zhi"
  - literal: "Yuan Lu"
  - literal: "Chenjie Zeng"
  - literal: "Joshua C. Denny"
  - literal: "Lee Schwamm"
  - literal: "Daniella Meeker"
  - literal: "Lucila Ohno-Machado"
  - literal: "Yong Chen"
  - literal: "Hua Xu"
issued:
  date-parts:
    - [2026, 5, 4]
url: "https://arxiv.org/abs/2605.02740"

# Custom fields
paper_id: "2605.02740"
paper_source: "openalex"
domain: "medicine"
tags:
  - "llm"
  - "language-model"
  - "transformer"
  - "pre-training"
  - "fine-tuning"
  - "multimodal"
architectures:
  - "decoder-only"
datasets:
  - "MarketScan"
concept_slugs:
  - "reclaim"
dataset_slugs:
  - "marketscan"
skill: "TimeSeriesSkill"
processed_at: "2026-05-07T07:37:44Z"
created_at: "2026-05-07T07:37:44Z"
---

# Foundation Models to Unlock Real-World Evidence from Nationwide Medical Claims

**Authors**: Fan Ma, Yuntian Liu, Xiang Lan, Weipeng Zhou, Jun Ni, Mauro Giuffrè, Lingfei Qian, Xueqing Peng, Yujia Zhou, Ruey-Ling Weng, Huan He, Lu Li, Qingyu Chen, Andrew Loza, Laila Rasmy, Degui Zhi, Yuan Lu, Chenjie Zeng, Joshua C. Denny, Lee Schwamm, Daniella Meeker, Lucila Ohno-Machado, Yong Chen, Hua Xu
**Date**: 2026-05-04
**Paper ID**: [openalex:2605.02740](https://arxiv.org/abs/2605.02740)

## Summary

ReClaim is a generative foundation model trained on 43.8 billion longitudinal medical events from MarketScan administrative claims spanning 2008-2022. The model, which scales up to 1.7 billion parameters, demonstrates superior performance in disease-onset prediction compared to established benchmarks like LightGBM and the Delphi model. Beyond predictive tasks, the model enhances real-world evidence generation by improving accuracy in expenditure forecasting and significantly reducing bias in target trial emulation. These findings validate administrative claims as a robust, scalable substrate for general-purpose healthcare foundation models.

## Key Contributions

- Proposed ReClaim, a generative transformer trained on 43.8 billion events from nationwide claims data, achieving a mean AUC of 75.6% across 1,000+ disease-onset tasks.
- Demonstrated that ReClaim outperforms LightGBM and Delphi models, with significant performance gains specifically for rare diseases.
- Showed that ReClaim improves real-world evidence generation, increasing explained variance in expenditure forecasting and reducing systematic bias in target trial emulation by 72%.

## Open Questions & Future Work

- [[multimodal-healthcare-foundation-models-integration]]
- [[causal-inference-embedding-validation]]

## Key Concepts

- [[reclaim]]: A generative transformer model trained on large-scale longitudinal medical claims data for disease prediction and real-world evidence generation.

## Archivist Review

Approved ReClaim as it represents a significant scale in medical foundation modeling. Approved MarketScan as the foundational dataset for these claims-based models. Open questions were consolidated and refined to capture the challenges of multimodal integration and the integration of learned representations into causal inference, which are essential directions for clinical foundation models.

### Approved Concepts
- ReClaim: It is the central foundation model proposed for processing administrative medical claims data at scale, demonstrating a significant shift towards training on multi-year, nationwide datasets.

### Approved Open Questions
- Multimodal Healthcare Foundation Models: Multimodal integration is critical for transitioning foundation models from population-level pattern recognition to clinically actionable, patient-specific insights.
- Causal Inference Embedding Validation: Validating this approach is essential for moving toward automated, data-driven confounding adjustment in real-world evidence generation.

## Datasets

- [[marketscan]]

## Links

- [Abstract](https://arxiv.org/abs/2605.02740)
- [PDF](https://arxiv.org/pdf/2605.02740)

