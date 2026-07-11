---
# CSL-compatible fields
title: "ShapeTalk: Combining Natural Language and Sketch for Time-Series Pattern Querying"
author:
  - literal: "G. S. Sun"
  - literal: "Yueqiao Chen"
  - literal: "Emily Guo"
  - literal: "Yutong Yao"
  - literal: "Dongyu Liu"
issued:
  date-parts:
    - [2026, 7, 8]
url: "https://arxiv.org/abs/2607.07073"

# Custom fields
paper_id: "2607.07073"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "multimodal"
  - "time-series"
  - "semantic-search"
architectures:
  []
datasets:
  []
concept_slugs:
  - "shapetalk-system"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-11T07:05:13Z"
created_at: "2026-07-11T07:05:13Z"
---

# ShapeTalk: Combining Natural Language and Sketch for Time-Series Pattern Querying

**Authors**: G. S. Sun, Yueqiao Chen, Emily Guo, Yutong Yao, Dongyu Liu
**Date**: 2026-07-08
**Paper ID**: [openalex:2607.07073](https://arxiv.org/abs/2607.07073)

## Summary

ShapeTalk is a novel querying system that addresses the limitations of visual time-series search by enabling both natural language and sketch-based inputs. By treating these modalities as complementary—text for semantic composition and sketching for geometric refinement—the system facilitates iterative query formulation in domains like finance and healthcare. The architecture leverages an LLM-based parsing pipeline to translate natural language into interpretable, editable shape constraints, resulting in a more flexible search experience. Evaluations suggest that this dual-modality approach effectively lowers the barrier to entry while allowing for precise pattern specification.

## Key Contributions

- Proposes ShapeTalk, a unified system integrating natural language semantic parsing and geometric sketching for intuitive time-series pattern querying.
- Implements an LLM-based semantic parsing pipeline that converts free-form text into editable shape-feature constraints, increasing query accessibility.
- Demonstrates through user studies that the dual-modality approach significantly aids in iterative query formulation and handling complex or vague pattern specifications.

## Open Questions & Future Work

- [[joint-multimodal-query-interpretation]]
- [[temporal-scale-visibility-in-analytics]]

## Key Concepts

- [[shapetalk-system]]: A coordinated natural-language and sketch-based querying system that allows for iterative, composite time-series pattern search.

## Archivist Review

Approved the ShapeTalk system as a novel interaction paradigm for time-series querying and retained the two proposed open questions as they address critical, non-local bottlenecks in multimodal visual analytics and temporal scale handling. No datasets were approved as none were central to the contribution.

### Approved Concepts
- ShapeTalk System: It introduces a novel dual-modality interaction paradigm for time-series querying, moving beyond single-modal rigid inputs.

### Approved Open Questions
- Joint Multimodal Query Interpretation: This addresses the core bottleneck of visual analytics interfaces that rely on manual switching between input methods rather than fluid, intelligent integration.
- Visibility of Temporal Scale: Temporal scale is an intrinsic property of time-series analysis that, if mismanaged, leads to misleading or null results.

## Links

- [Abstract](https://arxiv.org/abs/2607.07073)
- [PDF](https://arxiv.org/pdf/2607.07073)

