""" 
680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s: str, i: int, j: int, deletion: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    if deletion == 0:
                        return False
                    else:
                        # try deleting s[i] or s[j]
                        return is_palindrome(s, i+1, j, deletion-1) or is_palindrome(s, i, j-1, deletion-1)
                else:
                    i += 1
                    j -= 1
            return True

        return is_palindrome(s, 0, len(s)-1, 1)
