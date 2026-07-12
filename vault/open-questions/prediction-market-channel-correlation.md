---
created_at: '2026-07-12T07:24:59Z'
source_papers:
- '[[openalex-2607.08199-volatility-in-prediction-markets-a-structural-approach]]'
title: Correlating Market Information Channels
---

**Background:** Prediction-market price innovations consist of two components: public signal resolution (deadline-resolution channel) and informed trading (private information channel). Currently, these two channels are modeled as conditionally orthogonal, despite potential interactions between public news and informed trading.

**Question / Future Work:** The development of models that explicitly account for the correlation or joint dynamics between the public-signal deadline-resolution channel and the private-signal order-flow channel remains an unresolved challenge. Existing approaches often rely on a conditional orthogonality assumption for tractability, which potentially omits information about how news events and informed trading are correlated in real time.

**Why It Matters:** Understanding the dependency between public information and order flow is crucial for accurate volatility modeling and derivatives pricing in prediction markets, as assuming independence may lead to biased conditional variance forecasts.

**Evidence:** In practice the two channels may be correlated: a public news event can simultaneously move the consensus and trigger informed order flow, and informed trading itself may be timed around expected public information.