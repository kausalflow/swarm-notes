---
created_at: '2026-07-10T08:15:18Z'
source_papers:
- '[[openalex-2510.20769-csu-pcast-a-dual-branch-transformer-framework-for-medium-ran]]'
title: Mitigating precipitation smoothing in DL models
---

**Background:** Deep learning-based ensemble precipitation forecasting models often exhibit smoother output fields compared to satellite observations and traditional numerical weather prediction (NWP) systems, which frequently correlates with an underestimation of high-end precipitation intensities.

**Question / Future Work:** There is an unresolved challenge in identifying training objectives or architectural modifications that can prevent the excessive smoothing of precipitation fields by deep learning models. Further research is required to determine how to preserve spatial variability and high-end intensity without sacrificing the stability and reliability gains achieved by current Transformer-based autoregressive frameworks.

**Why It Matters:** Addressing this smoothing issue is critical for improving the utility of deep learning weather models for high-impact hydrometeorological event forecasting, where precise spatial structure and peak intensity are often more important than aggregate statistical performance.

**Evidence:** This behavior may partly reflect the regression-based nature of the model, since optimization toward average error can favor smoother fields and suppress small-scale, high-amplitude precipitation features.