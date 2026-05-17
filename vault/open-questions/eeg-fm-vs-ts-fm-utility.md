---
created_at: '2026-05-17T07:31:14Z'
source_papers:
- '[[openalex-2605.14698-neuroatlas-benchmarking-foundation-models-for-clinical-eeg-a]]'
title: Utility of EEG Pretraining
---

**Background:** Foundation models have been proposed to extract generalized representations from large-scale EEG data across various clinical domains. However, the extent to which these EEG-specific models provide performance gains over generic time-series foundation models is currently uncertain.

**Question / Future Work:** Research needs to clarify the source of performance improvements in EEG foundation models by systematically disentangling the contributions of EEG-specific architectural inductive biases, EEG-specific pretraining data, and generic large-scale temporal representation learning. Comparing models across a wider array of clinical tasks is essential to determine whether specialized neurophysiological pretraining is necessary.

**Why It Matters:** Crucial for guiding the development of the next generation of unified EEG foundation models and avoiding unnecessary data-intensive overhead.

**Evidence:** EEG-specific FMs do not consistently outperform time-series FMs, which have neither EEG-focused architectures nor been pretrained on EEG.