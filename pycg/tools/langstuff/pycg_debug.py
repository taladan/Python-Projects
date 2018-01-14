#!/usr/bin/python3
# -*- coding utf-8 -*-

"""
pycg_debug.py

This is going to be a debugging tool.

Author: Taladan
Last Edited: December 8, 2017
"""


class pycDebug:

    def __init__(self):
        # Necessary Variables
        self.types = ['debug', 'info', 'warning', 'testing', 'error']
        self.progname = "PyCGen"

    def list_types(self):
        return ', '.join(self.types)

    # Debug Message - passes a message of type 'dt'
    """
    Example to use the pycg_debug module

    d = debug()
    print(d.debug_msg('info', 'details.py',
                        'Info to test initUI printing a debug message.'))
    """
    def debug_msg(self, dt, module_name, msg):
        try:
            if dt.lower() not in self.types:
                return str(self.progname + "  --  " + module_name +
                           "debug type must be one of: " + self.types)
            else:
                return str(self.progname + " -- " + module_name + " " + dt +
                           " : " + msg)
        except ValueError:
            return str(""" debug_msg must have three arguments: Debug Type
                       Debug type must be one of: """ + self.list_types() +
                       """ The name of the calling module, and the message to be
                       passed.""")
