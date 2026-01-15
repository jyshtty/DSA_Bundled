# leetcode 138: Copy List with Random Pointer
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list.
# https://leetcode.com/problems/copy-list-with-random-pointer/
# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Example 2:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

# Approach: Hashmap
# Use a hashmap to store the mapping from old nodes to new nodes.
# First, traverse the list to create new nodes and store in map.
# Then, traverse again to set next and random pointers.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Implementation:

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldtonew = {None: None}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            oldtonew[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldtonew[curr]
            copy.next = oldtonew[curr.next]
            copy.random = oldtonew[curr.random]
            curr = curr.next
        
        return oldtonew[head]
