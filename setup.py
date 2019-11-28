import sys
from cx_Freeze import setup, Executable
import os

# os.environ['TCL_LIBRARY'] = r'C:\Python34\tcl\tcl8.6'
# os.environ['TK_LIBRARY'] = r'C:\Python34\tcl\tk8.6'

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options = {"packages": ["os"]}

executables= [Executable('RD_tool.py', base=base, icon=r"static/icone.ico")]
 
 
# On appelle la fonction setup
setup(
    name = "RD_Dedup_tool",
    options = {'built.exe': build_exe_options},
    version = "1.0",
    description = "A - B = C where C is in A but not in B and will be put on suppression list",
    executables = executables
)