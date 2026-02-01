"""
LeetCode: Contains Duplicate
Difficulty: Easy
Link: https://leetcode.com/problems/contains-duplicate/

Problem:
Given an integer array nums, return true if any value appears more than once
in the array, otherwise return false.

Example:
Input: nums = [1, 2, 3, 3]
Output: true

Input: nums = [1, 2, 3, 4]
Output: false

Approach:
Use a set to store unique values and compare its length with the original list.

Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set=set(nums)
        if len(num_set)!=len(nums):
            return True
        else:
            return False
