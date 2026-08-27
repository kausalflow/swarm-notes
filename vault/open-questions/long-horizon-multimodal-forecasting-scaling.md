---
created_at: '2026-08-27T15:58:47Z'
source_papers:
- '[[openalex-2608.23373-modalities-should-talk-to-each-other-dual-stream-multimodal]]'
title: Extending Multimodal Forecast Horizons
---

**Background:** Long-horizon epidemic forecasting requires fusing structured epidemiological time series with auxiliary unstructured text such as news headlines and weekly surveillance reports.

**Question / Future Work:** Future work needs to extend cross-modal fusion architectures beyond a 12-week horizon without letting cumulative forecasting error grow unchecked, which likely requires designing richer decoding mechanisms rather than relying on a single pooled lookback representation.

**Why It Matters:** Extending forecast horizons is crucial for long-term public health planning and tests the scalability of cross-modal conditioning mechanisms over extended durations.

**Evidence:** A second direction is extending the forecast horizon well beyond the 12 weeks demonstrated here without letting error grow with it; this will likely require a richer decoding mechanism than the single pooled representation used in this study, since our own attempts to push past H=12 with the current decoder did not hold up