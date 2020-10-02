import curses


class AsciiWindow():
    def __init__(self):
        self.stdscr = curses.initscr()


    def clearTerminal(self):
        self.stdscr.clear()
        self.stdscr.refresh()


    def setAscii(self, asciiString):
        self.clearTerminal()
        self.stdscr.addstr(asciiString)
        self.stdscr.refresh()


    def exit(self):
        curses.nocbreak()
        curses.echo()
        curses.endwin()
