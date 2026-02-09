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
| Sycophancy Detection | Validated | Anti-sycophancy measures, agreement bias reduction, independent reasoning |
| Creativity | In Development | Novel hypothesis generation, divergent thinking, QMoE |

We welcome collaborators for any module. Contact us to get involved.

## Resources

- **Website**: [https://criticaldata.github.io/bodhi](https://criticaldata.github.io/bodhi)
- **PyPI Package**: [bodhi-llm](https://pypi.org/project/bodhi-llm/)
- **Evaluation Scripts**: [humbleai-healthbench](https://github.com/sebasmos/humbleai-healthbench)
- **Curiosity Driven QMoE**: [curious-qmoe](https://github.com/sebasmos/curious-qmoe)

## Publications

1. Cajas Ordoñez SA, Castro R, Celi LA, Delos Reyes R, Engelmann J, Ercole A, Hilel A, Kalla M, Kinyera L, Lange M, Lunde TM, Meni MJ, Premo AE, Sedlakova J. "Beyond overconfidence: Embedding curiosity and humility for ethical medical AI." *PLOS Digital Health* 5(1): e0001013, 2026. [Paper](https://doi.org/10.1371/journal.pdig.0001013)

2. Arslan J, Benke K, Cajas Ordoñez SA, Castro R, Celi LA, Cruz Suarez GA, Delos Reyes R, Engelmann J, Ercole A, Hilel A, Kalla M, Kinyera L, Lange M, Lunde TM, Meni MJ, Ocampo Osorio F, Perets O, Premo AE, Sedlakova J, Vig P. "An Engineering Framework for Curiosity Driven and Humble AI in Clinical Decision Support." *BMJ Health & Care Informatics*, 2026. (Under Review) [Preprint](https://www.medrxiv.org/content/10.64898/2026.02.06.26345664v1) | [Code](https://github.com/sebasmos/humbleai-healthbench)

3. Cajas Ordoñez SA, Lange M, Lunde TM, Meni MJ, Premo AE. "Humility and Curiosity in Human–AI Systems for Health Care." *The Lancet* 406(10505): 804-805, 2025. [Paper](https://doi.org/10.1016/S0140-6736(25)01626-5)

4. Cajas Ordoñez SA, Torres Torres LF, Meni MJ, Duran Paredes CA, Arazo E, Bosch C, Carbajo RS, Lai Y, Celi LA. "Uncertainty Makes It Stable: Curiosity Driven Quantized Mixture of Experts." *arXiv:2511.11743*, 2025. [arXiv](https://arxiv.org/abs/2511.11743) | [Code](https://github.com/sebasmos/curious-qmoe)

5. Celi LA. "Teaching Machines to Doubt." *Nature Medicine*, 2025. [Paper](https://www.nature.com/articles/s41591-025-04013-x)


## Contact

For collaboration inquiries, reach us through the [contact form](https://criticaldata.github.io/bodhi#contact) on our website.

## License

© 2026 BODHI Research Group. Developed by MIT Critical Data and partner institutions worldwide.
