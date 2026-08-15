#!/usr/bin/env python3
"""Word-count method for the GPTedit-10 revision (see METRICS.md).

Strips comments, LaTeX commands, and environment markers over the compiled
body of the .tex file; counts whitespace-separated tokens containing at least
one alphanumeric character.  main = \\begin{document} to \\appendix,
appendix = \\appendix to \\end{document}.
"""
import re
import sys


def strip_tex(text: str) -> str:
    # remove comments (unescaped %)
    text = re.sub(r"(?<!\\)%.*", "", text)
    # remove environment markers
    text = re.sub(r"\\(begin|end)\{[^}]*\}(\[[^\]]*\])?", " ", text)
    # remove command tokens (keep braced arguments' text)
    text = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", text)
    # remove remaining escapes and braces/brackets
    text = re.sub(r"[\\{}\[\]]", " ", text)
    return text


def count_words(text: str) -> int:
    return sum(1 for tok in text.split() if re.search(r"[A-Za-z0-9]", tok))


def main(path: str) -> None:
    src = open(path, encoding="utf-8").read()
    body = src.split(r"\begin{document}", 1)[1]
    body = body.rsplit(r"\end{document}", 1)[0]
    if r"\appendix" in body:
        main_part, app_part = body.split(r"\appendix", 1)
    else:
        main_part, app_part = body, ""
    m = count_words(strip_tex(main_part))
    a = count_words(strip_tex(app_part))
    print(f"main {m}  appendix {a}  total {m + a}")


if __name__ == "__main__":
    main(sys.argv[1])
