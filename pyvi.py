import curses

stdscr = curses.initscr()

curses.noecho()
curses.cbreak()

stdscr.keypad(True)

stdscr.clear()

stdscr.addstr(0, 0, "HELLO")

stdscr.refresh()
stdscr.getkey()

curses.nocbreak()
stdscr.keypad(False)
curses.echo()

curses.endwin()

