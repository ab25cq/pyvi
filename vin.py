import curses
import os

EDITOR_MODE = 0
INSERT_MODE = 1

class ViWin:
    def __init__(self, vi):
        self.scrolltop = 0
        self.cursor_x = 0
        self.cursor_y = 0
        self.vi = vi
        
        self.texts = ["ABC", "BBB", "CCC", "DDD", "EEE"]

    def input(self):
        global gAppEnd
        
        key = gStdScr.getch()
        
        if key == ord('j'):
            maxy = curses.LINES
            self.cursor_y = self.cursor_y + 1
            
            if self.cursor_y > self.scrolltop + maxy-1:
                self.scrolltop = self.scrolltop + 1
                self.cursor_y = self.cursor_y -1
            
            if self.cursor_y + self.scrolltop >= len(self.texts):
                self.cursor_y = self.cursor_y - 1
                
        elif key == ord('k'):
            self.cursor_y = self.cursor_y - 1
            
            if self.cursor_y < 0:
                self.scrolltop = self.scrolltop -1
                self.cursor_y = 0
                
                if self.scrolltop < 0:
                    self.scrolltop = 0
            
        elif key == ord('l'):
            self.cursor_x = self.cursor_x + 1
            
            line = self.texts[self.scrolltop+self.cursor_y]
            
            if self.cursor_x >= len(line):
                self.cursor_x = self.cursor_x - 1
        elif key == ord('h'):
            self.cursor_x = self.cursor_x - 1
            
            if self.cursor_x < 0:
                self.cursor_x = 0
        elif key == ord('q'):
            gAppEnd = True
        elif key == ord('i'):
            self.vi.mode = INSERT_MODE
    
    def insert_mode(self):
        key = gStdScr.getch()
        
        if key == 27:
            self.vi.mode = EDITOR_MODE
        else:
            str = "" + chr(key)
            
            if self.scrolltop + self.cursor_y < len(self.texts):
                line = self.texts[self.scrolltop + self.cursor_y]
                self.texts[self.scrolltop + self.cursor_y] = line + str
            else:
                self.texts.append(str)
        
    def view(self):
        maxy = curses.LINES
        gStdScr.clear()
        i = 0
        top = self.scrolltop
        for line in self.texts[top:top+maxy]:
            if i == self.cursor_y:
                gStdScr.addstr(i, 0, line[0:self.cursor_x])
                gStdScr.addstr(i, self.cursor_x, line[self.cursor_x], curses.A_REVERSE)
                gStdScr.addstr(i, self.cursor_x+1, line[self.cursor_x+1:len(line)])
            else :
                gStdScr.addstr(i, 0, line)
            i = i + 1
            
        gStdScr.refresh()

class Vi:
    def __init__(self):
        self.active_win = ViWin(self)
        self.wins = [ self.active_win ]
        self.mode = EDITOR_MODE
        
    def view(self):
        for it in self.wins:
            it.view()
            
    def input(self):
        if self.mode == INSERT_MODE:
            self.active_win.insert_mode()
        else:
            self.active_win.input()

### init curses ###
gStdScr = curses.initscr()
curses.noecho()
curses.cbreak()
gStdScr.keypad(True)
os.environ.setdefault('ESCDELAY', '0')

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

