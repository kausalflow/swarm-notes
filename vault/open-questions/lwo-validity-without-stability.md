---
created_at: '2026-05-31T08:09:07Z'
source_papers:
- '[[openalex-2605.30292-leave-a-window-out-modifying-the-jackknife-for-predictive-in]]'
title: LWO validity without stability
---

**Background:** Leave-one-out (jackknife) predictive inference methods typically rely on the assumption of data exchangeability to provide valid coverage guarantees. In time series contexts where data is dependent, these methods often fail to achieve valid coverage.

**Question / Future Work:** Developing modifications to the LWO method that achieve valid coverage in the presence of temporal dependence without requiring algorithmic stability assumptions remains an open problem. Current variants of the jackknife, such as jackknife+ or CV+, bypass stability assumptions in exchangeable settings, but it is unclear if an LWO analog exists for non-exchangeable time series data.

**Why It Matters:** Relaxing stability requirements would significantly broaden the applicability of LWO-type methods, as many modern black-box predictors do not satisfy rigorous stability criteria.