"""
Group Anagrams
Difficulty: Medium
Link: https://neetcode.io/problems/anagram-groups/question

Problem:
Given an array of strings strs, group all anagrams together into sublists.
You may return the output in any order.

An anagram is a string that contains the exact same characters as another
string, but the order of the characters can be different.

Examples:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Input: strs = ["x"]
Output: [["x"]]

Input: strs = [""]
Output: [[""]]

Approach:
Sort each string to form a key and use a dictionary to group strings
that share the same sorted representation.

Complexity:
- Recommended Time Complexity: O(m * n)
- My Solution Time Complexity: O(m * n log n)
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for string in strs:
            key = "".join(sorted(string))
            if key in my_dict:
                my_dict[key].append(string)
            else:
                my_dict[key]= [string]

        My_list = list(my_dict.values())
        return My_list
