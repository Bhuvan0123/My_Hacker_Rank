# You are given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with the given integer. Insert this node at the tail of the linked list and return the head node of the linked list formed after inserting this new node. The given head pointer may be null, meaning that the initial list is empty.
def insertNodeAtTail(head, data):
    root=SinglyLinkedListNode(data)
    if head:
        curr=head
        while(curr.next):
            curr=curr.next
        curr.next=root
        return head
    return root