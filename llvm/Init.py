import sys
import os

def InitPath():
    pyscriptDir = os.path.dirname(os.path.dirname(__file__))
    sys.path.append(os.path.dirname(pyscriptDir))
