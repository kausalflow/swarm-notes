---
# CSL-compatible fields
title: "Time-Aligned Evolving Concept Graphs for Scientific Relation Forecasting"
author:
  - literal: "Fred Sun"
  - literal: "Jingze Wang"
  - literal: "Minkun Xu"
  - literal: "Shangqi Guo"
issued:
  date-parts:
    - [2026, 9, 16]
url: "https://arxiv.org/abs/2609.18163"

# Custom fields
paper_id: "2609.18163"
paper_source: "openalex"
domain: "nlp"
tags:
  - "graph-neural-network"
  - "information-extraction"
  - "knowledge-graph"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "time-aligned-evolving-concept-graphs"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-18T09:17:18Z"
created_at: "2026-09-18T09:17:18Z"
---

# Time-Aligned Evolving Concept Graphs for Scientific Relation Forecasting

**Authors**: Fred Sun, Jingze Wang, Minkun Xu, Shangqi Guo
**Date**: 2026-09-16
**Paper ID**: [openalex:2609.18163](https://arxiv.org/abs/2609.18163)

## Summary

This paper introduces a time-aligned evolving concept graph framework for scientific relation forecasting that jointly models semantic and structural evolution. By treating dated papers as shared update events, the approach reconstructs semantic and structural states from the same publication history through each prediction time. Evaluated on a large-scale graph comprising hundreds of thousands of papers and concepts, the framework significantly outperforms strong baselines in predicting relation formation and types.

## Key Contributions

- Proposes a time-aligned evolving concept graph framework that jointly models semantic and structural evolution for scientific relation forecasting.
- Treats dated papers as shared update events to reconstruct semantic and structural states from publication history through each prediction time.
- Achieves an improvement in mean relation AUROC to 0.9722 on a large-scale graph built from 187,848 papers, 270,687 concepts, and 7.45 million co-occurrence links.

## Key Concepts

- [[time-aligned-evolving-concept-graphs]]: A framework that jointly models semantic and structural evolution using dated papers as shared update events to forecast scientific relations.

## Archivist Review

Approved the core methodological framework note as a reusable dynamic graph forecasting contribution while rejecting paper-local empirical comparisons. Followed strict scarcity and quality criteria.

### Approved Concepts
- Time-Aligned Evolving Concept Graphs: Jointly models semantic and structural evolution by treating dated papers as shared update events for predicting scientific relations.

### Rejected Candidates
- [open_question] Refreshing Context vs. Frozen Context in Scientific Relation Forecasting (`refreshing-context-vs-frozen-context-scientific-relation-forecasting`) - paper_local: Paper-local empirical finding about context updating rather than a foundational open research question.

## Links

- [Abstract](https://arxiv.org/abs/2609.18163)
- [PDF](https://arxiv.org/pdf/2609.18163)

