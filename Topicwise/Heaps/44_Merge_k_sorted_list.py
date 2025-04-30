# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        from heapq import heappush, heappop, heapify
        hp = []
        heapify(hp)
        for i in A:
            heappush(hp, [i.val, i])
        head = ListNode(None)
        temp = head
        while hp:
            val, pointer = heappop(hp)
            Node = ListNode(val)
            temp.next = Node
            temp = temp.next

            if pointer.next:
                heappush(hp, [pointer.next.val, pointer.next])

        return head.next

x = ListNode(1)
y = ListNode(10)
z = ListNode(20)
x.next = y
y.next = z

x1 = ListNode(4)
y1 = ListNode(11)
z1 = ListNode(13)
x1.next = y1
y1.next = z1

x2 = ListNode(3)
y2 = ListNode(8)
z2 = ListNode(9)
x2.next = y2
y2.next = z2

obj = Solution()
print(obj.mergeKLists([x, x1, x2]))