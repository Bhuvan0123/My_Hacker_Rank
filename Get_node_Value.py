# Given a pointer to the head of a linked list and a specific position, determine the data value at that position. Count backwards from the tail node. The tail is at postion 0, its parent is at 1 and so on.
def getNode(llist, positionFromTail):
    arr=[]
    curr=llist
    while curr:
        arr.append(curr.data)
        curr=curr.next
    return (arr[len(arr)-positionFromTail-1])