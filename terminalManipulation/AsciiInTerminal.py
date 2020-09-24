import curses

my_ascii = """
asddasdassa
asdasasasasffaafs fas   assgd   fsdfsd  fsdfsf fdsdsfd
sdfsfdsfd

as

d

d"""





class TerminalWindow():
    def __init__(self):
        self.stdscr = curses.initscr()


    def clearTerminal(self):
        self.stdscr.clear()
        self.stdscr.refresh()


    def returnOriginalState(self):
        curses.nocbreak()
        curses.echo()
        curses.endwin()
