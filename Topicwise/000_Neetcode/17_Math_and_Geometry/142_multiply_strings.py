"""
Problem: Multiply Strings
Link: https://leetcode.com/problems/multiply-strings/

Description:
    Given two non-negative integers num1 and num2 as strings, return their
    product as a string. Do not use built-in big integer libraries or convert
    directly to integers.

Examples:
    Input:  num1 = "2", num2 = "3"      Output: "6"
    Input:  num1 = "123", num2 = "456"  Output: "56088"

Constraints:
    1 <= num1.length, num2.length <= 200
    num1 and num2 consist of digits only.
    Neither input has leading zeros except "0".
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        pos = [0] * (m + n)  # product of m-digit and n-digit numbers has at most m+n digits

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1  # p1 is carry position, p2 is current digit position
                total = mul + pos[p2]
                pos[p2] = total % 10
                pos[p1] += total // 10

        result = ''.join(str(d) for d in pos)
        return result.lstrip('0')  # remove leading zeros
