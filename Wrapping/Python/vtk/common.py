""" This module loads all the classes from the VTK Common library into its
namespace.  This is a required module."""

import os

if os.name == 'posix':
    from libvtkCommonPython import *
else:
    from vtkCommonPython import *
