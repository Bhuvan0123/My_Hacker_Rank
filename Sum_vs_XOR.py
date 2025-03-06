# Given an integer , find each  such that:

# where  denotes the bitwise XOR operator. Return the number of 's satisfying the criteria.
def sumXor(n):
    res=1
    while n:
        if n%2==0:
            res*=2
        else:
            res*=1
        n//=2
    return res
