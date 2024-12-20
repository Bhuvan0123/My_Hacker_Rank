'''
Happy Ladybugs is a board game having the following properties:

The board is represented by a string, , of length . The  character of the string, , denotes the
cell of the board.
If  is an underscore (i.e., _), it means the  cell of the board is empty.
If  is an uppercase English alphabetic letter (ascii[A-Z]), it means the  cell contains a
ladybug of color .
String  will not contain any other characters.
A ladybug is happy only when its left or right adjacent cell (i.e., ) is occupied 
by another ladybug having the same color.
In a single move, you can move a ladybug from its current position to any empty cell.
Given the values of  and  for  games of Happy Ladybugs, determine if it's 
possible to make all the ladybugs happy. For each game, return YES if all the ladybugs 
can be made happy through some number of moves. Otherwise, return NO.
'''

def happyLadybugs(b):
    # Write your code here
    if b.count("_") == 0 and len(re.sub(r'((.)\2+)', "", b)) != 0:
        return "NO"
    for a in set(b):
        if a != "_" and b.count(a) == 1:
            return "NO"
    return "YES"
