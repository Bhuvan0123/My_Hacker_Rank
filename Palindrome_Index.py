# Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.
def ispalin(s,l,r):
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True
    
def palindromeIndex(s):
    l,r=0,len(s)-1
    while l<r:
        if(s[l]!=s[r]):
            if ispalin(s,l+1,r):
                return l
            if ispalin(s,l,r-1):
                return r
            else:
                return -1
        l+=1
        r-=1
    return -1