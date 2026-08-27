---
created_at: '2026-08-27T15:58:06Z'
source_papers:
- '[[openalex-2608.23473-metacaster-meta-harness-optimized-agent-for-end-to-end-few-s]]'
title: Zero-Shot Learning for Lightweight Forecasters
---

**Background:** Lightweight time series forecasters require substantial training data, limiting their deployment in privacy-sensitive or data-scarce domains where acquiring large datasets is infeasible.

**Question / Future Work:** Investigate and develop methodologies that enable effective zero-shot learning for lightweight time series forecasters without relying on reference training examples or few-shot support sets.

**Why It Matters:** Zero-shot capabilities are crucial for deploying compact models instantly in entirely unseen domains without requiring any historical support data, bypassing the dependency on few-shot examples.

**Evidence:** However, our current work does not address the extreme zero-shot setting, where no reference examples are available. Without reference time series, the agent lacks basic statistical grounding of the target domain, leading to unreliable data generation.