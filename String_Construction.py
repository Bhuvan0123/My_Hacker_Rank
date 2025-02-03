# Amanda has a string of lowercase letters that she wants to copy to a new string. She can perform the following operations with the given costs. She can perform them any number of times to construct a new string :

# Append a character to the end of string  at a cost of  dollar.
# Choose any substring of  and append it to the end of  at no charge.
# Given  strings , find and print the minimum cost of copying each  to  on a new line.

# For example, given a string , it can be copied for  dollars. Start by copying ,  and  individually at a cost of  dollar per character. String  at thi
def stringConstruction(s):
    res=0
    n=len(s)
    if n==1 or n==0:
        return 0
    p=""
    for i in s:
        if i not in p:
            p+=i
            res+=1
        else:
            p+=i
    return res