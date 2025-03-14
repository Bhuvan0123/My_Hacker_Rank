# Poker Nim is another -player game that's a simple variation on a Nim game. The rules of the games are as follows:

# The game starts with  piles of chips indexed from  to . Each pile  (where ) has  chips.
# The players move in alternating turns. During each move, the current player must perform either of the following actions:

# Remove one or more chips from a single pile.
# Add one or more chips to a single pile.
# At least  chip must be added or removed during each turn.

# To ensure that the game ends in finite time, a player cannot add chips to any pile  more than  times.
# The player who removes the last chip wins the game.
# Given the values of , , and the numbers of chips in each of the  piles, determine whether the person who wins the game is the first or second person to move. Assume both players move optimally.
def pokerNim(k, c):
    res=0
    for i in c:
        res^=i
    return "First" if res else "Second"