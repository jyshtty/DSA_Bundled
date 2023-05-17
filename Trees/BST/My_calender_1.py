# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.
#
# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).
#
# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.
#
# Implement the MyCalendar class:
#
# MyCalendar() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

# Approach 1
# HINT
# 1. start should be greater than inseted ones
# 2. End should be less than inserted ones start
#
# By using above 2 make a BST

class Node:
    __slots__ = 'start', 'end', 'left', 'right'
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))

# Approach 2
# 1. Start of node is less than end of inserted node.
# 2. Start of inserted node is less than end of node

class MyCalendar(object):
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True
