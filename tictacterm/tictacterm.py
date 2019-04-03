import curses


NAME = 'tictacterm'
VERSION = '1.0.0'
YEAR = '2019'
AUTHOR = 'Dominic Gomez'
COPYRIGHT_NOTICE = 'Copyright '+YEAR+' '+AUTHOR

GRID = '\n'.join([
    ' | | ',
    '-+-+-',
    ' | | ',
    '-+-+-',
    ' | | '
])
TOKENS = ['X', 'O']


def main(stdscr):
    h, w = stdscr.getmaxyx()

    stdscr.clear()
    stdscr.box()

    stdscr.addstr(0, 2, NAME+' ('+VERSION+')')
    stdscr.addstr(h-2, (w-len(COPYRIGHT_NOTICE))//2, COPYRIGHT_NOTICE)

    key = None
    while key != ord('q'):
        if key == curses.KEY_MOUSE:
            iden, x, y, _, bstate = curses.getmouse()
            stdscr.addstr(0, 0, 'x: '+str(x))
            stdscr.addstr(1, 0, 'y: '+str(y))

        stdscr.refresh()

        key = stdscr.getch()


if __name__ == '__main__':
    curses.wrapper(main)
