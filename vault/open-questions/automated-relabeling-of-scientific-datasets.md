---
created_at: '2026-05-24T07:48:14Z'
source_papers:
- '[[openalex-2605.22233-a-robust-deep-learning-framework-for-prominence-detection-th]]'
title: Automated Relabeling of Scientific Datasets
---

**Background:** Solar prominence datasets used for training deep learning object detection models often suffer from labeling inconsistencies and temporal biases due to varying instrument degradation and visibility across the solar cycle.

**Question / Future Work:** Automated relabeling of solar prominence datasets is required to account for features that are visible in specialized processed imagery but ignored in standard observation pipelines. Developing robust criteria for updating ground truth definitions is essential to prevent systematic model bias and improve performance reliability over long-term solar cycles.

**Why It Matters:** The quality of ground truth labels limits the upper bound of model performance; without objective re-labeling, performance metrics remain confounded by the absence of labels for objects that are visibly present in optimized data.

**Evidence:** A potential solution to the issues identified here is to re-label the dataset using processed images, such as the WOW output, which enhances prominence visibility. We leave this task for future work.