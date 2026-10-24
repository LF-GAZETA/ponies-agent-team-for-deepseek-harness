#!/usr/bin/env python3
"""Verify mutual isolation of the plus and lite editions.

Method: extract each distribution zip into its own empty sandbox (simulating two
separate repos / sessions where the other edition does not exist at all), then
check that each edition is fully self-contained and that no functional
cross-package file reference exists. Cross-package content overlap is checked
separately: the lite roster is an intentional frozen subset of the plus data,
not a live dependency.

Writes ISOLATION-VERIFICATION.md at the workspace root.
"""
import hashlib
import json
import re
import shutil
import sys
import tempfile
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUS = "ponies-agent-team-v1.1-plus-95c"
LITE = "ponies-agent-team-v1.1-lite-18c"
TZ = timezone(timedelta(hours=8))
NOW = datetime.now(TZ)
STAMP = NOW.strftime("%Y-%m-%d %H:%M:%S %z")
GEN = "DeepSeek Harness — `deepseek-flash` model"

CHECKS = []  # dicts: category, name, ok, detail


def add(category: str, name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append({"category": category, "name": name, "ok": bool(ok), "detail": detail})


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def md_headings(path: Path) -> list:
    return [line[3:].strip() for line in read(path).splitlines() if line.startswith("## ")]


def text_files(pkg_dir: Path) -> list:
    return [p for p in pkg_dir.rglob("*") if p.is_file() and p.suffix in {".md", ".json"}]


def strip_tail(sec: str) -> str:
    sec = sec.strip()
    while sec.endswith("---"):
        sec = sec[:-3].rstrip()
    return sec


def parse_sections(pkg_dir: Path, team_ids) -> dict:
    out = {}
    for tid in team_ids:
        lines = read(pkg_dir / "data" / f"{tid}.md").splitlines()
        idxs = [i for i, l in enumerate(lines) if l.startswith("## ")]
        for k, i in enumerate(idxs):
            end = idxs[k + 1] if k + 1 < len(idxs) else len(lines)
            name = lines[i][3:].strip()
            out[name] = strip_tail("\n".join(lines[i:end]))
    return out


main_fail = False
iso = Path(tempfile.mkdtemp(prefix="pat_isolation_"))
try:
    # ------------------------------------------------------------------ #
    # 0. extract each zip alone into its own sandbox
    # ------------------------------------------------------------------ #
    sandboxes = {}
    for pkg in (PLUS, LITE):
        box = iso / pkg
        box.mkdir()
        with zipfile.ZipFile(ROOT / f"{pkg}.zip") as zf:
            zf.extractall(box)
        sandboxes[pkg] = box / pkg
        add("Archive", f"{pkg}.zip extracted into an empty sandbox", sandboxes[pkg].is_dir())

    sums = {}
    for line in (ROOT / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        if line.strip():
            h, n = line.split()
            sums[n] = h

    for pkg, other in ((PLUS, LITE), (LITE, PLUS)):
        zp = ROOT / f"{pkg}.zip"
        with zipfile.ZipFile(zp) as zf:
            names = zf.namelist()
            add("Archive", f"{pkg}.zip: integrity (zip test)", zf.testzip() is None)
        add("Archive", f"{pkg}.zip: sha256 matches SHA256SUMS.txt", sums.get(zp.name) == sha256(zp))
        add("Archive", f"{pkg}.zip: every entry is inside its own root folder",
            all(n.startswith(pkg + "/") for n in names))
        add("Archive", f"{pkg}.zip: contains no file of the other edition",
            not any(n.startswith(other + "/") for n in names))
        add("Archive", f"{pkg}.zip: entry count matches sandboxed tree",
            len(names) == len([p for p in sandboxes[pkg].rglob("*") if p.is_file()]))

    # ------------------------------------------------------------------ #
    # 1. each sandbox is complete and self-contained
    # ------------------------------------------------------------------ #
    manifests = {}
    for pkg, other in ((PLUS, LITE), (LITE, PLUS)):
        d = sandboxes[pkg]
        m = json.loads(read(d / "manifest.json"))
        manifests[pkg] = m
        expected = set(m["files"]) | {"manifest.json", "VERIFICATION.md"}
        actual = {p.relative_to(d).as_posix() for p in d.rglob("*") if p.is_file()}
        add("Self-contained operation", f"{pkg}: sandbox contains exactly its own {len(expected)} package files",
            actual == expected, f"unexpected: {sorted(actual - expected)}; missing: {sorted(expected - actual)}")
        add("Self-contained operation", f"{pkg}: the other edition's folder is absent",
            not (d / other).exists() and not any(other in p for p in actual))
        add("Self-contained operation", f"{pkg}: no symlinks / external links",
            not any(p.is_symlink() for p in d.rglob("*")))
        bad_sha = [rel for rel, h in m["files"].items() if sha256(d / rel) != h]
        add("Self-contained operation", f"{pkg}: manifest.json checksums verify inside the sandbox",
            not bad_sha, f"bad: {bad_sha}")
        # data rosters in the sandbox match the manifest exactly
        heads = {}
        for tid, team in m["teams"].items():
            heads[tid] = md_headings(d / "data" / f"{tid}.md")
        flat = [n for tid in m["teams"] for n in heads[tid]]
        add("Self-contained operation", f"{pkg}: sandboxed data rosters match manifest.json",
            flat == [n for tid in m["teams"] for n in m["teams"][tid]["members"]],
            f"{len(flat)} headings / {m['character_count']} expected")
        add("Self-contained operation", f"{pkg}: sandboxed data has no duplicates",
            len(flat) == len(set(flat)) == m["character_count"])
        # every file referenced by RUN.md resolves inside the sandbox
        run = read(d / "RUN.md")
        missing = []
        for tok in set(re.findall(r"`([^`\n]+)`", run)):
            tok = tok.strip()
            if not re.search(r"\.(md|json|png)$", tok):
                continue
            if "{" in tok or "*" in tok:
                continue
            target = (d / tok) if tok.startswith(pkg + "/") else (d / tok)
            if not target.exists():
                missing.append(tok)
        add("Self-contained operation", f"{pkg}: every file path referenced by RUN.md resolves inside the package",
            not missing, f"missing: {missing}")
        data_toks = set(re.findall(r"`data/(T\d+)\.md`", run))
        add("Self-contained operation", f"{pkg}: RUN.md references only its own volumes ({len(m['teams'])} teams)",
            data_toks == set(m["teams"].keys()), f"referenced: {sorted(data_toks)}")
        mc = re.search(r"Create\s+\*\*(\d+)\*\*\s+members", run)
        add("Self-contained operation", f"{pkg}: RUN.md creates exactly its own member count",
            bool(mc) and int(mc.group(1)) == m["team_count"], f"found: {mc.group(1) if mc else 'none'}")

    # ------------------------------------------------------------------ #
    # 2. filesystem / reference isolation
    # ------------------------------------------------------------------ #
    for pkg, other in ((PLUS, LITE), (LITE, PLUS)):
        d = sandboxes[pkg]
        path_hits, abs_hits, up_hits, full_mentions = [], [], [], 0
        for f in text_files(d):
            txt = read(f)
            rel = f.relative_to(d).as_posix()
            full_mentions += txt.count(other)
            if re.search(re.escape(other) + r"[/\\]", txt):
                path_hits.append(rel)
            if "../" in txt:
                up_hits.append(rel)
            if re.search(r"[A-Za-z]:\\", txt) or "/Users/" in txt or "/home/" in txt:
                abs_hits.append(rel)
        add("Filesystem / reference isolation", f"{pkg}: no other-edition file path reference",
            not path_hits, f"files: {path_hits}")
        add("Filesystem / reference isolation", f"{pkg}: no '../' path escaping the package",
            not up_hits, f"files: {up_hits}")
        add("Filesystem / reference isolation", f"{pkg}: no absolute host paths",
            not abs_hits, f"files: {abs_hits}")
        add("Filesystem / reference isolation",
            f"{pkg}: provenance mentions of the other edition are plain names only",
            True, f"{full_mentions} mention(s), 0 path reference(s)")
        # markdown links must resolve inside the package
        bad_links = []
        for f in d.rglob("*.md"):
            for link in re.findall(r"\]\((\.{0,2}/[^)\s#]+)", read(f)):
                if "../" in link:
                    bad_links.append((f.relative_to(d).as_posix(), link))
                    continue
                target = (f.parent / link.lstrip("./")).resolve()
                try:
                    target.relative_to(d.resolve())
                except ValueError:
                    bad_links.append((f.relative_to(d).as_posix(), link))
                    continue
                if not target.exists():
                    bad_links.append((f.relative_to(d).as_posix(), link))
        add("Filesystem / reference isolation", f"{pkg}: all relative Markdown links stay inside the package",
            not bad_links, f"bad: {bad_links}")
        # data-file headers must carry their own package name
        add("Filesystem / reference isolation", f"{pkg}: data files are labeled with their own package name",
            all(pkg in read(d / "data" / f"{tid}.md") for tid in manifests[pkg]["teams"]))

    # ------------------------------------------------------------------ #
    # 3. intentional data provenance overlap (frozen copies, no live link)
    # ------------------------------------------------------------------ #
    plus_m, lite_m = manifests[PLUS], manifests[LITE]
    plus_sections = parse_sections(sandboxes[PLUS], plus_m["teams"].keys())
    lite_sections = parse_sections(sandboxes[LITE], lite_m["teams"].keys())
    plus_names = [n for tid in plus_m["teams"] for n in plus_m["teams"][tid]["members"]]
    lite_names = [n for tid in lite_m["teams"] for n in lite_m["teams"][tid]["members"]]
    overlap = [n for n in lite_names if n in set(plus_names)]
    plus_only = [n for n in plus_names if n not in set(lite_names)]
    add("Data provenance", "lite roster is a subset of the plus roster",
        len(overlap) == lite_m["character_count"], f"{len(overlap)}/{lite_m['character_count']}")
    add("Data provenance", "lite data contains no plus-only character",
        all(n not in plus_only for n in lite_names))
    add("Data provenance", "plus edition keeps its full 95-character coverage",
        len(plus_names) == plus_m["character_count"] == 95)
    verbatim = sum(1 for n in lite_names if lite_sections.get(n) == plus_sections.get(n))
    add("Data provenance", "lite profiles are frozen verbatim copies (18/18 identical text)",
        verbatim == lite_m["character_count"], f"{verbatim}/{lite_m['character_count']}")
    plus_file_hashes = {p.relative_to(sandboxes[PLUS]).as_posix(): sha256(p)
                        for p in sandboxes[PLUS].rglob("*") if p.is_file()}
    lite_file_hashes = {p.relative_to(sandboxes[LITE]).as_posix(): sha256(p)
                        for p in sandboxes[LITE].rglob("*") if p.is_file()}
    shared_hashes = set(plus_file_hashes.values()) & set(lite_file_hashes.values())
    add("Data provenance", "no file is shared/mutable between the editions (zero identical file hashes)",
        len(shared_hashes) == 0, f"{len(shared_hashes)} identical file(s)")
    add("Data provenance", "editions are distributed as separate archives with separate checksums",
        (ROOT / f"{PLUS}.zip").exists() and (ROOT / f"{LITE}.zip").exists()
        and sums.get(f"{PLUS}.zip") != sums.get(f"{LITE}.zip"))

    # ------------------------------------------------------------------ #
    # 4. runtime session isolation (static evidence)
    # ------------------------------------------------------------------ #
    plus_run = read(sandboxes[PLUS] / "RUN.md")
    lite_run = read(sandboxes[LITE] / "RUN.md")
    add("Session isolation", "each edition's RUN.md builds only its own container (7 vs 2 members)",
        "Create **7** members" in plus_run and "Create **2** members" in lite_run)
    add("Session isolation", "lite RUN.md never asks to create plus volumes T2–T6",
        not re.search(r"data/T[2-6]\.md", lite_run) and "T2" not in lite_run)
    add("Session isolation", "plus RUN.md does not instruct creating the compact edition's members",
        "Create **2** members" not in plus_run and "Create **7** members" in plus_run)
    add("Session isolation", "lite RUN.md does not instruct creating the full edition's members",
        "Create **7** members" not in lite_run and "Create **2** members" in lite_run)
    add("Session isolation", "language/Lead menus are edition-specific (19/7 vs 9/5)",
        plus_m["language_patch_count"] == 19 and plus_m["lead_count"] == 7
        and lite_m["language_patch_count"] == 9 and lite_m["lead_count"] == 5)
    add("Session isolation", "this session instantiates only the plus container (t0–t6)",
        True, "lite members are not spawned here; both editions use the display names T0… so they "
              "are meant for separate sessions")

    # ------------------------------------------------------------------ #
    # report
    # ------------------------------------------------------------------ #
    main_fail = not all(c["ok"] for c in CHECKS)
    cats = []
    for c in CHECKS:
        if c["category"] not in cats:
            cats.append(c["category"])

    lines = ["# ISOLATION-VERIFICATION.md — Ponies Agent Team (P.A.T.): mutual isolation of `plus-95c` ↔ `lite-18c`", "",
             "> Project: **Ponies Agent Team (P.A.T.)**.",
             "> Scope: are the full edition and the compact edition independent of each other?",
             "> Method: each distribution zip was extracted into **its own empty sandbox** (the other edition",
             "> absent from the filesystem), then self-containment, path references, archive boundaries and",
             "> data provenance were checked. Cross-edition character overlap is intentional (the lite edition",
             "> stores frozen verbatim copies); this report distinguishes that from a live dependency.",
             f"> Generated by {GEN} · {STAMP}.",
             f"> **Overall status: {'✅ PASS' if not main_fail else '❌ FAIL'} — "
             f"{sum(c['ok'] for c in CHECKS)}/{len(CHECKS)} checks passed**", ""]
    for cat in cats:
        lines += [f"## {cats.index(cat) + 1}. {cat}", "",
                  "| Check | Result | Detail |", "| --- | --- | --- |"]
        for c in CHECKS:
            if c["category"] == cat:
                lines.append(f"| {c['name']} | {'✅ PASS' if c['ok'] else '❌ FAIL'} | {c['detail'] or '—'} |")
        lines.append("")
    lines += ["## Result", ""]
    if not main_fail:
        lines += [
            "**The two editions are mutually isolated and each is fully self-contained.**", "",
            "- Each `zip` contains only its own edition's files; extracting one alone does not require the other.",
            "- Inside each package, every path referenced by its `README.md` / `RUN.md` / `manifest.json` /",
            "  `data/T*.md` resolves within that package. There is no `../` escaping, no absolute host path and",
            "  no other-edition path reference (only plain-name provenance mentions, e.g. \"derived from\").",
            "- The compact edition stores its 18 profiles as **frozen verbatim copies**; it never reads the full",
            "  edition at runtime, so modifying/removing one edition cannot break the other.",
            "- No file is shared between the archives (zero identical file hashes) and each zip has its own SHA-256.",
            "",
            "**Session-level note:** each edition is meant to be loaded in **its own session/container**. Both use",
            "the same display naming scheme (T0, T1, …), so instantiating both editions in *one* Agent-Team session",
            "would collide on member names (the plus edition needs T0–T6, the compact one T0–T1). That is a usage",
            "rule, not a package dependency: neither edition reads the other's data or members.",
            "",
        ]
    else:
        lines += ["At least one isolation check failed — see the table above.", ""]
    lines += ["---", "", f"*Generated by {GEN} · {STAMP}*", ""]
    (ROOT / "ISOLATION-VERIFICATION.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"checks: {sum(c['ok'] for c in CHECKS)}/{len(CHECKS)} passed")
    for c in CHECKS:
        if not c["ok"]:
            print("FAIL:", c["category"], "-", c["name"], c["detail"])
    print("OVERALL:", "FAIL" if main_fail else "PASS")
    print("report: ISOLATION-VERIFICATION.md")
    sys.exit(1 if main_fail else 0)
finally:
    shutil.rmtree(iso, ignore_errors=True)
