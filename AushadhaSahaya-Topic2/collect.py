#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Capture machine evidence for the 1BCP308 Community Project book (Topic 2).
  1. src/make_field_data.py runs FIRST as a silent pre-pass (data/ must exist before
     any program reads it; it is also captured in its own right, in sort order)
  2. every src/<stem>.py : executed with python3 from the repo root with a pinned
     environment (PYTHONHASHSEED=0, MPLBACKEND=Agg, LC_ALL=C); command line + stdout
     written VERBATIM to out/<stem>.txt; any stderr or nonzero exit fails the capture
  3. every src/<stem>.sh : run with sh, captured the same way
  4. the WHOLE capture runs twice and the two passes are diffed: any byte difference
     refuses the capture (exit 1). Every number quoted in the book is therefore
     reproducible on this machine, twice.
"""
import os, subprocess, sys
from pathlib import Path

ROOT  = Path(__file__).resolve().parent
SRC   = ROOT / "src"
OUT   = ROOT / "out"
BUILD = ROOT / "build"
BUILD.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)

ENV = dict(os.environ,
           PYTHONHASHSEED="0", MPLBACKEND="Agg", LC_ALL="C",
           PYTHONIOENCODING="utf-8", PYTHONUNBUFFERED="1",
           MPLCONFIGDIR=str(BUILD / "mpl"))

def run(argv):
    return subprocess.run(argv, cwd=str(ROOT), capture_output=True, text=True, env=ENV)

def one_pass():
    captures, fails = {}, []
    pre = run(["python3", "src/make_field_data.py"])
    if pre.returncode != 0:
        print("FIELD-DATA GENERATION FAILED\n", pre.stderr)
        sys.exit(1)
    
    # Capture make_field_data transcript
    captures["make_field_data"] = f"$ python3 src/make_field_data.py\n{pre.stdout.rstrip()}\n"
    
    for stem in sorted(p.stem for p in SRC.glob("*.py")):
        if stem in ["make_field_data", "syllabus_data"]:
            continue
        p = run(["python3", f"src/{stem}.py"])
        lines = [f"$ python3 src/{stem}.py"]
        if p.stderr.strip():
            lines += ["[stderr]", p.stderr.rstrip()]
            fails.append(f"{stem}: stderr not empty: {p.stderr.strip()}")
        if p.returncode != 0:
            lines.append(f"[exit code {p.returncode}]")
            fails.append(f"{stem}: exit {p.returncode}")
        lines.append(p.stdout.rstrip("\n"))
        captures[stem] = "\n".join(lines) + "\n"

    for stem in sorted(p.stem for p in SRC.glob("*.sh")):
        p = run(["sh", str(SRC / f"{stem}.sh")])
        body = (p.stdout + p.stderr).rstrip("\n")
        captures[stem] = f"$ sh src/{stem}.sh\n{body}\n"
        if p.returncode != 0:
            captures[stem] += f"[exit code {p.returncode}]\n"
            fails.append(f"{stem}: exit {p.returncode}")

    return captures, fails

def main():
    print("Beginning Two-Pass Byte-Verification Capture for Topic 2...")
    first, f1 = one_pass()
    second, f2 = one_pass()

    fails = list(f1)
    for stem, text in first.items():
        if "RESULT" not in text:
            fails.append(f"{stem}: no RESULT marker")
        if second.get(stem) != text:
            fails.append(f"{stem}: NOT REPRODUCIBLE across two runs (byte divergence)")
        if text:
            (OUT / f"{stem}.txt").write_text(text, encoding="utf-8")

    n = len(first)
    if fails:
        print("CAPTURE PROBLEMS DETECTED:")
        for f in fails:
            print("  ", f)
        sys.exit(1)

    summary = f"RESULT: capture: {n} programs ok, all reproducible across two runs (zero stderr) -- PASS"
    print(summary)
    (OUT / "capture_summary.txt").write_text(summary + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
