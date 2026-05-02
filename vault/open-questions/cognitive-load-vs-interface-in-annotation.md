---
created_at: '2026-05-02T06:56:37Z'
source_papers:
- '[[openalex-2604.26637-atlas-an-annotation-tool-for-long-horizon-robotic-action-seg]]'
title: Annotation cognitive load bottleneck
---

**Background:** In human-annotated robotic action segmentation, the inclusion of multi-modal time-series data improves temporal boundary accuracy compared to vision-only approaches, but typically increases the duration of the annotation task.

**Question / Future Work:** It remains unclear whether the observed increase in annotation time when using multi-modal time-series data is fundamentally due to increased cognitive load during data interpretation or if it is an artifact of the specific interface design. Investigating the relationship between cognitive load and interface usability is necessary to optimize future annotation tools for both speed and accuracy.

**Why It Matters:** Identifying whether the slowdown is caused by cognitive load or interface limitations is critical for balancing annotation efficiency with the precision provided by multi-modal sensor data in robotics research.

**Evidence:** Interestingly, ATLAS with vision-only input is also 7.5 s faster than ATLAS with both vision and time-series data. We hypothesize that the additional sensor information increases the cognitive load during annotation... however, further experiments are required to validate this hypothesis.