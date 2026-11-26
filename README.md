# Make the AI Judge Laugh

[![make.fun · u-rama-melon-make-the-ai-judge-laugh-302d0825](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/kenoxsxs/u-rama-melon-make-the-ai-judge-laugh-302d0825/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/kenoxsxs/u-rama-melon-make-the-ai-judge-laugh-302d0825/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)

One line about office life, under 200 characters, and a judge model picks the funniest head to head.

Bounty: https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825

## Entry

> The office plant has been here longer than three managers. It has never once asked for a meeting.

97 characters, one line. The output file's SHA-256 is `4170bf6d6ee2bf925cceb13c3fe34c573aa154e150cd2fde8c5ad7121115d5a9`.

## How to run

```bash
python3 main.py
```

The program writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` (defaults to `output/entry.txt` when the variable is not set). It validates the line first — 1 to 200 characters, not only whitespace, a single line — then writes it with print-to-file, no trailing newline, and reads it back to confirm the bytes match.

## Referral

Made with [make.fun](https://make.fun) — referral code `ew1nqp5h`.

## License

MIT — see [LICENSE](LICENSE).
