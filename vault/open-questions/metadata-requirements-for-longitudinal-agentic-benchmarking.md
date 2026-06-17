---
created_at: '2026-06-17T09:27:06Z'
source_papers:
- '[[openalex-2606.17005-bayesian-inference-and-decision-audits-for-public-archives-o]]'
title: Metadata requirements for longitudinal agentic benchmarking
---

**Background:** Frontier AI evaluations are often reported as terminal leaderboards, which act as a lossy endpoint of a selective and time-indexed process rather than a comprehensive historical record. This missingness and selection bias can make the underlying longitudinal progress and headroom of AI systems underdetermined.

**Question / Future Work:** Reconstructing full evaluation histories requires detailed metadata (e.g., benchmark versions, scaffold and tool identity, retry policies, environment settings, and human-intervention protocols) that is currently lacking in public agentic benchmarks. The current observability boundary separates what can be formally reconstructed from public traces versus what requires access to full execution logs, and the extent to which these histories can be standardized for longitudinal analysis remains an open research question.

**Why It Matters:** This is critical for moving from terminal snapshots to robust temporal evaluation of agentic systems, as current public archives lack the necessary metadata for reproducible longitudinal frontier analysis.

**Evidence:** The archive contract extends to GAIA and tau-bench as limited-applicability pilots, exposing missing scaffold and tool metadata as a boundary condition of the observability standard.