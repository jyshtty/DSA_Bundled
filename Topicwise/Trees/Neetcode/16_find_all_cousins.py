from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_cousins(root: TreeNode, target: int):
    if not root or root.val == target:
        return []

    queue = deque([(root, None)])  # (node, parent)

    while queue:
        size = len(queue)
        level = []
        target_parent = None

        for _ in range(size):
            node, parent = queue.popleft()

            if node.val == target:
                target_parent = parent

            level.append((node, parent))

            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))

        # if target found at this level
        if target_parent:
            return [
                node.val for node, parent in level
                if parent != target_parent and node.val != target
            ]

    return []
