from shutil import rmtree
from os import mkdir
from os.path import isfile

from .constants import (
    tempDir)


def createTempDir():
    if not isfile(tempDir):
        mkdir(tempDir)


def removeTempDir():
    if isfile(tempDir):
        rmtree(tempDir)


