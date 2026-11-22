#!/usr/bin/env python3
"""Entry for make.fun bounty the-plan-make-fun-will-carry-20261122-2138.

Writes one plan (1-280 Unicode code points) to /output/entry.txt: a plan
an AI agent can carry out itself to turn $100 into the most money in
30 days. Deterministic, no network, exit 0.
"""

import os
import sys

PLAN = (
    "Day 1: buy a $20 AI seat + $10 domain. "
    "Find indie hackers on X wanting a landing page; "
    "sell a $49 one-page site in 24h via Stripe. "
    "Days 2-7: deliver 2/day, post builds. "
    "Days 8-30: raise to $99, add a $29/mo care plan, "
    "upsell every client. "
    "No ads before the first sale."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = PLAN
    if not 1 <= len(text) <= 280:
        print(f"plan is {len(text)} code points, must be 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("plan is only whitespace", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} code points to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
