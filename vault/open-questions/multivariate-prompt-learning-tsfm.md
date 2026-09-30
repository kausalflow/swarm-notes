---
created_at: '2026-09-30T10:49:01Z'
source_papers:
- '[[openalex-2609.34786-instance-adaptive-prompts-as-context-for-time-series-foundat]]'
title: Multivariate Prompt Learning for TSFMs
---

**Background:** Time-series foundation models can utilize instance-adaptive latent prompts as compact context surrogates to improve forecasting performance without the high computational cost of extending history lengths.

**Question / Future Work:** Investigate prompt learning and training methodologies directly within multivariate time-series settings, as existing approaches have been primarily restricted or evaluated under univariate settings.

**Why It Matters:** Extending prompt-based context surrogates to natively support multivariate time-series data is crucial for handling complex multi-variate dependencies and cross-channel correlations without relying solely on univariate-trained transfer.

**Evidence:** Our current study nevertheless has several limitations: the prompts are trained only under the univariate setting, leaving multivariate prompt training unexplored... Future work can investigate prompt learning directly in multivariate settings