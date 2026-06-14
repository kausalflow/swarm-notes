---
created_at: '2026-06-14T08:39:18Z'
source_papers:
- '[[openalex-2606.13024-causalmoe-a-billion-scale-multimodal-foundation-model-for-gr]]'
title: Predictive vs. Interventional Causality
---

**Background:** Neural Granger Causal Discovery (GCD) methods primarily focus on identifying predictive dependencies rather than uncovering true interventional causality. This constraint arises from the standard assumptions inherent in the GCD framework, such as the absence of hidden confounders and the prohibition of instantaneous effects.

**Question / Future Work:** It remains an open challenge to extend Granger causal discovery methods to reliably identify interventional causality in complex systems, moving beyond purely predictive statistical dependencies. The inherent limitations of the GCD framework prevent the discovery of causal mechanisms in systems with hidden confounders or feedback loops, which are common in real-world time series.

**Why It Matters:** Moving from predictive dependency to interventional causality is critical for real-world decision-making and scientific discovery, as predictive methods often fail to guide effective interventions when confounders are present.

**Evidence:** First, CausalMoE follows the GCD framework and therefore identifies predictive dependencies rather than interventional causality, relying on standard assumptions such as no hidden confounders and no instantaneous effects.