

# TreeNode class definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution class definition
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        if not descriptions:
            return None

        nodes = {}
        child_set = set()

        # Create nodes and track child nodes
        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)

            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

            child_set.add(child)

        # The root is the node that is never a child
        root_val = (set(nodes.keys()) - child_set).pop()
        return nodes[root_val]
