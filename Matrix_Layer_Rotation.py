'''
You are given a 2D matrix of dimension  and a positive integer . You have to rotate the matrix  times and print the resultant matrix. Rotation should be in anti-clockwise direction.

Rotation of a  matrix is represented by the following figure. Note that in one rotation, you have to shift elements by one step only.
'''
def matrixRotation(matrix, r):
    n=len(matrix)
    m=len(matrix[0])
    a=min(n//2,m//2)
    for i in range(a):
        k=2*(n-2*i)+2*(m-2*i-2)
        k=r%k
        l=[]
        for j in range(i,m-i):
            l.append(matrix[i][j])
        for j in range(i+1,n-i-1):
            l.append(matrix[j][-1-i])
        for j in range(-1-i,-1*m+i-1,-1):
            l.append(matrix[-1-i][j])
        for j in range(-1-i-1,n*-1+i,-1):
            l.append(matrix[j][i])
        l=l[k:]+l[:k]
        flag=0
        for j in range(i,m-i):
            matrix[i][j]=l[flag]
            flag+=1
        for j in range(i+1,n-i-1):
            matrix[j][-1-i]=l[flag]
            flag+=1
        for j in range(-1-i,-1*m+i-1,-1):
            matrix[-1-i][j]=l[flag]
            flag+=1
        for j in range(-1-i-1,n*-1+i,-1):
            matrix[j][i]=l[flag]
            flag+=1
    for i in matrix:
        for j in i:
            print(j,end=" ")
        print()
