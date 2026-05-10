---
created_at: '2026-05-10T07:20:46Z'
source_papers:
- '[[openalex-2605.06032-does-synthetic-data-help-empirical-evidence-from-deep-learni]]'
title: Architecture-Dependent Augmentation Mechanisms
---

**Background:** Deep learning forecasters for time series show strong architecture-dependent responses to synthetic data augmentation, with channel-mixing models typically benefiting while channel-independent models often suffer performance degradation.

**Question / Future Work:** The exact mechanisms and structural requirements that enable a time series forecasting architecture to effectively leverage synthetic data for distribution matching or regularization remain theoretically unresolved. Further research is required to determine why channel-mixing models successfully integrate synthetic patterns, while channel-independent models consistently incur performance penalties from the same synthetic sources.

**Why It Matters:** Understanding this dependency is critical for developing robust synthetic augmentation strategies for time series, as current practices lead to degradation in a majority of evaluated architecture/dataset combinations.

**Evidence:** The effect is sharply architecture-conditional: channel-mixing models (TimesNet, iTransformer) benefit in the majority of trials, while channel-independent models (DLinear, PatchTST) are consistently degraded.