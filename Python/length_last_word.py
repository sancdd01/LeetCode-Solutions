"""
58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        s2 = s.strip()
        arr = s2.split(' ')
        return len(arr[-1])
