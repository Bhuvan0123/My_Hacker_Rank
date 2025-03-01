# There are two -element arrays of integers,  and . Permute them into some  and  such that the relation  holds for all  where .

# There will be  queries consisting of , , and . For each query, return YES if some permutation ,  satisfying the relation exists. Otherwise, return NO.
def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i]+B[i]<k:
            return "NO"
    return "YES"