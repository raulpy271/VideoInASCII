from time import sleep

from .asciiTerminal import AsciiWindow
from ..utils.constants import videoResizedFrameRate


def loopInArrayOfAsciiArt(arrayOfAsciiArt):
    terminal = AsciiWindow()
    timeToSleepInEachFrame = 1/videoResizedFrameRate
    for frame in arrayOfAsciiArt:
        terminal.setAscii(frame)
        sleep(timeToSleepInEachFrame)
    terminal.exit()

