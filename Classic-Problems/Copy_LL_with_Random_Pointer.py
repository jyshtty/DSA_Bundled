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
