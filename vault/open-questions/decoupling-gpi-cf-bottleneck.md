---
created_at: '2026-06-04T08:42:53Z'
source_papers:
- '[[openalex-2606.01999-why-do-time-series-models-need-long-context-windows]]'
title: Decoupling GPI and CF
---

**Background:** Global time series forecasting models are often treated as monolithic systems that perform latent generative process inference and future value prediction simultaneously, typically requiring long context windows for both.

**Question / Future Work:** Developing methods to explicitly decouple Generative Process Identification (GPI) from Conditional Forecasting (CF) to enable more efficient context utilization and dynamic adaptation to non-stationary data-generating processes.

**Why It Matters:** This is a core architectural bottleneck for scaling time series foundation models, as decoupling could alleviate the need for uniformly long contexts and reduce computational overhead.

**Evidence:** investigating methodologies to decouple GPI in the context of highly time-varying data-generating processes is another interesting direction for future studies.