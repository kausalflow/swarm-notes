---
# CSL-compatible fields
title: "CRANE: Post-Hoc Counterfactual Retrieval for Multimodal Classifiers"
author:
  - literal: "Franco Rugolon"
  - literal: "Ioanna Miliou"
  - literal: "Panagiotis Papapetrou"
issued:
  date-parts:
    - [2026, 10, 22]
url: "https://arxiv.org/abs/2610.31594"

# Custom fields
paper_id: "2610.31594"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodalَة"
  - "explainability"
  - "counterfactuals"
  - "retrieval"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-25T09:29:49Z"
created_at: "2026-10-25T09:29:49Z"
---

# CRANE: Post-Hoc Counterfactual Retrieval for Multimodal Classifiers

**Authors**: Franco Rugolon, Ioanna Miliou, Panagiotis Papapetrou
**Date**: 2026-10-22
**Paper ID**: [openalex:2610.31594](https://arxiv.org/abs/2610.31594)

## Summary

The paper introduces CRANE, a post-hoc, model-agnostic framework for generating counterfactual explanations for multimodal classifiers through nearest-neighbour retrieval. By leveraging Multimodal Consensus Retrieval (MC-R)—which intersects per-modality neighbour sets to identify instances jointly close to the query across all modalities—CRANE ensures explanations remain plausible by construction and grounded in the joint training distribution. Experiments across four heterogeneous datasets and three fusion strategies show that MC-R achieves superior or competitive results compared to unimodal baselines.

## Key Contributions

- Introduces CRANE, the first post-hoc, model-agnostic framework for nearest-neighbour multimodal counterfactual generation.
- Proposes Multimodal Consensus Retrieval (MC-R), which intersects per-modality neighbour sets to identify instances jointly close to the query across every modality.
- Demonstrates across four heterogeneous datasets and three fusion strategies that MC-R achieves top-tier performance by grounding explanations in the joint training distribution.

## Archivist Review

Applied strict skill-specific and vault-wide filtering standards. Since the paper focuses on multimodal classifier explainability and counterfactual retrieval rather than time-series forecasting, temporal dynamics, or distribution shift mechanisms, all candidates were rejected to maintain the targeted scope of the vault.

### Rejected Candidates
- [concept] CRANE (`crane`) - paper_local: CRANE is a paper-specific framework name for multimodal counterfactual retrieval rather than a broadly recurring general forecasting or temporal modeling mechanism.
- [concept] Multimodal Consensus Retrieval (`multimodal-consensus-retrieval`) - not_reusable: This technique focuses on multimodal classifier explainability rather than core time-series forecasting, temporal modeling, or distribution dynamics relevant to the vault skill context.
- [open_question] Latent Space Clustering for Counterfactual Retrieval (`latent-space-clustering-for-retrieval-counterfactuals`) - not_reusable: The question addresses multimodal counterfactual explanations rather than core time-series forecasting, distribution shift, or temporal dynamics.

## Links

- [Abstract](https://arxiv.org/abs/2610.31594)
- [PDF](https://arxiv.org/pdf/2610.31594)

