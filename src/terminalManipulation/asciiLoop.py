from time import sleep

from .asciiTerminal import AsciiWindow
from ..utils.constants import (
    videoResizedFrameRate,
    keyToInterruptTheExecutation)


def loopInArrayOfAsciiArt(arrayOfAsciiArt, repeat=False):
    terminal = AsciiWindow()
    timeToSleepInEachFrame = int(10 * ( 60 / videoResizedFrameRate))


    def isPressedTheKey():
        return (
            waitForACharAndCheckIfMatchWithTheArgument(
                terminal, 
                timeToSleepInEachFrame, 
                keyToInterruptTheExecutation)
            )


    for frame in arrayOfAsciiArt:
        terminal.setAscii(frame)
        if isPressedTheKey():
            terminal.exit()
            return


    if repeat:
        loopInArrayOfAsciiArt(arrayOfAsciiArt, repeat)
    else: 
        terminal.exit()


def waitForACharAndCheckIfMatchWithTheArgument(
    terminal, milisseconds, charToMatch):
    char = terminal.waitForAChar(milisseconds)
    if char == charToMatch:
        return True
    else: return False
