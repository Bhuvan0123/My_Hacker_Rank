# Given a pointer to the root of a binary tree, you need to print the level order traversal of this tree. In level-order traversal, nodes are visited level by level from left to right. Complete the function  and print the values in a single line separated by a space.
def levelOrder(root):
    queue=[]
    queue.append(root)
    while queue:
        node=queue.pop(0)
        print(node.info,end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)