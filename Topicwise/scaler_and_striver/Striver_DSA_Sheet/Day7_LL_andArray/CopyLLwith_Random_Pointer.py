# leetcode 138: Copy List with Random Pointer
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node.
# https://leetcode.com/problems/copy-list-with-random-pointer/
# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Approach: Hash map or interweave nodes
# Time Complexity: O(n)
# Space Complexity: O(n) for hash map, O(1) extra for interweave
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