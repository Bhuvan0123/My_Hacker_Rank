# Two players are playing a game on a  chessboard. The rules of the game are as follows:

# The game starts with a single coin located at some  coordinates. The coordinates of the upper left cell are , and of the lower right cell are .

# In each move, a player must move the coin from cell  to one of the following locations:

# Note: The coin must remain inside the confines of the board.

# Beginning with player 1, the players alternate turns. The first player who is unable to make a move loses the game.
def chessboardGame(x, y):
    x-=1
    y-=1
    if (x//2)%2==0 and (y//2)%2==0:
        return "Second"
    return "First"