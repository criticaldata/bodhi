<p align="center">
  <img src="assets/bodhi-logo.png" alt="BODHI Logo" width="200">
</p>

# BODHI Framework

**Bridging, Open, Discerning, Humble, Inquiring**

An engineering framework for curiosity driven and humble AI in clinical decision support.

## Overview

BODHI addresses a critical gap in medical AI: large language models often express inappropriate confidence, conflating statistical pattern recognition with genuine medical understanding. Through a dual reflective architecture, BODHI decomposes epistemic uncertainty into task specific dimensions and constrains model responses using virtue based stance rules.

The framework operates through a two pass chain of thought protocol that separates internal reasoning from external communication, guided by a Virtue Activation Matrix mapping clinical complexity against model confidence.

## Key Results

- **97.3%** rate of appropriate clarifying questions (vs 7.8% baseline)
- **+16.6pp** improvement in overall clinical quality (p < 0.0001)
- **+89.6pp** improvement in context seeking behavior
- **Very large effect sizes** on curiosity (d = 16.38) and humility (d = 5.80) metrics

## Installation
```bash
pip install bodhi-llm
```

## Active Research Modules

BODHI is expanding into a modular platform. Current research branches:

| Module | Status | Focus |
|--------|--------|-------|
| Curiosity | Validated | Context seeking, clarifying questions, active inquiry |
| Humility | Validated | Uncertainty quantification, sycophancy detection, hedging |
| Creativity | In Development | Novel hypothesis generation, divergent thinking, QMoE |
| Coherence | In Development | Logical consistency, pre mortem analysis, bias detection |

We welcome collaborators for any module. Contact us to get involved.

## Resources

- **Website**: [https://criticaldata.github.io/bodhi.github.io/](https://criticaldata.github.io/bodhi.github.io/)
- **PyPI Package**: [bodhi-llm](https://pypi.org/project/bodhi-llm/)
- **Evaluation Scripts**: [humbleai-healthbench](https://github.com/sebasmos/humbleai-healthbench)
- **Curiosity Driven QMoE**: [curious-qmoe](https://github.com/sebasmos/curious-qmoe)

## Publications

1. Cajas Ordóñez SA, et al. "Beyond overconfidence: Embedding curiosity and humility for ethical medical AI." *PLOS Digital Health* 5(1): e0001013, 2026. [DOI](https://doi.org/10.1371/journal.pdig.0001013)

2. Arslan J, Benke K, Cajas Ordoñez SA, et al. "An Engineering Framework for Curiosity Driven and Humble AI in Clinical Decision Support." *BMJ Health & Care Informatics*, 2026. (Under Review)

3. Cajas Ordóñez SA, et al. "Humility and Curiosity in Human AI Systems for Health Care." *The Lancet* 406(10505): 804-805, 2025. [DOI](https://doi.org/10.1016/S0140-6736(25)01626-5)

4. Cajas Ordóñez SA, et al. "Uncertainty Makes It Stable: Curiosity Driven Quantized Mixture of Experts." *arXiv:2511.11743*, 2025. [arXiv](https://arxiv.org/abs/2511.11743)

## Team

**Principal Investigator:** Leo Anthony Celi (MIT, Beth Israel Deaconess, Harvard)

**Multidisciplinary Team Researchers:** Kurt Benke, Sebastian Cajas Ordonez, Rowell Castro, Gustavo Adolfo Cruz Suarez, Roben Delos Reyes, Justin Engelmann, Ari Ercole, Almog Hilel, Mahima Kalla, Janan Arslan, Leo Kinyera, Maximin Lange, Torleif Markussen Lunde, Mackenzie J Meni, Felipe Ocampo Osorio, Oriel Perets, Anna E Premo, Jana Sedlakova, Pritika Vig

MIT Critical Data, Laboratory for Computational Physiology, and collaborating institutions worldwide.

## Contact

For collaboration inquiries: sebasmos@mit.edu // mlange2@mit.edu // lceli@mit.edu

## License

© 2026 BODHI Research Group. Developed by MIT Critical Data and partner institutions worldwide.
