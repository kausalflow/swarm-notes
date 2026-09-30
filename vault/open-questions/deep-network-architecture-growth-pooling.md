---
created_at: '2026-09-30T10:50:01Z'
source_papers:
- '[[openalex-2609.33880-neuron-level-architecture-growth-a-controlled-evaluation-for]]'
title: Growth Methods for Deep Networks
---

**Background:** Convolutional EEG decoders are typically trained at a fixed width tuned by authors on specific datasets, which creates domain sensitivity issues and fails to account for inter-subject or inter-dataset variability.

**Question / Future Work:** Investigate and develop dynamic neural architecture growth methods capable of handling intervening pooling operations and deeper architectural blocks in complex convolutional decoders like Deep4Net without requiring architectural surrogates.

**Why It Matters:** Extending growth techniques to deeper networks with pooling layers is critical for understanding whether architectural growth can benefit deep architectures as effectively as shallow ones across diverse time-series decoding tasks.

**Evidence:** Deep4Net cannot be grown faithfully, because our growth implementation did not support the intervening pooling operations in the selected deeper blocks, changing the spatial dimension that prevents inclusion of growable layers.