"""
Valid Anagram
Difficulty: Easy
Link: https://neetcode.io/problems/is-anagram/question

Problem:
Given two strings s and t, return true if the two strings are anagrams
of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another
string, but the order of the characters can be different.

Examples:
Input: s = "racecar", t = "carrace"
Output: true

Input: s = "jar", t = "jam"
Output: false

Approach:
Sort both strings and compare the results. If they contain the same
characters with the same frequencies, their sorted versions will match.

Complexity:
- Time: O(n log n + m log m)
- Space: O(n + m)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s="".join(sorted(s))
        sorted_t="".join(sorted(t)) 

        return sorted_s == sorted_t
