---
created_at: '2026-03-26T06:26:52Z'
source_papers:
- '[[2603.24474-leveraging-synthetic-and-genetic-data-to-improve-epidemic-fo]]'
title: Joint Geographic Forecasting
---

**Background:** Forecasting multiple geographic locations simultaneously allows models to learn complex inter-state or inter-regional relationships that may improve accuracy, similar to successes seen in hierarchical modeling for influenza.

**Question / Future Work:** A future direction involves adapting the input/output framework to forecast geographic locations jointly, rather than individually. This requires developing training examples where recent observations from all US states are the input, and the next $H$ time steps for each state are the output, leveraging multi-location capabilities in synthetic data generators like MutAntiGen.