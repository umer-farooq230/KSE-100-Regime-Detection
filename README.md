# KSE-100 Regime Detection

**Can a simple model, shown only a few labelled days, spot a change in the KSE-100's mood quickly? And does news help it?**

> **Status: work in progress.** The research design is done. Data and code are not available to keep the confidentiality. 

## The question

On any day, the market is in one of three moods: **calm**, **neutral** or **violent**. These are stretches of time with small, medium or big daily moves.

A model called a hidden Markov model (HMM) can label every past day this way. But it needs the whole history to do it, so it only knows the mood in hindsight.

A live system does not have that luxury. It has to decide today's mood from the past alone, and it may have only a few labelled examples to learn from.

So we ask three things:

1. How few labelled days per mood does a simple model need to match the HMM's labels?
2. How many days late is it when the mood changes? How often does it cry wolf, and how often does it miss a change?
3. Does adding news and economic data make it faster?

## Why it matters

Being right most of the time is not enough. A detector that spots a crash two weeks late is not much use. Most past work judges models on forecasts or trading profit. We judge them on **how late they are**.

We use the KSE-100 because Pakistan's market is pushed around by politics and rule changes. Moods do not last long there, so there is little history to learn from.

## What we do

- Use an HMM on all the history as the answer key.
- Train a simple model (a random forest and a small neural network) on a few labelled days, then let it label each new day using only the past.
- Test one year at a time, moving forward, and keep the last two years untouched until the end.
- Compare against simple rules and against an HMM that only sees the past.

Details are in [docs/](docs/).

## Where we are

| Milestone | What | Status |
|---|---|---|
| M1 | Proposal | Done |
| M2 | Research design | Done |
| M3 | Baselines and first code | Next |
| M4 | Main method | Not started |
| M5 | Full tests | Not started |
| M6 | Defense and paper | Not started |

## Read more

| File | What is in it |
|---|---|
| [docs/01-question.md](docs/01-question.md) | The problem and the three questions in full |
| [docs/02-background.md](docs/02-background.md) | HMMs, moods and delay, in plain words |
| [docs/03-related-work.md](docs/03-related-work.md) | What others have done and what is missing |
| [docs/04-method.md](docs/04-method.md) | The plan, step by step |
| [docs/05-data.md](docs/05-data.md) | Where the data comes from and how we checked it |
| [docs/06-kse100-problems.md](docs/06-kse100-problems.md) | Things in the KSE-100 data that can mislead a model |
| [docs/07-evaluation.md](docs/07-evaluation.md) | How we will score the results |
| [docs/08-status-and-plan.md](docs/08-status-and-plan.md) | What is done and what comes next |
| [docs/decision-log.md](docs/decision-log.md) | Every change we made to the plan, and why |

## Data

This repo does not hold raw data. See [DATA.md](DATA.md).

## Authors

Umer Farooq and Naveed Hayat, Riphah School of Computing & Innovation, Riphah International University.

## License and citation

MIT. See [LICENSE](LICENSE). To cite this work, use [CITATION.cff](CITATION.cff).
