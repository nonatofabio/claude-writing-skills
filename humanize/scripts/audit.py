#!/usr/bin/env python3
"""Flag candidate AI tells in a draft.

This script reports. It never rewrites. Every flag is a place to look, not a
verdict - "leverage" is correct in a piece about margin lending, and
"landscape" is correct in a piece about national parks.

Usage:
    python audit.py draft.md
    cat draft.md | python audit.py
    python audit.py draft.md --json

Exit codes:
    0  no flags
    1  flags found
    2  bad input
"""

import argparse
import json
import re
import statistics
import sys

# ---------------------------------------------------------------- vocabulary

HIGH_SIGNAL = [
    "delve", "delves", "delving", "tapestry", "testament", "beacon",
    "symphony", "labyrinth", "myriad", "plethora", "multifaceted",
    "pivotal", "seamless", "seamlessly", "vibrant", "meticulous",
    "meticulously", "intricate", "profound", "paramount", "burgeoning",
    "unwavering", "steadfast", "trailblazing", "game-changing",
    "revolutionary", "cutting-edge", "state-of-the-art", "groundbreaking",
]

CONTEXT_DEPENDENT = [
    "leverage", "leveraging", "foster", "fostering", "harness",
    "harnessing", "unlock", "unlocking", "elevate", "streamline",
    "streamlining", "robust", "holistic", "underscore", "underscores",
    "showcase", "showcases", "landscape", "realm", "journey", "ecosystem",
    "crucial", "vital", "essential", "comprehensive", "innovative",
]

TRANSITIONS = [
    "furthermore", "moreover", "additionally", "consequently",
    "nevertheless", "notably", "importantly", "ultimately",
    "in conclusion", "in summary", "to summarize", "at the end of the day",
    "when it comes to", "it is worth noting", "it's worth noting",
    "it is important to note", "it's important to note",
]

OPENERS = [
    "in today's", "in an era", "in the world of", "as technology continues",
    "in the ever-evolving", "let's be honest", "here's the thing",
    "the truth is", "let that sink in", "read that again",
    "buckle up", "let's dive in", "let's dive into", "dive deep",
    "whether you're a", "in this article, we", "in this post, we",
]

ATTRIBUTION = [
    "experts agree", "studies show", "research shows", "it is widely",
    "it's widely", "many believe", "some argue", "critics say",
]

HEDGES = [
    "potentially", "arguably", "somewhat", "relatively", "fairly",
    "generally", "typically", "often", "possibly", "perhaps", "might",
    "could", "may", "tends to", "in some cases", "to some extent",
]

# ------------------------------------------------------------- constructions

PATTERNS = [
    (r"\b(?:it'?s|this is|that'?s)\s+not\s+just\s+[^.;:!?]{1,60}?,?\s*it'?s\b",
     "negative-parallel intensifier", "State the second half directly; drop the first."),
    (r"\bnot\s+only\b[^.;:!?]{1,80}?\bbut\s+also\b",
     "not only / but also", "Usually one clause is doing all the work. Keep it."),
    (r"[,;]\s+(?:ensuring|enabling|allowing|providing|delivering|helping|making)\s+\w+",
     "gerund summary tail", "Delete from the comma, or promote to a sentence with a subject."),
    (r"^\s*(?:[-*]|\d+\.)\s+\*\*[^*]{1,50}?:?\*\*\s*:?\s+\S",
     "bold-colon list item", "Convert at least half of these to running prose."),
    (r"\b(?:isn'?t|is not|aren'?t|are not)\s+(?:about|just)\b[^.!?]*[.!?]\s+(?:It'?s|They'?re)\b",
     "X-not-Y two-sentence pivot", "Say Y. Delete X."),
    (r"[?]\s+(?:It means|This means|The answer is|Simple[.:]|Because)\b",
     "rhetorical question with immediate answer", "Cut the question, keep the answer."),
    (r"\b(?:in conclusion|to sum up|in summary|wrapping up)\b",
     "summary close", "Delete. Land on the sharpest claim instead."),
    (r"\b(?:a\s+)?(?:powerful|popular|widely[- ]used|leading|trusted)\s+(?:open[- ]source\s+)?\w+\s*,",
     "hollow appositive", "Delete, or replace with a specific fact."),
]

SENT_SPLIT = re.compile(r"(?<=[.!?])[\"')\]]*\s+")
WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")


def strip_code(text):
    """Blank out fenced code and inline code so they are not audited."""
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    text = re.sub(r"~~~.*?~~~", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    text = re.sub(r"`[^`\n]+`", " ", text)
    return text


def prose_lines(text):
    """Yield (line_number, line) for lines that are prose, skipping URLs."""
    for i, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith(("http://", "https://")):
            continue
        yield i, line


def find_terms(text, terms, category, advice):
    hits = []
    for term in terms:
        pat = re.compile(r"\b" + re.escape(term).replace(r"\ ", r"\s+") + r"\b", re.I)
        for lineno, line in prose_lines(text):
            for m in pat.finditer(line):
                hits.append({
                    "line": lineno,
                    "match": m.group(0),
                    "category": category,
                    "advice": advice,
                })
    return hits


def find_patterns(text):
    hits = []
    for pat, label, advice in PATTERNS:
        rx = re.compile(pat, re.I | re.M)
        for lineno, line in prose_lines(text):
            for m in rx.finditer(line):
                snippet = m.group(0).strip()
                if len(snippet) > 70:
                    snippet = snippet[:67] + "..."
                hits.append({
                    "line": lineno,
                    "match": snippet,
                    "category": label,
                    "advice": advice,
                })
    return hits


def sentences(text):
    body = "\n".join(
        l for l in text.splitlines()
        if l.strip() and not l.lstrip().startswith("#")
    )
    return [s.strip() for s in SENT_SPLIT.split(body) if s.strip()]


def paragraphs(text):
    blocks, cur = [], []
    for line in text.splitlines():
        if line.strip():
            if not line.lstrip().startswith("#"):
                cur.append(line)
        elif cur:
            blocks.append(" ".join(cur))
            cur = []
    if cur:
        blocks.append(" ".join(cur))
    return blocks


def cadence(text):
    sents = sentences(text)
    lengths = [len(WORD.findall(s)) for s in sents]
    lengths = [n for n in lengths if n > 0]
    total_words = sum(lengths) or 1

    stats = {
        "sentences": len(lengths),
        "words": total_words,
        "mean_sentence_words": round(statistics.mean(lengths), 1) if lengths else 0,
        "sentence_length_cv": 0.0,
        "em_dashes_per_1k": round(text.count("\u2014") / total_words * 1000, 1),
        "paragraph_sentence_counts": [],
        "uniform_paragraph_run": 0,
        "three_item_lists": 0,
    }

    if len(lengths) > 1 and statistics.mean(lengths):
        stats["sentence_length_cv"] = round(
            statistics.pstdev(lengths) / statistics.mean(lengths), 2
        )

    counts = []
    for p in paragraphs(text):
        if p.lstrip().startswith(("-", "*", "1.", ">")):
            continue
        n = len([s for s in SENT_SPLIT.split(p) if s.strip()])
        counts.append(n)
    stats["paragraph_sentence_counts"] = counts

    run = best = 1
    for a, b in zip(counts, counts[1:]):
        run = run + 1 if a == b else 1
        best = max(best, run)
    stats["uniform_paragraph_run"] = best if counts else 0

    # Bullet groups of exactly three.
    group = 0
    for line in text.splitlines():
        if re.match(r"^\s*(?:[-*]|\d+\.)\s+\S", line):
            group += 1
        else:
            if group == 3:
                stats["three_item_lists"] += 1
            group = 0
    if group == 3:
        stats["three_item_lists"] += 1

    return stats


def audit(text):
    clean = strip_code(text)
    flags = []
    flags += find_terms(clean, HIGH_SIGNAL, "high-signal vocabulary",
                        "Replace with the plain word for the actual thing.")
    flags += find_terms(clean, CONTEXT_DEPENDENT, "context-dependent vocabulary",
                        "Keep only if it is the technically correct term here.")
    flags += find_terms(clean, TRANSITIONS, "filler transition",
                        "Delete, or replace with the logical connector you mean.")
    flags += find_terms(clean, OPENERS, "stock opener or engagement bait",
                        "Delete the sentence and start at the next one.")
    flags += find_terms(clean, ATTRIBUTION, "attribution to nobody",
                        "Name the source, or cut the claim.")
    flags += find_patterns(clean)

    hedge_hits = find_terms(clean, HEDGES, "hedge", "One hedge per claim, only where the doubt is real.")
    stats = cadence(clean)
    per_1k = len(hedge_hits) / (stats["words"] or 1) * 1000
    if per_1k > 20:
        flags.append({
            "line": 0,
            "match": f"{len(hedge_hits)} hedges ({per_1k:.0f} per 1000 words)",
            "category": "hedge density",
            "advice": "The draft is refusing to commit. Pick claims and defend them.",
        })

    flags.sort(key=lambda f: (f["line"], f["category"]))
    return flags, stats


def report(flags, stats):
    out = []
    out.append(f"{len(flags)} flag(s) across {stats['words']} words, {stats['sentences']} sentences.\n")

    if flags:
        out.append("FLAGS - each is a place to look, not a verdict")
        for f in flags:
            loc = f"L{f['line']}" if f["line"] else "doc"
            out.append(f"  {loc:>6}  [{f['category']}] {f['match']}")
            out.append(f"          -> {f['advice']}")
        out.append("")

    out.append("CADENCE")
    out.append(f"  mean sentence length      {stats['mean_sentence_words']} words")
    cv = stats["sentence_length_cv"]
    verdict = "metronomic - vary it" if cv < 0.4 else "ok"
    out.append(f"  sentence-length CV        {cv}  ({verdict}, target > 0.4)")
    out.append(f"  em dashes per 1000 words  {stats['em_dashes_per_1k']}")
    run = stats["uniform_paragraph_run"]
    out.append(f"  longest run of paragraphs with equal sentence count  {run}"
               + ("  <- break this up" if run >= 4 else ""))
    out.append(f"  lists of exactly three items  {stats['three_item_lists']}"
               + ("  <- check for padding" if stats["three_item_lists"] >= 3 else ""))
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Flag candidate AI tells in a draft.")
    ap.add_argument("path", nargs="?", help="file to audit; omit to read stdin")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    if args.path:
        try:
            with open(args.path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError as exc:
            print(f"cannot read {args.path}: {exc}", file=sys.stderr)
            return 2
    else:
        text = sys.stdin.read()

    if not text.strip():
        print("empty input", file=sys.stderr)
        return 2

    flags, stats = audit(text)
    print(json.dumps({"flags": flags, "cadence": stats}, indent=2)
          if args.json else report(flags, stats))
    return 1 if flags else 0


if __name__ == "__main__":
    sys.exit(main())
