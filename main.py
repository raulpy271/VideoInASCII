from sys import argv
from os.path import isfile

from src.utils.constants import videoPath


def main():
    print(videoPath)


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

