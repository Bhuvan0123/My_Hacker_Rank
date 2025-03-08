# Two players called  and  are playing a game with a starting number of stones. Player  always plays first, and the two players move in alternating turns. The game's rules are as follows:

# In a single move, a player can remove either , , or  stones from the game board.
# If a player is unable to make a move, that player loses the game.
# Given the starting number of stones, find and print the name of the winner.  is named First and  is named Second. Each player plays optimally, meaning they will not make a move that causes them to lose the game if a winning move exists.

# For example, if ,  can make the following moves:

#  removes  stones leaving .  will then remove  stones and win.
#  removes  stones leaving .  cannot move and loses.
#  would make the second play and win the game.
def gameOfStones(n):
    if (n%7)<2:
        return "Second"
    return "First"