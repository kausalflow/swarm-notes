---
created_at: '2026-03-29T06:09:00Z'
source_papers:
- '[[openalex-2603.25251-does-explanation-correctness-matter-linking-computational-xa]]'
title: Finer Correctness Range Analysis
---

**Background:** Functional metrics are used to evaluate Explainable AI (XAI) methods computationally, with correctness being a widely used measure of how well an explanation reflects the model's reasoning.

**Question / Future Work:** The comparison between explanation correctness at 100% and 85% levels resulted in inconclusive findings regarding the impact on human understanding (forward simulation accuracy). Further investigation is required with finer granularity in this range (70–100%) to precisely characterize the functional form of the relationship between correctness and understanding, as this range is where practical differences between XAI methods often occur.

**Why It Matters:** Resolving the inconclusive finding between 85% and 100% correctness is crucial because this small performance gap is common between state-of-the-art XAI methods, and understanding if this difference is meaningful to users is vital for guiding practical XAI development.

**Evidence:** The unresolved comparison between 85% and 100% correctness highlights the need for finer granularity in the 70–100% range, which is where practical differences between XAI methods often fall.