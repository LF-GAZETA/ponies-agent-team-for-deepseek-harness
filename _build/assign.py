#!/usr/bin/env python3
"""Randomly split the 95-character MLP roster into 7 volume teams (T0-T6)
and the 18-character lite roster into 2 teams (T0-T1); scaffold package dirs."""
import json
import random
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "_build"
BUILD.mkdir(exist_ok=True)

G4 = [
    "Twilight Sparkle", "Rainbow Dash", "Rarity", "Applejack", "Fluttershy", "Pinkie Pie", "Spike",
    "Apple Bloom", "Scootaloo", "Sweetie Belle", "Princess Celestia (Daybreaker)",
    "Princess Luna (Nightmare Moon)", "Princess Cadance", "Shining Armor", "Starlight Glimmer",
    "Trixie", "Sunset Shimmer", "King Sombra", "Queen Chrysalis", "Discord", "Spitfire", "Soarin'",
    "Lightning Dust", "Big Macintosh", "Granny Smith", "Braeburn", "Babs Seed", "Pear Butter",
    "Bright Mac", "Silver Spoon", "Diamond Tiara", "Princess Flurry Heart", "Derpy Hooves",
    "Doctor Whooves", "Minuette", "Bon Bon", "Octavia Melody", "Vinyl Scratch", "Maud Pie",
    "Coco Pommel", "Suri Polomare", "Zecora", "Mayor Mare", "Sci-Twi (Midnight Sparkle)",
    "Adagio Dazzle", "Sonata Dusk", "Aria Blaze", "Flash Sentry", "Cheerilee", "Cozy Glow",
    "Sunburst", "Tempest Shadow (Fizzlepop Berrytwist)", "Princess Ember", "Gallus",
    "Marble Pie", "Silverstream", "Ocellus", "Thorax", "Moondancer", "Lord Tirek", "Sugar Belle",
    "Wallflower Blush", "Juniper Montage", "Glorisa Daisy", "Night Light", "Twilight Velvet",
    "Luster Dawn", "Star Swirl the Bearded", "Rainbowshine", "Lyra Heartstrings", "Daring Do",
    "Limestone Pie", "Yona", "Nurse Redheart", "Prince Blueblood", "Aloe", "Lotus Blossom",
    "Stygian (Pony of Shadows)", "Radiant Hope", "Rolling Thunder", "Short Fuse", "Lemon Hearts",
    "Shoeshine", "Smolder",
]

G5 = [
    "Sunny Starscout", "Izzy Moonbow", "Pipp Petals", "Zipp Storm", "Hitch Trailblazer",
    "Misty Brightdawn", "Opalina Acrana", "Sprout Cloverleaf", "Blaize Skysong", "Cloudpuff",
    "Sparky Sparkeroni",
]

LITE_G4 = [
    "Twilight Sparkle", "Rainbow Dash", "Rarity", "Applejack", "Fluttershy", "Pinkie Pie",
    "Spike", "Princess Celestia (Daybreaker)", "Princess Luna (Nightmare Moon)",
    "Starlight Glimmer", "Trixie", "Sunset Shimmer",
]
LITE_G5 = [
    "Sunny Starscout", "Izzy Moonbow", "Pipp Petals", "Zipp Storm", "Hitch Trailblazer",
    "Misty Brightdawn",
]

assert len(G4) == 84, len(G4)
assert len(G5) == 11, len(G5)
assert len(LITE_G4) == 12 and len(LITE_G5) == 6

ALL = G4 + G5
assert len(ALL) == 95 and len(set(ALL)) == 95
series = {n: "G4/EQG" for n in G4}
series.update({n: "G5" for n in G5})

rng = random.SystemRandom()
TZ = timezone(timedelta(hours=8))
now = datetime.now(TZ).isoformat(timespec="seconds")

# --- plus: 95 chars -> 7 teams (14,14,14,14,13,13,13, order shuffled) ---
order = ALL[:]
rng.shuffle(order)
sizes = [14, 14, 14, 14, 13, 13, 13]
rng.shuffle(sizes)
teams = {}
i = 0
for t, s in enumerate(sizes):
    tid = f"T{t}"
    members = order[i:i + s]
    i += s
    teams[tid] = {
        "count": s,
        "series_mix": {
            "G4/EQG": sum(1 for m in members if series[m] == "G4/EQG"),
            "G5": sum(1 for m in members if series[m] == "G5"),
        },
        "members": members,
    }
assert i == 95 and sum(t["count"] for t in teams.values()) == 95

assignment = {
    "package": "ponies-agent-team-v1.1-plus-95c",
    "generated_at": now,
    "random_source": "Python random.SystemRandom() (unseeded => not reproducible by design)",
    "character_count": 95,
    "series_counts": {"G4/EQG": 84, "G5": 11},
    "team_count": 7,
    "teams": teams,
}
(BUILD / "assignment.json").write_text(json.dumps(assignment, ensure_ascii=False, indent=2), encoding="utf-8")
for tid, t in teams.items():
    payload = {
        "package": assignment["package"],
        "team": tid,
        "count": t["count"],
        "series_mix": t["series_mix"],
        "roster": t["members"],
        "output_file": f"ponies-agent-team-v1.1-plus-95c/data/{tid}.md",
    }
    (BUILD / f"team-{tid}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

# --- lite: 18 chars -> 2 teams of 9 ---
lite_order = LITE_G4 + LITE_G5
assert len(lite_order) == 18 and len(set(lite_order)) == 18
rng.shuffle(lite_order)
lite_teams = {
    "T0": {"count": 9, "series_mix": {"G4/EQG": 0, "G5": 0}, "members": lite_order[:9]},
    "T1": {"count": 9, "series_mix": {"G4/EQG": 0, "G5": 0}, "members": lite_order[9:]},
}
for t in lite_teams.values():
    t["series_mix"]["G4/EQG"] = sum(1 for m in t["members"] if series[m] == "G4/EQG")
    t["series_mix"]["G5"] = sum(1 for m in t["members"] if series[m] == "G5")
lite_assignment = {
    "package": "ponies-agent-team-v1.1-lite-18c",
    "generated_at": now,
    "derived_from": "ponies-agent-team-v1.1-plus-95c (subset of its 95 characters)",
    "random_source": "Python random.SystemRandom() (unseeded => not reproducible by design)",
    "character_count": 18,
    "series_counts": {"G4/EQG": 12, "G5": 6},
    "team_count": 2,
    "teams": lite_teams,
}
(BUILD / "lite-assignment.json").write_text(json.dumps(lite_assignment, ensure_ascii=False, indent=2), encoding="utf-8")

# --- scaffold package directories ---
for pkg in ["ponies-agent-team-v1.1-plus-95c", "ponies-agent-team-v1.1-lite-18c"]:
    (ROOT / pkg / "data").mkdir(parents=True, exist_ok=True)
    (ROOT / pkg / "assets").mkdir(parents=True, exist_ok=True)

print("OK", now)
for tid, t in teams.items():
    print(f"{tid}: {t['count']} chars | G4/EQG={t['series_mix']['G4/EQG']} G5={t['series_mix']['G5']} | " + ", ".join(t["members"]))
print()
for tid, t in lite_teams.items():
    print(f"LITE {tid}: {t['count']} chars | " + ", ".join(t["members"]))
