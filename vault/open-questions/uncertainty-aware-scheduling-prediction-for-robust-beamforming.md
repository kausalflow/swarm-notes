---
created_at: '2026-07-12T07:28:26Z'
source_papers:
- '[[openalex-2607.08454-spatio-temporal-scheduling-prediction-under-backhaul-delay-f]]'
title: Uncertainty-aware predictive beamforming
---

**Background:** In delay-constrained networks, predictive models often exhibit a sharp degradation in accuracy as the prediction horizon increases due to inherent stochasticity and uncertainty.

**Question / Future Work:** There is a significant and rapid decline in scheduling prediction accuracy as the backhaul latency increases, particularly when moving from a one-interval delay to longer horizons. Future work should investigate uncertainty-aware prediction models that can produce confidence intervals or reliability scores, allowing the downstream beamforming algorithms to adaptively weight or gate the incoming predictions based on their trustworthiness.

**Why It Matters:** Uncertainty-aware predictions directly enhance system robustness and fault tolerance in edge-based wireless networks, as they provide a mechanism to safely handle unreliable information or backhaul anomalies.