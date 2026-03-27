---
created_at: '2026-03-27T14:08:19Z'
source_papers:
- '[[openalex-2603.08707-impermanent-a-live-benchmark-for-temporal-generalization-in]]'
title: Expand data scope
---

**Background:** The Impermanent benchmark is a framework for evaluating time series forecasting models using a live, continuously updated data stream based on GitHub software development activity.

**Question / Future Work:** The current iteration of Impermanent is built on univariate series derived from four types of GitHub events (issues opened, pull requests opened, push events, and new stargazers) for 400 repositories, with forecasts generated for one target count at a time. Future work should involve capturing co-movement between repositories and incorporating additional external covariates into the forecasting tasks.