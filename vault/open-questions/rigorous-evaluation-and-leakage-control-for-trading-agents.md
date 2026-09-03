---
created_at: '2026-09-03T09:17:42Z'
source_papers:
- '[[openalex-2608.31041-agentic-quantitative-trading-a-survey-of-workflows-systems-a]]'
title: Rigorous Evaluation of Trading Agents
---

**Background:** Evaluating agentic trading systems under historical backtests often yields overly optimistic performance metrics due to temporal leakage, data contamination, and unmodeled market frictions.

**Question / Future Work:** Design rigorous evaluation benchmarks and protocols that properly isolate information leakage, account for live market frictions such as transaction costs and liquidity constraints, and separate alpha attribution from market and style exposures.

**Why It Matters:** Without leakage-controlled and friction-aware evaluation benchmarks, published agentic trading strategies cannot be reliably distinguished from overfitting, memorization, or luck.

**Evidence:** Benchmark evidence further shows that strong model or forecasting capability does not reliably translate into trading performance under live market conditions and reliability controls.