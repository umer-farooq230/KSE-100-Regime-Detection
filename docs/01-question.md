# The question

## The problem

An HMM can label every day of KSE-100 history as calm, neutral or violent. It does this by looking at the whole history at once, so each label is made with hindsight.

A live system cannot do that. On each new day it must decide the mood using only the days before it. It also has very few labelled days to learn from. And we care about more than accuracy. We care about **how many days late** it is.

## Research questions

**Question 1.** How few labelled days per mood does a simple model need to match the HMM's labels? We try a small number of days (from 5 up to a few dozen) and see where more days stop helping.

**Question 2.** When the mood changes, how many days pass before the model notices? How often does it raise an alarm when nothing changed? How often does it miss a change? We compare this with simple rules.

**Question 3.** Does adding news and economic data help the model notice sooner than prices alone?

## What we will build

1. A checked KSE-100 dataset.
2. A model that labels each day using only the past.
3. A comparison against simple rules and an HMM that only sees the past.
4. A test of whether news and economic data help.

## What is in scope

- KSE-100 daily closing prices
- Three moods: calm, neutral, violent

## What is out of scope

- Trading strategies and profit
- Intraday data
- Simulated data. We planned this once and dropped it. See the [decision log](decision-log.md).

## A result of "no help" is still a result

If news does not help, we will say so. That is a fair answer to question 3. The plan accepts four outcomes: news helps, helps only in some periods, gives no gain, or makes things worse.
