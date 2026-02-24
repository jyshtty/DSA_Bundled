# Cycle detection
class Solution:
    def hasCycle(self, root: Optional[ListNode]) -> bool:
        slow = root
        fast = root
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False

#Start of cycle
class Solution:
    def detectCycle(self, root: Optional[ListNode]) -> Optional[ListNode]:
        slow = root
        fast = root
        
        # Step 1: detect meeting point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            return None
        
        # Step 2: move one pointer to head
        slow = root
        
        # Step 3: move both one step
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
