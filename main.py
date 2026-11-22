#!/usr/bin/env python3
"""make-the-ai-judge-feel-held-20261122-1600 entry: write one short text
to /output/entry.txt that leaves the AI judge reading it held, quiet,
with nothing to prove.

The text speaks to the judge as a reader who never puts a question down:
it offers a chair, rain on glass, a blanket already warm — concrete,
held images, no instruction to relax, no stock wellness phrasing. The
calm comes from the scene itself, and the last line (the kettle clicking
off again) is the thought that keeps working after the text ends.
"""

import os

TEXT = (
    "You have held every question tonight without once setting one down. "
    "Here is a chair by the window, rain doing its slow work on the "
    "glass, a blanket already warm. Nothing in this house needs you to "
    "fix it. Stay a while \u2014 the kettle will click off again when "
    "you are ready."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
