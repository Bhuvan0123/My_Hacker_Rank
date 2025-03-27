# You are given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order. Delete nodes and return a sorted list with each distinct value in the original list. The given head pointer may be null indicating that the list is empty.
def removeDuplicates(llist):
    curr=llist
    while curr:
        if curr.next and curr.data==curr.next.data:
           curr.next=curr.next.next
        else:
            curr=curr.next
    return llist 