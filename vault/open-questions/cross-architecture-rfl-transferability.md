---
created_at: '2026-10-01T11:15:05Z'
source_papers:
- '[[openalex-2609.37255-loss-guided-pretraining-data-selection-for-time-series-found]]'
title: Cross-Architecture Reference Loss Transferability
---

**Background:** Time-series foundation models are increasingly pretrained on large, heterogeneous collections of temporal windows, yet the generalizability of data selection methods across diverse downstream architectures and cross-modal pretraining paradigms remains underexplored.

**Question / Future Work:** Determine the theoretical and practical limits of cross-architecture and cross-modal reference loss transfer, specifically investigating how differing predictive objectives (e.g., quantile loss versus distributional log-likelihood) impact the transferability of difficulty scores for data pruning.

**Why It Matters:** Understanding cross-architecture score transferability is crucial for making pretraining data selection efficient and avoiding the need to train dedicated reference models for every new foundation model architecture.

**Evidence:** A plausible explanation is that TimesFM scores point and quantile errors, whereas Moirai uses a distributional negative log-likelihood, so they may not assign similar difficulty to high-uncertainty windows.