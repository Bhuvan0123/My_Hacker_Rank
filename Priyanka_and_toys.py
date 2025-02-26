# Priyanka works for an international toy company that ships by container. Her task is to the determine the lowest cost way to combine her orders for shipping. She has a list of item weights. The shipping company has a requirement that all items loaded in a container must weigh less than or equal to 4 units plus the weight of the minimum weight item. All items meeting that requirement will be shipped in one container.

# What is the smallest number of containers that can be contracted to ship the items based on the given list of weights?

# For example, there are items with weights . This can be broken into two containers:  and . Each container will contain items weighing within  units of the minimum weight item.
def toys(w):
    w.sort()
    n=len(w)
    res=0
    i=0
    while i<n:
        maxi=w[i]+4
        while (i<n and w[i]<=maxi):
            i+=1
        res+=1
    return res