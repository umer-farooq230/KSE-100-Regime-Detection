"""Set C: Set B + macro features.

The macro variables are NOT decided yet (M3). This is a generic version: pass
any daily macro table [date, <col1>, <col2>, ...] (e.g. USD/PKR, policy rate,
oil) and every column gets change and z-score features automatically.

LEAKAGE RULE: macro values are shifted by 1 trading day, because most macro
series are published/settled after the PSX close. Remove the shift only for
series you have verified are known before the close.
"""
import pandas as pd

import set_b_sentiment
from config import (DATE_COL, MACRO_CHANGE_WINDOWS, MACRO_ZSCORE_WINDOW)


def build(prices: pd.DataFrame, sentiment: pd.DataFrame,
          macro: pd.DataFrame, lag_days: int = 1) -> pd.DataFrame:
    base = set_b_sentiment.build(prices, sentiment)

    m = macro.copy()
    m[DATE_COL] = pd.to_datetime(m[DATE_COL])
    m = m.sort_values(DATE_COL).set_index(DATE_COL)
    # Align to trading days, carry the last known value forward (causal)
    m = m.reindex(m.index.union(base.index)).ffill().reindex(base.index)

    out = pd.DataFrame(index=base.index)
    for col in m.columns:
        for w in MACRO_CHANGE_WINDOWS:
            out[f"{col}_chg_{w}d"] = m[col].pct_change(w)
        mu = m[col].rolling(MACRO_ZSCORE_WINDOW).mean()
        sd = m[col].rolling(MACRO_ZSCORE_WINDOW).std()
        out[f"{col}_zscore"] = (m[col] - mu) / sd

    out = out.shift(lag_days)
    return base.join(out)
