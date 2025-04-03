# Complete the  function in your editor below, which has  parameter: a pointer to the root of a binary tree. It must print the values in the tree's inorder traversal as a single line of space-separated values.
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.info,end=" ")
        inOrder(root.right)