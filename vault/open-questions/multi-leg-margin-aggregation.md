---
created_at: '2026-05-14T07:39:28Z'
source_papers:
- '[[openalex-2605.10428-a-taxonomy-of-event-linked-perpetual-futures-variant-designs]]'
title: Multi-leg Margin Aggregation
---

**Background:** Perpetual futures linked to event spreads and event baskets involve multiple constituent legs that can resolve at different times, creating complex terminal jump risks.

**Question / Future Work:** There is an unresolved design challenge in calibrating margin requirements for event-linked spread and basket perpetuals that have multiple, potentially non-simultaneous resolution events and multiple terminal-collapse outcomes, requiring a multi-period, jump-aware margin aggregation rule.

**Why It Matters:** Proper margin calibration is the primary mechanism for preventing bad debt in binary prediction-market perpetuals, and the aggregation of multiple jump-risk channels in complex variants is a critical, unresolved risk-engineering bottleneck.

**Evidence:** For a basket whose legs resolve at different times, the margin schedule must be extended to a multi-period framework: each leg contributes its own jump-aware schedule active during the period from contract creation to that leg’s τ^(i), with per-leg schedules superposed under the basket’s weight vector.