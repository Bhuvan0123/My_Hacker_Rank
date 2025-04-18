# You are given a function . You are also given  lists. The  list consists of  elements.

# You have to pick one element from each list so that the value from the equation below is maximized:

# %

#  denotes the element picked from the  list . Find the maximized value  obtained.

#  denotes the modulo operator.

# Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.
from itertools import product
n,m=map(int,input().split())
arr=[(list(map(int,input().split()))[1:]) for _  in range(n)]
res=0
for i in product(*arr):
    temp=sum(x**2 for x in i)%m
    res=max(res,temp)
print(res)