# Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.
from collections import Counter
def isValid(s):
    count=Counter(Counter(s).values())
    values=list(count.keys())
    if len(count)==1 or (len(count)==2 and ((abs(values[0]-values[1])==1 and 1 in count.values()) or count[1]==1 )):
        return "YES"
    return "NO"