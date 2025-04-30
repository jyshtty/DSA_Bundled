def reverse(head):
    if not head:
        return
    temp = head
    prev = None
    while temp:
        next1 = temp.next
        temp.next = prev
        prev = temp
        temp = next1
    head = prev
    return head


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self, head=None):
        self.head = head


def display(head):
    string = ""
    if not head:
        return string + "End"
    temp = head
    while temp:
        string += f"{temp.data} >>"
        temp = temp.next
    return string


ll = Linkedlist()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

ll.head = node1
node1.next = node2
node2.next = node3
node3.next = node4

print(display(ll.head))
returned_head = reverse(ll.head)
print(display(returned_head))
