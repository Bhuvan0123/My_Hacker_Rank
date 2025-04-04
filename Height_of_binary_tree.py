# The height of a binary tree is the number of edges between the tree's root and its furthest leaf.
def height(root):
    if not root:
        return -1
    hl=height(root.left)
    hr=height(root.right)
    return max(hl,hr)+1