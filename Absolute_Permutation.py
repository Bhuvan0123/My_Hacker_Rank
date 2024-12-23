'''
We define  to be a permutation of the first  natural numbers in the range . 
Let  denote the value at position  in permutation  using -based indexing.

 is considered to be an absolute permutation if  holds true for every .

Given  and , print the lexicographically smallest absolute permutation . If no absolute 
permutation exists, print -1.
'''
def absolutePermutation(n, k):
    if k==0:
        return list(range(1,n+1))
    elif k!=0 and n%(2*k)!=0:
        return [-1]
    res=[]
    for i in range(1,n+1):
        if (i-1)%(2*k)+1<=k:
            res.append(i+k)
        else:
            res.append(i-k)
    return res