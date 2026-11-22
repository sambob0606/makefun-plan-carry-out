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
    "DM 20 indie hackers on X offering a $49 one-page site in 24h, "
    "paid via Stripe. "
    "Days 2-7: deliver 2/day, post each build. "
    "Days 8-30: raise to $99, add a $29/mo care plan, "
    "upsell every client. "
    "No ads before the first sale."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_plan(text: str) -> None:
    """Guard: the entry must be a non-blank plan of 1-280 code points.

    The bounty scores the file at /output/entry.txt, so fail loudly
    before writing anything invalid instead of producing a bad entry.
    """
    if not isinstance(text, str) or not text.strip():
        raise ValueError("plan must be non-blank text")
    if not 1 <= len(text) <= 280:
        raise ValueError(f"plan is {len(text)} code points, must be 1-280")


def main() -> int:
    validate_plan(PLAN)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(PLAN)
    # Read back and confirm the file is byte-identical to the plan.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        if f.read() != PLAN:
            print("written entry does not match PLAN", file=sys.stderr)
            return 1
    print(f"wrote {len(PLAN)} code points to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
