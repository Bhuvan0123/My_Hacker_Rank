'''
Ema built a quantum computer! Help her test its capabilities by solving the problem below.

Given a grid of size , each cell in the grid is either  or .

A valid plus is defined here as the crossing of two segments (horizontal and vertical) of equal lengths. These lengths must be odd, and the middle cell of its horizontal segment must cross the middle cell of its vertical segment.

In the diagram below, the blue pluses are valid and the orange ones are not valid. 
'''
def twoPluses(grid):

    h, w = len(grid), len(grid[0])
    res = []
    isgood = lambda r, c: grid[r][c] == 'G'
    func = lambda x: 2*x-1
    mini = min(h, w)
    for step in range(1, mini // 2 + (1 if mini % 2 else 0)):
        for r in range(step, h-step):
            for c in range(step, w-step):
                if isgood(r, c):
                    s1 = {(r2, c) for r2 in range(r-1, r-step-1, -1) if isgood(r2, c)}
                    s2 = {(r2, c) for r2 in range(r+1, r+step+1, +1) if isgood(r2, c)}
                    s3 = {(r, c2) for c2 in range(c-1, c-step-1, -1) if isgood(r, c2)}
                    s4 = {(r, c2) for c2 in range(c+1, c+step+1, +1) if isgood(r, c2)}
                    if len(s1)==step and len(s2)==step and len(s3)==step and len(s4)==step:
                        res.append((func(2*step+1), {(r, c)}|s1|s2|s3|s4))
    if not res: 
        return 1
    if len(res) == 1:
        return res.pop()[0]
    combs = [s1*s2 for (s1, a), (s2, b) in combinations(res, 2) if a.isdisjoint(b)]
    return max(combs) if combs else res.pop()[0]
