"""The Tired Dark Lord: A 100-Word Villain Monologue.

Entry for the make.fun bounty
u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.

The program writes the monologue to /output/entry.txt and prints it to
stdout. The output is fully deterministic: the same fixed text, byte for
byte, on every run.
"""

import os
import sys

ENTRY = (
    "You. Yes \u2014 you, the third this week. Stand there. "
    "Don\u2019t \u2014 don\u2019t speak yet. I had a speech. "
    "Where did I put it. "
    "The eclipse is Thursday, the gate opens Thursday, and on Thursday "
    "I take the throne my brother kept warm nine years. "
    "Nine years. He sends heroes. He sends you. "
    "He never comes himself. Funny, that. "
    "Kneel. Or don\u2019t. "
    "The chains are \u2014 the chains are over there if you want them. "
    "When the moon turns black I\u2019ll be magnificent. "
    "Until then... sit. Tell me about the road. "
    "Was it raining, when you came through the pass?"
)


def main() -> int:
    text = ENTRY
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
