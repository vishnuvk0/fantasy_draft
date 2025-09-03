# Fantasy Draft Order Generator

A Python script that generates fair and deterministic fantasy draft order using SHA-256 hashing.

## How it works

1. `govt_first_name`.append(`team_name`). using team names from `team_names.txt`.
2. Generates SHA-256 hashes for each person
3. Sorts teams by hash value (ascending) to determine draft order
4. fallback mechanism first_name + "ganeshcock"+ `date_time` for missing team names.

## Usage
run by a github actions workflow.
https://github.com/vishnuvk0/fantasy_draft/actions
```bash
python3 src/fantasy_final.py
```

## Features

- **Deterministic**: Same team names always produce the same order
- **Fair**: SHA-256 ensures unpredictable but consistent ordering
- **Auditable**: hash material and timestamp for verification

## Output

The script displays:
- Draft order (1st pick, 2nd pick, etc.)
- Team names and SHA-256 hashes
- Audit info
