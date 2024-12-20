'''
19-12-2024

Given an array of strings of digits, try to find the occurrence of a given pattern of
digits. In the grid and pattern arrays, each string represents a row in the grid. 
For example, consider the following grid:

1234567890  
0987654321  
1111111111  
1111111111  
2222222222  
The pattern array is:

876543  
111111  
111111

The pattern begins at the second row and the third column of the grid and continues in 
the following two rows. The pattern is said to be present in the grid. The return value
should be YES or NO, depending on whether the pattern is found. In this case, return YES.
'''


def gridSearch(G, P):
    for i in range(len(G)-len(P)+1):
        for j in range(len(G[0])-len(P[0])+1):
            for k in range(len(P)):
                if G[i+k][j:j+len(P[0])]!=P[k]:
                    break
                if k==len(P)-1:
                    return "YES"
    return "NO"