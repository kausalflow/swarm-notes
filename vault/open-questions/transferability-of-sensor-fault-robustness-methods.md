---
created_at: '2026-05-14T07:37:45Z'
source_papers:
- '[[openalex-2605.10822-benchmarking-sensor-fault-robustness-in-forecasting]]'
title: Transferability of Sensor-Fault Robustness
---

**Background:** Cyber-physical systems rely on sensor streams that are susceptible to technical faults such as noise, bias, missing readings, and temporal misalignments. Standard forecasting evaluation often relies on nominal error metrics that may not reflect model reliability under these structured faults.

**Question / Future Work:** There is a need to understand whether models favored by clean-MSE metrics effectively generalize their robustness to diverse, unseen, or structured sensor-fault scenarios. Specifically, it remains an open question how to best perform cross-dataset transfer of robustness-improvement methods to novel fault scenarios and whether such methods transfer uniformly across different forecasting architectures and fault families.

**Why It Matters:** This question addresses the core challenge of ensuring the reliability of predictive models in critical industrial infrastructure where data quality is inherently non-stationary and fault-prone. Tracking this helps identify if current robustness methods are universal or merely overfit to specific fault types or model architectures.