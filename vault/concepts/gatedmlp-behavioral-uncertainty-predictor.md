---
title: "Behavioral Uncertainty Predictor (GatedMLP)"
slug: "gatedmlp-behavioral-uncertainty-predictor"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2603.25670-uncertainty-guided-label-rebalancing-for-cps-safety-monitori]]"
processed_at: "2026-03-29T06:09:13Z"
created_at: "2026-03-29T06:09:13Z"
---

# Behavioral Uncertainty Predictor (GatedMLP)

> *Auto-generated stub. Edit this file to add more details.*

A GatedMLP model trained to summarize time-series telemetry into distributional kinematic features and output a single behavioral uncertainty score.


## Why It Matters

This custom predictor is essential for quantifying the uncertainty that drives the label rebalancing, making the overall method functional.

## Evidence

> U-Balance first trains a GatedMLP-based uncertainty predictor that summarizes each telemetry window into distributional kinematic features and outputs an uncertainty score.

## Related Papers

- [[openalex-2603.25670-uncertainty-guided-label-rebalancing-for-cps-safety-monitori]]
