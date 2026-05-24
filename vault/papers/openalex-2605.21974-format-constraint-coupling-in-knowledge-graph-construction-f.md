---
# CSL-compatible fields
title: "Format-Constraint Coupling in Knowledge Graph Construction from Statistical Tables"
author:
  - literal: "Jingxuan Qi"
  - literal: "Zhiqiang Ye"
  - literal: "Yuxiang Feng"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.21974"

# Custom fields
paper_id: "2605.21974"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "knowledge-graph"
  - "information-extraction"
  - "rag"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  - "CSVFidelity-Bench"
concept_slugs:
  - "format-constraint-coupling"
dataset_slugs:
  - "csvfidelity-bench"
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:47:48Z"
created_at: "2026-05-24T07:47:48Z"
---

# Format-Constraint Coupling in Knowledge Graph Construction from Statistical Tables

**Authors**: Jingxuan Qi, Zhiqiang Ye, Yuxiang Feng
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.21974](https://arxiv.org/abs/2605.21974)

## Summary

This paper investigates the degradation of knowledge graph fidelity during extraction from statistical CSV tables, identifying a phenomenon dubbed 'format-constraint coupling.' The authors show that the interaction between serialization format and schema constraints can cause catastrophic declines in fact coverage, primarily driven by surface-form anchoring. Furthermore, they demonstrate that current retrieval-based metrics fail to capture these extraction errors, proposing direct graph access as a necessary diagnostic tool. The work concludes with the release of CSVFidelity-Bench to facilitate more robust evaluation of structured data extraction pipelines.

## Key Contributions

- Identified format-constraint coupling as a significant failure mode in knowledge graph construction from statistical tables, showing super-additive performance degradation.
- Demonstrated that standard retrieval-based evaluation masks construction quality, while direct graph inspection reveals significant fidelity gaps up to 47.6 percentage points.
- Introduced CSVFidelity-Bench, a benchmark containing 15 datasets and 1,892 gold standard facts across 6 domains to support fidelity-aware evaluation of structured extraction.

## Open Questions & Future Work

- [[fidelity-aware-kg-evaluation]]

## Key Concepts

- [[format-constraint-coupling]]: A phenomenon where the interaction between data serialization formats and schema constraints in statistical tables leads to super-additive performance degradation.

## Archivist Review

I approved the concept of Format-Constraint Coupling as it describes a clear, reusable failure mode in KG construction. I also approved the CSVFidelity-Bench dataset and a corresponding open question regarding the need for better fidelity-aware evaluation metrics, as retrieval-based proxies are proven to be insufficient in this context. Other candidates were either too local to this specific paper or fell under generic ML benchmarking.

### Approved Concepts
- Format-Constraint Coupling: Identifies a novel systematic failure mode in LLM-based information extraction where serialization and schema constraints interact negatively to reduce knowledge graph fidelity.

### Approved Open Questions
- Fidelity-aware evaluation of construction: Current evaluation practices for GraphRAG often mask upstream construction errors, requiring better diagnostic tools for fidelity.

## Datasets

- [[csvfidelity-bench]]

## Links

- [Abstract](https://arxiv.org/abs/2605.21974)
- [PDF](https://arxiv.org/pdf/2605.21974)

