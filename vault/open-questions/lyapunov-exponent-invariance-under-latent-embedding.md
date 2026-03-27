---
created_at: '2026-03-27T15:44:13Z'
source_papers:
- '[[openalex-2603.22655-generalizing-dynamics-modeling-more-easily-from-representati]]'
title: Lyapunov Exponent Invariance Preservation
---

**Background:** The framework utilizes an encoder-decoder structure, PDE-DER, to map original state observations into a latent space where dynamics are modeled. This transformation, involving PLMs and reconstruction/forecasting objectives, is mathematically shown to not preserve the maximal Lyapunov exponent between the original and latent spaces.

**Question / Future Work:** Investigate whether modifications to the PDE-DER architecture or pre-training objectives, such as enforcing stricter invertibility constraints or employing architectures proven to maintain Lyapunov exponents under transformation, can lead to a latent space representation where the maximal Lyapunov exponent is invariant between the original and embedded dynamics. This is important for ensuring that the stability and chaotic properties of the true system dynamics are accurately preserved and measurable in the learned latent space.

**Why It Matters:** Preserving the Lyapunov exponent's invariance during embedding is crucial for latent space methods aiming to faithfully represent system chaos/stability, as non-invariance complicates interpretability and transferability of chaotic properties.

**Evidence:** According to [10] if the integrated states x learnt from x0 in the original space are identical to x^ obtained by decoding from latent variable z, the Lyapunov exponents computed on x and z remain invariant under the transformation. The invariance holds when x_i = x̂_i, ∀ i ∈ [T]. While this constraint cannot hold under our framework... According to the above proof, the Lyapunov exponent invariance condition does not hold under our framework, indicating that the Lyapunov exponents calculated by the original states x and the latent representations z are not invariant under the transformation.