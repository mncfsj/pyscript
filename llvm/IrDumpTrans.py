import Init
Init.InitPath()

import sys
from pyscript.file.FileIO import *

if (__name__ == "__main__"):
    srcFile = sys.argv[1]
    destFile = sys.argv[2]
    str = "*** IR Dump"
    copyFile(srcFile, destFile)
    InsertDownLine(destFile, str, "{\n")
    InsertUpLine(destFile, str, "}\n\n")
    deleteFirstLine(destFile)
    deleteFirstLine(destFile)
    appendFileLine(destFile, "}\n")
