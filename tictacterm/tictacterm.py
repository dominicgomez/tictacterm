import curses
import math


PROG = 'tictacterm'
VER = '1.0.0'
YEAR = '2019'
AUTHOR = 'Dominic Gomez'
COPR_NOTICE = 'Copyright '+YEAR+' '+AUTHOR

HLINE = u'\u2500'
PLUS = u'\u253C'
VLINE = u'\u2502'
CUR = u'\u2588'

ROWS = 3
COLS = 3
# CELL_H = 1
# CELL_W = 1
# GRID = [
#     PLUS.join([HLINE*CELL_WIDTH]*3)
# ]
# I'm just gonna do it the cheap way for now.
GRID = [
    ' | | ',
    '-+-+-',
    ' | | ',
    '-+-+-',
    ' | | '
]

PLAYERS = ['X', 'O']


def main():
    stdscr = curses.initscr()
    _prepterm(stdscr)

    h, w = stdscr.getmaxyx()

    # Render the title.
    _, x = _center(stdscr, 1, len(PROG))
    title_y, title_x = 0, x
    stdscr.addstr(title_y, title_x, PROG)

    # Create the grid window.
    lines, cols = len(GRID), max(len(ln) for ln in GRID)
    grid_y, grid_x = _center(stdscr, lines, cols)
    gridwin = stdscr.derwin(lines, cols, grid_y, grid_x)
    # gridwin.box() makes something fail. FIXME
    # Render the grid.
    for i, ln in enumerate(GRID):
        stdscr.addstr(grid_y+i, grid_x, ln)

    # Create the player windows.
    p1win = stdscr.derwin(h-3, grid_x-1, 1, 1)
    p2win = stdscr.derwin(h-3, w-(grid_x+cols)-1, 1, grid_x+cols)
    # Render the player labels.
    p1label_y, p1label_x = _center(p1win, 1, len(PLAYERS[0]))
    p2label_y, p2label_x = _center(p2win, 1, len(PLAYERS[1]))
    p1win.addstr(
        p1label_y,
        p1label_x,
        PLAYERS[0],
        curses.color_pair(1) | curses.A_STANDOUT
    )
    p2win.addstr(p2label_y, p2label_x, PLAYERS[1], curses.color_pair(4))

    # Create the message window (2 cells narrower than the terminal window to
    # avoid the border).
    msgwin = stdscr.derwin(1, w-2, h-2, 1)
    # Display the copyright notice in the message window.
    msgwin.addstr(0, 0, COPR_NOTICE, curses.A_DIM)

    # Render the cursor.
    cursor_y, cursor_x = _termpos(1, 1)
    gridwin.addstr(cursor_y, cursor_x, CUR, curses.A_BLINK)

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
        elif key in [ord('\n'), ord(' ')]:
            pass

        stdscr.refresh()
        gridwin.refresh()
        p1win.refresh()
        p2win.refresh()
        msgwin.refresh()

        key = stdscr.getch()

    _resetterm(stdscr)


def _prepterm(stdscr):
    # Prepare the terminal for rendering.

    # These changes must be reset when the program terminates.
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    curses.curs_set(False)
    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_RED, -1)
        curses.init_pair(2, curses.COLOR_GREEN, -1)
        curses.init_pair(3, curses.COLOR_YELLOW, -1)
        curses.init_pair(4, curses.COLOR_BLUE, -1)
        curses.init_pair(5, curses.COLOR_MAGENTA, -1)
        curses.init_pair(6, curses.COLOR_CYAN, -1)

    stdscr.clear()
    stdscr.box()


def _termpos(row, col):
    if (row, col) == (0, 0):
        return (0, 0)
    elif (row, col) == (0, 1):
        return (0, 2)
    elif (row, col) == (0, 2):
        return (0, 4)
    elif (row, col) == (1, 0):
        return (2, 0)
    elif (row, col) == (1, 1):
        return (2, 2)
    elif (row, col) == (1, 2):
        return (2, 4)
    elif (row, col) == (2, 0):
        return (4, 0)
    elif (row, col) == (2, 1):
        return (4, 2)
    elif (row, col) == (2, 2):
        return (4, 4)
    else:
        pass


def _center(win, elem_h, elem_w):
    h, w = win.getmaxyx()
    return math.floor((h-elem_h)/2), math.floor((w-elem_w)/2)


def _resetterm(stdscr):
    # Reset changes made to the terminal on startup.
    stdscr.keypad(False)
    curses.nocbreak()
    curses.echo()
    curses.endwin()


if __name__ == '__main__':
    main()
