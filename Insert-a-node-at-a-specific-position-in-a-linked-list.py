# Given a pointer to the head node of a linked list and an integer to insert at a certain position, create a new node with the given integer as its  attribute, insert this node at the desired position, and return the head node.

# A position of 0 indicates the head, a position of 1 indicates one node away from the head, and so on. The head pointer given may be null, meaning that the initial list is empty.
def insertNodeAtPosition(llist, data, position):
    curr=llist
    node=SinglyLinkedListNode(data)
    if not llist:
        return node
    while(curr.next and position>1):
        position-=1
        curr=curr.next
    nextnode=curr.next
    curr.next=node
    node.next=nextnode
    return llist