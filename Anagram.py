# Two words are anagrams of one another if their letters can be rearranged to form the other word.

# Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.
from collections import Counter
def anagram(s):
    if len(s)%2==1:
        return -1
    n=len(s)//2
    res=0
    f1=Counter(s[:n])
    f2=Counter(s[n:])
    for i in f1:
        if f1[i]>f2.get(i,0):
            res+=f1[i]-f2.get(i,0)
    return res
    