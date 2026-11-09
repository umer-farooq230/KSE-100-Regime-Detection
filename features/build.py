"""Build all feature sets and save them as CSVs.

Usage:
    python build.py --prices data/kse100.csv \
                    [--sentiment data/sentiment.csv] \
                    [--macro data/macro.csv] \
                    [--out features_out]

Sets B and C are built only if their input files are given.
Rows with NaNs (indicator warm-up) are dropped, and A/B/C are cut to the SAME
date range so any performance difference comes from the features, not the sample.
"""
import argparse
from pathlib import Path

import pandas as pd

import set_a_returns
import set_b_sentiment
import set_c_macro
from config import DATE_COL


def check_causal(builder, prices, n_checks=5, **kwargs):
    """Look-ahead test: features at day t must not change if future days are removed."""
    full = builder(prices, **kwargs)
    idx = range(len(prices) // 2, len(prices) - 1, max(1, len(prices) // (2 * n_checks)))
    for i in idx:
        trunc = builder(prices.iloc[: i + 1], **kwargs)
        a, b = full.iloc[len(trunc) - 1], trunc.iloc[-1]
        if not ((a - b).abs().fillna(0) < 1e-9).all():
            raise AssertionError(f"Look-ahead detected at row {i} in {builder.__module__}")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prices", required=True)
    ap.add_argument("--sentiment")
    ap.add_argument("--macro")
    ap.add_argument("--out", default="features_out")
    ap.add_argument("--skip-check", action="store_true")
    args = ap.parse_args()

    prices = pd.read_csv(args.prices)
    sets = {"A": set_a_returns.build(prices)}
    if not args.skip_check:
        check_causal(set_a_returns.build, prices)

    if args.sentiment:
        sent = pd.read_csv(args.sentiment)
        sets["B"] = set_b_sentiment.build(prices, sent)
        if args.macro:
            macro = pd.read_csv(args.macro)
            sets["C"] = set_c_macro.build(prices, sent, macro)

    # Common sample: drop warm-up NaNs, then intersect dates across sets
    clean = {k: v.dropna() for k, v in sets.items()}
    common = None
    for v in clean.values():
        common = v.index if common is None else common.intersection(v.index)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for k, v in clean.items():
        v.loc[common].to_csv(out / f"features_set_{k}.csv", index_label=DATE_COL)
        print(f"Set {k}: {v.loc[common].shape[1]} features, {len(common)} rows "
              f"({common.min().date()} to {common.max().date()})")


if __name__ == "__main__":
    main()
