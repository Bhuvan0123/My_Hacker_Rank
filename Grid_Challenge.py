# Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.
def gridChallenge(grid):
    n=len(grid)
    sorted_grid = [''.join(sorted(row)) for row in grid]
    for i in range(len(sorted_grid[0])):
        for j in range(1,n):
            if sorted_grid[j][i]<sorted_grid[j-1][i]:
                return 'NO'
    return 'YES'