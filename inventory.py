"""A small shop inventory, used to show SecureLint on pull requests."""

import json
import pickle
import sys
from pathlib import Path

STOCK_FILE = Path("stock.json")
CACHE_FILE = Path("stock.cache")


def load_stock() -> dict[str, int]:
    if CACHE_FILE.exists():
        # An old shortcut, known and accepted for now (listed in the baseline).
        return pickle.loads(CACHE_FILE.read_bytes())
    return json.loads(STOCK_FILE.read_text(encoding="utf-8"))


def show_stock(stock: dict[str, int]) -> None:
    for item, count in sorted(stock.items()):
        print(f"{item:<20} {count:>5}")


def main() -> int:
    stock = load_stock()
    if len(sys.argv) > 1 and sys.argv[1] == "show":
        show_stock(stock)
        return 0
    print("usage: python inventory.py show")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
