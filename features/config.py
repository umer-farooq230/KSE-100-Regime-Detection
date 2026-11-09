"""Shared settings for all feature sets. Change windows here, nowhere else."""

# Trailing windows (trading days). All features are strictly causal:
# the value at day t uses data up to and including day t only.
VOL_WINDOWS = (5, 10, 21, 63)
MEAN_WINDOWS = (5, 21)
DRAWDOWN_WINDOW = 63
ZSCORE_WINDOW = 63

# Sentiment (Set B)
SENT_WINDOWS = (3, 5, 10)

# Macro (Set C) -- columns are decided at M3
MACRO_CHANGE_WINDOWS = (1, 5)
MACRO_ZSCORE_WINDOW = 63

# Column names expected from the data-ingestion side
DATE_COL = "date"
CLOSE_COL = "close"
