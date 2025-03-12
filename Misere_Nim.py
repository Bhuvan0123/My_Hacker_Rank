# Two people are playing game of Misère Nim. The basic rules for this game are as follows:

# The game starts with  piles of stones indexed from  to . Each pile  (where ) has  stones.
# The players move in alternating turns. During each move, the current player must remove one or more stones from a single pile.
# The player who removes the last stone loses the game.
# Given the value of  and the number of stones in each pile, determine whether the person who wins the game is the first or second person to move. If the first player to move wins, print First on a new line; otherwise, print Second. Assume both players move optimally.
def misereNim(s):
    res=0
    add=0
    n=len(s)
    for i in s:
        res^=i
        add+=i
    if n==add:
        if n%2==0:
            return "First"
        else:
            return "Second"
    if res:
        return "First"
    return "Second"