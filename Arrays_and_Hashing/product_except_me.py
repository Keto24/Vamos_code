"""
Products of Array Except Self
Difficulty: Medium
Link: https://neetcode.io/problems/products-of-array-discluding-self/question

Problem:
Given an integer array nums, return an array output where output[i]
is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up:
Could you solve it in O(n) time without using the division operation?

Examples:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Approach:
Count the number of zeros first. If more than one zero exists,
all outputs are zero. Otherwise compute the total product of
non-zero elements and construct the result accordingly.

Complexity:
- Recommended Time Complexity: O(n)
- My Solution Time Complexity: O(n)

Learning / Review:
- nums.count(0) helps handle edge cases with zeros efficiently.
- math.prod([...]) computes the product of elements in a list.
- The division approach works because the problem guarantees
  results fit within 32-bit integers.
- Handling zero cases separately avoids division-by-zero errors.
"""

from typing import List
import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        total = math.prod([n for n in nums if n != 0])
        res = []
        for n in nums:
            if zero_count == 0:
                res.append(total // n)
            else:
                res.append(total if n == 0 else 0)
        return res
