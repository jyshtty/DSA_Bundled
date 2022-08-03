class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        def foo(node):
            if node is None:
                return node
            node.left, node.right = node.right, node.left
            foo(node.left)
            foo(node.right)
        foo(A)
        return A