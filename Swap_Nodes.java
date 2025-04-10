// A binary tree is a tree which is characterized by one of the following properties:

// It can be empty (null).
// It contains a root node only.
// It contains a root node with a left subtree, a right subtree, or both. These subtrees are also binary trees.
// In-order traversal is performed as

// Traverse the left subtree.
// Visit root.
// Traverse the right subtree.
// For this in-order traversal, start from the left child of the root node and keep exploring the left subtree until you reach a leaf. When you reach a leaf, back up to its parent, check for a right child and visit it if there is one. If there is not a child, you've explored its left and right subtrees fully. If there is a right child, traverse its left subtree then its right in the same manner. Keep doing this until you have traversed the entire tree. You will only store the values of a node as you visit when one of the following is true:

// it is the first node visited, the first time visited
// it is a leaf, should only be visited once
// all of its subtrees have been explored, should only be visited once while this is true
// it is the root of the tree, the first time visited
// Swapping: Swapping subtrees of a node means that if initially node has left subtree L and right subtree R, then after swapping, the left subtree will be R and the right subtree, L.
static void swapSubtrees(Node[] tree, int k, int d, int i) {
    if (i == -1) return;
    
    Node node = tree[i];
    
    // swap subtrees at depth h where h = 1k, 2k, 3k, ...
    if (d % k == 0) {
        int tmp = node.leftIndex;
        node.leftIndex = node.rightIndex;
        node.rightIndex = tmp;
    }
    
    // traverse and increment depth
    swapSubtrees(tree, k, d + 1, node.leftIndex);
    swapSubtrees(tree, k, d + 1, node.rightIndex);
}