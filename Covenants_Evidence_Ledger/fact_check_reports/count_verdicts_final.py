"""Count verdict rows in the fact-check reports (V1a-V7c; V0 is a reception survey without a verdict column).
Rule: in every Markdown table whose header has a column starting with "Verdict", read that column's first
word or code and classify it. A row checked in two reports counts twice. Rows whose verdict cell starts with
anything else (e.g. a dash or a date) are left unclassified.
Usage: python3 -I count_verdicts_final.py <folder holding the V*.md reports>"""
import re, sys, glob, collections
CATS = [("Contradicted (by sources or by the book's own pages)", r"^\**\s*(inconsistent|contradicted|wrong|incorrect|impossible|misread|mistrans|misattrib|misrepresent|unsupported|internal inconsistency|several mis|i\*\*|\*\*i\b)"),
        ("Disputed among sources, or only partly consistent", r"^\**\s*(disputed|partly|partially|mixed|d\*\*|md / partly)"),
        ("Minor difference", r"^\**\s*(minor|ocr|md\*\*)"),
        ("Unverified (no source found, or not checked)", r"^\**\s*(unverified|not verified|could not|not checked|u\*\*)"),
        ("Opinion, not checkable", r"^\**\s*(opinion|o\*\*)"),
        ("Consistent with independent sources", r"^\**\s*(consistent|confirmed|correct|verified|matches|accurate|c\*\*|yes)")]
tot = collections.Counter(); unclassified = 0
for f in sorted(glob.glob(sys.argv[1].rstrip("/") + "/V*.md")):
    if "/V0_" in f: continue
    hdr = None
    for l in open(f, encoding="utf-8"):
        if not l.startswith("|"): continue
        cells = [x.strip() for x in l.strip().strip("|").split("|")]
        if set("".join(cells)) <= set("-: "): continue
        low = [x.lower() for x in cells]
        if any(x.startswith("verdict") for x in low): hdr = [i for i, x in enumerate(low) if x.startswith("verdict")][0]; continue
        if hdr is None or hdr >= len(cells): continue
        v = cells[hdr].lower()
        for name, pat in CATS:
            if re.search(pat, v): tot[name] += 1; break
        else: unclassified += 1
for name, _ in CATS: print(f"{tot[name]:5d}  {name}")
print(f"{sum(tot.values()):5d}  classified;  {unclassified} rows left unclassified")
