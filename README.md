# basketball-analytics

Parsing and analyzing NBA player statistics in Python.

## Overview

`explorer.py` reads a CSV of per-player season averages, converts each row into a structured record, and answers several questions about the data:

- **Player summaries** — a formatted line for every player showing points, rebounds, and assists
- **Team scoring** — total points contributed by each team, aggregated from its individual players
- **Scorer check** — a reusable function testing whether a given player averages above a points threshold
- **Rebound threshold** — a count of how many players average over 7 rebounds per game

## Data

`data.csv` — one row per player, with columns for name, team, points, rebounds, and assists.

## Running it

```bash
python3 explorer.py
```

No installation required. The script uses only Python's standard library.

## Implementation notes

Everything here is written from scratch rather than with a data analysis library. The CSV is parsed manually with `split()`, rows are converted to dictionaries so fields can be accessed by name instead of position, and the team totals are accumulated by hand — checking whether a team already exists as a key, then either adding to its running total or creating a new entry.

That last operation is what `pandas.groupby()` does in a single line. Building it manually first was a deliberate choice: the goal was to understand what the abstraction is doing before using it.

## Next steps

- Rewrite the same analysis in pandas and compare the two approaches