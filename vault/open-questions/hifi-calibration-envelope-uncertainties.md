---
created_at: '2026-03-27T15:44:35Z'
source_papers:
- '[[openalex-2603.23015-janusbm-a-dual-fidelity-multi-zone-white-box-building-modeli]]'
title: Extend HiFi calibration to envelope
---

**Background:** Calibration of high-fidelity (HiFi) building energy models often requires isolating parameters to avoid non-identifiability issues, such as fixing envelope parameters while tuning hydronic components. Remaining structured residuals at the zone level point to unaccounted structural uncertainties.

**Question / Future Work:** Develop an extended calibration methodology for high-fidelity (HiFi) models that systematically incorporates and tunes building envelope properties alongside hydronic parameters, requiring new constraints or techniques to mitigate parameter non-identifiability issues. Additionally, future model extensions should account for or incorporate structural uncertainties like sensor placement, interior modifications, or air leakage using suitable grey-box representations to resolve remaining zone-level residuals.

**Why It Matters:** A fully calibrated model that accounts for both thermal distribution and envelope physics is necessary for robust digital twin applications and high-fidelity dynamic analysis.

**Evidence:** the current HiFi calibration intentionally isolates hydronic impacts by tuning UFH-related parameters while keeping building envelope parameters fixed to avoid non-identifiability, and additional constraints will be required when extending the calibration to include envelope properties. In addition, remaining structured residuals at the zone level indicate structural uncertainties beyond hydronic heat exchange, such as sensor placement, interior modifications, and air leakage, suggesting that future model extensions should account for these effects, or incorporate them with suitable grey-box representations.