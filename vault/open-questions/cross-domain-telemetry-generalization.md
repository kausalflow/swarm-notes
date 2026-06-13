---
created_at: '2026-06-13T08:15:43Z'
source_papers:
- '[[openalex-2606.11553-apex-a-network-native-time-series-foundation-model-for-forec]]'
title: Generalizing across heterogeneous telemetry
---

**Background:** Wireless network telemetry often exhibits complex, cross-layer dependencies across protocol layers, such as those found in DHCP, RF, and roaming data.

**Question / Future Work:** There is a need to extend foundational time-series models to incorporate broader protocol-level telemetries (e.g., RF signals and roaming patterns) to provide a more holistic monitoring solution for wireless edge operations, as current approaches often focus on specific protocols. Expanding the input schema and pre-training objectives to accommodate these diverse, coupled signals remains a critical step for general-purpose network-native foundation models.

**Why It Matters:** The current research is siloed within a single network protocol. Proving that the model's architectural principles generalize across different protocol layers is essential for establishing it as a true general-purpose foundation model for network operations.