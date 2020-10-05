import ffmpeg
from numpy import (frombuffer, uint8)

from ..utils.videoResolution import getVideoResolution
from ..utils.constants import (
    videoResizedPath,
    ffmpegGlobalArguments)


def getArrayFromResizedVideo():
    videoBytes = extractBytesFromResizedVideo()
    videoArray = convertVideoBytes2numpyArray(videoBytes)
    videoResolution = getVideoResolution(videoResizedPath)
    return reshapeVideoArray(videoArray, videoResolution)


def extractBytesFromResizedVideo():
    stream = ffmpeg.input(videoResizedPath)
    stream = ffmpeg.output(stream, 'pipe:', format='rawvideo', pix_fmt='rgb24')
    stream = stream.global_args(*ffmpegGlobalArguments)
    videoBytes, _ = ffmpeg.run(stream, capture_stdout=True)
    return videoBytes


def convertVideoBytes2numpyArray(videoBytes):
    return frombuffer(videoBytes, uint8)


def reshapeVideoArray(videoArray, videoResolution):
    width, height = videoResolution
    return videoArray.reshape([-1, height, width, 3])


