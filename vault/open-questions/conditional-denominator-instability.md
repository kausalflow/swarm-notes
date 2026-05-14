---
created_at: '2026-05-14T07:39:28Z'
source_papers:
- '[[openalex-2605.10428-a-taxonomy-of-event-linked-perpetual-futures-variant-designs]]'
title: Conditional Denominator Instability
---

**Background:** Conditional-probability perpetuals compute their underlying value as a ratio of two event probabilities, which faces instability when the denominator event approaches zero.

**Question / Future Work:** The conditional-probability perpetual requires a design specification that handles the undefined or highly sensitive state of the underlying index when the conditioning event's probability approaches zero, which remains an unresolved failure mode needing explicit handling like denominator floors or halt triggers.

**Why It Matters:** This represents a fundamental structural failure mode for the specific instrument variant that is currently theoretically conjectured but lacks a deployed or formally specified solution.

**Evidence:** Any conditional-probability perpetual whose underlying is computed as I_t^cond = I_t^(A∩B) / I_t^(B)... inherits an unbounded local sensitivity ∂I^cond/∂I^(B) as the conditioning event’s marginal I_t^(B) → 0. Without explicit denominator floors, conditioning-event halt rules, or early termination triggers, the contract’s underlying becomes ill-defined and unhedgeable.