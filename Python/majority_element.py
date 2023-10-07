""" 
169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}
        l = len(nums)
        m_e = l // 2

        for num in nums:
            if num in elements:
                elements[num] += 1
            else:
                elements[num] = 1

        for key, value in elements.items():
            if value > m_e:
                return key
