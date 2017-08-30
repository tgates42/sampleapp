#!/usr/bin/env python
"""\
%(app)s

Usage:
   %(cmd)s [options]
   %(cmd)s (-h | --help)
   %(cmd)s --version

Options:
  -h --help              Show this screen
  --version              Show version

"""
# vi:syntax=python

from __future__ import print_function, division

import sys
import os

__version__ = '0.1'
__appname__ = None

def main():
    """
    Read command line options and pass to the main command line entry point.
    """
    run_main()

def get_basedir():
    """
    Locate the current directory of this file
    """
    return os.path.dirname(os.path.abspath(sys.modules[__name__].__file__))

def run_main():
    """
    Main Command Line Entry Point
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sampleapp.settings")
    sys.path.append(os.path.join(get_basedir(), 'sampleapp'))
    from django.core.management import execute_from_command_line
    execute_from_command_line([sys.argv[0], 'runserver', '0.0.0.0:80'])

if __name__ == '__main__':
    main()

# vim: set ft=python:
