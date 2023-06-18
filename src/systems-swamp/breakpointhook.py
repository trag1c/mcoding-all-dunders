"""Adds locals to default Pdb debugger at `breakpoint()`"""
import contextlib
import linecache
import reprlib
import sys
from pathlib import Path
from pdb import Pdb
from pprint import pformat
from textwrap import indent


class PdbLocals(Pdb):
    """Pdb... with locals (and some minor formatting)"""

    def _short_path(self, filename) -> Path:
        try:
            return Path(filename).resolve().relative_to(Path.cwd())
        except ValueError:
            return Path(filename).resolve()

    def _header(self, frame, lineno):
        name = frame.f_code.co_name if frame.f_code.co_name else "<lambda>"
        filename = self._short_path(frame.f_code.co_filename)
        return f'File "{filename}" line {lineno} in {name}'

    def _code_line(self, frame, lineno):
        if lineno is not None:
            path = self.canonic(frame.f_code.co_filename)
            if line := linecache.getline(path, lineno, frame.f_globals):
                return indent(line.strip(), " " * 4)

    def _return_value(self, frame):
        if "__return__" in frame.f_locals:
            rv = frame.f_locals["__return__"]
            return "Returning -> " + reprlib.repr(rv)

    def _locals(self):
        return {
            k: v for k, v in self.curframe_locals.items() if k != "__return__"
        }

    def format_stack_entry(self, frame_lineno, lprefix=": "):
        frame, lineno = frame_lineno
        lines = [self._header(frame, lineno) + "\n"]
        if line := self._code_line(frame, lineno):
            lines.append(line + "\n")
        lines.append(f"Locals: {pformat(self._locals())}")
        if return_value := self._return_value(frame):
            lines.append(return_value)
        lines.append("")
        return "\n".join(lines)


def set_trace(*, header=None):
    pdb = PdbLocals()
    if header is not None:
        pdb.message(header)
    pdb.set_trace(sys._getframe().f_back)


@contextlib.contextmanager
def debug_with_locals():
    sys.breakpointhook = set_trace
    yield
    sys.breakpointhook = sys.__breakpointhook__


# Example
def foo(x, y):
    z = x + y
    return z


def main():
    breakpoint()
    result = foo(1, 1)
    print(result)


if __name__ == "__main__":
    # enter "continue" before main finishes the first time
    with debug_with_locals():
        main()
    main()
