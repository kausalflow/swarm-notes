---
created_at: '2026-06-28T08:16:17Z'
source_papers:
- '[[openalex-2606.27168-deep-learning-model-emulators-for-marine-biogeochemistry-for]]'
title: 3D Biogeochemical Emulator Scaling
---

**Background:** Deep learning emulators for marine biogeochemistry models have demonstrated potential in one-dimensional water column configurations, but their performance and scalability in three-dimensional regional ocean models remain unexplored.

**Question / Future Work:** There is a need to extend the current one-dimensional emulation framework for marine biogeochemistry to three-dimensional regional applications, which will require integrating additional architectural components like convolutional layers or graph neural networks to handle spatial dynamics and significantly higher training costs.

**Why It Matters:** Scaling to three-dimensional systems is critical for operational relevance, as biogeochemical dynamics are inherently spatial and horizontal transport is a major factor not captured in one-dimensional test-beds.

**Evidence:** We recognize that the additional complexity of the three-dimensional dynamics will likely require additional deep learning components, such as convolutional layers or graph neural networks (which are well-suited to the spatial aspect of the task). Such a model would also be considerably more expensive to train.