---
created_at: '2026-07-16T07:14:14Z'
source_papers:
- '[[openalex-2607.11653-bet-on-features-anytime-valid-and-feature-aware-auditing-of]]'
title: Nonlinear Conditional Quantile Auditing
---

**Background:** Conditional quantile forecast auditing currently relies on sequential betting frameworks that are typically linear in the auditor's feature dictionary. These linear models often fail to capture complex, high-dimensional miscalibration patterns.

**Question / Future Work:** Extend the current auditing framework beyond linear betting strategies to accommodate nonlinear classes, such as kernelized or neural skeptics, while simultaneously maintaining anytime-validity and deriving regret-to-power guarantees.

**Why It Matters:** Linear methods may lack the representational power to detect subtle conditional miscalibration in high-dimensional settings, which is a major limitation for complex black-box models.