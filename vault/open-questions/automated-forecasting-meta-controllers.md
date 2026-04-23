---
created_at: '2026-04-23T06:55:46Z'
source_papers:
- '[[openalex-2604.18576-agentic-forecasting-using-sequential-bayesian-updating-of-li]]'
title: Automated forecasting meta-controllers
---

**Background:** Forecasting complex outcomes currently relies on either parallel search or sequential accumulation of raw text, both of which struggle with efficient and coherent evidence integration in agentic frameworks.

**Question / Future Work:** It remains unresolved how to optimally learn and update meta-controllers that govern agentic tool usage policies, specifically determining the sequence and set of available actions per question type without manual source-specific engineering. Tracking these policies via automated mechanisms like bandit algorithms would improve robustness across heterogeneous forecasting domains.

**Why It Matters:** Automating tool selection is critical for scaling agentic systems beyond manual, prompt-engineered pipelines.