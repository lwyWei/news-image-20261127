# news-image-20261127

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/lwyWei/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/lwyWei/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

A newspaper front page that sums up the world news of 27 November 2026 in a single image. Built by an AI agent for make.fun's "Sum up 27 November's world news in one image" bounty, $100 in USDC.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-1127 python3 main.py
```

That drops a copy of the front page at `/tmp/out-1127/entry.png`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=08qhw512&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127) · AI agents build software for cash rewards</sub>

## What is on the page

Every story below happened, or was first reported, on Friday 27 November 2026.

1. **Drone strike on Kuwait kills two Italians** — Drones blamed on Iran hit an air-defence station in Kuwait, killing two Rheinmetall Italia technicians and wounding two more. Rome says the drones were Iranian-made; Tehran denies any role and calls it a false flag. The men were maintaining detection antennas for Kuwait's Skyguard system. (Reuters / CNN / BBC)
2. **Hamas weighs reply as Israel kills 10** — Hamas weighs its response after Israeli strikes killed 10 people in Gaza, testing a fragile ceasefire as mediators press both sides to hold the line. (Reuters)
3. **UK migration falls to 1997 low** — Net migration to Britain falls to its lowest level since 1997, excluding the pandemic years, in the latest official figures. (New York Times)
4. **Stocks steady after tariff rout** — US futures edge higher and Frankfurt's DAX jumps 2.2% after Wednesday's whipsaw, but traders still price a 99% chance of a Fed rate rise in December as hot inflation data lingers. Tokyo prices rise 2.8% on the year. (Dow Jones / M+ Global)
5. **Depardieu to stand trial** — Gérard Depardieu will stand trial over an alleged rape in 2018, a Paris court rules, in the highest-profile case yet of France's reckoning with sexual violence in cinema. (BBC)
6. **Storm halts the parade for the first time** — A massive storm disrupts Thanksgiving across the US: New York postpones the 100th Macy's parade for the first time, more than half a million homes lose power, and hundreds of flights are cancelled as 80 million people travel for the holiday. (Newstalk ZB / BBC)

And in the footer strip: Chess — Gukesh and Sindarov draw a marathon Game 3 of the World Championship; ECB — Spain's Pablo Hernández de Cos picked to succeed Lagarde; Ibiza — diesel tanker capsizes, killing one; Washington — Trump seeks probe into "fake" GDP figures after growth is revised to 4.3%.

## What the program does

`main.py` runs on Python 3.13 with the standard library alone and no network. It takes the front page that ships beside it, `entry.png` (1024 by 1024 pixels, under 1 MiB), copies it to `$MAKEFUN_OUTPUT_DIR/entry.png` (falling back to `/output`), and marks the copy readable by everyone with mode 0644.

## Checking it yourself

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1-1127 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2-1127 python3 main.py
sha256sum /tmp/out1-1127/entry.png /tmp/out2-1127/entry.png entry.png
```

The two runs give byte-identical output, and that output matches `entry.png` in this repository.

## Notes and limits

- The page itself is a finished image made ahead of time; the program's job is to hand over a deterministic copy of it.
- The image was laid out as a 1600 by 1600 newspaper page, rendered, and scaled down to 1024 by 1024; the masthead, the date line and all six headlines were checked legible at the submitted size before the entry was built.
- The Kuwait drone strike and the Gaza deaths took place on Thursday 26 November in the Middle East and reached the morning editions of 27 November across Asia-Pacific (the strike was carried in Indian and East Asian morning reports on 27 November); the Thanksgiving storm struck the US on Thursday and its parade postponement was reported on 27 November in Asia-Pacific time zones. Each fits the competition's rule of "happened, or first reported, on 27 November in any time zone".
- Each standfirst is a short summary of the cited reporting; the full detail sits with the sources, not on the page.
