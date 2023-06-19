import contextlib
import linecache
import reprlib
import sys
from pathlib import Path
from pdb import Pdb
from pprint import pformat
from textwrap import indent


class PdbLocals(Pdb):
    """
    Adds locals + extra formatting to default Pdb debugger at `breakpoint()`
    """

    def _short_path(self, filename):
        try:
            return Path(filename).resolve().relative_to(Path.cwd())
        except ValueError:
            return Path(filename).resolve()

    def _header(self, lineno):
        name = self.curframe.f_code.co_name or "<lambda>"
        filename = self._short_path(self.curframe.f_code.co_filename)
        return f'File "{filename}" line {lineno} in {name}'

    def _code_line(self, lineno):
        if lineno is not None:
            path = self.canonic(self.curframe.f_code.co_filename)
            if line := linecache.getline(path, lineno, self.curframe.f_globals):
                return indent(line.strip(), " " * 4)

    def _return_value(self):
        if "__return__" in self.curframe.f_locals:
            rv = self.curframe.f_locals["__return__"]
            return "Returning -> " + reprlib.repr(rv)

    def _locals(self):
        local_values = {
            k: v for k, v in self.curframe_locals.items() if k != "__return__"
        }
        result = f"Locals: {pformat(local_values)}"
        if return_value := self._return_value():
            result += "\n" + return_value
        return result

    def format_stack_entry(self, frame_lineno, lprefix=": "):
        _, lineno = frame_lineno
        lines = [self._header(lineno)]
        if line := self._code_line(lineno):
            lines.append(line)
        lines.append(self._locals())
        return "\n\n".join(lines) + "\n"


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
    with debug_with_locals():
        main()
