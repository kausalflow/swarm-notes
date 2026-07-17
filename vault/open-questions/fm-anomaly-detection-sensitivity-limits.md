---
created_at: '2026-07-17T07:09:20Z'
source_papers:
- '[[openalex-2607.12454-exploring-zero-shot-foundation-models-for-multivariate-time]]'
title: FM Anomaly Detection Sensitivity Limits
---

**Background:** Foundation models pre-trained on univariate time series forecasting are increasingly evaluated for anomaly detection, yet their strong predictive capability often allows them to capture and 'normalize' anomalous temporal dynamics. This behavior results in high prediction error primarily at the onset of anomalies rather than throughout their duration.

**Question / Future Work:** Establishing whether forecasting-based foundation models can be reliably adapted for anomaly detection requires identifying which internal model properties or training data characteristics enable distinguishing persistent anomalies from normal fluctuations. Research must address the systematic discrepancy between a model's temporal capture capabilities and its detection sensitivity to non-boundary-based anomalous regimes.

**Why It Matters:** This is a central limitation preventing the direct use of powerful forecasting FMs for critical industrial monitoring tasks.