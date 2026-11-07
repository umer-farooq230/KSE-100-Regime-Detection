# Data

## Prices

The main series is **6,127 daily KSE-100 closes**, from 2002 to 13 October 2026.

| Source | Covers | Use |
|---|---|---|
| Public CSV (PSXpert, on GitHub) | 2002 to 13 Oct 2026 | Main series. Where it came from is not documented. |
| Karandaaz portal | 2010 to 23 Oct 2026 | Second source for checking, and fills 14 to 23 Oct. Personal, non-commercial use only. |
| IMS Peshawar Excel file | About 1997 to 2016 | Not yet opened. May give 2001 and a check for 2002 to 2009. |
| Official PSX portal | Not yet tested | To confirm how the index is defined. |

## Checks done on the main series

- No duplicate dates.
- No weekend rows.
- No mismatch between the stored return and the return we work out ourselves.
- All 10 closes from 2026 that we checked match news reports to within 0.01 points.
- 33 gaps longer than 5 days. We flag them. We never fill them in.

## Cleaning steps

1. Sort by date and drop duplicates.
2. Check returns against our own calculation.
3. Check against the other sources.
4. Flag gaps. Never fill them.
5. Flag the 2008 price-floor window.
6. Build features from past data only, and split the data by time.

## News

For the tone test (Sets B and C) we need dated Pakistani news. We are checking which sources cover which years. News that comes out after the market closes counts for the next trading day only.

We will check the tone scorer on a sample of Pakistani headlines that we label by hand.

## What is not in this repo

No raw price files and no news text. See [DATA.md](../DATA.md).
