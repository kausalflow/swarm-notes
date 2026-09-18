---
title: "Learned Atmospheric Critic"
slug: "learned-atmospheric-critic"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2609.18381-every-fixed-metric-has-a-blind-spot-a-learned-atmospheric-cr]]"
processed_at: "2026-09-18T09:17:29Z"
created_at: "2026-09-18T09:17:29Z"
---

# Learned Atmospheric Critic

> *Auto-generated stub. Edit this file to add more details.*

A discriminator-based realism scoring mechanism that learns to separate weather model outputs from reference data to detect unphysical spatial artifacts.


## Why It Matters

Introduces a dynamic discriminator-based scoring mechanism to evaluate weather forecast realism and identify unphysical artifacts that fixed metrics miss.

## Evidence

> We propose to train a discriminator for separating reference data from the model's output, and using its output logit to obtain a divergence-like realism score.

## Related Papers

- [[openalex-2609.18381-every-fixed-metric-has-a-blind-spot-a-learned-atmospheric-cr]]
