---
created_at: '2026-03-26T06:26:38Z'
source_papers:
- '[[2603.24562-scaling-recurrence-aware-foundation-models-for-clinical-reco]]'
title: Cross-System Generalization Limits
---

**Background:** The generalization capability of foundation models trained on one health system's data to an external cohort is often limited by differences in coding systems, vocabulary coverage, and population demographics.

**Question / Future Work:** Further investigation is required to understand the precise performance trade-offs and generalization boundaries when applying models trained on one large de-identified health system cohort to others that feature different clinical coding practices (e.g., lack of hierarchical code structure), varied population mixes, and different follow-up patterns. This also includes understanding how the lack of hierarchical structure in tokenization impacts the model's ability to capture high-level clinical signals during transfer.