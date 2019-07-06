#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""p_code utility     p_code(offset1: int, offset2: int)

This is a utility for sending sections of module code to the terminal window.

Uses inspect() to automatically determine file and lineno where p_code() was called.

Sends corresponding code between offsets (positive or negative) to terminal,
zero and out of range values do not cause error exceptions ....

"""
# pylint: disable = missing-docstring, multiple-statements

def p_yellow(msg): print("\u001b[33;1m" + str(msg) +"\u001b[0m")
def p_green(msg): print("\u001b[32;1m" + str(msg) +"\u001b[0m")
def p_blue(msg): print("\u001b[34;1m" + str(msg) +"\u001b[0m")
def p_red(msg): print("\u001b[31;1m" + str(msg) +"\u001b[0m")

def p_code(title: str, offset1: int = 1, offset2: int = 1, indents: int = 0):
   # pylint: disable = redefined-outer-name
    """
    This function sends code from the currently running module to terminal,
    from current p_code() line + offset1,  to current line + offset2.
    This allows general editing of module code,
    without the need to update the export ranges used for unedited sections of code.
    Note:   negative offsets are okay,  offset defaults are 1,1 ...
            indents will remove multiples of 4 spaces from start of source code lines, default 0
    Original script in "modules/builtins/print/p_code.py"
      """
    print()
    p_green(title)
    import inspect
    callerframerecord = inspect.stack()[1] # 0 represents this lineno, 1 for lineno in caller module
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    current = info.lineno
    text = open(info.filename, 'r')
    line = text.readline()
    n = 0
    while line != "":
        n += 1
        if n > current + offset2:
            break
        if n >= current + offset1:
            code = ">>> "+line[indents*4:]
            p_yellow(code[:-1])
        line = text.readline()
    p_blue("\nPress Enter to run ....")  # <-- runs any code that follows p_code() line
    input()

if __name__ == "__main__":
    p_green(__doc__)
    p_code("""p_code() script:\n""", 16-50, -4)
    print("""Demo done ....""")
