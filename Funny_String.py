# In this challenge, you will determine whether a string is funny or not. To determine whether a string is funny, create a copy of the string in reverse e.g. . Iterating through each string, compare the absolute difference in the ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. If the list of absolute differences is the same for both strings, they are funny.

# Determine whether a give string is funny. If it is, return Funny, otherwise return Not Funny.
def funnyString(s):
    n=len(s)
    s1=s
    s2=s1[::-1]
    a1,a2=[],[]
    for i in range(n-1):
        a1.append(abs(ord(s1[i])-ord(s1[i+1])))
        a2.append(abs(ord(s2[i])-ord(s2[i+1])))
    return "Funny" if a1==a2 else "Not Funny"