---
created_at: '2026-10-03T10:07:18Z'
source_papers:
- '[[openalex-2609.40265-opentslm-teemoe-a-unified-time-series-language-model-for-for]]'
title: Preventing Capability Dilution in TSLMs
---

**Background:** General-purpose temporal models handle multiple time-series tasks like numerical forecasting, context-conditioned prediction, and temporal reasoning within a single architecture, but current approaches often experience capability dilution or specialist performance degradation when combining these heterogeneous tasks.

**Question / Future Work:** Investigate how general-purpose time-series language models can acquire broad multi-task capabilities without diluting the performance of strong task-specific models, particularly comparing modular mixture-of-experts composition against full joint training across diverse domains.

**Why It Matters:** Understanding the trade-offs between modular mixture-of-experts and joint multi-task training is foundational for scaling time-series foundation models to handle complex downstream workflows involving both numerical prediction and textual reasoning.

**Evidence:** This raises a central question: can a general-purpose model acquire broad capabilities without diluting specialist performance?