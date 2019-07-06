#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

"""PySide2 example

"""

"""Credits:
adapted by twallace51@gmail.com
using Linux Mint 19, Python 3.7, PySide2,  geany and pylint3 as IDE
"""

if True: # example support
    # pylint: disable = import-error, multiple-statements, missing-docstring
    import sys
    from PySide2.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
    def p_green(msg): print("\u001b[32;1m" + str(msg) +"\u001b[0m")
    def p_blue(msg): print("\u001b[34;1m" + str(msg) +"\u001b[0m")
    def p_yellow(msg): print("\u001b[33;1m" + str(msg) +"\u001b[0m")
    def p_red(msg): print("\u001b[31;1m" + str(msg) +"\u001b[0m")
    def p_alert(msg): print("\u001b[31;1m\u001b[5m" + str(msg) +"\u001b[0m") # flashing warning

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

    p_green(__doc__)
    p_blue("Press Enter key to continue ....")
    input()

if True: # example code ....

    my_app = QApplication()
    my_window = QWidget()

    my_window.setGeometry(1200, 300, 500, 100)
    my_window.show()

    sys.exit(my_app.exec_())
