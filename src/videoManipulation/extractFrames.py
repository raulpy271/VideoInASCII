import ffmpeg
import numpy 

from ..utils.videoResolution import getVideoResolution
from ..utils.constants import videoResizedPath 


def getArrayFromResizedVideo():
    videoBytes = extractBytesFromResizedVideo()
    videoArray = convertVideoBytes2numpyArray(videoBytes)
    videoResolution = getVideoResolution(videoResizedPath)
    return reshapeVideoArray(videoArray, videoResolution)


def extractBytesFromResizedVideo():
    stream = ffmpeg.input(videoResizedPath)
    stream = ffmpeg.output(stream, 'pipe:', format='rawvideo', pix_fmt='rgb24')
    videoBytes, _ = ffmpeg.run(stream, capture_stdout=True)
    return videoBytes


def convertVideoBytes2numpyArray(videoBytes):
    return numpy.frombuffer(videoBytes, numpy.uint8)


def reshapeVideoArray(videoArray, videoResolution):
    height, width = videoResolution
    return videoArray.reshape([-1, height, width, 3])


