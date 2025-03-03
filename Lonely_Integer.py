# Given an array of integers, where all elements but one occur twice, find the unique element.
def lonelyinteger(a):
    arr=set(a)
    for i in arr:
        if a.count(i)==1:
            return i