# Kitty has a tree, , consisting of  nodes where each node is uniquely labeled from  to . Her friend Alex gave her  sets, where each set contains  distinct nodes. Kitty needs to calculate the following expression on each set:

# where:

#  denotes an unordered pair of nodes belonging to the set.
#  denotes the number of edges on the unique (shortest) path between nodes  and .
# Given  and  sets of  distinct nodes, calculate the expression for each set. For each set of nodes, print the value of the expression modulo  on a new line.
import sys, math

# Pretty important line here.
sys.setrecursionlimit(10**6)

def preprocess_original_tree(node, parent):
    # "Jumping" in the current node.
    global timer
    tin[node] = timer
    timer += 1

    # Building a chart of the 2^i ancestors of each node.
    up[node][0] = parent

    # Setting each node's (which is the current child) 2^i ancestors' value.
    for i in range(1, LOG):
        if up[node][i - 1] != -1:
            up[node][i] = up[up[node][i - 1]][i - 1]

    # Perform DFS to set current node's children's depth recursively.
    for neighbor in adj[node]:
        if neighbor == parent:
            continue
        depth[neighbor] = depth[node] + 1
        preprocess_original_tree(neighbor, node)

    # "Jumping" out of the current node.
    tout[node] = timer
    timer += 1

def lift_node(node, k):
    # Jumping to the greatest 2^i ancestor each time.
    for i in range(LOG - 1, -1, -1):
        if k & (1 << i):
            node = up[node][i]
    return node

def get_lca(u, v):
    # Equalizing both node's depths.
    if depth[u] < depth[v]:
        u, v = v, u
    u = lift_node(u, depth[u] - depth[v])
    if u == v:
        return u

    # Jumping to the greatest 2^i ancestor each time.
    for i in range(LOG - 1, -1, -1):
        if up[u][i] != up[v][i]:
            u = up[u][i]
            v = up[v][i]
    return up[u][0]

def get_distance(u, v):
    ancestor = get_lca(u, v)

    # It uses the original tree's preprocessed depths.
    return depth[u] + depth[v] - 2 * depth[ancestor]

def build_virtual_tree(nodes):
    # Adding relevant nodes to virtual tree.
    nodes.sort(key=lambda x: tin[x])
    m = len(nodes)
    vt_nodes = nodes[:]
    for i in range(m - 1):
        vt_nodes.append(get_lca(nodes[i], nodes[i + 1]))
    vt_nodes = list(set(vt_nodes))
    vt_nodes.sort(key=lambda x: tin[x])

    # Connecting nodes in virtual tree.
    tree = {node: [] for node in vt_nodes}
    stack = []
    
    # All virtual tree nodes are stored in the order in which they were found, thus preserving their hierarchy from left to right.
    for node in vt_nodes:
        # Validating if the last ancestor in the stack is the ancestor of the current node.
        while stack and tout[stack[-1]] < tin[node]:
            stack.pop()
        if stack:
            tree[stack[-1]].append(node)
        stack.append(node)
    return tree, vt_nodes

def solve_query(query_nodes):
    # Traversing query nodes (virtual tree's nodes)
    def dp(u):
        nonlocal res
        s = query_val.get(u, 0)

        # Performing DFS.
        for v in vt[u]:
            sub = dp(v)
            # Since 
            # sum(u in sub) * sum(v not in sub) 
            # = (sum(u in sub)) * (sum(v not in sub)) 
            # = sub * (S_total - sub)
            res = (res + sub * (S_total - sub) % MOD * get_distance(u, v)) % MOD
            s += sub

        # Returning the total sum of the current subtree.
        return s

    if len(query_nodes) < 2:
        return 0
    S_total = sum(query_nodes)
    query_val = {node: node for node in query_nodes}
    vt, vt_nodes = build_virtual_tree(query_nodes)

    res = 0
    dp(vt_nodes[0])
    return res

MOD = 10**9 + 7
timer = 0

data = sys.stdin.read().split()
it = iter(data)
n = int(next(it))
q = int(next(it))

LOG = int(math.log2(n)) + 1
up = [[-1] * LOG for _ in range(n + 1)]
depth = [0] * (n + 1)
tin = [0] * (n + 1)
tout = [0] * (n + 1)

# Building original tree.
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = int(next(it)), int(next(it))
    adj[u].append(v)
    adj[v].append(u)

preprocess_original_tree(1, -1)

res = []
for _ in range(q):
    k = int(next(it))
    query_nodes = [int(next(it)) for _ in range(k)]
    res.append(str(solve_query(query_nodes)))

sys.stdout.write("\n".join(res))