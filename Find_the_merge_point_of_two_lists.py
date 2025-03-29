# Given pointers to the head nodes of  linked lists that merge together at some point, find the node where the two lists merge. The merge point is where both lists point to the same node, i.e. they reference the same memory location. It is guaranteed that the two head nodes will be different, and neither will be NULL. If the lists share a common node, return that node's  value.
def findMergeNode(head1, head2):
    n1=head1
    n2=head2
    while n1!=n2:
        if not n1 is None:
            n1=n1.next
        else:
            n1=head2
        if not n2 is None:
            n2=n2.next
        else:
            n2=head1
    if n1!=None:
        return n1.data
    return -1