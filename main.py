# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        temp = head
        count = 0
        while count != n:
            temp = temp.next
            count = count + 1

        temp2 = head

        while temp and temp.next:
            temp = temp.next
            temp2 = temp2.next

        if temp2 and temp2.next and temp2.next.next:
            temp2.next = temp2.next.next
        elif temp2 and temp2.next:
            temp2.next = temp2.next.next
        else:
            head = None

        return head

if __name__ == "__main__":
    obj = Solution()
    print(obj.removeNthFromEnd(head, n))
