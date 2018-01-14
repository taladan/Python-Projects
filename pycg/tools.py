#!/usr/bin/python3
# -*- coding utf-8 -*-
"""
This is a toolbox for pycg.  It should handle all
the debugging and common functions that pycg needs
to have.

Author - Taladan At Gmail dot com
Last Edited: Jan 11, 2018
"""
import functools


class Debugger:
    def io(function):
        @functools.wraps(function)
        def _debug(*args, **kwargs):
            output = function(*args, **kwargs)
            print(f"{function.__name__}({args}, {kwargs}): {output}")
            return output
        return _debug


