from numpy import (frombuffer, uint8)

from ..videoManipulation.resizeVideo import resizedVideoResolution
from ..utils.constants import videoResizedPath


def getArrayFromResizedVideo():
    videoBytes = extractBytesFromResizedVideo()
    videoArray = convertVideoBytes2numpyArray(videoBytes)
    videoResolution = resizedVideoResolution()
    return reshapeVideoArray(videoArray, videoResolution)


def extractBytesFromResizedVideo():
    with open(videoResizedPath, 'rb') as videoBytesObject:
        videoBytes = videoBytesObject.read()
        return videoBytes


def convertVideoBytes2numpyArray(videoBytes):
    videoArray = frombuffer(videoBytes, uint8)
    return videoArray 


def reshapeVideoArray(videoArray, videoResolution):
    width, height = videoResolution
    return videoArray.reshape([-1, height, width, 3])


