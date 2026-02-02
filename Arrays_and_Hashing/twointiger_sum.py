"""
Two Sum
Difficulty: Easy
Link: https://neetcode.io/problems/two-integer-sum/question

Problem:
Given an array of integers nums and an integer target, return the indices
i and j such that nums[i] + nums[j] == target and i != j.

You may assume that exactly one valid answer exists.
Return the answer with the smaller index first.

Examples:
Input: nums = [3,4,5,6], target = 7
Output: [0,1]

Input: nums = [4,5,6], target = 10
Output: [0,2]

Input: nums = [5,5], target = 10
Output: [0,1]

Approach:
Use a set to check if the complement exists, then locate the index
of the complement after the current index.

Complexity:
- Recommended Time Complexity: O(n)
- My Solution Time Complexity: O(n²)
"""

from typing import List


class     Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_num = set(nums)
        for i in range(len(nums)):
            diff = target - nums[i] 
            if diff in my_num:
                try:
                    j = nums.index(diff, i+1 )
                    return [i,j]
                except ValueError:
                    continue
