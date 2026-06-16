"""
Problem: Min Stack
Link: https://leetcode.com/problems/min-stack/

Description:
    Design a stack that supports push, pop, top, and retrieving the
    minimum element — all in O(1) time.

Examples:
    MinStack minStack = new MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()  -> -3
    minStack.pop()
    minStack.top()     -> 0
    minStack.getMin()  -> -2

Constraints:
    -2^31 <= val <= 2^31 - 1
    pop, top, getMin are called on non-empty stacks.
    At most 3 * 10^4 calls will be made.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        # parallel stack that records the current minimum at every level;
        # avoids needing to rescan when the current min is popped
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
