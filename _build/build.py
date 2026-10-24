#!/usr/bin/env python3
"""Build, verify and package both editions (plus-95c and lite-18c).

Steps:
 1. Parse + verify the seven plus data volumes against the randomized assignment.
 2. Derive the lite data files (18 characters -> T0/T1) from the plus volumes.
 3. Generate TEAMS.md, manifest.json, VERIFICATION.md for both packages.
 4. Zip both packages, check archive integrity and write SHA256SUMS.txt when everything passes.
"""
import hashlib
import json
import re
import sys
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "_build"
TZ = timezone(timedelta(hours=8))
NOW = datetime.now(TZ)
STAMP = NOW.strftime("%Y-%m-%d %H:%M:%S %z")
GEN = "DeepSeek Harness — `deepseek-flash` model"

PLUS = "ponies-agent-team-v1.1-plus-95c"
LITE = "ponies-agent-team-v1.1-lite-18c"

G5_SET = {"Sunny Starscout", "Izzy Moonbow", "Pipp Petals", "Zipp Storm", "Hitch Trailblazer",
          "Misty Brightdawn", "Opalina Acrana", "Sprout Cloverleaf", "Blaize Skysong", "Cloudpuff",
          "Sparky Sparkeroni"}

FIELDS = [
    "Series/Continuity", "Species/Kind", "Gender", "Age/Stage", "Residence",
    "Occupation/Role/Affiliation", "Appearance", "Personality", "Likes", "Dislikes",
    "Fears/Weaknesses", "Skills/Abilities", "Family & Relationships",
    "Background/Biography", "Speech Style/Catchphrases", "Notable Quotes", "Trivia/Notes",
]

LANG_PLUS = [
    {"id": 1, "label": "简体中文 · 上海话", "group": "Simplified Chinese", "notes": "Simplified script, Shanghainese dialect flavour"},
    {"id": 2, "label": "简体中文 · 广东粤语", "group": "Simplified Chinese", "notes": "Simplified script, Cantonese (Guangdong) dialect flavour"},
    {"id": 3, "label": "简体中文 · 东北话", "group": "Simplified Chinese", "notes": "Simplified script, Northeastern Mandarin dialect flavour"},
    {"id": 4, "label": "简体中文 · 四川话", "group": "Simplified Chinese", "notes": "Simplified script, Sichuanese dialect flavour"},
    {"id": 5, "label": "简体中文 · 新疆话", "group": "Simplified Chinese", "notes": "Simplified script, Xinjiang Mandarin dialect flavour"},
    {"id": 6, "label": "简体中文 · 普通话", "group": "Simplified Chinese", "notes": "Simplified script, Standard Mandarin"},
    {"id": 7, "label": "繁体中文 · 港澳粤语", "group": "Traditional Chinese", "notes": "Traditional script, Cantonese (Hong Kong / Macau) dialect flavour"},
    {"id": 8, "label": "繁体中文 · 台湾话", "group": "Traditional Chinese", "notes": "Traditional script, Taiwanese Mandarin dialect flavour"},
    {"id": 9, "label": "英语 · 美式英语", "group": "English", "notes": "American English — master / base language"},
    {"id": 10, "label": "英语 · 英式英语", "group": "English", "notes": "British English"},
    {"id": 11, "label": "法语", "group": "Other", "notes": "French"},
    {"id": 12, "label": "德语", "group": "Other", "notes": "German"},
    {"id": 13, "label": "意大利语", "group": "Other", "notes": "Italian"},
    {"id": 14, "label": "西班牙语", "group": "Other", "notes": "Spanish"},
    {"id": 15, "label": "葡萄牙语", "group": "Other", "notes": "Portuguese"},
    {"id": 16, "label": "日语", "group": "Other", "notes": "Japanese"},
    {"id": 17, "label": "韩语", "group": "Other", "notes": "Korean"},
    {"id": 18, "label": "阿拉伯语", "group": "Other", "notes": "Arabic"},
    {"id": 19, "label": "希伯来语", "group": "Other", "notes": "Hebrew"},
]
LANG_LITE = [
    {"id": 1, "label": "简体中文 · 普通话", "group": "Simplified Chinese", "notes": "Simplified script, Standard Mandarin"},
    {"id": 2, "label": "繁体中文 · 港澳粤语", "group": "Traditional Chinese", "notes": "Traditional script, Cantonese (Hong Kong / Macau) dialect flavour"},
    {"id": 3, "label": "繁体中文 · 台湾话", "group": "Traditional Chinese", "notes": "Traditional script, Taiwanese Mandarin dialect flavour"},
    {"id": 4, "label": "英语 · 美式英语", "group": "English", "notes": "American English — master / base language"},
    {"id": 5, "label": "法语", "group": "Other", "notes": "French"},
    {"id": 6, "label": "德语", "group": "Other", "notes": "German"},
    {"id": 7, "label": "意大利语", "group": "Other", "notes": "Italian"},
    {"id": 8, "label": "葡萄牙语", "group": "Other", "notes": "Portuguese"},
    {"id": 9, "label": "日语", "group": "Other", "notes": "Japanese"},
]
LEADS_PLUS = ["Princess Cadance", "Princess Celestia (Daybreaker)", "Princess Luna (Nightmare Moon)",
              "Twilight Sparkle", "Opaline Arcana", "Sunny Starscout", "Sunset Shimmer"]
LEADS_LITE = ["Twilight Sparkle", "Sunny Starscout", "Sunset Shimmer",
              "Princess Celestia (Daybreaker)", "Princess Luna (Nightmare Moon)"]
LANG_WORDS_PLUS = ["上海话", "广东粤语", "东北话", "四川话", "新疆话", "普通话", "港澳粤语",
                   "台湾话", "美式英语", "英式英语", "法语", "德语", "意大利语", "西班牙语",
                   "葡萄牙语", "日语", "韩语", "阿拉伯语", "希伯来语"]
LANG_WORDS_LITE = ["普通话", "港澳粤语", "台湾话", "美式英语", "法语", "德语", "意大利语",
                   "葡萄牙语", "日语"]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def parse_team_file(path: Path):
    text = read_text(path)
    lines = text.splitlines()
    headings, idxs = [], []
    for i, line in enumerate(lines):
        if line.startswith("## "):
            headings.append(line[3:].strip())
            idxs.append(i)
    sections = {}
    for k, i in enumerate(idxs):
        end = idxs[k + 1] if k + 1 < len(idxs) else len(lines)
        sections[headings[k]] = "\n".join(lines[i:end])
    return text, headings, sections


def analyze_profile(sec: str) -> dict:
    missing, duplicates, empty = [], [], []
    positions = {}
    for label in FIELDS:
        pat = re.compile(r"^\*\*" + re.escape(label) + r":\*\*", re.M)
        ms = list(pat.finditer(sec))
        if not ms:
            missing.append(label)
        else:
            if len(ms) > 1:
                duplicates.append(label)
            positions[label] = ms[0]
    present = [l for l in FIELDS if l in positions]
    order_ok = [positions[l].start() for l in present] == sorted(positions[l].start() for l in present)
    for i, lab in enumerate(present):
        start = positions[lab].end()
        end = positions[present[i + 1]].start() if i + 1 < len(present) else len(sec)
        content = sec[start:end].strip()
        content = re.sub(r"(?m)^-{3,}\s*$", "", content).strip()
        if len(content) < 2:
            empty.append(lab)
    return {"missing": missing, "duplicates": duplicates, "empty": empty,
            "order_ok": order_ok, "words": len(sec.split())}


def verify_volume_files(pkg_dir: Path, assignment: dict):
    """Return (per-team results, name -> list[(team, section text)])."""
    results, index = {}, {}
    for tid, team in assignment["teams"].items():
        expected = team["members"]
        path = pkg_dir / "data" / f"{tid}.md"
        res = {"team": tid, "expected": expected, "path": path, "status": "PASS",
               "issues": [], "characters": {}, "headings": []}
        if not path.exists():
            res["status"] = "FAIL"
            res["issues"].append("data file missing")
            results[tid] = res
            continue
        text, headings, sections = parse_team_file(path)
        res["headings"] = headings
        if headings != expected:
            res["status"] = "FAIL"
            missing = [n for n in expected if n not in headings]
            extra = [n for n in headings if n not in expected]
            if missing:
                res["issues"].append(f"missing headings: {missing}")
            if extra:
                res["issues"].append(f"unexpected headings: {extra}")
            if len(headings) == len(expected) and not missing and not extra:
                res["issues"].append("heading order differs from roster")
        for name, sec in sections.items():
            info = analyze_profile(sec)
            res["characters"][name] = info
            if name not in expected:
                continue
            if info["missing"]:
                res["status"] = "FAIL"
                res["issues"].append(f"{name}: missing fields {info['missing']}")
            if info["duplicates"]:
                res["status"] = "FAIL"
                res["issues"].append(f"{name}: duplicate fields {info['duplicates']}")
            if info["empty"]:
                res["status"] = "FAIL"
                res["issues"].append(f"{name}: empty fields {info['empty']}")
            if not info["order_ok"]:
                res["status"] = "FAIL"
                res["issues"].append(f"{name}: field order not canonical")
            if info["words"] < 120:
                res["status"] = "FAIL"
                res["issues"].append(f"{name}: too short ({info['words']} words)")
            elif info["words"] < 200 and res["status"] == "PASS":
                res["status"] = "WARN"
                res["issues"].append(f"{name}: short profile ({info['words']} words)")
            index.setdefault(name, []).append((tid, sec))
        results[tid] = res
    return results, index


# --------------------------------------------------------------------------- #
# lite data derivation
# --------------------------------------------------------------------------- #
LITE_HEADER = """# Team {tid} — Roster ({count} characters)

> Project: **Ponies Agent Team (P.A.T.)** — compact edition data volume
> Package: `{pkg}` · Volume {idx} of {total}
> Source material: My Little Pony: Friendship is Magic / Equestria Girls (G4), My Little Pony: Make Your Mark / Tell Your Tale (G5)
> Derived from: `{parent}` (character profiles copied verbatim)
> Language base: American English (localized at runtime by a language patch — keep the master data in English)
> Generated by: {gen}

"""


def strip_section_tail(sec: str) -> str:
    sec = sec.rstrip()
    while sec.endswith("---"):
        sec = sec[:-3].rstrip()
    return sec


def build_lite_data(plus_index: dict, lite_assignment: dict) -> list[str]:
    problems = []
    for n, entries in plus_index.items():
        if len(entries) > 1:
            problems.append(f"{n}: appears in multiple volumes {[e[0] for e in entries]}")
    lite_dir = ROOT / LITE
    (lite_dir / "data").mkdir(parents=True, exist_ok=True)
    idx = 0
    for tid, team in lite_assignment["teams"].items():
        idx += 1
        parts = [LITE_HEADER.format(tid=tid, count=team["count"], pkg=LITE, idx=idx,
                                    total=lite_assignment["team_count"], parent=PLUS, gen=GEN)]
        for name in team["members"]:
            entries = plus_index.get(name)
            if not entries:
                problems.append(f"{tid}: {name} not found in plus data")
                continue
            parts.append(strip_section_tail(entries[0][1]))
        (lite_dir / "data" / f"{tid}.md").write_text("\n\n---\n\n".join(parts) + "\n", encoding="utf-8")
    return problems


# --------------------------------------------------------------------------- #
# documents
# --------------------------------------------------------------------------- #
def write_teams_md(pkg_name: str, pkg_dir: Path, assignment: dict) -> None:
    series_lookup = {n: ("G5" if n in G5_SET else "G4/EQG")
                     for t in assignment["teams"].values() for n in t["members"]}
    lines = [f"# TEAMS.md — Team status · `{pkg_name}`", "",
             "> Project: **Ponies Agent Team (P.A.T.)**.",
             f"> {assignment['team_count']} volume teams · {assignment['character_count']} characters · "
             "completely random assignment (no canon grouping).",
             "> The volumes are storage splits only: at runtime every character lives in one logical container.",
             "> Authority: `manifest.json` (machine-readable) · `data/T*.md` (full profiles).",
             f"> Generated by {GEN}.", "", "## Summary", "",
             "| Team | Characters | G4/EQG | G5 | Data file |", "| --- | ---: | ---: | ---: | --- |"]
    for tid, team in assignment["teams"].items():
        mix = team["series_mix"]
        lines.append(f"| {tid} | {team['count']} | {mix['G4/EQG']} | {mix['G5']} | `data/{tid}.md` |")
    lines.append(f"| **Total** | **{assignment['character_count']}** | **{assignment['series_counts']['G4/EQG']}** | "
                 f"**{assignment['series_counts']['G5']}** | {assignment['team_count']} files |")
    lines += ["", "## Rosters", ""]
    for tid, team in assignment["teams"].items():
        lines += [f"### {tid} — {team['count']} characters", ""]
        for name in team["members"]:
            lines.append(f"- **{name}** — {series_lookup[name]}")
        lines.append("")
    lines += ["---", "", f"*Generated by {GEN} · {STAMP}*", ""]
    (pkg_dir / "TEAMS.md").write_text("\n".join(lines), encoding="utf-8")


def write_manifest(pkg_name: str, pkg_dir: Path, assignment: dict, langs, leads,
                   variant: str, edition: str, extra: dict | None = None) -> None:
    files = {}
    for rel in ["README.md", "RUN.md", "TEAMS.md", "assets/cover.png"]:
        p = pkg_dir / rel
        if p.exists():
            files[rel] = sha256(p)
    for tid in assignment["teams"]:
        p = pkg_dir / "data" / f"{tid}.md"
        if p.exists():
            files[f"data/{tid}.md"] = sha256(p)
    manifest = {
        "package": pkg_name,
        "project": "Ponies Agent Team",
        "abbreviation": "P.A.T.",
        "version": "1.1",
        "variant": variant,
        "edition": edition,
        "description": f"Ponies Agent Team (P.A.T.) {edition} edition — {assignment['character_count']} complete "
                       "MLP character profiles split into volume teams for AI roleplay sessions.",
        "generated_by": {"model": "deepseek-flash", "framework": "DeepSeek Harness", "generated_at": STAMP},
        "character_count": assignment["character_count"],
        "series_counts": assignment["series_counts"],
        "team_count": assignment["team_count"],
        "base_language": "American English",
        "language_patches": langs,
        "language_patch_count": len(langs),
        "leads": leads,
        "lead_count": len(leads),
        "lead_spelling_note": "Canonical English spellings used; original request wrote 'Twilght Sparkle' "
                              "(Twilight Sparkle) and 'Opalina Acrana' (Opaline Arcana).",
        "random_assignment": {
            "method": "random.SystemRandom() shuffle, unseeded (not reproducible by design)",
            "note": "Team membership is fully random; teams are storage volumes, not canon groups.",
        },
        "teams": {tid: {"count": t["count"], "series_mix": t["series_mix"],
                        "data_file": f"data/{tid}.md", "members": t["members"]}
                  for tid, t in assignment["teams"].items()},
        "data_format_fields": FIELDS,
        "files": files,
        "files_checksum_algorithm": "sha256",
        "run_file": "RUN.md",
        "readme": "README.md",
        "teams_file": "TEAMS.md",
        "verification_file": "VERIFICATION.md",
        "notes": [
            "Project name: Ponies Agent Team, abbreviated P.A.T. (packages: ponies-agent-team-v1.1-*).",
            "RUN.md is the operator guide: language patch -> global Lead -> create volume members and verify -> brief close.",
            "Never use the DSH Ask-Questions tool in the RUN.md flow; all prompts are plain chat text.",
            "Language patches are runtime translations on top of the American-English master data; data files are never translated in place.",
        ],
    }
    if extra:
        manifest.update(extra)
    (pkg_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def docs_checks(pkg_dir: Path, lang_words, leads) -> dict:
    readme_p = pkg_dir / "README.md"
    run_p = pkg_dir / "RUN.md"
    readme = read_text(readme_p) if readme_p.exists() else ""
    run = read_text(run_p) if run_p.exists() else ""
    return {
        "README.md exists": readme_p.exists(),
        "README.md has image placeholder + banner reference": ("IMAGE PLACEHOLDER" in readme
                                                               and "assets/cover.png" in readme),
        "README.md ends with AI generation credit": ("Generated by" in readme[-1200:]
                                                     and "deepseek-flash" in readme[-1200:]),
        "assets/cover.png banner exists (>5 KB)": ((pkg_dir / "assets" / "cover.png").exists()
                                                   and (pkg_dir / "assets" / "cover.png").stat().st_size > 5000),
        "RUN.md exists": run_p.exists(),
        "RUN.md documents steps 1-4": all(s in run for s in ["Step 1", "Step 2", "Step 3", "Step 4"])
                                      and all(s in run for s in ["一 /", "二 /", "三 /", "四 /"]),
        "RUN.md Step 4 imitates the global main Lead's voice": ("Voice rule (mandatory)" in run
                                                              and "imitate the global main Lead" in run
                                                              and "1–3 sentences" in run),
        "RUN.md bans the Ask-Questions tool": 'Never use the DSH "Ask Questions" tool' in run,
        "RUN.md + README.md list all language options": all(w in run for w in lang_words)
                                                        and all(w in readme for w in lang_words),
        "RUN.md lists all Lead options": all(l in run for l in leads),
        "README.md + RUN.md name the project 'Ponies Agent Team' with abbreviation 'P.A.T.'":
            ("Ponies Agent Team" in readme and "P.A.T." in readme
             and "Ponies Agent Team" in run and "P.A.T." in run),
        "TEAMS.md generated": (pkg_dir / "TEAMS.md").exists(),
    }


def write_verification(pkg_name: str, pkg_dir: Path, assignment: dict, results: dict,
                       index: dict, docs: dict, cross: dict, zip_plan: dict | None) -> None:
    all_names = [n for t in assignment["teams"].values() for n in t["members"]]
    found_names = sorted(index.keys())
    dupes = {n: [t for t, _ in v] for n, v in index.items() if len(v) > 1}
    series_lookup = {n: ("G5" if n in G5_SET else "G4/EQG") for n in all_names}
    actual_mix = {"G4/EQG": 0, "G5": 0}
    for n in found_names:
        actual_mix[series_lookup.get(n, "G4/EQG")] += 1

    total_fail = sum(1 for r in results.values() if r["status"] == "FAIL")
    total_warn = sum(1 for r in results.values() if r["status"] == "WARN")
    total_sections = sum(len(r["headings"]) for r in results.values())
    docs_fail = [k for k, v in docs.items() if not v]
    cross_fail = [k for k, v in cross.items() if not v["ok"]]
    len_ok = (len(found_names) == len(set(found_names)) == assignment["character_count"])
    overall = (total_fail == 0 and not docs_fail and not cross_fail and len_ok and not dupes
               and total_sections == assignment["character_count"]
               and actual_mix == assignment["series_counts"])

    lines = [f"# VERIFICATION.md — `{pkg_name}`", "",
             "> Automated integrity report for this package.",
             "> Project: **Ponies Agent Team (P.A.T.)**.",
             f"> Generated by {GEN} · {STAMP}.",
             f"> **Overall status: {'✅ PASS' if overall else '❌ FAIL'}**"
             + (" (profiles are complete; some are shorter than the 200-word soft target)"
                if total_warn and overall else ""), "",
             "## 1. Team partition & character profiles", "",
             "| Team | Expected | Found | Headings match | 17 fields complete | Word range | Status |",
             "| --- | ---: | ---: | --- | --- | --- | --- |"]
    for tid, r in results.items():
        counts = [c["words"] for c in r["characters"].values()] or [0]
        fields_ok = "✅" if r["characters"] and all(
            not c["missing"] and not c["empty"] and not c["duplicates"] for c in r["characters"].values()) else "❌"
        headers_ok = "✅" if r["headings"] == r["expected"] else "❌"
        lines.append(f"| {tid} | {len(r['expected'])} | {len(r['headings'])} | {headers_ok} | "
                     f"{fields_ok} | {min(counts)}–{max(counts)} words | {r['status']} |")
    lines.append(f"| **Total** | **{assignment['character_count']}** | **{len(found_names)} distinct** | — | — | — | "
                 f"**{'PASS' if total_fail == 0 else 'FAIL'}** |")
    lines += ["", "Global checks:", "",
              f"- characters found exactly once: **{len(found_names)} / {assignment['character_count']}** "
              f"({'✅' if len_ok and not dupes and total_sections == assignment['character_count'] else '❌'})",
              f"- total character sections in data files: **{total_sections} / {assignment['character_count']}** "
              f"({'✅' if total_sections == assignment['character_count'] else '❌'})",
              f"- duplicate characters: **{len(dupes)}** ({'✅' if not dupes else '❌ ' + str(dupes)})",
              f"- series mix G4/EQG: **{actual_mix['G4/EQG']} / {assignment['series_counts']['G4/EQG']} expected** "
              f"({'✅' if actual_mix['G4/EQG'] == assignment['series_counts']['G4/EQG'] else '❌'})",
              f"- series mix G5: **{actual_mix['G5']} / {assignment['series_counts']['G5']} expected** "
              f"({'✅' if actual_mix['G5'] == assignment['series_counts']['G5'] else '❌'})",
              f"- short-profile warnings (soft 200-word floor): **{total_warn}**", ""]
    issues = []
    for tid, r in results.items():
        for msg in r["issues"]:
            issues.append(f"- `{tid}`: {msg}")
    lines += ["## 2. Profile issues", ""] + (issues if issues else ["No profile issues found. ✅"]) + [""]
    lines += ["## 3. Cross-package / provenance checks", ""]
    for name, info in cross.items():
        lines.append(f"- {name}: **{'✅ PASS' if info['ok'] else '❌ FAIL'}** — {info['detail']}")
    lines += ["", "## 4. Document checks", ""]
    for k, v in docs.items():
        lines.append(f"- {k}: **{'✅' if v else '❌'}**")
    lines += ["", "## 5. Archive", ""]
    if zip_plan:
        lines.append(f"- distribution archive: `{zip_plan['name']}` — contains all **{zip_plan['entries']}** "
                     "package files (folder root preserved); integrity verified with a zip test during packaging.")
        lines.append("- SHA-256 checksums of the distribution archives: see `SHA256SUMS.txt` at the "
                     "distribution root (next to the two `.zip` files).")
    else:
        lines.append("- archive not created yet (package verification did not pass or build is in progress)")
    lines += ["", "---", "", f"*Generated by {GEN} · {STAMP}*", ""]
    (pkg_dir / "VERIFICATION.md").write_text("\n".join(lines), encoding="utf-8")


def count_files(pkg_dir: Path) -> int:
    return len([p for p in pkg_dir.rglob("*") if p.is_file()])


def make_zip(pkg_name: str) -> dict:
    pkg_dir = ROOT / pkg_name
    zip_path = ROOT / f"{pkg_name}.zip"
    files = sorted(p for p in pkg_dir.rglob("*") if p.is_file())
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in files:
            zf.write(p, arcname=f"{pkg_name}/{p.relative_to(pkg_dir).as_posix()}")
    with zipfile.ZipFile(zip_path) as zf:
        names = zf.namelist()
        ok = zf.testzip() is None and len(names) == len(files)
    return {"name": zip_path.name, "path": zip_path, "size": zip_path.stat().st_size,
            "entries": len(names), "ok": ok, "sha256": sha256(zip_path)}


def summarize(results: dict) -> str:
    return "  ".join(f"{tid}:{r['status']} ({len(r['characters'])}/{len(r['expected'])})"
                     for tid, r in results.items())


def print_issues(results: dict) -> None:
    for tid, r in results.items():
        for msg in r["issues"][:10]:
            print(f"  [{tid}] {msg}")
        if len(r["issues"]) > 10:
            print(f"  [{tid}] ... {len(r['issues']) - 10} more issues")


def main() -> int:
    assignment = json.loads((BUILD / "assignment.json").read_text(encoding="utf-8"))
    lite_assignment = json.loads((BUILD / "lite-assignment.json").read_text(encoding="utf-8"))
    plus_dir = ROOT / PLUS
    lite_dir = ROOT / LITE

    print("== plus volume verification ==")
    plus_results, plus_index = verify_volume_files(plus_dir, assignment)
    print(summarize(plus_results))
    print_issues(plus_results)

    print("\n== lite data derivation (from plus volumes) ==")
    lite_problems = build_lite_data(plus_index, lite_assignment)
    print("problems:", lite_problems if lite_problems else "none")
    lite_results, lite_index = verify_volume_files(lite_dir, lite_assignment)
    print(summarize(lite_results))
    print_issues(lite_results)

    lite_names = [n for t in lite_assignment["teams"].values() for n in t["members"]]
    missing_in_plus = [n for n in lite_names if n not in plus_index]
    subset_ok = (not missing_in_plus and len(lite_names) == lite_assignment["character_count"]
                 and all(len(plus_index.get(n, [])) == 1 for n in lite_names))
    cross_plus = {"lite subset available in plus data": {
        "ok": subset_ok,
        "detail": f"{lite_assignment['character_count'] - len(missing_in_plus)}/"
                  f"{lite_assignment['character_count']} lite characters found exactly once in plus volumes"
                  + (f"; missing: {missing_in_plus}" if missing_in_plus else "")}}
    cross_lite = {"profiles derived from plus package": {
        "ok": subset_ok,
        "detail": f"all {lite_assignment['character_count']} lite characters copied verbatim from `{PLUS}` data volumes"}}

    docs_plus = docs_checks(plus_dir, LANG_WORDS_PLUS, LEADS_PLUS)
    docs_lite = docs_checks(lite_dir, LANG_WORDS_LITE, LEADS_LITE)

    # documents (except archive info) first
    write_teams_md(PLUS, plus_dir, assignment)
    write_teams_md(LITE, lite_dir, lite_assignment)
    write_manifest(PLUS, plus_dir, assignment, LANG_PLUS, LEADS_PLUS, "95c", "plus")
    write_manifest(LITE, lite_dir, lite_assignment, LANG_LITE, LEADS_LITE, "18c", "lite",
                   extra={"derived_from": PLUS,
                          "derived_from_note": "Character profiles are copied verbatim from the plus package data volumes."})
    write_verification(PLUS, plus_dir, assignment, plus_results, plus_index, docs_plus, cross_plus, None)
    write_verification(LITE, lite_dir, lite_assignment, lite_results, lite_index, docs_lite, cross_lite, None)

    overall = (all(r["status"] != "FAIL" for r in plus_results.values())
               and all(r["status"] != "FAIL" for r in lite_results.values())
               and all(docs_plus.values()) and all(docs_lite.values()) and subset_ok and not lite_problems)
    if not overall:
        print("\nOVERALL: FAIL — fix the reported issues, then re-run.")
        return 1

    # finalize archive section (entry counts) then zip
    entries_plus = count_files(plus_dir)
    entries_lite = count_files(lite_dir)
    write_verification(PLUS, plus_dir, assignment, plus_results, plus_index, docs_plus, cross_plus,
                       {"name": f"{PLUS}.zip", "entries": entries_plus})
    write_verification(LITE, lite_dir, lite_assignment, lite_results, lite_index, docs_lite, cross_lite,
                       {"name": f"{LITE}.zip", "entries": entries_lite})

    print("\n== packaging ==")
    zip_plus = make_zip(PLUS)
    zip_lite = make_zip(LITE)
    print(f"plus zip: {zip_plus['size']:,} bytes, {zip_plus['entries']} entries, ok={zip_plus['ok']}")
    print(f"lite zip: {zip_lite['size']:,} bytes, {zip_lite['entries']} entries, ok={zip_lite['ok']}")
    if not (zip_plus["ok"] and zip_lite["ok"]):
        print("\nOVERALL: FAIL — archive integrity check failed.")
        return 1

    sums = ROOT / "SHA256SUMS.txt"
    sums.write_text(f"{zip_plus['sha256']}  {zip_plus['name']}\n{zip_lite['sha256']}  {zip_lite['name']}\n",
                    encoding="utf-8")
    print("SHA256SUMS.txt written")
    print("\nOVERALL: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
