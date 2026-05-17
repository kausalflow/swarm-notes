---
# CSL-compatible fields
title: "Text Knows What, Tables Know When: Clinical Timeline Reconstruction via Retrieval-Augmented Multimodal Alignment"
author:
  - literal: "Sayantan Kumar"
  - literal: "Shahriar Noroozizadeh"
  - literal: "Juyong Kim"
  - literal: "Jeremy C. Weiss"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.15168"

# Custom fields
paper_id: "2605.15168"
paper_source: "openalex"
domain: "nlp"
tags:
  - "multimodal"
  - "language-model"
  - "retrieval-augmented-generation"
  - "instruction-tuning"
  - "benchmark"
architectures:
  []
datasets:
  - "mimic-iii"
  - "mimic-iv"
concept_slugs:
  - "retrieval-augmented-multimodal-alignment-framework"
dataset_slugs:
  - "mimic-iii"
  - "mimic-iv"
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:32:39Z"
created_at: "2026-05-17T07:32:39Z"
---

# Text Knows What, Tables Know When: Clinical Timeline Reconstruction via Retrieval-Augmented Multimodal Alignment

**Authors**: Sayantan Kumar, Shahriar Noroozizadeh, Juyong Kim, Jeremy C. Weiss
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.15168](https://arxiv.org/abs/2605.15168)

## Summary

This paper addresses the challenge of creating accurate clinical timelines by integrating imprecise but semantically rich clinical narratives with precise but incomplete structured EHR data. The authors propose a multi-step, graph-based pipeline that anchors events from text and calibrates their timing using retrieved structured EHR rows as external evidence. Experiments on the i2m4 benchmark show that this multimodal alignment significantly improves absolute timestamp accuracy compared to text-only methods, while uncovering clinical events not represented in tabular data.

## Key Contributions

- Proposes a novel retrieval-augmented multimodal alignment framework for clinical timeline reconstruction, outperforming unimodal text-only approaches.
- Establishes a graph-based multi-step pipeline that uses structured EHR data as external temporal evidence to calibrate unstructured clinical narratives.
- Demonstrates significant improvements in absolute timestamp accuracy (AULTC) and temporal concordance on the i2m4 benchmark using MIMIC-III and MIMIC-IV datasets.

## Open Questions & Future Work

- [[scaling-clinical-timeline-annotation-and-generalization]]

## Key Concepts

- [[retrieval-augmented-multimodal-alignment-framework]]: A graph-based reconstruction framework that calibrates text-extracted event timelines using retrieved structured EHR data as external temporal evidence.

## Archivist Review

I approved the retrieval-augmented multimodal alignment framework as it offers a robust, reusable method for temporal calibration in heterogeneous data environments. I limited dataset approval to MIMIC-III and IV due to their foundational status in clinical informatics, while rejecting the i2m4 benchmark as a routine evaluation artifact. The open question was narrowed to focus on the identified bottleneck of multimodal dependency and domain generalizability.

### Approved Concepts
- Retrieval-Augmented Multimodal Alignment Framework: Provides a structured mechanism for cross-modal temporal calibration, separating semantic text extraction from tabular temporal anchoring.

### Approved Open Questions
- Scaling Clinical Timeline Annotation: Exposes the bottleneck of multimodal dependency in automated clinical trajectory modeling.

### Rejected Candidates
- [dataset] i2m4 benchmark (`i2m4-benchmark`) - not_novel: Routine benchmark for clinical time-series research.

## Datasets

- [[mimic-iii]]
- [[mimic-iv]]

## Links

- [Abstract](https://arxiv.org/abs/2605.15168)
- [PDF](https://arxiv.org/pdf/2605.15168)

