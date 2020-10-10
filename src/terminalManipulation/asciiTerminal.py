import curses


class AsciiWindow():
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()


    def clearTerminal(self):
        self.stdscr.clear()
        self.stdscr.refresh()


    def setAscii(self, asciiString):
        self.clearTerminal()
        self.stdscr.addstr(asciiString)
        self.stdscr.refresh()


    def waitForAChar(self, milisseconds):
        self.stdscr.timeout(milisseconds)
        return self.stdscr.getch()


    def exit(self):
        curses.nocbreak()
        curses.echo()
        curses.endwin()
