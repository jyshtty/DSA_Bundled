# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        Removes the nth node from the end of a singly linked list.

        This function uses a two-pointer approach:
        - First pointer moves n steps ahead
        - Second pointer starts from head and moves with first pointer
        - When first pointer reaches end, second pointer is at the node before the one to remove

        Time Complexity: O(n) where n is the length of the linked list
        Space Complexity: O(1) as we only use constant extra space

        Args:
            head: The head node of the linked list
            n: The position from the end to remove (1-based)

        Returns:
            The head of the modified linked list
        """
        # Edge case: if head is None, return None
        if not head:
            return None

        # First pointer: move n steps ahead
        temp = head
        count = 0
        while count != n:
            temp = temp.next
            count = count + 1

        # If temp is None after moving n steps, it means we need to remove the head
        if temp is None:
            return head.next

        # Second pointer: starts from head
        temp2 = head

        # Move both pointers until first pointer reaches the end
        while temp and temp.next:
            temp = temp.next
            temp2 = temp2.next

        # Remove the nth node from end by updating the next pointer
        if temp2 and temp2.next:
            temp2.next = temp2.next.next

        return head

if __name__ == "__main__":
    # Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    obj = Solution()
    n = 2  # Remove 2nd node from end (should remove node with value 4)

    # Print original list
    def print_list(node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")

    print("Original list:")
    print_list(head)

    # Remove nth node from end
    new_head = obj.removeNthFromEnd(head, n)

    print(f"After removing {n}th node from end:")
    print_list(new_head)
