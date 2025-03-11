# Nim is the most famous two-player algorithm game. The basic rules for this game are as follows:

# The game starts with a number of piles of stones. The number of stones in each pile may not be equal.
# The players alternately pick up  or more stones from  pile
# The player to remove the last stone wins.
# For example, there are  piles of stones having  stones in them. Play may proceed as follows:
def nimGame(pile):
    res=pile[0]
    for i in range(1,len(pile)):
        res^=pile[i]
    if res==0:
        return "Second"
    return "First"