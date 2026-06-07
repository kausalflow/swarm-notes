---
# CSL-compatible fields
title: "Warning Message Content Increases Help Seeking in a Large-Scale Dark Web CSAM Intervention"
author:
  - literal: "Caoilte Ó Ciardha"
  - literal: "Joel Scanlan"
  - literal: "Tegan Insoll"
  - literal: "Juha Nurmi"
  - literal: "Nina Vaaranen-Valkonen"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.06417"

# Custom fields
paper_id: "2606.06417"
paper_source: "openalex"
domain: "nlp"
tags:
  - "language-model"
  - "text-classification"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:20:09Z"
created_at: "2026-06-07T08:20:09Z"
---

# Warning Message Content Increases Help Seeking in a Large-Scale Dark Web CSAM Intervention

**Authors**: Caoilte Ó Ciardha, Joel Scanlan, Tegan Insoll, Juha Nurmi, Nina Vaaranen-Valkonen
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.06417](https://arxiv.org/abs/2606.06417)

## Summary

This study evaluates the effectiveness of intervention warning messages on the Tor search engine Ahmia.fi for individuals seeking child sexual abuse material (CSAM). By conducting a large-scale field experiment over 140 days involving 3 million searches, the authors show that message framing significantly impacts engagement with self-help resources. Specifically, harm-focused messages were found to be most effective at increasing click-through rates compared to neutral or alternative thematic messages. The findings provide empirical support for optimizing behavioral interventions in high-anonymity environments.

## Key Contributions

- Demonstrates that thematic content and framing of warning messages significantly influence user help-seeking behavior in anonymous online environments.
- Shows that harm-focused messaging yields the highest engagement rates compared to other thematic frames and neutral controls.
- Reports a field experiment on the Tor search engine Ahmia.fi involving 3 million CSAM-related searches, showing an increase in help-seeking click-through rates from 8.73% to 15.67%.

## Open Questions & Future Work

- [[user-heterogeneity-in-csam-interventions]]

## Archivist Review

The paper presents an important empirical finding on intervention efficacy in anonymous environments but does not introduce a widely reusable forecasting mechanism, representation, or architecture fitting the vault's time-series focus. The open question regarding heterogeneity is approved as it addresses a fundamental limitation in behavior-based forecasting and intervention analysis in privacy-sensitive domains.

### Approved Open Questions
- Heterogeneity in CSAM Intervention Responses: Understanding subgroup-specific responses is essential to optimize the design of interventions for diverse populations, potentially increasing engagement rates for groups that are currently underserved by generic messaging.

### Rejected Candidates
- [dataset] Ahmia.fi Field Experiment (`ahmia-fi-field-experiment`) - not_reusable: The dataset is specific to one platform experiment and lacks general reusability as a standalone benchmark or reference corpus.

## Links

- [Abstract](https://arxiv.org/abs/2606.06417)
- [PDF](https://arxiv.org/pdf/2606.06417)

