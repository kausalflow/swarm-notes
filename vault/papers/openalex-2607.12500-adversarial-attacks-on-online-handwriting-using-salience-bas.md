---
# CSL-compatible fields
title: "Adversarial Attacks on Online Handwriting using Salience-based Temporal Editing"
author:
  - literal: "Yataro Tamura"
  - literal: "Brian Kenji Iwana"
  - literal: "Jiseok Lee"
issued:
  date-parts:
    - [2026, 7, 14]
url: "https://arxiv.org/abs/2607.12500"

# Custom fields
paper_id: "2607.12500"
paper_source: "openalex"
domain: "nlp"
tags:
  - "adversarial-examples"
  - "robustness"
  - "time-series"
  - "information-extraction"
architectures:
  []
datasets:
  - "unipen"
  - "casia-olhwdb"
concept_slugs:
  - "salience-based-temporal-editing"
dataset_slugs:
  - "unipen"
  - "casia-olhwdb"
skill: "TimeSeriesSkill"
processed_at: "2026-07-17T07:10:35Z"
created_at: "2026-07-17T07:10:35Z"
---

# Adversarial Attacks on Online Handwriting using Salience-based Temporal Editing

**Authors**: Yataro Tamura, Brian Kenji Iwana, Jiseok Lee
**Date**: 2026-07-14
**Paper ID**: [openalex:2607.12500](https://arxiv.org/abs/2607.12500)

## Summary

This paper addresses the vulnerability of online handwriting recognition to adversarial attacks, noting that conventional image-based spatial perturbations introduce unnatural artifacts into time-series trajectories. The authors propose a novel attack framework based on salience-guided temporal editing, which generates adversarial samples by strategically inserting and deleting trajectory points to preserve visual smoothness. Experiments on the Unipen and CASIA-OLHWDB datasets demonstrate that this approach achieves superior black-box transferability compared to traditional methods while maintaining the integrity of the original handwriting.

## Key Contributions

- Introduced a salience-guided temporal editing framework that generates adversarial handwriting examples via point insertion and deletion rather than additive noise.
- Demonstrated that the proposed method preserves visual handwriting structure while significantly outperforming conventional image-based attacks in one-shot black-box transferability.
- Established temporal editing as a more realistic and potent threat model for online handwriting recognition compared to standard spatial perturbation methods.

## Open Questions & Future Work

- [[temporal-editing-defenses]]

## Key Concepts

- [[salience-based-temporal-editing]]: An adversarial attack framework for online handwriting that modifies pen trajectories by inserting and deleting points based on temporal salience.

## Archivist Review

The review focuses on the shift from additive spatial noise to structural temporal editing for adversarial attacks on trajectory data. The approved concept and open question capture this core contribution and the resulting security gap, which are both highly reusable for future sequence-based research. The datasets are approved as they are established benchmarks for the online handwriting domain.

### Approved Concepts
- Salience-based Temporal Editing: It shifts the adversarial paradigm for time-series handwriting from additive noise to trajectory-preserving editing, addressing the problem of unnatural artifacts in previous methods.

### Approved Open Questions
- Defenses against temporal editing: Since temporal editing attacks pose a distinct, more realistic threat to online handwriting than additive spatial noise, creating corresponding defenses is necessary for the security of deployed handwriting recognition systems.

## Datasets

- [[unipen]]
- [[casia-olhwdb]]

## Links

- [Abstract](https://arxiv.org/abs/2607.12500)
- [PDF](https://arxiv.org/pdf/2607.12500)

