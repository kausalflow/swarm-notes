---
created_at: '2026-09-03T09:17:02Z'
source_papers:
- '[[openalex-2608.30502-when-the-martingale-never-stops-firing-anytime-valid-gating]]'
title: Anytime-Valid Inference on Non-Exchangeable Streams
---

**Background:** Anytime-valid statistical monitors such as conformal test martingales rely on the assumption of data exchangeability to provide theoretical false-alarm guarantees, yet real-world machine learning forecast streams often violate this condition.

**Question / Future Work:** Develop robust anytime-valid inference frameworks and score-transformation mechanisms that maintain theoretical false-alarm guarantees when deployed on non-exchangeable, serially dependent, or adaptively coupled real-world forecast streams.

**Why It Matters:** Crucial for bridging the gap between theoretical guarantees of e-value methods/martingales and their practical failures in online machine learning pipelines where data dependence and feedback loops are ubiquitous.

**Evidence:** The guarantee is conditional. A deployment inherits it only if the stream it monitors behaves exchangeably. The premise is hardest to satisfy where these monitors are most useful, on dependent data and inside loops where the monitor modifies the learner whose scores it reads.