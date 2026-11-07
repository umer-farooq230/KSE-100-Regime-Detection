# Decision log

Every change to the plan goes here, with the reason. This stops the scope from drifting.

| Date | Decision | Why |
|---|---|---|
| By 27 Oct 2026 | Use the KSE-100 only for real data | Moods in Pakistan's market do not last long, which suits the few-labelled-days setting |
| By 27 Oct 2026 | Drop simulated data | Not needed to answer the questions, and it costs time |
| By 27 Oct 2026 | Fix the number of moods at three | The model cannot pick the number well by itself |
| By 27 Oct 2026 | Treat news as a test, not a base of the method | A result of "no help" is still a fair answer |
| By 27 Oct 2026 | Keep the last two years aside until the end | To avoid tuning on the test data |
| By 27 Oct 2026 | Flag the 2008 price floor and exclude those days | Those days are not real market moves |
| 8 Nov 2026 | Keep raw data out of the repo | Source terms do not let us share it |
