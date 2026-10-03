---
# CSL-compatible fields
title: "Grounding Time-Series Foundation Models in Digital Twin Topology for Predictive Maintenance"
author:
  - literal: "Sizhe Ma"
  - literal: "Katherine A. Flanigan"
  - literal: "Mario E. Berges"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.40071"

# Custom fields
paper_id: "2609.40071"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "foundation-model"
  - "multivariate"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  - "c-mapss"
concept_slugs:
  []
dataset_slugs:
  - "c-mapss"
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:08:26Z"
created_at: "2026-10-03T10:08:26Z"
---

# Grounding Time-Series Foundation Models in Digital Twin Topology for Predictive Maintenance

**Authors**: Sizhe Ma, Katherine A. Flanigan, Mario E. Berges
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.40071](https://arxiv.org/abs/2609.40071)

## Summary

This paper investigates grounding time-series foundation models (TSFMs) in digital twin topologies for predictive maintenance tasks such as remaining useful life (RUL) prediction. The authors benchmark five TSFMs with frozen backbones on the C-MAPSS dataset, revealing that multivariate models outperform univariate ones. They propose a topology-informed fusion approach that restricts cross-attention according to physical asset connectivity derived from digital twins. Ablation studies demonstrate that pretrained weights, target adaptation, and physical topology provide complementary performance boosts for downstream regression.

## Key Contributions

- Benchmarked five TSFMs with frozen backbones on C-MAPSS remaining useful life prediction, showing multivariate architectures outperform univariate ones.
- Proposed a topology-informed fusion approach integrating asset structure and digital twin topology to shape cross-attention.
- Conducted ablation studies across C-MAPSS operating conditions, demonstrating that pretrained weights, target adaptation, and digital twin topology are complementary sources of improvement.

## Open Questions & Future Work

- [[generalizing-tsfm-digital-twin-topology-across-domains]]

## Archivist Review

Applied strict selectivity, avoiding duplicate concepts and approving only the canonical C-MAPSS dataset. No standalone vault concepts met the rigorous high-impact threshold required for permanent notes.

### Approved Open Questions
- Generalizing TSFM Topological Grounding: Essential for validating the generalizability and domain-independence of grounding time-series foundation models in digital twin topological knowledge across heterogeneous industrial systems.

### Rejected Candidates
- [open_question] Generalizing TSFM Topological Grounding (`generalizing-tsfm-digital-twin-topology-across-domains`) - low_impact: The open question is well-supported and addresses generalizability across domains, but we are keeping the count strictly limited and selecting C-MAPSS as the primary dataset.

## Datasets

- [[c-mapss]]

## Links

- [Abstract](https://arxiv.org/abs/2609.40071)
- [PDF](https://arxiv.org/pdf/2609.40071)

