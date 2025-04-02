# Complete the  function in the editor below. It received  parameter: a pointer to the root of a binary tree. It must print the values in the tree's postorder traversal as a single line of space-separated values.
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info,end=" ")