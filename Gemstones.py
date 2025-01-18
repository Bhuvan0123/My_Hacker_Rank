# There is a collection of rocks where each rock has various minerals embeded in it. Each type of mineral is designated by a lowercase letter in the range . There may be multiple occurrences of a mineral in a rock. A mineral is called a gemstone if it occurs at least once in each of the rocks in the collection.

# Given a list of minerals embedded in each of the rocks, display the number of types of gemstones in the collection.
def gemstones(arr):
    res=0
    s=set(list("".join(arr)))
    for i in s:
        temp=0
        for j in arr:
            if i not in j:
                temp=1
                break
        if temp==0:
            res+=1
    return res