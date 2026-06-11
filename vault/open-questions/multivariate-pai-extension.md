---
created_at: '2026-06-11T09:07:24Z'
source_papers:
- '[[openalex-2606.08935-pai-preserving-amplitude-information-in-representation-based]]'
title: Multivariate PAI Extension
---

**Background:** Current representation-based time-series anomaly detection methods often operate on univariate data, using encoders that may not inherently model multi-channel interactions.

**Question / Future Work:** Extend the proposed PAI scoring scheme, which currently uses point-wise and window-based raw-signal scores for univariate time series, to multivariate settings by designing new raw-signal components that can effectively incorporate or account for cross-channel dependencies.

**Why It Matters:** Most real-world anomaly detection applications involve multivariate data; therefore, a method limited to univariate series has significant practical constraints.

**Evidence:** The raw-signal scores magG and T2 are computed per series and do not model cross-channel dependencies, so multivariate extension requires additional design.