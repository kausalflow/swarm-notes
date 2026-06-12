---
created_at: '2026-06-12T08:55:26Z'
source_papers:
- '[[openalex-2606.10583-nova-symbolic-regression-discovery-of-interpretable-car-foll]]'
title: Overcoming lane-change discrimination ceiling
---

**Background:** Car-following and lane-change behaviors exhibit temporal dependencies that cannot be fully captured by static, single-snapshot kinematic feature sets. Existing symbolic regression models based on instantaneous kinematics have reached a structural discrimination ceiling in lane-change intent classification, particularly for distinguishing lane-changing from maintaining current lanes.

**Question / Future Work:** Investigate whether temporal-history features, such as lateral velocity, gap-evolution rates over 1–3 second windows, can extract additional predictive signal to overcome the identified discrimination ceiling in lane-change intent forecasting.

**Why It Matters:** This is a clear, bounded bottleneck identified by the authors that prevents further progress in lane-change modeling using their symbolic regression approach.

**Evidence:** The Stay-class recall plateau at 94-96% across all NOVA variants, with Left and Right recall in the 40-60% range, identifies the binding constraint... Resolving this discrimination ceiling likely requires temporal-history features (lateral velocity, gap-evolution rates over 1–3 second windows), which we leave to future work.