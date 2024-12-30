# Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. In each operation, select a pair of adjacent letters that match, and delete them.

# Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String
def superReducedString(s):
    stack=[]
    for i in s:
        stack.append(i)
        if len(stack)>1 and stack[-1]==stack[-2]:
            stack.pop()
            stack.pop()
    if stack==[]:
        return "Empty String"
    return "".join(stack)