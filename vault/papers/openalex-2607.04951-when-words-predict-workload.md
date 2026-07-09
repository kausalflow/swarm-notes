---
# CSL-compatible fields
title: "When Words Predict Workload"
author:
  - literal: "Anubhab Banerjee"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2607.04951"

# Custom fields
paper_id: "2607.04951"
paper_source: "openalex"
domain: "nlp,system"
tags:
  - "llm"
  - "language-model"
  - "agent"
  - "model-compression"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "linguistic-resource-forecasting-lrf-gateway"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:18:48Z"
created_at: "2026-07-09T08:18:48Z"
---

# When Words Predict Workload

**Authors**: Anubhab Banerjee
**Date**: 2026-07-06
**Paper ID**: [openalex:2607.04951](https://arxiv.org/abs/2607.04951)

## Summary

This paper addresses the failure of standard LLM schedulers that rely solely on token counts when processing linguistically rigid texts, which cause unpredictable VRAM spikes and OOM errors. The author introduces a Linguistic Resource Forecasting (LRF) gateway that employs an XGBoost predictor to analyze 16-dimensional text-structure vectors and forecast memory demand prior to allocation. By combining this predictor with a dynamic, latency-aware routing threshold, the system effectively offloads high-complexity requests to remote hardware while keeping edge GPU memory usage within safe bounds. Live trials confirm that this method significantly outperforms static token-based scheduling, achieving an order-of-magnitude reduction in operational misroutes.

## Key Contributions

- Introduced a CPU-side Linguistic Resource Forecasting (LRF) gateway that predicts workload complexity via 16-dimensional text-structure vectors and XGBoost to prevent OOM crashes on edge hardware.
- Formulated a dynamic routing strategy using a closed-form threshold (Tauroute(t)) based on real-time latency telemetry, achieving an 8.2% relative reduction in misroutes.
- Demonstrated in a 6,000-request live trial that LRF reduces the operational misroute fraction to 0.087–0.095, compared to 0.849 for token-count baselines, while maintaining peak VRAM at 4.82 GiB.

## Open Questions & Future Work

- [[downstream-classification-accuracy-for-esc-routing]]

## Key Concepts

- [[linguistic-resource-forecasting-lrf-gateway]]: A CPU-side gateway that uses structural text analysis to predict LLM workload complexity and gate routing decisions.

## Archivist Review

I have approved the LRF gateway as a novel scheduling paradigm shift from token-based to text-structure based load forecasting. The open question regarding downstream classifier accuracy was slightly renamed for better clarity and to ensure it remains applicable to broader authorship classification tasks beyond specific named tools.

### Approved Concepts
- Linguistic Resource Forecasting (LRF) Gateway: The gateway enables pre-allocation routing decisions based on text structure rather than token count, preventing memory saturation.

### Approved Open Questions
- Downstream Classifier Routing Accuracy: Understanding whether these models successfully distinguish authorship once the escalation trigger is met is critical to justifying the computational and latency costs of cloud-tier offloading.

### Rejected Candidates
- [open_question] Downstream Binoculars Classifier Accuracy (`binoculars-downstream-accuracy`) - other: The title was refined for better clarity and to avoid tying the question strictly to a specific commercial tool name.

## Links

- [Abstract](https://arxiv.org/abs/2607.04951)
- [PDF](https://arxiv.org/pdf/2607.04951)

