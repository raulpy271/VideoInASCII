from statistics import mean
from .constants import ascii_chars


def convertPixel2char(pixel):
    biggestChannelIntensity = 255
    pixelMean = mean(pixel)
    rangeOfEachChar = biggestChannelIntensity / (len(ascii_chars) - 1 )
    return ascii_chars[round(pixelMean / rangeOfEachChar)]

