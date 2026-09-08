#!/usr/bin/env python3
"""Validate repository JSON, JSON-LD and Turtle files."""

from __future__ import annotations

import json
from pathlib import Path

from rdflib import Graph


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    for path in sorted(ROOT.rglob("*.json*")):
        with path.open(encoding="utf-8") as stream:
            json.load(stream)
        print(f"JSON OK: {path.relative_to(ROOT)}")

    for path in sorted(ROOT.glob("*.ttl")):
        Graph().parse(path, format="turtle")
        print(f"Turtle OK: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
