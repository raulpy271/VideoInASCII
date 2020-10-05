from sys import argv
from os.path import isfile

from src.videoManipulation.resizeVideo import resizeVideo
from src.videoManipulation.extractFrames import getArrayFromResizedVideo
from src.terminalManipulation.asciiLoop import loopInArrayOfAsciiArt
from src.videoManipulation.extractAscii import convertVideoArray2asciiArtList
from src.utils.constants import videoPath
from src.utils.tempFiles import (
    createTempDir,
    removeTempDir)


def helpMessage():
    print("the \"" + videoPath + "\" file doesnt exist")


def main():
    print("\nloading video")
    videoAscii = getAsciiArray()
    loopInArrayOfAsciiArt(videoAscii)
    removeTempDir()


def getAsciiArray():
    removeTempDir()
    createTempDir()
    resizeVideo()
    video = getArrayFromResizedVideo()
    videoAscii = convertVideoArray2asciiArtList(video)
    return videoAscii


def getVideoPath():
    try:
        userVideoPathArgument = str(argv[1])
    except: 
        userVideoPathArgument = videoPath
    finally:
        return userVideoPathArgument


if __name__ == "__main__":
    videoPath = getVideoPath()
    if not isfile(videoPath):
        helpMessage()
    else: main()

