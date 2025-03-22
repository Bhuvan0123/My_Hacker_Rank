# Given a pointer to the head of a singly-linked list, print each  value from the reversed list. If the given list is empty, do not print anything.
def reversePrint(llist):
    stack=[]
    curr=llist
    while curr:
        stack.append(curr.data)
        curr=curr.next
    for i in stack[::-1]:
        print(i)