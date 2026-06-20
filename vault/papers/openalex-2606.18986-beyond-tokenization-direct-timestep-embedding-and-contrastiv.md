---
# CSL-compatible fields
title: "Beyond Tokenization: Direct Timestep Embedding and Contrastive Alignment for Time-Series Question Answering"
author:
  - literal: "Yafeng Wu"
  - literal: "Huu Hiep Nguyen"
  - literal: "Thuy Nguyen"
  - literal: "Hung Le"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.18986"

# Custom fields
paper_id: "2606.18986"
paper_source: "openalex"
domain: "nlp,time-series"
tags:
  - "llm"
  - "time-series"
  - "question-answering"
  - "contrastive-learning"
  - "embedding"
  - "benchmark"
  - "tsqa"
architectures:
  - "decoder-only"
datasets:
  - "Time-MQA"
concept_slugs:
  - "cade-framework"
dataset_slugs:
  - "time-mqa"
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:17:06Z"
created_at: "2026-06-20T08:17:06Z"
---

# Beyond Tokenization: Direct Timestep Embedding and Contrastive Alignment for Time-Series Question Answering

**Authors**: Yafeng Wu, Huu Hiep Nguyen, Thuy Nguyen, Hung Le
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.18986](https://arxiv.org/abs/2606.18986)

## Summary

This paper addresses the limitation of standard LLM tokenization on continuous time-series data, which leads to loss of magnitude and scale information. The authors introduce CADE, a framework that employs a point-wise linear encoder to map individual timesteps directly into the LLM's embedding space, bypassing traditional patch-based windowing. To enhance semantic consistency, a supervised contrastive loss aligns time-series representations with text-based class anchors. The method is validated on the Time-MQA benchmark, showing superior performance over existing LLM-based TSQA approaches.

## Key Contributions

- Proposes CADE, a framework that replaces patch-based encoding with point-wise linear timestep embedding to preserve granular temporal information.
- Introduces a one-directional supervised contrastive loss to align time-series embeddings directly with class-name text anchors.
- Demonstrates consistent performance improvements across six TSQA tasks on the Time-MQA benchmark compared to LLM baselines.

## Open Questions & Future Work

- [[explicit-temporal-concept-alignment]]

## Key Concepts

- [[cade-framework]]: A framework for time-series question answering that uses point-wise linear encoders and a supervised contrastive loss to align numerical time-series data with LLM embedding spaces.

## Archivist Review

The CADE framework is approved as it offers a specific architectural departure from standard patch-based time-series tokenization. Time-MQA is approved as the central benchmark for evaluating these LLM-based TSQA methods. The open question regarding explicit temporal alignment is approved as it addresses a core bottleneck in the semantic grounding of numerical data for LLMs.

### Approved Concepts
- CADE (Contrastive Alignment with Direct Embedding): The CADE framework provides a viable alternative to patch-based tokenization for integrating continuous-valued time series into LLMs.

### Approved Open Questions
- Explicit Temporal Concept Alignment: This is a fundamental limitation in grounding time-series data in language models; without explicit concept alignment, models lack robust reasoning capabilities for time-series analysis.

### Rejected Candidates
- [concept] Contrastive Alignment (`cade-framework-contrastive-alignment`) - subcomponent_of_broader_mechanism: This is a sub-component of the CADE framework; the framework itself is the more appropriate entry for the vault.
- [concept] Direct Timestep Embedding (`cade-framework-direct-timestep-embedding`) - subcomponent_of_broader_mechanism: This is a sub-component of the CADE framework; the framework itself is the more appropriate entry for the vault.

## Datasets

- [[time-mqa]]

## Links

- [Abstract](https://arxiv.org/abs/2606.18986)
- [PDF](https://arxiv.org/pdf/2606.18986)

