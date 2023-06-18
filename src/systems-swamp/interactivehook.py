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
******************** We in the interactive session, babey! *********************
********************************************************************************
"""


def displayhook(value):
    builtins._ = value
    if value is None:
        return
    pprint(value)


def _startup():
    print(BANNER)
    sys.displayhook = displayhook


sys.__interactivehook__ = _startup
