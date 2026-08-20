---
created_at: '2026-08-20T05:21:03Z'
source_papers:
- '[[openalex-2608.16092-feedforward-active-speech-suppression-based-on-time-series-p]]'
title: Real-Time Neural Network Inference Latency
---

**Background:** Active noise control systems utilizing neural networks for time-series prediction face deployment challenges due to the computational overhead of model inference exceeding the real-time constraints imposed by audio sampling intervals.

**Question / Future Work:** Investigate and optimize the computational efficiency and neural network architecture to reduce inference latency below the strict requirements of real-time audio sampling intervals.

**Why It Matters:** Real-time hardware deployment is crucial for practical active noise control systems; bridging this latency gap is a key engineering and algorithmic bottleneck.

**Evidence:** Its average inference time on a CPU (Intel Core Ultra 7 155H) was 1.19 \times 10^{-4}~\mathrm{s}. Since this is longer than the sampling interval of 6.25 \times 10^{-5}~\mathrm{s}, further implementation adjustments will be necessary for real-time processing.