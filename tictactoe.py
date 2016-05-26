import curses
import curses.textpad
import random
import time


board = [' '] * 10
# board[0] = "X"

z = 0  # for the 'playersymbol' function


def test(i, screen, dims):  # alternates between 'X' and 'O'
    global z
    if z == 0:
        s = 'X'
        board[i] = s
        z += 1
        # fills the list of moves with the players' corresponding symbols
        return "X"
    else:
        s = "O"
        board[i] = s
        z -= 1
        return "O"


def get_computer_move(screen, dims):
    i = random.randrange(1, 10)
    if i == 7:
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6), int(dims[1]/6), test(i, screen, dims))
    elif i == 8:
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6), int(dims[1]/2), test(i, screen, dims))
    elif i == 9:
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6), int(dims[1]/6*5), test(i, screen, dims))
    elif i == 4:
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6*3), int(dims[1]/6), test(i, screen, dims))
    elif i == 5:
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6*3), int(dims[1]/2), test(i, screen, dims))
    elif i == 6:
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6*3), int(dims[1]/6*5), test(i, screen, dims))
    elif i == 1:
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6*5), int(dims[1]/6), test(i, screen, dims))
    elif i == 2:
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6*5), int(dims[1]/2), test(i, screen, dims))
    elif i == 3:
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6*5), int(dims[1]/6*5), test(i, screen, dims))
    return()


def rewrite(i):  # to avoid overwriting existing steps
    global board
    global write
    global c
    if board[i] == " ":
        write = True
    else:
        write = False


def tie(screen, dims):
    check = 0
    for r in range(0, 10):
        if board[r] == "X":
            check += 1
    return(check > 4)


def getPlayerMove(c, screen, dims):
    # prints the players' symbols on the space associated with the num keys
    if c == ord('7'):
        i = 7
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6), int(dims[1]/6), test(i, screen, dims))
    elif c == ord('8'):
        i = 8
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6), int(dims[1]/2), test(i, screen, dims))
    elif c == ord('9'):
        i = 9
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6), int(dims[1]/6*5), test(i, screen, dims))
    elif c == ord('4'):
        i = 4
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6*3), int(dims[1]/6), test(i, screen, dims))
    elif c == ord('5'):
        i = 5
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6*3), int(dims[1]/2), test(i, screen, dims))
    elif c == ord('6'):
        i = 6
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6*3), int(dims[1]/6*5), test(i, screen, dims))
    elif c == ord('1'):
        i = 1
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6*5), int(dims[1]/6), test(i, screen, dims))
    elif c == ord('2'):
        i = 2
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6*5), int(dims[1]/2), test(i, screen, dims))
    elif c == ord('3'):
        i = 3
        rewrite(i)
        if write:
            screen.addstr(int(dims[0]/6*5), int(dims[1]/6*5), test(i, screen, dims))
    return()

player1 = "X"
player2 = "O"


def winner1():  # returns true if player1 wins

    global player1
    global board
    return ((board[7] == player1 and board[8] == player1 and board[9] == player1) or  # horizontal
            (board[4] == player1 and board[5] == player1 and board[6] == player1) or  # horizontal
            (board[1] == player1 and board[2] == player1 and board[3] == player1) or  # horizontal
            (board[7] == player1 and board[4] == player1 and board[1] == player1) or  # vertical
            (board[8] == player1 and board[5] == player1 and board[2] == player1) or  # vertical
            (board[9] == player1 and board[6] == player1 and board[3] == player1) or  # vertical
            (board[7] == player1 and board[5] == player1 and board[3] == player1) or  # diagonal
            (board[9] == player1 and board[5] == player1 and board[1] == player1))  # diagonal


def winner2():  # returns true if player2 wins
    global player2
    global board
    return ((board[7] == player2 and board[8] == player2 and board[9] == player2) or  # horizontal
            (board[4] == player2 and board[5] == player2 and board[6] == player2) or  # horizontal
            (board[1] == player2 and board[2] == player2 and board[3] == player2) or  # horizontal
            (board[7] == player2 and board[4] == player2 and board[1] == player2) or  # vertical
            (board[8] == player2 and board[5] == player2 and board[2] == player2) or  # vertical
            (board[9] == player2 and board[6] == player2 and board[3] == player2) or  # vertical
            (board[7] == player2 and board[5] == player2 and board[3] == player2) or  # diagonal
            (board[9] == player2 and board[5] == player2 and board[1] == player2))  # diagonal


def winning(screen, dims, name1, name2):  # whether one of the players won, prints this text
    if winner1():
        screen.addstr(int(dims[0]/2-2), int(dims[1]/2-7), name1 + " won!")  # X
    elif winner2():
        screen.addstr(int(dims[0]/2-2), int(dims[1]/2-7), name2 + " won!")  # O
    return()


def one_player(screen, name1, name2):
    global z
    dims = screen.getmaxyx()
    screen = curses.newwin(int(dims[0]), int(dims[1]), 0, 0)
    screen.box()
    for i in range(0, int(dims[0])):
        screen.addstr(i, int(dims[1]/3), '|')  # vertical
        screen.addstr(i, int(dims[1]/3*2), '|')
    for i in range(0, int(dims[1])):
        screen.addstr(int(dims[0]/3), i, '_')  # horizontal
        screen.addstr(int(dims[0]/3*2), i, '_')
    screen.addstr(0, 1, "TIC-TAC-TOE ------ Use number keys to place 'X' and 'O', press 'q' to quit.")
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    curses.curs_set(0)

    while True:
        if winner1() or winner2():  # if one of the players won
            winning(screen, dims, name1, name2)
            screen.refresh()
            c = screen.getch()
            if c == ord('q'):  # if 'q' pressed the game exits
                break  # Exit the while loop
        elif tie(screen, dims):
            screen.addstr(int(dims[0]/2-2), int(dims[1]/2-7), "It's tie!")
            c = screen.getch()
            if c == ord('q'):  # if 'q' pressed the game exits
                break  # Exit the while loop
        elif z == 0:
            c = screen.getch()
            if c == ord('q'):  # if 'q' pressed the game exits
                break  # Exit the while loop
            elif z == 0:  # if 'q' is not pressed the game continues
                getPlayerMove(c, screen, dims)
                screen.refresh()
        else:
            get_computer_move(screen, dims)
            time.sleep(1)
    curses.endwin()


def multi_player(screen, name1, name2):
    global z
    dims = screen.getmaxyx()
    screen = curses.newwin(int(dims[0]), int(dims[1]), 0, 0)
    screen.box()
    for i in range(0, int(dims[0])):
        screen.addstr(i, int(dims[1]/3), '|')  # vertical
        screen.addstr(i, int(dims[1]/3*2), '|')
    for i in range(0, int(dims[1])):
        screen.addstr(int(dims[0]/3), i, '_')  # horizontal
        screen.addstr(int(dims[0]/3*2), i, '_')
    screen.addstr(0, 1, "TIC-TAC-TOE ------ Use number keys to place 'X' and 'O', press 'q' to quit.")
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    curses.curs_set(0)

    while True:
        if winner1() or winner2():  # if one of the players won
            winning(screen, dims, name1, name2)
            screen.refresh()
            c = screen.getch()
            if c == ord('q'):  # if 'q' pressed the game exits
                break  # Exit the while loop
        elif tie(screen, dims):
            screen.addstr(int(dims[0]/2-2), int(dims[1]/2-7), "It's tie!")
            c = screen.getch()
            if c == ord('q'):  # if 'q' pressed the game exits
                break  # Exit the while loop
        else:
            c = screen.getch()
            if c == ord('q'):  # if 'q' pressed the game exits
                break  # Exit the while loop
            else:  # if 'q' is not pressed the game continues
                getPlayerMove(c, screen, dims)
                screen.refresh()
    curses.endwin()


def menu(screen, name1, name2, multi_single):
    dims = screen.getmaxyx()
    screen = curses.newwin(int(dims[0]), int(dims[1]), 0, 0)
    screen.box()
    screen.addstr(0, int(dims[1]/2-4), "MENU")
    screen.addstr(5, 5, 'Welcome ' + name1 + " and " + name2 + ' in this TicTacToe Game!')
    screen.addstr(10, 3, 'If you need help, press "h" or press "s" to start a game against computer!')
    while True:
        c = screen.getch()
        screen.refresh()
        if c == ord('h'):
            screen.addstr(15, 5, 'You can navigate the symbols with num keys!')
        elif c == ord('s'):
            if multi_single == 1:
                one_player(screen, name1, name2)
            else:
                multi_player(screen, name1, name2)
            break
        elif c == ord('q'):  # if 'q' pressed the game exits
            break
    curses.endwin()


def main():

    name1 = input('Type your name! ')
    name2 = "Computer"
    multi_single = int(input(name1 + " ,if you want to play against computer press 1 or play multi press 2!"))
    if multi_single == 1:
        screen = curses.initscr()
        menu(screen, name1, name2, multi_single)
    elif multi_single == 2:
        name2 = input('Type your friend name! ')
        screen = curses.initscr()
        menu(screen, name1, name2, multi_single)


main()
