# A linked list is said to contain a cycle if any node is visited more than once while traversing the list. Given a pointer to the head of a linked list, determine if it contains a cycle. If it does, return . Otherwise, return .
def has_cycle(head):
    curr=head
    arr=dict()
    while curr:
        arr[curr]=arr.get(curr,0)+1
        if arr[curr]>1:
            return 1
        curr=curr.next
    return 0