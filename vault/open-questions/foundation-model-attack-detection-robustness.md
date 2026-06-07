---
created_at: '2026-06-07T08:18:58Z'
source_papers:
- '[[openalex-2606.06347-attack-detection-using-time-series-foundation-models]]'
title: Robustness of Foundation-Model-Based Detectors
---

**Background:** Cyber-physical systems often employ model-based detectors to identify anomalies, but these detectors can be vulnerable to sophisticated attacks specifically designed to exploit known system dynamics. Data-driven approaches, particularly those utilizing time-series foundation models, are being explored as alternative or secondary defense layers that do not rely on explicit knowledge of the plant's parameters.

**Question / Future Work:** Future work is needed to characterize the performance of foundation-model-based detectors against adaptive adversaries who have black-box query access to the underlying model, allowing them to potentially co-optimize their attack policy to evade both traditional and data-driven defenses. Understanding these theoretical robustness limits is essential for ensuring that foundation-model-based security layers do not provide a false sense of security.

**Why It Matters:** This is technically crucial because relying solely on empirical success against standard attacks may lead to a false sense of security; understanding the theoretical limits of foundation-model-based detection against adaptive threats is essential for developing resilient cyber-physical security architectures.