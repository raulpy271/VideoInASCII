from sys import argv
from os.path import isfile
from time import sleep

from src.videoManipulation.resizeVideo import resizeVideo
from src.videoManipulation.extractFrames import getArrayFromResizedVideo
from src.terminalManipulation.asciiLoop import loopInArrayOfAsciiArt
from src.videoManipulation.extractAscii import convertVideoArray2asciiArtList
from src.utils.constants import videoPath
from src.utils.tempFiles import (
    createTempDir,
    removeTempDir)


def main():
    print("\nloading video")


    removeTempDir()
    createTempDir()
    resizeVideo()
    video = getArrayFromResizedVideo()
    videoAscii = convertVideoArray2asciiArtList(video)
    print(
        "\nvideo loaded" +
        "\nentering in the loop, press C-d to cancel the ascii loop")


    sleep(1)
    loopInArrayOfAsciiArt(videoAscii)
    removeTempDir()



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
        print("the \"" + videoPath + "\" file doesnt exist")
    else: main()

