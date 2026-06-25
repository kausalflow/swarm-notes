---
# CSL-compatible fields
title: "Explainable AI for Mental Health Prediction in Drug-Affected Populations with Dragonfly Algorithm and GAN Oversampling"
author:
  - literal: "Ahnaf Atef Choudhury"
  - literal: "Shahriar Siddique Ayon"
  - literal: "Md. Ebrahim Hossain"
  - literal: "Abdullah Al Mamun"
issued:
  date-parts:
    - [2026, 6, 22]
url: "https://arxiv.org/abs/2606.22780"

# Custom fields
paper_id: "2606.22780"
paper_source: "openalex"
domain: "medicine"
tags:
  - "machine-translation"
  - "explainability"
  - "gan"
  - "generative-adversarial-network"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-25T08:20:31Z"
created_at: "2026-06-25T08:20:31Z"
---

# Explainable AI for Mental Health Prediction in Drug-Affected Populations with Dragonfly Algorithm and GAN Oversampling

**Authors**: Ahnaf Atef Choudhury, Shahriar Siddique Ayon, Md. Ebrahim Hossain, Abdullah Al Mamun
**Date**: 2026-06-22
**Paper ID**: [openalex:2606.22780](https://arxiv.org/abs/2606.22780)

## Summary

This paper presents an explainable machine learning framework for predicting mental health in drug-affected populations, addressing key challenges of class imbalance and hyperparameter optimization. The approach combines PCA-IG feature selection, GAN-based oversampling, and a Dragonfly Algorithm-optimized XGBoost model to handle high-dimensional clinical data effectively. Experimental results demonstrate high accuracy and robust F1-scores, while SHAP analysis provides clinical interpretability by identifying key behavioral and physical factors influencing predictions.

## Key Contributions

- Proposes a hybrid mental health prediction framework for drug-affected populations that integrates PCA-IG feature selection, GAN-based oversampling, and Dragonfly Algorithm-optimized XGBoost.
- Demonstrates superior predictive performance, achieving 94.17% accuracy and 93.80% weighted F1-score, outperforming traditional and baseline models.
- Employs SHAP-based explainability to provide instance-level insights into predictive drivers like sleep quality and emotional regulation, enhancing clinical trust.

## Open Questions & Future Work

- [[longitudinal-multimodal-mental-health-forecasting-scalability]]

## Archivist Review

The proposed concepts for hyperparameter optimization using a meta-heuristic algorithm are standard practices in machine learning and do not meet the novelty threshold for a permanent vault entry. I approved a refined open question that focuses on the broader, systemic bottleneck of moving mental health predictive models from static clinical snapshots to longitudinal, multimodal forecasting, which is a significant research challenge in this domain.

### Approved Open Questions
- Longitudinal Multimodal Mental Health Forecasting: The transition from static research models to robust clinical decision support requires addressing the bottleneck of cross-sectional data limitations and the lack of temporal dynamics in current behavioral health forecasting. Tracking mental health in high-risk populations demands longitudinal, multimodal approaches that current standard predictive frameworks struggle to integrate.

### Rejected Candidates
- [concept] Dragonfly Algorithm (DA)-optimized XGBoost (`dragonfly-algorithm-optimized-xgboost`) - not_novel: Meta-heuristic hyperparameter optimization of tree-based models is a standard practice and not a novel or reusable conceptual contribution for the time-series forecasting literature.

## Links

- [Abstract](https://arxiv.org/abs/2606.22780)
- [PDF](https://arxiv.org/pdf/2606.22780)

