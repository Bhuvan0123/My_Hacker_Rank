'''
Larry has been given a permutation of a sequence of natural numbers incrementing from  as an 
array. He must determine whether the array can be sorted using the following operation any number
of times:

Choose any  consecutive indices and rotate their elements in such a way that .
'''

def larrysArray(A):
    n=len(A)
    res=0
    for i in range(n):
        for j in range(i+1,n):
            if A[i]>A[j]:
                res+=1
    if res%2==0:
        return "YES"
    return "NO"
