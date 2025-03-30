# Given a reference to the head of a doubly-linked list and an integer, , create a new DoublyLinkedListNode object having data value  and insert it at the proper location to maintain the sort.
def sortedInsert(llist, data):
    curr=llist
    x=DoublyLinkedListNode(data)
    if not curr:
        return x
    if curr and data<curr.data:
        x.next=curr
        curr.prev=x
        curr=x
        return curr
    while curr:
        curr=curr.next
        if(curr.data>data):
            curr=curr.prev
            x.next=curr.next
            x.prev=curr
            if(curr.next):
                curr.next.prev=x
            curr.next=x
            return llist
        else:
            if not curr.next:
                curr.next=x
                x.next=None
                x.prev=curr
                return llist
            else:
                continue
    return llist