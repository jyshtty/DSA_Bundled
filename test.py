# def foo(para):
#     para = 100
#
# def test():
#     para = None
#     foo(para)
#     return para
#
# print(test())
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recur(A, B, hm):

    node = TreeNode(A[0])
    index = hm[node.data]



def foo(A, B, hm):
    hm = {}
    for i in range(len(B)):
        hm[B[i]] = i

    ans = []
    recur(A, B, ans)
