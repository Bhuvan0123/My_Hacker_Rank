# This exercise focuses on traversing a linked list. You are given a pointer to the  node of a linked list. The task is to print the  of each node, one per line. If the head pointer is , indicating the list is empty, nothing should be printed.

# Function Description

# Complete the  function with the following parameter(s):

# : a reference to the head of the list
# Print

# For each node, print its  value on a new line (console.log in Javascript).
def printLinkedList(head):
    while(head):
        print(head.data)
        head=head.next