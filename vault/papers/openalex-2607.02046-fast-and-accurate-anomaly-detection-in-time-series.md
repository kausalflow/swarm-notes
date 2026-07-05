---
# CSL-compatible fields
title: "Fast and Accurate Anomaly Detection in Time Series"
author:
  - literal: "Emanuele Mele"
  - literal: "Massimo Cafaro"
  - literal: "Angelo Coluccia"
  - literal: "Italo Epicoco"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.02046"

# Custom fields
paper_id: "2607.02046"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "haar-wavelet-t-test-anomaly-detection"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:52:02Z"
created_at: "2026-07-05T07:52:02Z"
---

# Fast and Accurate Anomaly Detection in Time Series

**Authors**: Emanuele Mele, Massimo Cafaro, Angelo Coluccia, Italo Epicoco
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.02046](https://arxiv.org/abs/2607.02046)

## Summary

This paper presents an unsupervised anomaly detection algorithm for time series that combines Haar discrete wavelet transforms with a specialized t-test. By utilizing multiresolution decomposition to isolate anomalous signals, the method addresses the challenges of class imbalance and the lack of labeled training data. Extensive empirical evaluation across 343 diverse datasets confirms that the proposed approach achieves state-of-the-art performance compared to existing unsupervised and self-supervised benchmarks.

## Key Contributions

- Introduces a novel unsupervised anomaly detection algorithm that leverages Haar discrete wavelet transforms and a custom t-test to identify anomalous events.
- Provides the theoretical foundation for the proposed t-test mechanism within the wavelet domain.
- Demonstrates superior performance against state-of-the-art unsupervised and self-supervised anomaly detection methods across a comprehensive evaluation set of 343 datasets.

## Open Questions & Future Work

- [[multivariate-time-series-anomaly-detection-extension]]

## Key Concepts

- [[haar-wavelet-t-test-anomaly-detection]]: An unsupervised anomaly detection method for time series that utilizes Haar discrete wavelet transforms and a statistically grounded t-test.

## Archivist Review

The proposed Haar-Wavelet approach is a distinct, statistically-grounded mechanism for unsupervised anomaly detection that fits well within the vault's focus on signal processing and time-series analysis. The open question was refined to better align with existing naming conventions in the vault regarding multivariate extensions. No datasets were approved as the evaluation set described was an aggregate of 343 datasets rather than a novel, critical named benchmark.

### Approved Concepts
- Haar-Wavelet t-test Anomaly Detection: The algorithm combines multiresolution signal analysis via Haar wavelets with statistical hypothesis testing for anomaly identification, providing a novel framework for unsupervised time series analysis.

### Approved Open Questions
- Multivariate time series anomaly detection extension: Multivariate anomaly detection is critical for real-world applications involving complex systems, yet many high-performance algorithms remain limited to univariate data. Developing such an extension would significantly enhance the utility of the proposed methodology in industrial settings where sensors are highly correlated.

### Rejected Candidates
- [open_question] Extending to multivariate time series (`multivariate-time-series-extension`) - other: Renamed to be more descriptive and distinct within the existing vault taxonomy.

## Links

- [Abstract](https://arxiv.org/abs/2607.02046)
- [PDF](https://arxiv.org/pdf/2607.02046)

