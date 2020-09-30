from math import floor

import ffmpeg

from ..utils.videoResolution import (
    getVideoResolution,
    getNewVideoResolution)
from ..utils.constants import (
    videoResizedFrameRate,
    videoPath,
    videoResizedPath) 


def resizeVideo(videoPath):
    newResolution = (
        getNewVideoResolution(getVideoResolution(videoPath)))
    evenResolution = forceResolutionBeDivisibleBy2(newResolution)
    ffmpegArguments = {
        'r' : videoResizedFrameRate,
        'vf' : 
            'scale=' + tupleOfResolution2String(evenResolution)
        }
    stream = ffmpeg.input(videoPath)
    stream = ffmpeg.output(stream, videoResizedPath, **ffmpegArguments)
    ffmpeg.run(stream)


def forceResolutionBeDivisibleBy2(tupleOfresolution):
    return tuple(
        map((lambda x: (floor(x / 2)) * 2 ), tupleOfresolution)
        )


def tupleOfResolution2String(tupleOfresolution):
    return (
        str(tupleOfresolution[0]) + ':' + str(tupleOfresolution[1])
        )

