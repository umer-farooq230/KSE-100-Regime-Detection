# Things in the KSE-100 data that can mislead a model

These are facts about how Pakistan's market has worked. If we ignore them, the model learns the wrong thing.

## 1. The 2008 price floor

From 28 August to 15 December 2008, prices were held at a floor. Those days are not real market moves. We found 29 days with near-zero returns. We flag them and leave them out of both fitting and scoring.

## 2. Uneven circuit breakers

From 23 June to 27 August 2008, the daily lower limit was cut to 1% while the upper limit was raised to 10%. Falls were capped and rises were not. We flag this window and report results with it and without it.

## 3. Daily price limits

On days when the index hits its limit, a big piece of news can only move it so far. The move gets squeezed. We flag days near the limit and report results with them flagged.

## 4. Holidays and gaps

Days off and gaps in the record mean calendar time and trading time are not the same. We count by trading day. Gaps are flagged and never filled in.

## Big moves we see in the data

Some of the biggest daily moves line up with known events:

| Date | Move |
|---|---|
| May 2002 | -7.7% |
| March 2020 | -6.8% |
| May 2025 | +9.0% |
| March 2026 | -7.3% |

These links are loose. We have not shown that the events caused the moves, and the event labels are not final.
