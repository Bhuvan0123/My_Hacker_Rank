# James found a love letter that his friend Harry has written to his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

# To do this, he follows two rules:

# He can only reduce the value of a letter by , i.e. he can change d to c, but he cannot change c to d or d to b.
# The letter  may not be reduced any further.
# Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.
def theLoveLetterMystery(s):
    res=0
    n=len(s)
    for i in range(n//2):
        ri=n-i-1
        if s[i]!=s[ri]:
            res+=abs(ord(s[i])-ord(s[ri]))
    return res