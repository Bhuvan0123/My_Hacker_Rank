'''
Bomberman lives in a rectangular grid. Each cell in the grid either contains a bomb or nothing at all.

Each bomb can be planted in any cell of the grid but once planted, it will detonate after exactly 3 seconds. Once a bomb detonates, it's destroyed — along with anything in its four neighboring cells. This means that if a bomb detonates in cell , any valid cells  and  are cleared. If there is a bomb in a neighboring cell, the neighboring bomb is destroyed without detonating, so there's no chain reaction.

Bomberman is immune to bombs, so he can move freely throughout the grid. Here's what he does:

Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
After one second, Bomberman does nothing.
After one more second, Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs. No bombs detonate at this point.
After one more second, any bombs planted exactly three seconds ago will detonate. Here, Bomberman stands back and observes.
Bomberman then repeats steps 3 and 4 indefinitely.
Note that during every second Bomberman plants bombs, the bombs are planted simultaneously (i.e., at the exact same moment), and any bombs planted at the same time will detonate at the same time.

Given the initial configuration of the grid with the locations of Bomberman's first batch of planted bombs, determine the state of the grid after  seconds.
'''
def tostring(grid):
    res=[]
    for s in grid:
        res.append(''.join(['.' if x<=0 else 'O' for x in s]))
    return res
    
    
def dentote(grid, i, j):
    grid[i][j]=0
    if i>0 and grid[i-1][j]!=1:
        grid[i-1][j]=0
    if j>0 and grid[i][j-1]!=1:
        grid[i][j-1]=0
    if i<len(grid)-1 and grid[i+1][j]!=1:
        grid[i+1][j]=0
    if j<len(grid[0])-1 and grid[i][j+1]!=1:
        grid[i][j+1]=0
    
    
def plant(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j]<=0):
                grid[i][j]=3
    pass
    
        
def nexttick(grid, tick):
    if tick==2:
        return
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]>1:
                grid[i][j]-=1
    if tick==1 or tick%2 == 0 and tick!=2 :
        plant(grid)
        return
  
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==1:
                dentote(grid, i, j)
                
               
def togrid(grid):
    res=[]
    for s in grid:
        res.append([0 if x=='.' else 3 for x in s])
    return res
    
def bomberMan(n, grid):
    if n%2==0:
        return ['O'*len(grid[0])]*len(grid)
    grid=togrid(grid)
    if n==1:
        return tostring(grid)
    for i in range(1, min(8, 4+n%4+1)):
        nexttick(grid, i)
    return tostring(grid)
