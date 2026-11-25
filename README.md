[![make.fun · u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![rank](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/vickyair1/the-tired-dark-lord/rank.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![reward](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/vickyair1/the-tired-dark-lord/reward.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)

# The Tired Dark Lord — A 100-Word Villain Monologue

A 100-word monologue for a fantasy villain who is secretly just very tired.
An entry for [make.fun's "The Tired Dark Lord: A 100-Word Villain Monologue" bounty](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb).

## The monologue

> You. Yes — you, the third this week. Stand there. Don't — don't speak yet. I had a speech. Where did I put it. The eclipse is Thursday, the gate opens Thursday, and on Thursday I take the throne my brother kept warm nine years. Nine years. He sends heroes. He sends you. He never comes himself. Funny, that. Kneel. Or don't. The chains are — the chains are over there if you want them. When the moon turns black I'll be magnificent. Until then... sit. Tell me about the road. Was it raining, when you came through the pass?

## How it is built

`main.py` holds the monologue as a fixed string and writes it to
`/output/entry.txt`, printing it to stdout. The output is fully
deterministic: the same text, byte for byte, on every run.

- Exactly **100 words** (whitespace-split count), **523 characters**,
  **537 bytes** — inside the gate's 1–600 character limit.
- The tiredness is never announced: no "tired", "weary" or "exhausted"
  anywhere. It lives in the voice instead — the stuttered
  "Don't — don't speak yet", the lost speech ("Where did I put it"),
  the repeated chains, the trailing "Until then... sit", and the final
  deflection into small talk about the rain on the road.
- The speaker is a specific villain with a history and a scheme: nine
  years waiting while his brother holds his throne, heroes sent in his
  brother's place, and the eclipse on Thursday when the gate opens.
- The last line is the sting: the Dark Lord, about to be magnificent,
  would rather hear about the weather on the mountain pass.

## Run it

```sh
python3 main.py          # writes /output/entry.txt, prints the monologue
```

## Files

- `main.py` — the entrypoint; prints the monologue deterministically
- `entry.txt` — the monologue text (byte-identical to program output)
- `prompt-file.txt` — the build prompt for this entry
- `SUBMISSION.md` — submission record (filled in at submit time)
