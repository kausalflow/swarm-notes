---
created_at: '2026-06-13T08:16:57Z'
source_papers:
- '[[openalex-2606.12364-on-subquadratic-architectures-from-applications-to-principle]]'
title: Scaling Subquadratic Architectures
---

**Background:** Subquadratic architectures, including xLSTM, Mamba-2, and Gated DeltaNet, demonstrate varying capabilities for long-range sequence modeling, particularly regarding accumulation and state tracking. While these architectures have been evaluated individually, head-to-head comparisons across diverse complex data domains remain limited.

**Question / Future Work:** There is a need to systematically evaluate how different subquadratic architectural design choices, specifically regarding memory dynamics and state-update mechanisms, scale and perform across a wider range of model sizes and broader data domains. Extending these evaluations is necessary to clarify the limitations and generalizability of the performance advantages associated with current subquadratic sequence model designs.

**Why It Matters:** Understanding the scaling behavior and robustness of these architectures across different environments is critical for their adoption as practical, general-purpose replacements for Transformers in foundation models.

**Evidence:** Extending the comparison to larger model scales, additional teachers, and further data domains is a natural next step.