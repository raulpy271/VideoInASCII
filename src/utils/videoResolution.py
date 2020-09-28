from os import get_terminal_size

import ffmpeg

from .constants import videoPath




def getVideoResolution(videoPath):
    jsonRepresentationOfVideo = (
        ffmpeg.probe(videoPath)["streams"][0])
    return (
        int(jsonRepresentationOfVideo["width"]), 
        int(jsonRepresentationOfVideo["height"]) 
        )




def getNewVideoResolution(videoResolution):
    terminalResolution = get_terminal_size()
    tupleOfaspectRatio = (
        videoResolution[0] / terminalResolution[0],
        videoResolution[1] / terminalResolution[1])


    if tupleOfaspectRatio[0] > tupleOfaspectRatio[1]:
        biggestAspecRatio = tupleOfaspectRatio[0]
    else:
        biggestAspecRatio = tupleOfaspectRatio[1]


    return tuple ( 
        map( int, (
            videoResolution[0] / biggestAspecRatio,
            videoResolution[1] / biggestAspecRatio)
            )
        )




  
