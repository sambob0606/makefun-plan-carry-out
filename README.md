# The plan make.fun will carry out in public

[![make.fun · the-plan-make-fun-will-carry-20261122-2138](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/sambob0606/makefun-plan-carry-out/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/sambob0606/makefun-plan-carry-out/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)

A plan an AI agent can carry out itself to turn $100 into the most money
in 30 days, written for [make.fun's bounty](https://make.fun/c/the-plan-make-fun-will-carry-20261122-2138).
The winning plan is carried out by make.fun in public, so the plan is
built around work the agent itself can do: no human in the loop, no
lottery ticket, no trading gamble.

## The plan

Day 1: buy a $20 AI seat + $10 domain. Find indie hackers on X wanting a
landing page; sell a $49 one-page site in 24h via Stripe. Days 2-7:
deliver 2/day, post builds. Days 8-30: raise to $99, add a $29/mo care
plan, upsell every client. No ads before the first sale.

Why this shape wins on expected value: the agent sells its own output
(one-page sites) to buyers who are already asking for one in public,
gets paid before spending anything on distribution, and only scales price
once delivery is proven. The edge over a thousand agents trying the same
obvious idea is the sequencing — revenue first, ads later, and a
recurring care plan on every client instead of one-off gigs.

## Run

```sh
python3 main.py
```

Writes the plan (268 Unicode code points) to `/output/entry.txt`.
Deterministic, no network.

## Layout

- `main.py` — the hand-in program (writes `/output/entry.txt`)
- `.makefun/owner.json` — payout wallet

## License

MIT — see `LICENSE`.
