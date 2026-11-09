#Set A: return-based features from KSE-100 closes only
import numpy as np
import pandas as pd

from config import (CLOSE_COL, DATE_COL, DRAWDOWN_WINDOW, MEAN_WINDOWS,
                    VOL_WINDOWS, ZSCORE_WINDOW)


def build(prices: pd.DataFrame) -> pd.DataFrame:
    df = prices[[DATE_COL, CLOSE_COL]].copy()
    df[DATE_COL] = pd.to_datetime(df[DATE_COL])
    df = df.sort_values(DATE_COL).set_index(DATE_COL)

    close = df[CLOSE_COL]
    ret = np.log(close).diff()
    out = pd.DataFrame(index=df.index)

    out["ret_1d"] = ret
    out["abs_ret_1d"] = ret.abs()

    for w in VOL_WINDOWS:
        out[f"vol_{w}d"] = ret.rolling(w).std()
    for w in MEAN_WINDOWS:
        out[f"mean_ret_{w}d"] = ret.rolling(w).mean()

    # Volatility acceleration: short vs long vol (spikes show up here first)
    out["vol_ratio_5_21"] = out["vol_5d"] / out["vol_21d"]

    # Return z-score vs trailing distribution
    mu = ret.rolling(ZSCORE_WINDOW).mean()
    sd = ret.rolling(ZSCORE_WINDOW).std()
    out["ret_zscore"] = (ret - mu) / sd

    # Drawdown from trailing high
    out["drawdown"] = close / close.rolling(DRAWDOWN_WINDOW).max() - 1.0

    # Trailing skew of returns (tail asymmetry)
    out["skew_21d"] = ret.rolling(21).skew()

    return out.replace([np.inf, -np.inf], np.nan)
