---
# CSL-compatible fields
title: "Topological optimization with birth and death cochains"
author:
  - literal: "Thomas Weighill"
  - literal: "Ling Zhou"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25575"

# Custom fields
paper_id: "2603.25575"
paper_source: "openalex"
domain: "graph-learning"
tags:
  - "topology"
  - "optimization"
  - "loss-function"
  - "data-analysis"
architectures:
  []
datasets:
  []
concept_slugs:
  - "birth-and-death-cochains"
  - "birth-and-death-content-loss"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:08:02Z"
created_at: "2026-03-29T06:08:02Z"
---

# Topological optimization with birth and death cochains

**Authors**: Thomas Weighill, Ling Zhou
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25575](https://arxiv.org/abs/2603.25575)

## Summary

This paper introduces birth and death cochains, which serve as unique generalizations of birth and death simplices within persistent cohomology. The authors leverage these cochains to define birth and death content, functioning as generalized persistence times. This content is then formalized as a novel loss function for various topological optimization problems involving point clouds, time series, and scalar fields. The utility of this approach is demonstrated through a final application to the topological optimization of arctic ice image data.

## Key Contributions

- Introduced birth and death cochains as unique generalizations of birth and death simplices in persistent cohomology.
- Defined birth and death content using these cochains, generalizing birth and death times.
- Demonstrated the efficacy of using birth and death content as loss functions for topological optimization across point clouds, time series, and scalar fields.
- Applied topological optimization, guided by the new loss, to a dataset of arctic ice images.

## Limitations

The paper applies the technique to point clouds, time series, scalar fields, and ice images, but does not detail comparative performance against established methods on specific benchmarks for each domain.

## Open Questions & Future Work

- [[symmetric-relative-cohomology-for-birth-cochains]]
- [[alternative-birth-death-cochain-characterizations]]

## Key Concepts

- [[birth-and-death-cochains]]: Generalized versions of birth and death simplices used in persistent cohomology that are always unique for a given class.
- [[birth-and-death-content-loss]]: A loss function derived from birth and death cochains, generalizing birth and death times for use in topological optimization.

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 2 concept(s), 2 open question(s), and 0 dataset(s), with 1 rejected candidate note(s).

### Approved Concepts
- Birth and Death Cochains: These cochains are introduced as unique, generalized structures for persistent cohomology classes, making them fundamental to the paper's methodology.
- Birth and Death Content Loss Function: The paper proposes using this content derived from cochains as a novel loss function for optimization tasks, which is the primary applied contribution.

### Approved Open Questions
- Symmetric relative cohomology for birth cochains: Closing this theoretical asymmetry would provide a more complete and unified algebraic framework for both birth and death events in persistent cohomology.
- Alternative cochain characterizations: Exploring alternative characterizations can deepen the theoretical understanding of birth and death cochains beyond their current variational definition, potentially revealing intrinsic algebraic properties.

### Rejected Candidates
- [concept] Topological Optimization with Birth and Death Cochains (`topological-optimization-with-birth-and-death-cochains`) - generic: The title is too descriptive of the entire paper's topic rather than a specific, reusable technical contribution; the specific concept 'Birth and Death Cochains' has been captured.

## Links

- [Abstract](https://arxiv.org/abs/2603.25575)
- [PDF](https://arxiv.org/pdf/2603.25575)

