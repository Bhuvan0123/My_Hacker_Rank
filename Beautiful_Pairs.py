# You are given two arrays,  and , both containing  integers.

# A pair of indices  is beautiful if the  element of array  is equal to the  element of array . In other words, pair  is beautiful if and only if . A set containing beautiful pairs is called a beautiful set.

# A beautiful set is called pairwise disjoint if for every pair  belonging to the set there is no repetition of either  or  values. For instance, if  and  the beautiful set  is not pairwise disjoint as there is a repetition of , that is .

# Your task is to change exactly  element in  so that the size of the pairwise disjoint beautiful set is maximum.
from collections import Counter
def beautifulPairs(A, B):
    freqA=Counter(A)
    res=0
    for i in B:
        if freqA[i]>0:
            res+=1
            freqA[i]-=1
    if len(A)==res:
        return res-1
    else:
        return res+1
