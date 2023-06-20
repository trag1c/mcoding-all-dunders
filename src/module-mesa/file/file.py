"""Sets a directory relative to _this_ file"""
from pathlib import Path

ASSETS = Path(__file__).parent / "assets"

with (ASSETS / "haiku.txt").open() as f:
    print(f.read())
