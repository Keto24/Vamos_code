        """
Top K Frequent Elements
Difficulty: Medium
Link: https://neetcode.io/problems/top-k-elements-in-list/question

Problem:
Given an integer array nums and an integer k, return the k most frequent
elements within the array.

The test cases are generated such that the answer is always unique.
You may return the output in any order.

Examples:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Input: nums = [7,7], k = 1
Output: [7]

Approach:
Use a dictionary to count the frequency of each number, then sort the
dictionary items by frequency in descending order and return the top k keys.

Complexity:
- Recommended Time Complexity: O(n)
- My Solution Time Complexity: O(n log n)

Learning / Review:
- This time I learned this syntax:
  [num for num, _ in sorted(seen.items(), key=lambda x: x[1], reverse=True)[:k]]

  Explanation:
  - seen.items() returns (key, value) pairs from the dictionary
  - sorted(..., key=lambda x: x[1], reverse=True) sorts the pairs by frequency
    (the value) in descending order
  - [:k] slices the first k most frequent pairs
  - num for num, _ extracts only the number (key) and ignores the frequency
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] = seen[num]+ 1
            else:
                seen[num] = 1
        return [ num for num, _ in sorted(seen.items(), key=lambda x: x[1], reverse=True)[:k]]

