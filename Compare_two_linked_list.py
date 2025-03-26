# You’re given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to check if they are equal. If all data attributes are equal and the lists are the same length, return . Otherwise, return .
def compare_lists(llist1, llist2):
    c1=llist1
    c2=llist2
    while c1 and c2:
        if c1.data!=c2.data:
            return 0
        c1=c1.next
        c2=c2.next
    if c1 or c2:
        return 0
    return 1