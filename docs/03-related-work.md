# Related work

## What exists

- **Regime models.** Hamilton (1989) started the use of regime-switching models in economics. Everything here builds on that.
- **Online detection.** Issa and Horvath (2023) detect regime changes as they happen, using only price paths. They test on made-up, equity and crypto data.
- **Volatility forecasts.** Lyu and Lee (2026) test whether a path-based feature set beats a standard baseline at forecasting volatility, on US and developed markets.
- **Risk and trading.** Shu, Yu and Mulvey (2024) use a jump model, which gives longer-lasting regimes than an HMM. They judge it on risk and return of a strategy.
- **Pakistan.** Attaullah et al. (2022) and Fraz et al. (2022) show that regime changes exist in Pakistani markets, including the KSE-100.
- **News tone.** FinBERT (Araci, 2019) and the Loughran-McDonald word lists (2011) score the tone of finance text.

## What is missing

1. Most work is on US and developed markets. The KSE-100 gets little attention.
2. The Pakistani studies show that regimes exist. None of them measure how late a live detector is.
3. Most models are fitted on the full history. Few ask what happens with only a handful of labelled days.
4. The detection papers use prices only. We found no work that adds timestamped Pakistani news.
5. Papers judge forecast error or trading profit. We judge delay, false alarms and misses.

We do not claim this is new until our reading is complete. We read the abstracts of three of these papers, and none of them uses Pakistani news.

## References

1. Hamilton, J. D. (1989). A new approach to the economic analysis of nonstationary time series and the business cycle. *Econometrica*, 57(2), 357-384.
2. Shu, Y., Yu, C., & Mulvey, J. M. (2024). Downside risk reduction using regime-switching signals: a statistical jump model approach. *Journal of Asset Management*, 25(5), 493-507.
3. Issa, Z., & Horvath, B. (2023). Non-parametric online market regime detection and regime clustering for multidimensional and path-dependent data structures. arXiv:2306.15835.
4. Lyu, Y., & Lee, K. (2026). Scale or speed? When do path signatures improve volatility-regime forecasts? arXiv:2610.06690.
5. Attaullah, Hamid, K., Saeed, M. Y., & Hussain, S. (2022). Regime shift behavior and interconnectedness of stock market volatility and exchange rate movements. *Sustainable Business and Society in Emerging Economies*, 4(2), 383-392.
6. Fraz, et al. (2022). Modeling and forecasting stock market volatility of CPEC founding countries: nonlinear time series and machine learning models. *JISR-MSSE*, SZABIST.
7. Araci, D. (2019). FinBERT: Financial sentiment analysis with pre-trained language models. arXiv:1908.10063.
8. Loughran, T., & McDonald, B. (2011). When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks. *Journal of Finance*, 66(1), 35-65.
