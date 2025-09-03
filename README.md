# Fantasy Draft Order Generator

A Python script that generates fair and deterministic fantasy draft order using SHA-256 hashing.

## How it works

1. Uses team names from `team_names.txt` combined with owner names
2. Generates SHA-256 hashes for each team
3. Sorts teams by hash value (ascending) to determine draft order
4. Provides fallback mechanism for missing team names

## Usage

```bash
python src/fantasy_final.py
```

## Features

- **Deterministic**: Same team names always produce the same order
- **Fair**: SHA-256 ensures unpredictable but consistent ordering
- **Auditable**: Shows hash material and timestamp for verification
- **Flexible**: Handles missing/invalid team names with fallbacks

## Output

The script displays:
- Draft order (1st pick, 2nd pick, etc.)
- Team names and SHA-256 hashes
- Audit information including hash materials