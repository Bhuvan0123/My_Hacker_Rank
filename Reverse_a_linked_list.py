# Given the pointer to the head node of a linked list, change the next pointers of the nodes so that their order is reversed. The head pointer given may be null meaning that the initial list is empty.
def reverse(llist):
    res=None
    while llist:
        temp=SinglyLinkedListNode(llist.data)
        temp.next=res
        res=temp
        llist=llist.next
    return res