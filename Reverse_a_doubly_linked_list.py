# Given the pointer to the head node of a doubly linked list, reverse the order of the nodes in place. That is, change the next and prev pointers of the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.

# Note: The head node might be NULL to indicate that the list is empty.
def reverse(llist):
    curr=llist
    res=None
    while curr:
        nex=curr.next
        curr.next=res
        res=curr
        curr=nex
        res.prev=curr
    return res