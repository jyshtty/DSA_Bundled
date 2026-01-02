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

            if node.val == target: # found target
                target_parent = parent # record target's parent

            level.append((node, parent)) # store current level nodes with their parents

            if node.left: # add left child to queue
                queue.append((node.left, node)) # add right child to queue
            if node.right:
                queue.append((node.right, node))

        # if target found at this level, other nodes in this level are cousins
        # else continue to next level. ingore nodes from previous levels.
        if target_parent: # return cousins
            return [
                node.val for node, parent in level
                if parent != target_parent and node.val != target
            ]

    return []
