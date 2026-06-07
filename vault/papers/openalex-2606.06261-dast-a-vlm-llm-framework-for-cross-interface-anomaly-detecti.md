---
# CSL-compatible fields
title: "DAST: A VLM-LLM Framework for Cross-Interface Anomaly Detection in O-RAN"
author:
  - literal: "Francesco Spinelli"
  - literal: "Esteban Municio"
  - literal: "Pau Baguer"
  - literal: "Ginés García-Avilés"
  - literal: "Xavier Costa-Pérez"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.06261"

# Custom fields
paper_id: "2606.06261"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "vision-language-model"
  - "anomaly-detection"
  - "zero-shot-learning"
  - "agent"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dast-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:20:20Z"
created_at: "2026-06-07T08:20:20Z"
---

# DAST: A VLM-LLM Framework for Cross-Interface Anomaly Detection in O-RAN

**Authors**: Francesco Spinelli, Esteban Municio, Pau Baguer, Ginés García-Avilés, Xavier Costa-Pérez
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.06261](https://arxiv.org/abs/2606.06261)

## Summary

The authors present DAST, a multi-agent framework designed for anomaly detection in O-RAN networks where traditional time-series methods struggle with high-dimensional telemetry and lack of labeled data. By utilizing a three-stage VLM-LLM-VLM pipeline, the system transforms KPI streams into visual and textual representations to perform cross-interface reasoning. This approach enables zero-shot detection of performance-degradation and Denial-of-Service attacks while providing actionable decision rationales. Experimental results on real O-RAN network traces demonstrate superior performance compared to state-of-the-art TSAD baselines.

## Key Contributions

- Introduces DAST, a zero-shot multi-agent VLM-LLM framework for cross-interface anomaly detection in disaggregated O-RAN environments.
- Implements a three-stage pipeline (VLM → LLM → VLM) that translates multivariate KPI telemetry into visual heatmaps and textual descriptions to identify anomalous interfaces and operational impacts.
- Achieves 0.910 F1-Score and 0.843 Accuracy on O-RAN performance degradation traces, outperforming traditional TSAD baselines.

## Open Questions & Future Work

- [[multi-vendor-oran-generalization]]
- [[autonomous-oran-mitigation-loops]]

## Key Concepts

- [[dast-framework]]: A multi-agent framework that chains VLM and LLM models to detect, classify, and explain cross-interface anomalies by converting multivariate time-series into visual and textual representations.

## Archivist Review

The DAST framework is approved for its novel cross-modal approach to anomaly detection in infrastructure telemetry, providing a reusable template for multi-agent VLM-LLM pipelines. The open questions regarding multi-vendor generalization and autonomous closed-loop control address critical bottlenecks for the O-RAN/6G compute continuum. No datasets were approved as none were provided with specific names that act as a primary, reusable resource.

### Approved Concepts
- DAST Framework: The DAST pipeline represents a novel, multi-agent approach to anomaly detection in complex, high-dimensional O-RAN telemetry by leveraging cross-modal (VLM-LLM) reasoning instead of traditional univariate or multivariate statistical TSAD models.

### Approved Open Questions
- Multi-vendor O-RAN validation: Ensuring generalizability across the fragmented O-RAN ecosystem is critical for practical operational adoption.
- Closing the autonomous loop: Autonomous closed-loop operation is a fundamental requirement for self-healing networks.

## Links

- [Abstract](https://arxiv.org/abs/2606.06261)
- [PDF](https://arxiv.org/pdf/2606.06261)

