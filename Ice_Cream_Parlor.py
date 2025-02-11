# Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.

# Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

# Example.  

# The two flavors that cost  and  meet the criteria. Using -based indexing, they are at indices  and .
from itertools import combinations
def icecreamParlor(m, arr):
    store=[]
    comb=combinations(enumerate(arr),2)
    for (i,_),(j,_) in comb:
        if(arr[i]+arr[j]==m):
            store=[i+1,j+1]
    return store