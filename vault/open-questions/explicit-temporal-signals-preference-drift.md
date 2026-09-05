---
created_at: '2026-09-05T08:42:12Z'
source_papers:
- '[[openalex-2609.02468-deepaffinity-long-term-aspect-preference-prediction-in-ecomm]]'
title: Explicit Temporal Signals and Preference Drift
---

**Background:** E-commerce user preference models often rely on sequence-based interaction histories without explicitly incorporating rich temporal metadata such as exact timestamps, inter-event time gaps, or cyclical patterns like seasonality.

**Question / Future Work:** Investigate the integration of explicit temporal signals—such as timestamps, inter-event time gaps, and periodic seasonal patterns—into the model's stringification and input representation, alongside studying preference drift over longer forecasting horizons.

**Why It Matters:** Explicitly modeling time intervals and cyclical trends is critical for capturing long-term preference evolution and seasonal drift in user behavior, which simple event-order sequences fail to represent fully.

**Evidence:** Integrating these signals into the stringification, and studying preference drift over longer horizons, are natural next steps alongside scaling the SLM backbone.