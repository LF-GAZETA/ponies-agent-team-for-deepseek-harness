#!/usr/bin/env python3
"""Trim the collection README: remove four sections and three Chinese paragraphs."""
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "README.md"
lines = P.read_text(encoding="utf-8").splitlines()

REMOVE_HEADINGS = [
    "## Shared design / 共同设计",
    "## Verification / 校验",
    "## Replacing the images / 图片替换",
    "## Extending the dataset / 扩展数据集",
]
for h in REMOVE_HEADINGS:
    assert lines.count(h) == 1, f"heading not unique/missing: {h}"

out = []
skipping = False
for line in lines:
    if line in REMOVE_HEADINGS:
        skipping = True
        continue
    if skipping:
        if line.startswith("## "):
            skipping = False
            out.append(line)
        continue
    out.append(line)

# remove their TOC entries
TOC_ANCHORS = [
    "(#shared-design--共同设计)",
    "(#verification--校验)",
    "(#replacing-the-images--图片替换)",
    "(#extending-the-dataset--扩展数据集)",
]
before_toc = len([l for l in out if l.startswith("- [")])
out = [l for l in out if not any(a in l for a in TOC_ANCHORS)]
after_toc = len([l for l in out if l.startswith("- [")])
assert after_toc == before_toc - 4, (before_toc, after_toc)

# remove the three Chinese paragraphs
CN_PREFIXES = ("**共同设计**：", "**两个版本相互隔离**：", "**GitHub 说明**：")
removed_cn = [l for l in out if l.startswith(CN_PREFIXES)]
assert len(removed_cn) == 3, f"expected 3 Chinese paragraphs, found {len(removed_cn)}"
out = [l for l in out if not l.startswith(CN_PREFIXES)]

# collapse runs of blank lines
collapsed = []
for line in out:
    if line == "" and collapsed and collapsed[-1] == "":
        continue
    collapsed.append(line)

text = "\n".join(collapsed).strip() + "\n"
P.write_text(text, encoding="utf-8")

print("removed sections:", all(h not in text for h in REMOVE_HEADINGS))
print("removed TOC entries: 4")
print("removed Chinese paragraphs:", len(removed_cn))
print("remaining headings:")
for line in text.splitlines():
    if line.startswith("## "):
        print("  ", line)
print("lines:", len(text.splitlines()))
