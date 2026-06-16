"""
Problem: Copy List with Random Pointer
Link: https://leetcode.com/problems/copy-list-with-random-pointer/

Description:
    A linked list where each node has a next pointer and a random pointer
    (which can point to any node or null). Return a deep copy of the list.

Examples:
    Input:  [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Constraints:
    0 <= n <= 1000
    -10^4 <= Node.val <= 10^4
    Node.random is null or points to a node in the linked list.
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        old_to_new = {None: None}  # map original nodes to their copies; None handles null randoms

        # first pass: create all new nodes
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # second pass: wire up next and random pointers using the map
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new[curr.next]
            old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]
