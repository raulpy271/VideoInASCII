from shutil import rmtree
from os import mkdir
from os.path import isdir

from .constants import (
    tempDir)


def createTempDir():
    if not isdir(tempDir):
        mkdir(tempDir)


def removeTempDir():
    if isdir(tempDir):
        rmtree(tempDir)


