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
    print("the \"" + videoPath.getVideoPath() + "\" file doesnt exist")


def main(videoAscii):
    print("\nloading video")
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
        userVideoPathArgument = videoPath.getVideoPath()
    finally:
        return userVideoPathArgument


if __name__ == "__main__":
    videoPath.setVideoPath(getVideoPath())
    if not isfile(videoPath.getVideoPath()):
        helpMessage()
    else: 
        videoAscii = getAsciiArray()
        main(videoAscii)

