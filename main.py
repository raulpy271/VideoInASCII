from sys import argv
from os.path import isfile

from src.videoManipulation.resizeVideo \
    import resizeVideo
from src.videoManipulation.extractFrames \
    import getArrayFromResizedVideo
from src.terminalManipulation.asciiLoop \
    import loopInArrayOfAsciiArt
from src.videoManipulation.extractAscii \
    import convertVideoArray2asciiArtList
from src.utils.constants import (
    videoPath, 
    defaultPath)
from src.utils.tempFiles import (
    createTempDir,
    removeTempDir)


def helpMessage():
    print(
"""This program read a video and show it in terminal with ascii art style.
Usage: python main.py [<video_path>] [-R | --repeat] [-H | --help]

    video_path : path of your video, if dont passed the default path are {videoPath}
    -R | --repeat : to repeat the video indefitely, if dont passed then dont repeat.
    -H | --help : show this message

Read more in the README file.
""".format(
        videoPath=defaultPath
        )
    )


def main(videoAscii):
    loopInArrayOfAsciiArt(videoAscii, canRepeat())
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


def canRepeat():
    try:
        return "--repeat" in argv or "-R" in argv
    except: 
        return False


def canShowHelp():
    try:
        return "--help" in argv or "-H" in argv
    except: 
        return False


if __name__ == "__main__":
    videoPath.setVideoPath(getVideoPath())
    if not isfile(videoPath.getVideoPath()) \
        or canShowHelp():
        helpMessage()
    else: 
        print("\nloading video")
        videoAscii = getAsciiArray()
        main(videoAscii)

