"""
When in an interactive session – import these functions and call
activate_pretty to pretty print the result of all expressions
"""

import builtins
import sys
from pprint import pprint


def activate_pretty():
    def hook(value):
        builtins._ = value
        if value is None:
            return
        pprint(value)

    sys.displayhook = hook


def deactivate_pretty():
    sys.displayhook = sys.__displayhook__
