# Given a pointer to the root of a binary tree, print the top view of the binary tree.
def topView(root):
    if root is None:
        return
    from collections import deque
    queue=deque([(root,0)])
    top={}
    while queue:
        node,val=queue.popleft()
        if val not in top:
            top[val]=node.info
        if node.left:
            queue.append((node.left,val-1))
        if node.right:
            queue.append((node.right,val+1))
    for i in sorted(top):
        print(top[i],end=" ")