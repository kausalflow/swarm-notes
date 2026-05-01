---
created_at: '2026-05-01T07:22:49Z'
source_papers:
- '[[openalex-2604.25650-using-large-language-models-for-black-box-testing-of-fmu-bas]]'
title: Adaptive Calibration of Simulation Oracles
---

**Background:** In black-box testing of complex simulation models, test oracles are frequently defined using qualitative behavioural assertions, such as settling time or monotonic behaviour, rather than precise numerical ground truth.

**Question / Future Work:** The validity of qualitative test oracles depends on how well high-level behavioural operators map to the underlying dynamics of the system. There is currently a need for methods to automatically adapt or calibrate these oracle parameters—such as thresholds and time windows—to avoid false positives or negatives, as fixed constraints may be too rigid for varying system behaviours.

**Why It Matters:** This is a fundamental challenge in automated test generation for dynamic systems, where relying solely on fixed, expert-defined thresholds limits scalability and reduces the reliability of test verdicts.