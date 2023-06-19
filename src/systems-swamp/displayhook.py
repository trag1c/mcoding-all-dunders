"""
When in an interactive session – import these functions and call
activate_pretty to pretty print the result of all expressions
"""

import builtins
import sys
from pprint import pprint


def activate_pretty():
    def hook(value):
        if value is not None:
            pprint(value)
        builtins._ = value

    sys.displayhook = hook


def deactivate_pretty():
    sys.displayhook = sys.__displayhook__
