---
# CSL-compatible fields
title: "Stellar Variability and Distance Indicators in the Near-infrared in Nearby Galaxies. II. Pulsating Stars in the Carina Dwarf Spheroidal"
author:
  - literal: "Chow-Choong Ngeow"
  - literal: "Anupam Bhardwaj"
  - literal: "Prashant Nishad"
  - literal: "Das Susmita"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24249"

# Custom fields
paper_id: "2603.24249"
paper_source: "openalex"
domain: "astronomy"
tags:
  - "astronomy"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  - "Carina dwarf Spheroidal"
concept_slugs:
  []
dataset_slugs:
  - "carina-dwarf-spheroidal"
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:29:59Z"
created_at: "2026-03-28T05:29:59Z"
---

# Stellar Variability and Distance Indicators in the Near-infrared in Nearby Galaxies. II. Pulsating Stars in the Carina Dwarf Spheroidal

**Authors**: Chow-Choong Ngeow, Anupam Bhardwaj, Prashant Nishad, Das Susmita
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24249](https://arxiv.org/abs/2603.24249)

## Summary

This paper presents near-infrared ($JHK_s$ bands) time-series photometry of pulsating stars within the Carina dwarf Spheroidal (dSph) galaxy to establish precise distance measurements. Using 43 RR Lyrae stars as standard candles, the authors derived a distance modulus of $20.079\pm0.028\pm0.045$ mag to Carina. The distance determination was cross-validated by showing consistency with Period-Luminosity relations established for Dwarf Cepheids. A notable finding is the systematic deviation in distance moduli derived from Anomalous Cepheids, which points towards an unaddressed metallicity dependence in their period-luminosity relationship.

## Key Contributions

- Determined a precise distance modulus to the Carina dwarf Spheroidal galaxy using near-infrared time-series observations of pulsating stars.
- Obtained a distance modulus of $20.079\pm0.028\pm0.045$ mag (distance of $103.7\pm1.3\pm2.2$ kpc) anchored by 43 RR Lyrae stars in the $JHK_s$ bands.
- Validated the distance determination by showing excellent agreement between RR Lyrae and Period-Luminosity relations derived for Dwarf Cepheids (DCep) calibrated via SX Phoenicis or delta-Scuti stars.
- Observed a systematic offset in distance moduli derived from Anomalous Cepheids (ACep) compared to RR Lyrae, suggesting a metallicity dependence in the ACep period-luminosity relation.

## Limitations

The study notes a systematic difference in distance estimates between ACep and RR Lyrae, hinting at uncalibrated metallicity effects in the ACep standard candle model.

## Archivist Review

The analysis focused heavily on astrophysical measurement rather than novel machine learning techniques, resulting in no approved concepts. The 'Carina dwarf Spheroidal' dataset was approved as it is the specific, named target of the observational study. The rejected candidates relate to established astrophysical tools (standard candles, P-L relations) rather than reusable ML/forecasting concepts.

### Rejected Candidates
- [concept] Pulsating Stars as Standard Candles (`pulsating-stars-as-standard-candles`) - not_novel: The use of pulsating stars (RR Lyrae, ACep, DCep) as standard candles is a well-established astrophysical technique, not a novel concept introduced by this paper.
- [concept] Period-Luminosity Relations (`period-luminosity-relations`) - not_novel: Period-Luminosity relations are fundamental, well-known concepts in stellar astronomy, not a novel contribution warranting a vault entry based on this specific application.
- [concept] Metallicity Dependence of Period-Luminosity Relation (`metallicity-dependence-of-period-luminosity-relation`) - not_reusable: While the paper notes a systematic dependence, the *concept* of metallicity affecting P-L relations is established in astrophysics; the finding here is a specific measurement/confirmation, not a new reusable ML mechanism.

## Datasets

- [[carina-dwarf-spheroidal]]

## Links

- [Abstract](https://arxiv.org/abs/2603.24249)
- [PDF](https://arxiv.org/pdf/2603.24249)

