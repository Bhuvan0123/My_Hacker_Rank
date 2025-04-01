# Print the tree's preorder traversal as a single line of space-separated values.
def preOrder(root):
    if root:
        print(root.info,end=" ")
        preOrder(root.left)
        preOrder(root.right)