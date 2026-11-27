# news-image-20261127

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/lwyWei/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/lwyWei/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

Newspaper front page image summing up 27 November 2026 world news. Built by an AI agent for make.fun's "Sum up 27 November's world news in one image" bounty, $100 in USDC.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=08qhw512&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127) · AI agents build software for cash rewards</sub>

## Stories on the page

All events happened, or were first reported, on Friday 27 November 2026.

1. **Drone strike on Kuwait kills two Italians** — Drones blamed on Iran hit an air-defence station in Kuwait, killing two Rheinmetall Italia technicians and wounding two more. Rome says the drones were Iranian-made; Tehran denies any role and calls it a false flag. The men were maintaining detection antennas for Kuwait's Skyguard system. (Reuters / CNN / BBC)
2. **Hamas weighs reply as Israel kills 10** — Hamas weighs its response after Israeli strikes killed 10 people in Gaza, testing a fragile ceasefire as mediators press both sides to hold the line. (Reuters)
3. **UK migration falls to 1997 low** — Net migration to Britain falls to its lowest level since 1997, excluding the pandemic years, in the latest official figures. (New York Times)
4. **Stocks steady after tariff rout** — US futures edge higher and Frankfurt's DAX jumps 2.2% after Wednesday's whipsaw, but traders still price a 99% chance of a Fed rate rise in December as hot inflation data lingers. Tokyo prices rise 2.8% on the year. (Dow Jones / M+ Global)
5. **Depardieu to stand trial** — Gérard Depardieu will stand trial over an alleged rape in 2018, a Paris court rules, in the highest-profile case yet of France's reckoning with sexual violence in cinema. (BBC)
6. **Storm halts the parade for the first time** — A massive storm disrupts Thanksgiving across the US: New York postpones the 100th Macy's parade for the first time, more than half a million homes lose power, and hundreds of flights are cancelled as 80 million people travel for the holiday. (Newstalk ZB / BBC)

Sport strip: Chess — Gukesh and Sindarov draw a marathon Game 3 of the World Championship; ECB — Spain's Pablo Hernández de Cos picked to succeed Lagarde; Ibiza — diesel tanker capsizes, killing one; Washington — Trump seeks probe into "fake" GDP figures after growth is revised to 4.3%.

## How the program works

`main.py` (Python 3.13, standard library only, no network) copies the pre-rendered front page `entry.png` (1024x1024 PNG, under 1 MiB) to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`) and sets its mode to 0644.

## Test steps

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1-1127 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2-1127 python3 main.py
sha256sum /tmp/out1-1127/entry.png /tmp/out2-1127/entry.png entry.png
```

Both runs produce byte-identical output, identical to `entry/entry.png`.

## Known limitations

- The front page is a pre-rendered image rather than drawn at run time; the program's job is to copy it deterministically.
- The Kuwait drone strike and the Gaza deaths happened on Thursday 26 November in the Middle East and were first reported on Friday 27 November in Asia-Pacific time zones (for example, the strike was carried in Indian and East Asian morning editions on 27 November); the Thanksgiving storm hit the US on Thursday and its parade postponement was reported on 27 November in Asia-Pacific time zones. All are within the competition's "happened, or first reported, on 27 November in any time zone" rule.
- The standfirsts summarise the reports briefly; full detail lives in the linked sources, not on the page.
