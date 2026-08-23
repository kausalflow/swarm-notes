---
created_at: '2026-08-23T05:19:46Z'
source_papers:
- '[[openalex-2608.20304-calibration-induced-degeneracy-in-llm-financial-forecasting]]'
title: Calibration-Induced Degeneracy in LLM Forecasting
---

**Background:** Machine learning pipelines that integrate generated semantic or textual features into quantitative forecasting models often suffer from calibration-induced degeneracy, where optimization boundary constraints zero out feature weights and render downstream data acquisition useless.

**Question / Future Work:** Investigate whether automated data-driven feature selection and calibration-viability checkpoints can be generalized across diverse multi-modal large language model architectures and complex trading horizons without suffering from boundary-induced degeneracy or look-ahead biases.

**Why It Matters:** Preventing wasted computational and financial resources during large-scale inference by ensuring that calibrated models retain a non-degenerate pathway for newly acquired features is a critical operational requirement for automated ML pipelines.

**Evidence:** Costly LLM features are useful only if calibration leaves them a path into the forecast. In a next-day risk experiment for two broad-market exchange-traded funds, full-history scoring preceded the 2022 calibration. All four LLM importance weights reached zero; the 856 later scores therefore could not affect the evaluation. We call this calibration-induced degeneracy.