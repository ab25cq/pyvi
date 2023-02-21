import curses

class ViWin:
    def __init__(self):
        self.scrolltop_x = 0
        self.scrolltop_y = 0
        self.cursor_x = 0
        self.cursor_y = 0
        
        self.texts = []
        
    def input(self):
        global gAppEnd
        
        key = gStdScr.getch()
        
        if key == ord('q'):
            gAppEnd = True
        
    def view(self):
        gStdScr.clear()
        gStdScr.addstr(0, 0, "HELLO")
        gStdScr.refresh()

class Vi:
    def __init__(self):
        self.active_win = ViWin()
        self.wins = [ self.active_win ]
        
    def view(self):
        for it in self.wins:
            it.view()
            
    def input(self):
        self.active_win.input()

### init curses ###
gStdScr = curses.initscr()
curses.noecho()
curses.cbreak()
gStdScr.keypad(True)

### init app ###
gAppEnd = False
gVi = Vi()

### main loop ###

while not gAppEnd:
    gVi.view()
    gVi.input()

# end curses ###
curses.nocbreak()
gStdScr.keypad(False)
curses.echo()

curses.endwin()

