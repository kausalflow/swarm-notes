---
created_at: '2026-05-08T06:28:02Z'
source_papers:
- '[[openalex-2605.03719-a-public-dataset-of-ariel-simulated-observations-for-develop]]'
title: Deep learning uncertainty quantification limits
---

**Background:** Deep learning models for scientific time-series data, such as exoplanetary spectra, face significant challenges when test data distributions differ from training distributions, a phenomenon known as domain or distribution shift. Current uncertainty quantification methods often fail to reliably reflect this shift, producing overconfident estimates for out-of-distribution inputs.

**Question / Future Work:** It remains an open challenge to develop robust, well-calibrated uncertainty quantification methods for deep learning-based exoplanetary data reduction pipelines. Existing techniques often replicate the training set's uncertainty distribution rather than providing reliable epistemic uncertainty estimates that scale appropriately for novel, out-of-distribution observational scenarios, hindering the assessment of model reliability in survey missions.

**Why It Matters:** Reliable uncertainty quantification is essential for scientific mission pipelines to distinguish between confident predictions and scenarios where the model is operating outside its training domain, which is critical for survey missions like Ariel.