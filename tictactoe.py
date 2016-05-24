import curses
import curses.textpad


board = [' '] * 10

z = 0 #for the 'playersymbol' function

def test(i): #alternates between 'X' and 'O'
    global z
    if z == 0:
        z += 1
        s = 'X'
        board[i] = s #fills the list of moves with the players' corresponding symbols
        return "X"
    else:
        s = "O"
        board[i] = s
        z -= 1
        return "O"

def rewrite(i): #to avoid overwriting existing steps
    global board
    global write
    global c
    if board[i] == " ":
        write = True
    else:
        write = False


def getPlayerMove(c): #prints the players' symbols on the space associated with the num keys
    if c == ord('7'):
        i = 7
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6),int(dims[1]/6), test(i))
    elif c == ord('8'):
        i = 8
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6),int(dims[1]/2),test(i))
    elif c == ord('9'):
        i = 9
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6),int(dims[1]/6*5),test(i))
    elif c == ord('4'):
        i = 4
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6*3),int(dims[1]/6),test(i))
    elif c == ord('5'):
        i = 5
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6*3),int(dims[1]/2),test(i))
    elif c == ord('6'):
        i = 6
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6*3),int(dims[1]/6*5),test(i))
    elif c == ord('1'):
        i = 1
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6*5),int(dims[1]/6),test(i))
    elif c == ord('2'):
        i = 2
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6*5),int(dims[1]/2),test(i))
    elif c == ord('3'):
        i = 3
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6*5),int(dims[1]/6*5),test(i))
    return()

player1 = "X"
player2 = "O"

def winner1(): #returns true if player1 wins
    global player1
    global board
    return ((board[7] == player1 and board[8] == player1 and board[9] == player1) or #horizontal
    (board[4] == player1 and board[5] == player1 and board[6] == player1) or #horizontal
    (board[1] == player1 and board[2] == player1 and board[3] == player1) or #horizontal
    (board[7] == player1 and board[4] == player1 and board[1] == player1) or #vertical
    (board[8] == player1 and board[5] == player1 and board[2] == player1) or #vertical
    (board[9] == player1 and board[6] == player1 and board[3] == player1) or #vertical
    (board[7] == player1 and board[5] == player1 and board[3] == player1) or #diagonal
    (board[9] == player1 and board[5] == player1 and board[1] == player1)) #diagonal

def winner2(): #returns true if player2 wins
    global player2
    global board
    return ((board[7] == player2 and board[8] == player2 and board[9] == player2) or #horizontal
    (board[4] == player2 and board[5] == player2 and board[6] == player2) or #horizontal
    (board[1] == player2 and board[2] == player2 and board[3] == player2) or #horizontal
    (board[7] == player2 and board[4] == player2 and board[1] == player2) or #vertical
    (board[8] == player2 and board[5] == player2 and board[2] == player2) or #vertical
    (board[9] == player2 and board[6] == player2 and board[3] == player2) or #vertical
    (board[7] == player2 and board[5] == player2 and board[3] == player2) or #diagonal
    (board[9] == player2 and board[5] == player2 and board[1] == player2)) #diagonal


def winning(): #whether one of the players won, prints this text
    if winner1():
        screen.addstr(int(dims[0]/2-2), int(dims[1]/2-7), "Player 'X' won!")
    elif winner2():
        screen.addstr(int(dims[0]/2-2), int(dims[1]/2-7), "Player 'O' won!")
    return()


screen = curses.initscr() #draws the board
dims = screen.getmaxyx()
screen = curses.newwin(int(dims[0]), int(dims[1]),0 ,0)
screen.box()
for i in range (0, int(dims[0])):
    screen.addstr(i, int(dims[1]/3), '|') #vertical
    screen.addstr(i, int(dims[1]/3*2), '|')
for i in range (0, int(dims[1])):
    screen.addstr(int(dims[0]/3), i, '_') #horizontal
    screen.addstr(int(dims[0]/3*2), i, '_')
screen.addstr(0, 1, "TIC-TAC-TOE ------ Use number keys to place 'X' and 'O', press 'q' to quit.")

curses.noecho()
curses.cbreak()
screen.keypad(True)
curses.curs_set(0)

while True:
    c = screen.getch()
    if c == ord('q'): #if 'q' pressed the game exits
        break  # Exit the while loop
    elif winner1() or winner2(): #if one of the players won
        winning()
    elif c == ord('q'): #if 'q' pressed the game exits
        break  # Exit the while loop
    elif c != ord('q'): #if 'q' is not pressed the game continues
        getPlayerMove(c)


curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()
