---
# CSL-compatible fields
title: "ProCAVE: A Self-Adaptive, Full-Lifecycle Edge Caching Framework for Video Streaming via Predictive Bandwidth Estimation and Preference-Aware Deep Reinforcement Learning"
author:
  - literal: "Yeganeh Chatri"
  - literal: "Behzad Akbari"
  - literal: "Foad Ghaderi"
  - literal: "Pejman Goudarzi"
issued:
  date-parts:
    - [2026, 8, 4]
url: "https://arxiv.org/abs/2608.03313"

# Custom fields
paper_id: "2608.03313"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "transformer"
  - "reinforcement-learning"
  - "multimodal"
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
processed_at: "2026-08-07T06:04:42Z"
created_at: "2026-08-07T06:04:42Z"
---

# ProCAVE: A Self-Adaptive, Full-Lifecycle Edge Caching Framework for Video Streaming via Predictive Bandwidth Estimation and Preference-Aware Deep Reinforcement Learning

**Authors**: Yeganeh Chatri, Behzad Akbari, Foad Ghaderi, Pejman Goudarzi
**Date**: 2026-08-04
**Paper ID**: [openalex:2608.03313](https://arxiv.org/abs/2608.03313)

## Summary

The paper introduces ProCAVE, a self-adaptive deep reinforcement learning framework for edge video streaming that unifies predictive bandwidth modeling via a lightweight Transformer, proactive ABR selection via PPO, and preference-aware cache control via DDPG. Evaluated on MovieLens preference traces and Ghent 4G bandwidth measurements, ProCAVE improves byte hit rates, reduces backhaul load, and enhances user Quality of Experience (QoE) compared to existing reactive baselines like FlyCache.

## Key Contributions

- Proposes ProCAVE, a self-adaptive edge caching framework unifying predictive bandwidth modeling, proactive bitrate selection, and preference-aware cache control using deep reinforcement learning.
- Employs a lightweight Transformer for short-term throughput forecasting combined with a PPO-driven ABR agent and a DDPG-based continuous cache controller.
- Demonstrates improved byte hit rate, reduced backhaul load, and enhanced QoE compared to existing baselines such as FlyCache using MovieLens preference traces and Ghent 4G bandwidth measurements.

## Archivist Review

The paper proposes ProCAVE, an application-level edge video streaming framework combining standard DRL algorithms (PPO and DDPG) and lightweight Transformers for bandwidth forecasting. As noted in the critic review summary, these are domain-specific applications of existing techniques rather than reusable foundational machine learning or time-series modeling concepts. Therefore, no concepts, datasets, or open questions qualify for permanent vault notes under our strict selection criteria.

## Links

- [Abstract](https://arxiv.org/abs/2608.03313)
- [PDF](https://arxiv.org/pdf/2608.03313)

