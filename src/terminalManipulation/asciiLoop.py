from time import sleep

from .asciiTerminal import AsciiWindow
from ..utils.constants import videoResizedFrameRate


def loopInArrayOfAsciiArt(arrayOfAsciiArt, repeat=False):
    terminal = AsciiWindow()
    timeToSleepInEachFrame = 1/videoResizedFrameRate
    for frame in arrayOfAsciiArt:
        terminal.setAscii(frame)
        sleep(timeToSleepInEachFrame)
    if repeat:
        loopInArrayOfAsciiArt(arrayOfAsciiArt, repeat)
    else: terminal.exit()


