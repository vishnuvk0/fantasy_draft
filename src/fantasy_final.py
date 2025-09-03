#!/usr/bin/env python3
import hashlib
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

NAMES = [
    "vishnu",
    "siddharth",
    "abhiram",
    "sayak",
    "gursimar",
    "shivi",
    "wahidur",
    "rishi",
    "tanav",
    "tanay",
    "andypramith",
    "abhay",
]

TEAM_FILE = Path("team_names.txt")
PACIFIC_TZ = ZoneInfo("America/Los_Angeles")

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def is_valid_team_name(s: str) -> bool:
    """
    Team name must start and end with a non-space character.
    Any characters (spaces inside, symbols, casing) are allowed.
    """
    if not s:
        return False  # empty handled separately (fallback)
    return s == s.strip()

def load_team_names() -> list[str]:
    """
    Load (or initialize) team names file so it has exactly len(NAMES) lines.
    Extra lines are ignored; missing lines are padded with "".
    """
    if not TEAM_FILE.exists():
        TEAM_FILE.write_text("\n" * (len(NAMES) - 1), encoding="utf-8")
    lines = TEAM_FILE.read_text(encoding="utf-8").splitlines()
    # normalize length
    if len(lines) < len(NAMES):
        lines += [""] * (len(NAMES) - len(lines))
    elif len(lines) > len(NAMES):
        lines = lines[:len(NAMES)]
    return lines

def save_team_names(team_names: list[str]) -> None:
    TEAM_FILE.write_text("\n".join(team_names), encoding="utf-8")

def main():
    print("Fantasy Draft Order Generator")
    print("Using existing team names from file.")
    print()

    team_names = load_team_names()

    # One timestamp per run for all fallbacks
    run_ts = datetime.now(PACIFIC_TZ).isoformat()

    # Collect finalized names for hashing and for saving
    finalized_team_names: list[str] = []

    for idx, gov_name in enumerate(NAMES):
        current = team_names[idx]
        
        # Use existing names or fallback
        if current and is_valid_team_name(current):
            finalized_team_names.append(current)
        else:
            finalized_team_names.append("")  # marker for fallback later

    # Persist any edits (non-empty kept or replaced; empty lines stay empty)
    save_team_names(finalized_team_names)

    results = []
    for gov_name, team in zip(NAMES, finalized_team_names):
        if team:
            material = f"{gov_name}{team}"  # exact: no delimiter, gov_name is already lowercase in NAMES
            note = ""
        else:
            material = f"{gov_name}ganeshcock{run_ts}"
            note = "(fallback used: ganeshcock + timestamp)"
        digest = sha256_hex(material)
        results.append({
            "name": gov_name,
            "team_name": team if team else "<no team name>",
            "sha256": digest,
            "hash_material": material,
            "note": note,
        })

    # Sort by hex digest lexicographically (ascending)
    results.sort(key=lambda r: r["sha256"])

    # Output
    print("\n=== DRAFT ORDER (ascending by SHA-256 hex) ===")
    for i, r in enumerate(results, start=1):
        note = f"  {r['note']}" if r["note"] else ""
        print(f"{i:2d}. {r['name']:12s} | Team: {r['team_name']}{note}")
        print(f"    SHA256: {r['sha256']}")

    print("\nAudit info:")
    print(f"- Run timestamp (Pacific): {run_ts}")
    print("- Hash material for each entry is shown below:")
    for r in results:
        print(f"{r['name']:12s} -> {r['hash_material']}")

    print("\nSaved updated team names to:", TEAM_FILE.resolve())

if __name__ == "__main__":
    main()

