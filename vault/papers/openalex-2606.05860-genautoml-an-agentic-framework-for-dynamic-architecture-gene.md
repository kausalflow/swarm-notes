---
# CSL-compatible fields
title: "GenAutoML: An Agentic Framework for Dynamic Architecture Generation and Optimization in Time-Series Analysis"
author:
  - literal: "Oleeviya Babu Poikarayil"
  - literal: "Cédric Schockaert"
  - literal: "Abdulrahman Nahhas"
  - literal: "Christian Daase"
  - literal: "Mursal Dawodi"
  - literal: "Jawid Ahmad Baktash"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.05860"

# Custom fields
paper_id: "2606.05860"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "neural-architecture-search"
  - "agent"
  - "normalization"
architectures:
  []
datasets:
  []
concept_slugs:
  - "genautoml"
  - "dynamic-revin"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:18:31Z"
created_at: "2026-06-07T08:18:31Z"
---

# GenAutoML: An Agentic Framework for Dynamic Architecture Generation and Optimization in Time-Series Analysis

**Authors**: Oleeviya Babu Poikarayil, Cédric Schockaert, Abdulrahman Nahhas, Christian Daase, Mursal Dawodi, Jawid Ahmad Baktash
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.05860](https://arxiv.org/abs/2606.05860)

## Summary

GenAutoML is an agentic framework that employs Large Language Models as autonomous neural architects to generate, refine, and validate task-specific PyTorch architectures for time-series analysis. The system incorporates a reflection-based sandbox for iterative code refinement and a signature-aware runtime to guarantee architectural integrity. To handle non-stationary data, the framework includes a Dynamic Reversible Instance Normalization (Dyn-RevIN) module. Benchmarking on standard datasets shows that the framework produces highly efficient, low-latency models suitable for edge computing deployments without sacrificing predictive accuracy.

## Key Contributions

- Introduced GenAutoML, an agentic framework that utilizes LLMs to autonomously design and refine neural architectures for time-series forecasting and anomaly detection.
- Developed a Sandboxed Reflection Loop and Signature-Aware Runtime to ensure the safety and consistency of generated model code.
- Introduced Dyn-RevIN, a normalization technique that significantly enhances model robustness when facing non-stationary time-series data.
- Demonstrated that generated architectures like WaveInterferenceNet achieve ultra-low inference latency (<0.01 ms/sample) while maintaining state-of-the-art performance on ETTh1, ETTm1, and Weather benchmarks.

## Open Questions & Future Work

- [[reducing-generative-synthesis-latency]]
- [[hardware-aware-architecture-synthesis]]

## Key Concepts

- [[genautoml]]: An agentic framework that utilizes LLMs as neural architects to translate natural language specifications into specialized PyTorch time-series models.
- [[dynamic-revin]]: A dynamic adaptation of reversible instance normalization that enhances model robustness against non-stationary time-series data.

## Archivist Review

I approved the GenAutoML framework and its Dyn-RevIN module because they represent high-impact, reusable contributions to agentic model generation and non-stationary time-series handling. The approved open questions capture the two core bottlenecks for this technology: reducing synthesis latency and enforcing hardware-level constraints during generation. Generic architecture subcomponents and routine datasets were excluded to maintain the vault's standard of focusing on novel, cross-domain mechanisms.

### Approved Concepts
- GenAutoML: It establishes an agentic approach to neural architecture search for time-series, moving beyond static search spaces to model generation.
- Dynamic Reversible Instance Normalization (Dyn-RevIN): It addresses the critical challenge of non-stationarity by adding dynamic normalization capabilities to time-series forecasting models.

### Approved Open Questions
- Reducing Generative Synthesis Latency: This is the primary barrier to the practical, real-time application of agentic AutoML systems in edge computing scenarios.
- Hardware-Aware Architecture Synthesis: Enforcing hardware awareness is a prerequisite for moving beyond general-purpose models to deployment-specific, resource-efficient architectures.

### Rejected Candidates
- [open_question] Reducing Generative Synthesis Latency (`reducing-generative-latency-local-llms`) - duplicate_existing: This was a duplicate of the approved 'reducing-generative-synthesis-latency' candidate.

## Links

- [Abstract](https://arxiv.org/abs/2606.05860)
- [PDF](https://arxiv.org/pdf/2606.05860)

