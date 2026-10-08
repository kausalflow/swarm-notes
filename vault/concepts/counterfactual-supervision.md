---
title: "Counterfactual Supervision"
slug: "counterfactual-supervision"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2610.06180-anlu-enabling-in-context-time-series-anomaly-detection-in-fo]]"
processed_at: "2026-10-08T11:41:02Z"
created_at: "2026-10-08T11:41:02Z"
---

# Counterfactual Supervision

> *Auto-generated stub. Edit this file to add more details.*

A training supervision strategy that pairs a query with multiple conflicting reference records to force models to utilize in-context conditioning.


## Why It Matters

It solves the shortcut-learning problem where a detector ignores the conditioning reference by enforcing reference-dependent label divergence across counterfactual reference pairings.

## Evidence

> We therefore introduce counterfactual supervision, which pairs one query with two references that support different normal rules and labels the query under each.

## Related Papers

- [[openalex-2610.06180-anlu-enabling-in-context-time-series-anomaly-detection-in-fo]]
