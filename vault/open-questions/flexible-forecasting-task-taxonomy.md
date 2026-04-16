---
created_at: '2026-04-16T06:28:04Z'
source_papers:
- '[[openalex-2604.11529-tempusbench-an-evaluation-framework-for-time-series-forecast]]'
title: Flexible Forecasting Task Taxonomy
---

**Background:** Current forecasting evaluation frameworks often lack a nuanced taxonomy, focusing primarily on basic characteristics like forecast horizon and domain while ignoring key statistical properties. Furthermore, standardized protocols for hyperparameter tuning are frequently absent, complicating fair comparisons between foundation models and traditional domain-specific methods.

**Question / Future Work:** Future work aims to create a more comprehensive and flexible benchmark taxonomy that integrates statistical properties—such as (non-)stationarity, seasonality, sparsity, and variable types—alongside a standardized hyperparameter tuning protocol. The goal is to move beyond generic task categories to allow for granular performance diagnostics across different data-generating processes.

**Why It Matters:** A standardized, property-aware taxonomy is essential for understanding the specific strengths and weaknesses of different model architectures, moving the field beyond simple leaderboard rankings.

**Evidence:** We plan to develop a more flexible benchmark taxonomy in which to define tasks in the coming months, which we will release with the full version of this paper.