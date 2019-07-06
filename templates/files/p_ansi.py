#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""Colorized printing to terminal, using ansi codes

Reference:
  http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

For alternative, refer to:
  https://pypi.org/project/plumbum/
"""

if True: # ansi escapes for color to terminal
    #pylint: disable = multiple-statements, missing-docstring
    def clear_scr(): print("\u001b[2J")
    def p_red(msg): print("\u001b[31;1m" + str(msg) +"\u001b[0m")
    def p_green(msg): print("\u001b[32;1m" + str(msg) +"\u001b[0m")
    def p_yellow(msg): print("\u001b[33;1m" + str(msg) +"\u001b[0m")
    def p_blue(msg): print("\u001b[34;1m" + str(msg) +"\u001b[0m")
    def p_mag(msg): print("\u001b[35;1m" + str(msg) +"\u001b[0m")
    def p_cyan(msg): print("\u001b[36;1m" + str(msg) +"\u001b[0m")
    def p_white(msg): print("\u001b[37;1m" + str(msg) +"\u001b[0m")
    def p_orange(msg): print("\u001b[38;5;208m" +  str(msg) +"\u001b[0m")
    def p_alert(msg): print("\u001b[31;1m\u001b[5m" + str(msg) +"\u001b[0m") # flashing warning


if __name__ == "__main__":
    p_green(__doc__)

