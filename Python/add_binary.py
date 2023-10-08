""" 
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a

        a = a[::-1]
        b = b[::-1]

        carry = 0
        result = []

        for i in range(len(a)):
            bit_sum = carry
            if i < len(b):
                bit_sum += int(a[i]) + int(b[i])
            else:
                bit_sum += int(a[i])

            result.append(str(bit_sum % 2))
            carry = bit_sum // 2

        if carry:
            result.append('1')

        return ''.join(result[::-1])
