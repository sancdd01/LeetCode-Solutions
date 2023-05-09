""" 
383. Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}

        for letter in magazine:
            if letter not in mag_dict:
                mag_dict[letter] = 1
            else:
                mag_dict[letter] += 1

        for letter in ransomNote:
            if letter not in mag_dict or mag_dict[letter] == 0:
                return False
            else:
                mag_dict[letter] -= 1
        return True
