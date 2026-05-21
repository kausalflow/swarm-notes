---
created_at: '2026-05-21T08:28:53Z'
source_papers:
- '[[openalex-2605.17804-gents-a-comprehensive-benchmark-library-for-generative-time]]'
title: Robust Generative Evaluation Metrics
---

**Background:** Generative time series models are frequently evaluated using neural network-based metrics that act as auxiliary supervisors to measure fidelity and utility, which are often sensitive to the choice of evaluator architecture.

**Question / Future Work:** There is a need to develop more robust and holistic evaluation metrics for generative time series models that are less dependent on the specific architecture or training parameters of auxiliary evaluator models to ensure reliable and reproducible benchmarking.

**Why It Matters:** The field lacks a standardized and robust method for evaluating generative quality, which directly impacts the community's ability to rank models fairly and meaningfully across diverse time series domains.

**Evidence:** Existing model-based metrics could have robustness issues, especially PS and DS, which are sensitive to the auxiliary evaluator models.