---
title: "Delta-Based Target Reformulation"
slug: "delta-based-target-reformulation"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2606.17692-delta-based-target-reformulation-for-short-term-electricity]]"
processed_at: "2026-06-19T09:24:33Z"
created_at: "2026-06-19T09:24:33Z"
---

# Delta-Based Target Reformulation

> *Auto-generated stub. Edit this file to add more details.*

A training strategy that reformulates forecasting as the prediction of consecutive time-step deltas to improve learning stability in non-stationary time series.


## Why It Matters

Addresses target non-stationarity in deep learning-based time-series forecasting by borrowing from classical differencing methods to stabilize the learning objective.

## Evidence

> Instead of directly predicting absolute load values, the proposed formulation trains models to predict the change in load between consecutive time steps, with final forecasts reconstructed using the last observed load.

## Related Papers

- [[openalex-2606.17692-delta-based-target-reformulation-for-short-term-electricity]]
