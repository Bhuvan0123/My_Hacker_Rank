# Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.
def mergeLists(head1, head2):
    res=SinglyLinkedList()
    while head1 or head2:
        if not head1:
            res.insert_node(head2.data)
            head2=head2.next
        elif not head2:
            res.insert_node(head1.data)
            head1=head1.next
        elif head1 and head2:
            if head1.data<=head2.data:
                res.insert_node(head1.data)
                head1=head1.next
            else:
                res.insert_node(head2.data)
                head2=head2.next
    return res.head