---
created_at: '2026-06-14T08:37:31Z'
source_papers:
- '[[openalex-2606.13300-quantizing-time-series-models-as-dynamical-systems-trajector]]'
title: Noise Model Sensitivity in Quantization
---

**Background:** Dynamical-systems stability theory is used to model the error propagation of neural network rollouts under parameter perturbation.

**Question / Future Work:** It remains unclear how the choice of noise model (e.g., Gaussian vs. structured quantization noise) in trajectory-based sensitivity metrics affects the performance and stability of quantization across different model architectures and at different scales. Investigating whether this ranking discrepancy persists in models with more complex dynamics or different architectural constraints is essential to understanding the limits of perturbation-based sensitivity estimation.

**Why It Matters:** The noise model choice impacts the layer-wise precision assignment, which directly dictates the model's accuracy-compression trade-off. Clarifying the noise model's role is critical for robust, generalizable quantization frameworks.

**Evidence:** Probe choice changes fine-grained sensitivity rankings, but its effect largely disappears at block and deployment scales. As partitions coarsen from tensors to blocks, γgauss and γquant become increasingly aligned, reaching near-perfect agreement on Pangu-Weather’s 28 blocks.