"""
Problem: Evaluate Reverse Polish Notation
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Description:
    Evaluate the value of an arithmetic expression in Reverse Polish
    Notation (postfix). Valid operators are +, -, *, /. Division truncates
    toward zero.

Examples:
    Input:  tokens = ["2","1","+","3","*"]         Output: 9   ((2+1)*3)
    Input:  tokens = ["4","13","5","/","+"]        Output: 6   (4+(13/5))
    Input:  tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22

Constraints:
    1 <= tokens.length <= 10^4
    tokens[i] is an integer or one of "+", "-", "*", "/"
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}

        for token in tokens:
            if token in ops:
                b, a = stack.pop(), stack.pop()  # b is top (second operand), a is below it
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))  # int() truncates toward zero (not floor)
            else:
                stack.append(int(token))

        return stack[0]
