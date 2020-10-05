from math import floor

import ffmpeg

from ..utils.videoResolution import (
    getVideoResolution,
    getNewVideoResolution)
from ..utils.constants import (
    ffmpegGlobalArguments,
    videoResizedFrameRate,
    videoPath,
    videoResizedPath) 


def resizeVideo():
    newResolution = (
        getNewVideoResolution(getVideoResolution(videoPath.getVideoPath())))
    evenResolution = forceResolutionBeDivisibleBy2(newResolution)
    outputArguments = {
        'r' : videoResizedFrameRate,
        'vf' : 
            'scale=' + tupleOfResolution2String(evenResolution)
        }
    stream = ffmpeg.input(videoPath.getVideoPath())
    stream = ffmpeg.output(stream, videoResizedPath, **outputArguments )
    stream = stream.global_args(*ffmpegGlobalArguments)

    ffmpeg.run(stream)


def forceResolutionBeDivisibleBy2(tupleOfresolution):
    return tuple(
        map((lambda x: (floor(x / 2)) * 2 ), tupleOfresolution)
        )


def tupleOfResolution2String(tupleOfresolution):
    return (
        str(tupleOfresolution[0]) + ':' + str(tupleOfresolution[1])
        )

