# Given an array of stick lengths, use  of them to construct a non-degenerate triangle with the maximum possible perimeter. Return an array of the lengths of its sides as  integers in non-decreasing order.

# If there are several valid triangles having the maximum perimeter:

# Choose the one with the longest maximum side.
# If more than one has that maximum, choose from them the one with the longest minimum side.
# If more than one has that maximum as well, print any one them.
# If no non-degenerate triangle exists, return .
def maximumPerimeterTriangle(sticks):
    sticks.sort()
    for i in range(len(sticks)-1,1,-1):
        if sticks[i]<(sticks[i-1]+sticks[i-2]):
            return (sticks[i-2],sticks[i-1],sticks[i])
    return [-1]
