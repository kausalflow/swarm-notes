---
created_at: '2026-03-27T14:08:51Z'
source_papers:
- '[[openalex-2602.21498-learning-recursive-multi-scale-representations-for-irregular]]'
title: Integrating ReIMTS with Diffusion Models
---

**Background:** The ReIMTS framework uses latent representations derived from IMTS backbone encoders, which can include temporal, variable, or observation representations. Diffusion-based IMTS models often predict noisy latent representations as part of their backbone process.

**Question / Future Work:** Develop strategies to adapt the ReIMTS framework to function with diffusion-based IMTS backbones, potentially by predicting clean observations during the denoising process or by integrating the recursive fusion mechanism directly within the diffusion model's denoising backbone.