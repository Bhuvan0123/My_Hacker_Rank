# Delete the node at a given position in a linked list and return a reference to the head node. The head is at position 0. The list may be empty after you delete the node. In that case, return a null value.
def deleteNode(llist, position):
    if not llist:
        return None
    if position==0:
        return llist.next
    curr=llist
    while position>1:
        curr=curr.next
        position-=1
    curr.next=curr.next.next
    return llist