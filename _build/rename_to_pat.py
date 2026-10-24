#!/usr/bin/env python3
"""Rename the project to "Ponies Agent Team (P.A.T.)".

- Static docs: root README, both package READMEs and RUN.md files.
- Banner generator texts (then the banners are regenerated separately).
- Plus data-file headers: add a project line (idempotent).
- Report generators: add the project line to MEMBER-/ISOLATION-VERIFICATION.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUS = ROOT / "ponies-agent-team-v1.1-plus-95c"
LITE = ROOT / "ponies-agent-team-v1.1-lite-18c"

DOC_PAIRS = {
    ROOT / "README.md": [
        ("# 🦄 Ponies Agent Team — Collection · `v1.1`",
         "# 🦄 Ponies Agent Team (P.A.T.) — Collection · `v1.1`"),
        ("![Ponies Agent Team — Collection banner](./assets/cover.png)",
         "![Ponies Agent Team (P.A.T.) — Collection banner](./assets/cover.png)"),
        ("**Ponies Agent Team** is a data package for AI roleplay sessions.",
         "**Ponies Agent Team (P.A.T.)** is a data package for AI roleplay sessions."),
        ("**Ponies Agent Team — Collection v1.1** 收录",
         "**Ponies Agent Team（P.A.T.）— Collection v1.1** 收录"),
    ],
    PLUS / "README.md": [
        ("# 🦄 Ponies Agent Team — `v1.1-plus-95c`",
         "# 🦄 Ponies Agent Team (P.A.T.) — `v1.1-plus-95c`"),
        ("![Ponies Agent Team — v1.1-plus-95c banner]",
         "![Ponies Agent Team (P.A.T.) — v1.1-plus-95c banner]"),
        ("Ponies Agent Team is a **data package for AI roleplay sessions**",
         "**Ponies Agent Team (P.A.T.)** is a **data package for AI roleplay sessions**"),
        ("**Ponies Agent Team — v1.1-plus-95c** 是一个面向",
         "**Ponies Agent Team（P.A.T.）— v1.1-plus-95c** 是一个面向"),
    ],
    PLUS / "RUN.md": [
        ("# RUN.md — Ponies Agent Team · `ponies-agent-team-v1.1-plus-95c`",
         "# RUN.md — Ponies Agent Team (P.A.T.) · `ponies-agent-team-v1.1-plus-95c`"),
        ('the persistent "volume" member of the Ponies Agent Team',
         'the persistent "volume" member of the Ponies Agent Team (P.A.T.)'),
    ],
    LITE / "README.md": [
        ("# 🦄 Ponies Agent Team — `v1.1-lite-18c`",
         "# 🦄 Ponies Agent Team (P.A.T.) — `v1.1-lite-18c`"),
        ("![Ponies Agent Team — v1.1-lite-18c banner]",
         "![Ponies Agent Team (P.A.T.) — v1.1-lite-18c banner]"),
        ("Ponies Agent Team **lite** is the compact edition",
         "**Ponies Agent Team (P.A.T.) — lite** is the compact edition"),
        ("**Ponies Agent Team — v1.1-lite-18c** 是完整版",
         "**Ponies Agent Team（P.A.T.）— v1.1-lite-18c** 是完整版"),
    ],
    LITE / "RUN.md": [
        ("# RUN.md — Ponies Agent Team · `ponies-agent-team-v1.1-lite-18c`",
         "# RUN.md — Ponies Agent Team (P.A.T.) · `ponies-agent-team-v1.1-lite-18c`"),
        ('the persistent "volume" member of the Ponies Agent Team',
         'the persistent "volume" member of the Ponies Agent Team (P.A.T.)'),
    ],
}

for path, pairs in DOC_PAIRS.items():
    text = path.read_text(encoding="utf-8")
    text = text.replace("Pony Agent Team", "Ponies Agent Team")
    for old, new in pairs:
        if old not in text:
            print(f"WARN: pattern not found in {path.name}: {old[:70]!r}")
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")
    print("updated", path.relative_to(ROOT))

# add a P.A.T. badge to the collection README (after the first badge line)
root_readme = ROOT / "README.md"
lines = root_readme.read_text(encoding="utf-8").splitlines()
for i, line in enumerate(lines):
    if line.startswith("![editions]"):
        lines.insert(i + 1, "![P.A.T.](https://img.shields.io/badge/abbreviation-P.A.T.-c77dff?style=flat-square)")
        break
root_readme.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("added P.A.T. badge")

# banner generator texts
banner_edits = {
    "_build/make_banners.py": [
        ('center("MY LITTLE PONY · AGENT TEAM", 96, font(30, True), (216, 194, 255, 255))',
         'center("PONIES AGENT TEAM · P.A.T.", 96, font(30, True), (216, 194, 255, 255))'),
        ('center("Pony Agent Team", 158, font(82, True), (255, 255, 255, 255))',
         'center("Ponies Agent Team", 158, font(82, True), (255, 255, 255, 255))'),
    ],
    "_build/make_collection_banner.py": [
        ('center("MY LITTLE PONY · AGENT TEAM COLLECTION", 70, font(24, True), (216, 194, 255, 255))',
         'center("PONIES AGENT TEAM · P.A.T. COLLECTION", 70, font(24, True), (216, 194, 255, 255))'),
        ('center("Pony Agent Team", 118, font(78, True), (255, 255, 255, 255))',
         'center("Ponies Agent Team", 118, font(78, True), (255, 255, 255, 255))'),
        ('center("Collection — v1.1", 234, font(42, True), (255, 214, 245, 255))',
         'center("Collection — v1.1 · P.A.T.", 234, font(42, True), (255, 214, 245, 255))'),
    ],
}
for rel, pairs in banner_edits.items():
    p = ROOT / rel
    t = p.read_text(encoding="utf-8")
    for old, new in pairs:
        if old not in t:
            print(f"WARN: banner pattern not found in {rel}: {old[:60]!r}")
        t = t.replace(old, new)
    p.write_text(t, encoding="utf-8")
    print("updated", rel)

# plus data-file headers: add the project line (idempotent)
PROJECT_LINE = "> Project: **Ponies Agent Team (P.A.T.)** — 17-field character volumes for AI roleplay"
for p in sorted((PLUS / "data").glob("T*.md")):
    text = p.read_text(encoding="utf-8")
    if "Ponies Agent Team (P.A.T.)" in text:
        print("skip (already tagged)", p.name)
        continue
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# Team "):
        print("WARN: unexpected header", p.name)
        continue
    insert_at = 2 if len(lines) > 1 and lines[1].strip() == "" else 1
    lines.insert(insert_at, PROJECT_LINE)
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("tagged", p.name)

# report generators
p = ROOT / "_build/member_verify.py"
t = p.read_text(encoding="utf-8")
t = t.replace(
    '"> Session: `ponies-agent-team-v1.1-plus-95c` · Team Lead `lead` · data-volume members `t0`–`t6`.",',
    '"> Project: **Ponies Agent Team (P.A.T.)** · Session: `ponies-agent-team-v1.1-plus-95c` · '
    'Team Lead `lead` · data-volume members `t0`–`t6`.",')
p.write_text(t, encoding="utf-8")
print("updated _build/member_verify.py")

p = ROOT / "_build/isolation_test.py"
t = p.read_text(encoding="utf-8")
t = t.replace(
    'lines = ["# ISOLATION-VERIFICATION.md — mutual isolation of `plus-95c` ↔ `lite-18c`", "",',
    'lines = ["# ISOLATION-VERIFICATION.md — Ponies Agent Team (P.A.T.): '
    'mutual isolation of `plus-95c` ↔ `lite-18c`", "",\n'
    '             "> Project: **Ponies Agent Team (P.A.T.)**.",')
p.write_text(t, encoding="utf-8")
print("updated _build/isolation_test.py")

print("DONE")
