from time import sleep

from .asciiTerminal import AsciiWindow
from ..utils.constants import videoResizedFrameRate


def loopInArrayOfAsciiArt(arrayOfAsciiArt):
    terminal = AsciiWindow()
    for frame in arrayOfAsciiArt:
        terminal.setAscii(frame)
        sleep(1/videoResizedFrameRate)
    terminal.exit()
