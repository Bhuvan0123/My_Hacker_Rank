# Two people are playing Nimble! The rules of the game are:

# The game is played on a line of  squares, indexed from  to . Each square  (where ) contains  coins. For example:
# The players move in alternating turns. During each move, the current player must remove exactly  coin from square  and move it to square  if and only if .
# The game ends when all coins are in square  and nobody can make a move. The first player to have no available move loses the game.
# Given the value of  and the number of coins in each square, determine whether the person who wins the game is the first or second person to move. Assume both players move optimally.

# Input Format

# The first line contains an integer, , denoting the number of test cases.
# Each of the  subsequent lines defines a test case. Each test case is described over the following two lines:

# An integer, , denoting the number of squares.
#  space-separated integers, , where each  describes the number of coins at square .
def nimbleGame(s):
    res=0
    for i in range(len(s)):
        if s[i]%2!=0:
            res^=i
    if res>0:
        return "First"
    return "Second"