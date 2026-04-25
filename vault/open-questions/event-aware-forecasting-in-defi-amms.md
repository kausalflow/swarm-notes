---
created_at: '2026-04-25T06:15:50Z'
source_papers:
- '[[openalex-2604.20374-towards-event-aware-forecasting-in-defi-insights-from-on-cha]]'
title: Event-Aware Forecasting in AMMs
---

**Background:** Automated Market Makers (AMMs) operate as deterministic state machines where price fluctuations are driven by discrete on-chain events rather than continuous market responses. Existing temporal point process (TPP) models often struggle to capture the micro-structural event dynamics and temporal sparsity inherent in these blockchain-native systems.

**Question / Future Work:** There is an unresolved challenge in effectively modeling the joint distribution of transaction types and occurrence times within AMM protocols, specifically due to the discrete nature of block-height based time and the occurrence of concurrent transactions within single blocks. Future research is needed to develop models that handle heavy-tailed event gaps and multi-label event occurrences that undermine standard intensity-based TPP formulations.

**Why It Matters:** Current TPP models fail to provide high-precision timing forecasts for DeFi market participants, where even block-level latency is a critical factor in arbitrage and liquidation efficiency.