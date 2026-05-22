---
# CSL-compatible fields
title: "Accurate, Efficient, and Explainable Deep Learning Approaches for Environmental Science Problems"
author:
  - literal: "Jimeng Shi"
issued:
  date-parts:
    - [2026, 5, 19]
url: "https://arxiv.org/abs/2605.19366"

# Custom fields
paper_id: "2605.19366"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "diffusion-model"
  - "forecasting"
  - "rag"
  - "explainability"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "walef"
  - "codicast"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-22T08:17:21Z"
created_at: "2026-05-22T08:17:21Z"
---

# Accurate, Efficient, and Explainable Deep Learning Approaches for Environmental Science Problems

**Authors**: Jimeng Shi
**Date**: 2026-05-19
**Paper ID**: [openalex:2605.19366](https://arxiv.org/abs/2605.19366)

## Summary

This dissertation presents Environmental Intelligence, a framework of AI-based approaches addressing three critical environmental challenges: water level management in coastal systems, global probabilistic weather forecasting, and scientific question-answering. The author introduces specialized architectures—WaLeF and FIDLAr—for flood forecasting and management, a conditional diffusion model (CoDiCast) for weather prediction, and a retrieval-augmented generation system (Hypercube-RAG) for domain-specific knowledge retrieval. These methods improve upon traditional physics-based models and standard LLM approaches by enhancing accuracy, computational efficiency, and explainability.

## Key Contributions

- Introduced WaLeF, a deep learning model for real-time water level forecasting that achieves superior accuracy and efficiency over physics-based models.
- Developed FIDLAr, a forecast-informed deep learning model for managing coastal water levels that provides interpretability alongside predictive performance.
- Proposed CoDiCast, a conditional diffusion model for global weather forecasting that offers explicit uncertainty quantification at scale.
- Presented Hypercube-RAG, a structured text cube-based retrieval-augmented generation framework that balances accuracy, efficiency, and explainability for environmental scientific question-answering.

## Open Questions & Future Work

- [[ai-prediction-evaluation-optimization-bottleneck]]

## Key Concepts

- [[walef]]: A deep learning model specifically designed for efficient water level forecasting in complex coastal river systems.
- [[codicast]]: A conditional diffusion model framework for accurate and efficient probabilistic weather forecasting with explicit uncertainty quantification.

## Archivist Review

I approved two domain-specific architectures (WaLeF and CoDiCast) that represent significant shifts toward neural surrogate modeling and generative probabilistic forecasting in environmental science. The open question regarding AI-driven optimization frameworks addresses the foundational challenge of transitioning from pure forecasting to decision-making in complex systems. Hypercube-RAG was rejected as a domain-specific implementation of retrieval-augmented generation rather than a broadly reusable forecasting mechanism.

### Approved Concepts
- WaLeF: Central deep learning architecture proposed for water level forecasting in coastal river systems, serving as a template for real-time hydrologic surrogate modeling.
- CoDiCast: Core method for probabilistic global weather forecasting using conditional diffusion models, addressing scale and uncertainty.

### Approved Open Questions
- AI-Driven Optimization Framework Applicability: Bridging the gap between neural prediction surrogates and decision-focused optimization is critical for moving beyond simple forecasting into actionable environmental management.

### Rejected Candidates
- [concept] Hypercube-RAG (`hypercube-rag`) - subcomponent_of_broader_mechanism: This is a RAG subcomponent tailored for scientific question-answering rather than a core forecasting mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2605.19366)
- [PDF](https://arxiv.org/pdf/2605.19366)

