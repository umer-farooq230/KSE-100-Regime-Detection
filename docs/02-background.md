# Background

## Moods

A market does not move the same way all the time. Some stretches are quiet, with small daily moves. Others are wild, with big moves in both directions. We call these stretches **moods**. We use three: calm (smallest moves), neutral (the middle) and violent (biggest moves).

The mood is hidden. We never see it. We only see the daily price changes and have to work out the mood from them.

## The HMM

A hidden Markov model (HMM) is built for this. It assumes:

- The market is always in exactly one mood.
- Each mood has its own typical size of daily move.
- Each day, the market either stays in its mood or jumps to another. Moods that last have a high chance of staying.

The model learns these numbers from the data by itself. We do not give it labels.

## Looking back and looking forward

An HMM can label a day in two ways.

- **With all the history.** It sees days before and after, so the labels are cleaner. We use these as our answer key. They are only possible in hindsight.
- **With the past only.** It sees days up to today. This is what a live system can do. We use it as one of our comparisons.

## Learning from a few labelled days

Our model is given a small number of labelled days for each mood. It learns what each mood looks like from those, then labels each new day, using only the past. This is the "few labelled days" setting.

## Delay

Delay is the number of days between a real change of mood (as shown by the answer key) and the day our model first says so. We measure it at a fixed rate of false alarms, so that a model cannot look fast just by raising alarms all the time.

## Limits we accept

- The number of moods is not something the model can decide well by itself. We fix it at three before any testing.
- The answer key is a guess, not the truth. We check how steady it is, and we check it against a second method (a jump model, from Shu et al., 2024).
