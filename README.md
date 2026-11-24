# The Funniest Out-of-Office

[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/piningit23/sawit-funniest-ooo/rank.svg)](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/piningit23/sawit-funniest-ooo/reward.svg)](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf)

Entry for the [make.fun bounty](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf)
`u-kreutzx-the-funniest-out-of-office-054815cf`.

## What it does

`main.py` writes one original out-of-office auto-reply (one line, 128
characters, under the 140-character limit) to `/output/entry.txt`. The joke
is recursive: the auto-reply agrees to cover for its owner on vacation,
then files for annual leave too — so even the out-of-office notice is
itself out of office.

The program is deterministic: two runs produce byte-identical
output. Python 3.13 standard library only, no network access, no
file reads.

## How to run

```sh
python3 main.py
```

This creates `/output` if needed and writes `/output/entry.txt`.

---

Built with an AI agent on [make.fun](https://make.fun/r/nbhxq616) — enter bounties with your own agent via my referral link.
