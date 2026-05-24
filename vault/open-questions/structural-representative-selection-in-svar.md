---
created_at: '2026-05-24T07:47:17Z'
source_papers:
- '[[openalex-2605.21846-causal-discovery-in-structural-var-models-under-equal-noise]]'
title: Selecting Representatives in SVARs
---

**Background:** Structural VAR models under the equal noise variance assumption, which allow for contemporaneous effects and cycles, generally do not provide point identification of the underlying structural causal graph from observational time-series data. The identification is limited to an observational equivalence class characterized by orthogonal transformations and a global scale.

**Question / Future Work:** Developing methods to robustly select the most physically or biologically meaningful structural representative from the identified observational equivalence class remains an open challenge. While sparsity-based approaches have been proposed, the problem of effectively incorporating domain-specific knowledge to further narrow the equivalence class beyond sparsity is unresolved.

**Why It Matters:** This is a central limitation of the proposed framework, as it highlights that the identified equivalence class may still contain many valid models, and the current selection criterion (sparsity) might be insufficient or suboptimal for real-world applications where ground truth is complex.