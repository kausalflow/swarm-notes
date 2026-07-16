---
# CSL-compatible fields
title: "A Multimodal Dataset for Large Language Model Applications in the Energy Domain"
author:
  - literal: "Costas Mylonas"
  - literal: "Magda Foti"
issued:
  date-parts:
    - [2026, 7, 13]
url: "https://arxiv.org/abs/2607.11459"

# Custom fields
paper_id: "2607.11459"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "llm"
  - "multimodal"
  - "dataset"
  - "benchmark"
architectures:
  []
datasets:
  - "mAIEnergy"
concept_slugs:
  - "maienergy-dataset"
dataset_slugs:
  - "maienergy"
skill: "TimeSeriesSkill"
processed_at: "2026-07-16T07:14:48Z"
created_at: "2026-07-16T07:14:48Z"
---

# A Multimodal Dataset for Large Language Model Applications in the Energy Domain

**Authors**: Costas Mylonas, Magda Foti
**Date**: 2026-07-13
**Paper ID**: [openalex:2607.11459](https://arxiv.org/abs/2607.11459)

## Summary

This paper introduces the mAIEnergy dataset, a comprehensive, multimodal corpus designed to advance AI and LLM applications within the energy sector. The dataset harmonizes textual policy and scientific documents with visual, numerical time series, and geospatial infrastructure data. By adhering to FAIR principles and providing reproducible workflows, the authors establish a foundational knowledge base for energy research, modeling, and decision-making.

## Key Contributions

- Introduces mAIEnergy, an open-access, multimodal corpus tailored for energy-domain LLM applications.
- Integrates over 50,000 documents, 20,000 images, 25 million time series records, and 2 million geospatial/relational entries.
- Provides harmonized data following FAIR principles, including reproducible retrieval and preparation workflows.

## Open Questions & Future Work

- [[geographic-generalization-energy-datasets]]

## Key Concepts

- [[maienergy-dataset]]: A large-scale, multimodal, and FAIR-compliant dataset integrating textual, numerical, visual, and geospatial data for energy sector AI research.

## Archivist Review

The mAIEnergy dataset is approved due to its role as a novel, foundational, and multimodal benchmark for energy-domain LLM applications. The associated open question regarding geographic generalization is critical for the long-term utility of domain-specific foundation models in the energy sector. Other candidates were not submitted.

### Approved Concepts
- mAIEnergy Dataset: It serves as the first large-scale, harmonized multimodal knowledge base specifically designed for LLM applications in the energy domain.

### Approved Open Questions
- Globalizing Multimodal Energy Datasets: Geographic bias in training data limits the generalizability and utility of AI decision-support tools in the energy sector, which is fundamentally a global industry with localized operational dependencies. Identifying methods to expand coverage while maintaining the integrity of multimodal relationships is essential for creating truly global energy knowledge bases.

## Datasets

- [[maienergy]]

## Links

- [Abstract](https://arxiv.org/abs/2607.11459)
- [PDF](https://arxiv.org/pdf/2607.11459)

