'''
Madison is a little girl who is fond of toys. Her friend Mason works in a toy manufacturing 
factory . Mason has a 2D board  of size  with  rows and  columns. The board is divided into 
cells of size  with each cell indicated by its coordinate . The cell  has an integer  written
on it. To create the toy Mason stacks  number of cubes of size  on the cell .

Given the description of the board showing the values of  and that the price of the toy is 
equal to the 3d surface area find the price of the toy.

Input Format

The first line contains two space-separated integers  and  the height and the width of the board
respectively.

The next  lines contains  space separated integers. The  integer in  line denotes .
'''
def surfaceArea(A):
    res=0
    for i in range(len(A)):
        for j in range(len(A[0])):
            res+=4*A[i][j]+2
            if i>0:
                res-=min(A[i][j],A[i-1][j])*2
            if j>0:
                res-=min(A[i][j],A[i][j-1])*2
    return res