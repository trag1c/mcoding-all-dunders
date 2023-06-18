"""Adds locals to breaks?"""
import contextlib
import linecache
import reprlib
import sys
from pathlib import Path
from pdb import Pdb
from pprint import pformat
from textwrap import indent


class PdbLocals(Pdb):
    @staticmethod
    def _short_path(filename) -> Path:
        """
        Returns a relative path to the frame file if possible or an absolute path
        """
        try:
            return Path(filename).resolve().relative_to(Path.cwd())
        except ValueError:
            return Path(filename).resolve()

    def format_stack_entry(self, frame_lineno, lprefix=': '):
        frame, lineno = frame_lineno
        name = frame.f_code.co_name if frame.f_code.co_name else "<lambda>"
        filename = PdbLocals._short_path(frame.f_code.co_filename)
        lines = [f"File \"{filename}\" line {lineno} in {name}", ""]

        if lineno is not None:
            path = self.canonic(frame.f_code.co_filename)
            if line := linecache.getline(path, lineno, frame.f_globals):
                lines += [indent(line.strip(), " " * 4), ""]

        lines += [f"Locals: {pformat(self.curframe_locals)}"]

        if '__return__' in frame.f_locals:
            rv = frame.f_locals['__return__']
            lines += ["Returning -> " + reprlib.repr(rv)]
        lines += [""]

        return "\n".join(lines)


def set_trace(*, header=None):
    pdb = PdbLocals()
    if header is not None:
        pdb.message(header)
    pdb.set_trace(sys._getframe().f_back)


@contextlib.contextmanager
def locals_debugger():
    sys.breakpointhook = set_trace
    yield
    sys.breakpointhook = sys.__breakpointhook__


# Example
def foo(x, y):
    z = x + y
    return z


def main():
    with locals_debugger():
        breakpoint()
        result = foo(1, 1)
        print(result)


if __name__ == "__main__":
    main()
