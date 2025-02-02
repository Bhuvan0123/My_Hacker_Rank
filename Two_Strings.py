# Given two strings, determine if they share a common substring. A substring may be as small as one character.
def twoStrings(s1, s2):
    return "YES" if (set(s1) & set(s2)) else "NO"
# another method
def twoStrings(s1, s2):
    k=s1
    x=s2
    if len(s1)<len(s2):
        k=s1
        x=s2
    else:
        k=s2
        x=s1
    
    k=list(set(k))
    for i in k:
        if i in x:
            return "YES"
    return "NO"