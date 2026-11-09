"""Set B: Set A + FinBERT news-sentiment features.

Input `sentiment` is a daily table from the NLP side:
    columns [date, sent_mean, n_articles]
where sent_mean = mean over articles of (P(positive) - P(negative)).

#LEAKAGE RULE: `date` must be the first trading day on which the news was
#usable. News published after the market close belongs to the NEXT trading day.
#Resolve that when producing the table; this module does not guess.
#"""
import pandas as pd

import set_a_returns
from config import DATE_COL, SENT_WINDOWS


def build(prices: pd.DataFrame, sentiment: pd.DataFrame) -> pd.DataFrame:
    base = set_a_returns.build(prices)

    s = sentiment.copy()
    s[DATE_COL] = pd.to_datetime(s[DATE_COL])
    s = s.groupby(DATE_COL).agg(sent_mean=("sent_mean", "mean"),
                                n_articles=("n_articles", "sum"))
    s = s.reindex(base.index)

    # No news on a day = neutral sentiment, zero volume (not NaN, not ffill)
    s["n_articles"] = s["n_articles"].fillna(0)
    s["sent_mean"] = s["sent_mean"].fillna(0.0)

    out = pd.DataFrame(index=base.index)
    out["sent_mean"] = s["sent_mean"]
    out["news_volume"] = s["n_articles"]
    out["sent_change_1d"] = s["sent_mean"].diff()

    for w in SENT_WINDOWS:
        out[f"sent_mean_{w}d"] = s["sent_mean"].rolling(w, min_periods=1).mean()
        out[f"news_volume_{w}d"] = s["n_articles"].rolling(w, min_periods=1).sum()
    out["sent_std_5d"] = s["sent_mean"].rolling(5, min_periods=2).std()

    return base.join(out)
