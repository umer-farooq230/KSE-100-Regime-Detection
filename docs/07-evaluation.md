# Evaluation

## What we measure

- **Delay.** Days from a real change of mood (per the answer key) to the first alarm.
- **False alarms.** Alarms when there was no change.
- **Misses.** Changes with no alarm in time.
- **Scores for each mood.** Calm, neutral and violent, one by one.

The main number is **delay at a fixed false-alarm rate**. Fixing the false-alarm rate stops a model looking fast by raising alarms all the time.

## What we compare against

- A rolling volatility rule
- An HMM that sees only the past (two versions)
- The answer key itself, as a reference

## How we keep the test fair

- We split the data by time only. Nothing from the future is used to train or to build features.
- News that comes out after the market closes counts for the next trading day only.
- We keep the last two years aside until the very end.
- We repeat each test with 10 random seeds.

## Checks on our answer key

The answer key is a guess. So we check it:

- Do the labels stay the same when we refit the HMM?
- Do two different HMM fits agree?
- Do the labels line up with a calendar of political events?
- Do results change if we require a mood to last 3, 5 or 10 days before we call it a change?
- Do results change with and without June to August 2008?
- If the neutral mood has very few days, we fall back to two moods.

## Ethics

- We use public price data and news we are allowed to use.
- The Karandaaz data is for personal, non-commercial use only.
- We check the tone scorer on Pakistani headlines that we label by hand.
- No personal data is used.
- We disclose where AI tools were used in the project documents.
- Big changes to the plan need the supervisor's approval.
