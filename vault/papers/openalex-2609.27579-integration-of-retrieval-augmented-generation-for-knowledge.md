---
# CSL-compatible fields
title: "Integration of Retrieval-Augmented Generation for Knowledge Access in the ELBE Accelerator Control System"
author:
  - literal: "Najmeh Mirian"
issued:
  date-parts:
    - [2026, 9, 23]
url: "https://arxiv.org/abs/2609.27579"

# Custom fields
paper_id: "2609.27579"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "retrieval-augmented-generation"
  - "rag"
  - "vector-database"
  - "embedding"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-26T09:37:58Z"
created_at: "2026-09-26T09:37:58Z"
---

# Integration of Retrieval-Augmented Generation for Knowledge Access in the ELBE Accelerator Control System

**Authors**: Najmeh Mirian
**Date**: 2026-09-23
**Paper ID**: [openalex:2609.27579](https://arxiv.org/abs/2609.27579)

## Summary

This paper presents a Retrieval-Augmented Generation (RAG) framework designed to integrate heterogeneous operational knowledge—such as electronic logbooks, interlock reports, and machine archive time-series data—into a unified AI-assisted support tool for the ELBE accelerator control system. The proposed architecture indexes facility documentation and historical records using domain-adapted embeddings in a vector database to enable LLM-driven, structured, and traceable responses for operators. The work details the underlying data integration strategies, system design, and key challenges involved in achieving real-time AI assistance in accelerator operations.

## Key Contributions

- Proposed a Retrieval-Augmented Generation (RAG) framework tailored for the ELBE accelerator control system to integrate heterogeneous operational knowledge.
- Designed a unified architecture indexing electronic logbooks, archive time-series data, and subsystem manuals via domain-adapted embeddings and a vector database.
- Outlined the system architecture, data integration strategy, and real-time operational challenges for AI-assisted accelerator control.

## Limitations

The work presents a framework and system architecture proposal with discussion of integration strategies and challenges, rather than completed real-time evaluations.

## Open Questions & Future Work

- [[rag-accelerator-control-limitations]]

## Archivist Review

The paper applies standard Retrieval-Augmented Generation to accelerator control systems. No novel architectural concepts or datasets are introduced that merit a permanent vault note, but the open question regarding RAG operational limitations in particle accelerator environments is specific and valuable to track.

### Approved Open Questions
- RAG Limitations in Accelerator Control: Addressing these limitations is crucial for ensuring the reliability, accuracy, and real-time usability of AI-assisted decision support tools in safety-critical accelerator environments.

## Links

- [Abstract](https://arxiv.org/abs/2609.27579)
- [PDF](https://arxiv.org/pdf/2609.27579)

