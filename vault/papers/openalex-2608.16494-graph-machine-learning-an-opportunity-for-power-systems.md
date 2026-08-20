---
# CSL-compatible fields
title: "Graph Machine Learning: An Opportunity for Power Systems"
author:
  - literal: "Martin Sadric"
  - literal: "Sebastian Pütz"
  - literal: "Christian Nauck"
  - literal: "Veit Hagenmeyer"
  - literal: "Frank Hellmann"
  - literal: "Dirk Witthaut"
  - literal: "Benjamin Schäfer"
issued:
  date-parts:
    - [2026, 8, 17]
url: "https://arxiv.org/abs/2608.16494"

# Custom fields
paper_id: "2608.16494"
paper_source: "openalex"
domain: "time-series"
tags:
  - "graph-neural-network"
  - "benchmark"
  - "dataset"
  - "evaluation"
  - "robustness"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-20T05:21:54Z"
created_at: "2026-08-20T05:21:54Z"
---

# Graph Machine Learning: An Opportunity for Power Systems

**Authors**: Martin Sadric, Sebastian Pütz, Christian Nauck, Veit Hagenmeyer, Frank Hellmann, Dirk Witthaut, Benjamin Schäfer
**Date**: 2026-08-17
**Paper ID**: [openalex:2608.16494](https://arxiv.org/abs/2608.16494)

## Summary

This paper surveys nearly 800 studies at the intersection of graph machine learning (GML) and power systems, examining applications across forecasting, state estimation, optimization, control, fault diagnosis, and cybersecurity. It highlights power systems as a uniquely challenging benchmark setting characterized by hard physical constraints, multi-scale dynamics, and safety-critical requirements. Furthermore, it identifies critical hurdles such as limited real-world deployment and scarce standardized datasets, culminating in a structured requirements catalog to guide future ML-ready power grid benchmark development.

## Key Contributions

- Surveys nearly 800 papers at the intersection of graph machine learning (GML) and power systems, covering forecasting, state estimation, optimization, control, fault diagnosis, and cybersecurity.
- Identifies power systems as a rich benchmark setting combining physical constraints, multi-scale dynamics, and safety-critical requirements.
- Derives a structured requirements catalog for ML-ready power grid benchmarks to guide future dataset development and improve reproducibility.

## Limitations

The field suffers from scarce standardized benchmarks, limited real-world deployment, and a lack of open datasets and models.

## Open Questions & Future Work

- [[foundation-models-vs-specialized-gml-power-systems-evaluation]]

## Archivist Review

The paper is an extensive literature survey summarizing nearly 800 papers on graph machine learning for power systems. While it provides a valuable structured requirements catalog for benchmarks, it does not propose a specific novel architectural or algorithmic concept suitable for a standalone vault note. The single candidate open question asks about foundation models vs specialized GML, but since the paper is a survey, this open question is broad rather than addressing an unresolved technical bottleneck from primary research. Therefore, all candidates are rejected to maintain strict vault quality.

### Approved Open Questions
- Foundation Models vs Specialized GML: Resolving whether a single grid foundation model can replace task-specific GML pipelines is critical for standardizing power system architectures and guiding future benchmark development.

### Rejected Candidates
- [open_question] Foundation Models vs Specialized GML (`foundation-models-vs-specialized-gml-power-systems-evaluation`) - low_impact: The paper is primarily a literature survey of existing work rather than a primary research paper proposing a novel technical mechanism or open experimental question.

## Links

- [Abstract](https://arxiv.org/abs/2608.16494)
- [PDF](https://arxiv.org/pdf/2608.16494)

