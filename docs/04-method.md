# Method

This is the plan. It is not built yet. Code starts at Milestone 3.

## Steps

1. **Keep two years aside.** The last two years of data stay untouched until every setting is fixed. They are used once, at the end.
2. **Clean the data.** Use log returns and count days by trading day, not calendar day. Remove the 2008 price-floor days. Flag days that hit the daily price limit. See [the problems with the data](06-kse100-problems.md).
3. **Test the basic idea.** Fit the same three-mood HMM on the KSE-100 and on a calmer index. Compare how long each mood lasts. This checks that the KSE-100 really does switch faster.
4. **Build features.** Make a small set of features from returns and volatility, using only past data. Later, add news tone and economic data.
5. **Test one year at a time.** For each year in turn:
   - Fit the HMM on data up to a cutoff date and name the moods by size of move.
   - Pick a few labelled days for each mood.
   - Train the model on them.
   - Label every day of the next year using only the past.
6. **Score it.** Measure delay, false alarms and misses. Compare with the answer key and with the baselines.
7. **Repeat.** Vary the number of labelled days, the feature set and the random seed (10 seeds).
8. **Report.** Give delay at a fixed false-alarm rate. Then run once on the two years kept aside.

## Models

- A random forest
- A small neural network

## Baselines

- **B1.** A rolling volatility rule: call the day violent when recent volatility passes a set level.
- **B2a.** An HMM that sees only the past, refitted as time goes on, using all data so far.
- **B2b.** The same, but using only the most recent stretch of data.

## Three feature sets

- **Set A.** Return and volatility features only.
- **Set B.** Set A plus news tone.
- **Set C.** Set B plus economic data. To be set at Milestone 3.

Comparing A, B and C answers question 3. The exact features and settings are kept in the private project notes until the paper is out.
