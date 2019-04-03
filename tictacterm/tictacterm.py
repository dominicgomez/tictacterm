import curses


NAME = 'tictacterm'
VERSION = '1.0.0'
YEAR = '2019'
AUTHOR = 'Dominic Gomez'
COPYRIGHT_NOTICE = 'Copyright '+YEAR+' '+AUTHOR

GRID = [
    ' | | ',
    '-+-+-',
    ' | | ',
    '-+-+-',
    ' | | '
]
TOKENS = ['X', 'O']


def main(stdscr):
    h, w = stdscr.getmaxyx()

    stdscr.clear()
    curses.curs_set(0)
    stdscr.box()

    # Render the title.
    y, x = 0, (w-len(NAME))//2
    stdscr.addstr(y, x, NAME)

    # Render the copyright notice.
    y, x = h-1, (w-len(COPYRIGHT_NOTICE))//2
    stdscr.addstr(y, x, COPYRIGHT_NOTICE)

    # Render the grid.
    rows, cols = len(GRID), max(len(ln) for ln in GRID)
    y, x = (h-rows)//2, (w-cols)//2
    for i, ln in enumerate(GRID):
        stdscr.addstr(y+i, x, ln)

    key = None
    while key != ord('q'):
        if key in [ord('h'), curses.KEY_LEFT]:
            pass
        elif key in [ord('j'), curses.KEY_DOWN]:
            pass
        elif key in [ord('k'), curses.KEY_UP]:
            pass
        elif key in [ord('l'), curses.KEY_RIGHT]:
            pass

        stdscr.refresh()

        key = stdscr.getch()


if __name__ == '__main__':
    curses.wrapper(main)
