#!/usr/bin/python3
# -*- coding utf-8 -*-

"""
Author: Taladan
Last Edited: Jan 6, 2018
"""

import functools


"""
debug(function) -- Outputs the name of the function,
*args and **kwargs passed to it
"""

def debug(function):
    @functools.wraps(function)
    def _debug(*args, **kwargs):
        output = function(*args, **kwargs)
        print('%s(%r, %r): %r' % (function.__name, args, kwargs, output))

        return output
    return _debug
