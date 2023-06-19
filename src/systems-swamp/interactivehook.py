"""
This file needs to be set as a PYTHONSTARTUP environment variable:

    export PYTHONSTARTUP=src/systems-swamp/interactivehook.py

It will then run when an interactive session is started.

Sets all outputs to be pretty printed + adds an introductory message
"""
import builtins
import sys
from pprint import pprint

BANNER = """
********************************************************************************
*********************** Remember to like and subscribe *************************
********************************************************************************
"""


def displayhook(value):
    if value is not None:
        pprint(value)
    builtins._ = value


def _startup():
    print(BANNER)
    sys.displayhook = displayhook


sys.__interactivehook__ = _startup
