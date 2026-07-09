---
title: "SlimCache"
slug: "slimcache"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2607.05095-fast-a-holistic-framework-for-optimizing-memory-io-computati]]"
processed_at: "2026-07-09T08:19:19Z"
created_at: "2026-07-09T08:19:19Z"
---

# SlimCache

> *Auto-generated stub. Edit this file to add more details.*

A memory optimization technique for dynamic graph training that uses batch compression and caching to minimize host-to-device data transfers.


## Why It Matters

Specifically targets the host-to-device memory bottleneck in memory-constrained dynamic graph training.

## Evidence

> FAST introduces SlimCache, which exploits within-batch compression and cross-batch caching to reduce host-device data movement under limited GPU memory budgets.

## Related Papers

- [[openalex-2607.05095-fast-a-holistic-framework-for-optimizing-memory-io-computati]]
