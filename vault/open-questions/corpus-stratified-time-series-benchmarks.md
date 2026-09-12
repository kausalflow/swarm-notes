---
created_at: '2026-09-12T08:55:38Z'
source_papers:
- '[[openalex-2609.10357-a-later-test-set-is-not-a-new-domain-pretraining-familiarity]]'
title: Corpus-Stratified Time-Series Benchmarks
---

**Background:** Time-series foundation models are evaluated almost exclusively on public archives that predate them, making it difficult to separate generalisation from memorisation or domain familiarity.

**Question / Future Work:** Future benchmarking for time-series foundation models requires constructing and utilizing evaluation frameworks where test domains are explicitly stratified by membership in each model's disclosed pretraining corpus, overcoming the limitation of current undisclosed or summary-level corpus data.

**Why It Matters:** Crucial for isolating true generalization capabilities from pretraining corpus familiarity and dataset leakage in zero-shot time-series forecasting.

**Evidence:** The decisive experiment is a benchmark whose domains are stratified by membership in each model’s disclosed corpus, which requires disclosure the field does not currently provide.