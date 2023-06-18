"""Sets a directory relative to _this_ file"""
from pathlib import Path

ASSETS = (Path(__file__) / ".." / "assets").resolve()

with open(ASSETS / "haiku.txt", "r") as f:
    print(f.read())
