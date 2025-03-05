# Given two integers,  and , find the maximal value of  xor , written , where  and  satisfy the following condition:


# For example, if  and , then



# Our maximum value is .
def maximizingXor(l, r):
    res=[]
    for i in range(l,r+1):
        for j in range(l,r+1):
            res.append(i^j)
    res.sort()
    return res[-1]
