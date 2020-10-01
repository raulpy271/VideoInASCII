from statistics import mean

from ..utils.constants import ascii_chars


def convertVideoArray2asciiArtList(videoArray):
    listOfAsciiArt = []
    for frame in videoArray:
        asciiArt = convertImageArray2asciiArt(frame)
        listOfAsciiArt.append(asciiArt)
    return listOfAsciiArt 


def convertImageArray2asciiArt(imageArray):
    asciiArt = ''
    for y in range(0, imageArray.shape[1]):
        for x in range(0, imageArray.shape[0]):
            asciiArt += convertPixel2char(imageArray[x][y])
        asciiArt += '\n'
    return asciiArt


def convertPixel2char(pixel):
    biggestChannelIntensity = 255
    pixelMean = mean(pixel)
    rangeOfEachChar = biggestChannelIntensity / (len(ascii_chars) - 1 )
    return ascii_chars[round(pixelMean / rangeOfEachChar)]

