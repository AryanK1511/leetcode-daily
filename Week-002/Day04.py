# A node in s tree
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


# Depth First Search Algorithm


def dfs(root: TreeNode):
    if not root:
        return None

    dfs(root.left)
    dfs(root.right)
    return


"""
1. Preorder traversal

=> In preorder traversal, logic is done on the current node before moving to the children. Let's say that we wanted to just print the value of each node in the tree to the console. In that case, at any given node, we would print the current node's value, then recursively call the left child, then recursively call the right child
"""


def preorder_dfs(root: TreeNode):
    if not root:
        return None

    print(root.val)
    preorder_dfs(root.left)
    preorder_dfs(root.right)
    return


"""
2. Inorder traversal

For inorder traversal, we first recursively call the left child, then perform logic (print in this case) on the current node, and then recursively call the right child. This means no logic will be done until we reach a node without a left child since calling on the left child takes priority over performing logic.
"""


def inorder_dfs(root: TreeNode):
    if not root:
        return None

    inorder_dfs(root.left)
    print(root.val)
    inorder_dfs(root.right)
    return


"""
3. Postorder traversal

In postorder traversal, we recursively call on the children first and then perform logic on the current node. This means no logic will be done until we reach a leaf node since calling on the children takes priority over performing logic. In a postorder traversal, the root is the last node where logic is done.
"""


def postorder_dfs(root: TreeNode):
    if not root:
        return None

    postorder_dfs(root.left)
    postorder_dfs(root.right)
    print(root.val)
