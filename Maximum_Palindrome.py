# In this challenge, Hannah provides a string  consisting of lowercase English letters. Every day, for  days, she would select two integers  and , take the substring  (the substring of  from index  to index ), and ask the following question:

# Consider all the palindromes that can be constructed from some of the letters from . You can reorder the letters as you need. Some of these palindromes have the maximum length among all these palindromes. How many maximum-length palindromes are there?

import math
import os
import random
import re
import sys

def initialize(s):
    n, z = len(s), ord('a')
    S, F, I = [[0] * L for _ in range(n + 1)], [1] * n, [1] * n
    for i, v in enumerate(s, 1):
        for j in range(L):          
            S[i][j] = S[i - 1][j] + (j == ord(v) - z)
    for i in range(1, n):
        F[i] = F[i - 1] * i % M     
        I[i] = pow(F[i], M - 2, M)  
    return(S, F, I)
    
def answerQuery(l, r):
    c, s, d = 0, 0, 1
    for j in [S[r][i] - S[l - 1][i] for i in range(L)]:
        c += j % 2                  
        s += j // 2                 
        d *= I[j // 2]             
    return((c or 1) * F[s] * d % M)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    L, M = 26, 1000000007
    S, F, I = initialize(input())
    for _ in range(int(input())):
        result = answerQuery(*map(int, input().split()))
        fptr.write(str(result) + '\n')
    fptr.close()