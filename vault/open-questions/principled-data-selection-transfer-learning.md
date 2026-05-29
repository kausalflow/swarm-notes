---
created_at: '2026-05-29T08:37:41Z'
source_papers:
- '[[openalex-2605.27269-transfer-learning-using-66-diseases-for-disease-forecasting]]'
title: Principled Data Selection for Transfer Learning
---

**Background:** In infectious disease forecasting, transfer learning often involves incorporating auxiliary data from different diseases or reporting streams to enhance predictive performance. This practice carries a risk of negative transfer, where auxiliary data fundamentally different from the target stream can degrade model accuracy.

**Question / Future Work:** There is a need for principled frameworks to select and screen auxiliary data sources in cross-domain transfer learning. Future research should focus on formalizing criteria—such as signal-to-noise ratios, entropy measures, or domain-similarity metrics—that predict whether auxiliary data will improve forecasting performance or introduce detrimental noise.

**Why It Matters:** The absence of systematic data selection frameworks prevents reliable wide-scale adoption of cross-pathogen transfer learning, as current methods cannot predict if auxiliary data will be beneficial or detrimental to model robustness.