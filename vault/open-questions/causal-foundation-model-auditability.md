---
created_at: '2026-06-14T08:39:18Z'
source_papers:
- '[[openalex-2606.13024-causalmoe-a-billion-scale-multimodal-foundation-model-for-gr]]'
title: Auditability and Benchmark Leakage
---

**Background:** Foundation models in time-series analysis are increasingly integrated with Large Language Models (LLMs) and Vision-Language Models (VLMs) to provide semantic and visual priors. However, the pre-training processes for these large models are often opaque and proprietary, complicating the auditing of data sources.

**Question / Future Work:** There is an unresolved need to ensure the robustness and auditability of multimodal causal foundation models against potential training data contamination or 'benchmark leakage'. It is difficult to determine whether superior performance in scientific causal discovery is due to genuine inferential capability or the model having 'memorized' ground-truth causal structures during its massive-scale multimodal pre-training.

**Why It Matters:** Benchmark leakage undermines the scientific validity of foundation models in causal discovery tasks, necessitating reliable probing and counterfactual testing methodologies.

**Evidence:** Third, since the pre-training of LLMs and VLMs are not fully auditable, potential benchmark leakage cannot be completely ruled out; therefore, additional probing or counterfactual tests are recommended before applying into high-stakes GCD tasks.