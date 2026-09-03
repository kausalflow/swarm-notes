---
# CSL-compatible fields
title: "Agentic Quantitative Trading: A Survey of Workflows, Systems, and Evaluation"
author:
  - literal: "Fengrui Hua"
  - literal: "H. L. Yang"
  - literal: "Xinlei Hao"
  - literal: "Haohan Zhang"
  - literal: "Bokai Cao"
  - literal: "Yiyan Qi"
  - literal: "Jia Li"
  - literal: "Jian Guo"
issued:
  date-parts:
    - [2026, 8, 31]
url: "https://arxiv.org/abs/2608.31041"

# Custom fields
paper_id: "2608.31041"
paper_source: "openalex"
domain: "finance"
tags:
  - "agent"
  - "autonomous-agent"
  - "tool-use"
  - "multi-agent"
  - "benchmark"
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
processed_at: "2026-09-03T09:17:42Z"
created_at: "2026-09-03T09:17:42Z"
---

# Agentic Quantitative Trading: A Survey of Workflows, Systems, and Evaluation

**Authors**: Fengrui Hua, H. L. Yang, Xinlei Hao, Haohan Zhang, Bokai Cao, Yiyan Qi, Jia Li, Jian Guo
**Date**: 2026-08-31
**Paper ID**: [openalex:2608.31041](https://arxiv.org/abs/2608.31041)

## Summary

This paper provides a comprehensive survey of agentic quantitative trading, reviewing workflows across factor mining, signal discovery, portfolio construction, order execution, and risk management. It examines system architectures, coordination mechanisms, and adaptation strategies, while analyzing diverse benchmarks across offline and live market evaluations. The findings reveal a heavy concentration on signal discovery over end-to-end integration and show that strong predictive capability does not reliably guarantee live trading success.

## Key Contributions

- Provides the first comprehensive survey of agentic quantitative trading workflows spanning factor mining, signal discovery, portfolio construction, order execution, and risk management.
- Systematically examines agentic quant systems across architecture, coordination, and adaptation paradigms.
- Compares benchmarks across strategy construction, offline trading, live market evaluation, and reliability assessment, revealing that predictive strength does not reliably translate to live trading performance.

## Limitations

Highlights that current agentic trading systems remain heavily concentrated on signal discovery while full integration with downstream portfolio construction, execution, and risk control is uncommon.

## Open Questions & Future Work

- [[end-to-end-agentic-trading-integration-and-execution]]
- [[rigorous-evaluation-and-leakage-control-for-trading-agents]]

## Archivist Review

The paper is a broad survey on agentic quantitative trading. It does not introduce a standalone reusable algorithmic model note or dataset, but it highlights important open research directions regarding end-to-end trading system integration and rigorous live evaluation/leakage control.

### Approved Open Questions
- End-to-End Agentic Trading Integration: Most current literature treats quantitative trading as a pure return-forecasting or signal-generation problem, ignoring the critical downstream bottlenecks of portfolio optimization, execution slippage, and risk control that dictate real-world profitability.
- Rigorous Evaluation of Trading Agents: Without leakage-controlled and friction-aware evaluation benchmarks, published agentic trading strategies cannot be reliably distinguished from overfitting, memorization, or luck.

### Rejected Candidates
- [open_question] Advanced Multi-Agent Coordination Mechanisms (`advanced-multi-agent-coordination-and-gating`) - duplicate_existing: Overlaps with existing general multi-agent governance and aggregation questions in the vault.

## Links

- [Abstract](https://arxiv.org/abs/2608.31041)
- [PDF](https://arxiv.org/pdf/2608.31041)

