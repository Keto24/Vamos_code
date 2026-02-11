"""
Encode and Decode Strings
Difficulty: Medium
Link: https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode150

Problem:
Design an algorithm to encode a list of strings to a single string.
The encoded string is then sent over the network and decoded back to
the original list of strings.

Implement the encode and decode methods.

Examples:
Input: ["Hello","World"]
Output: ["Hello","World"]

Input: [""]
Output: [""]

Approach:
Prefix each string with its length followed by a delimiter (#).
During decoding, read the length, extract the corresponding substring,
and move the pointer forward accordingly.

Complexity:
- Recommended Time Complexity: O(m) per encode() and decode()
- My Solution Time Complexity: O(m)

Learning / Review:
- This time I reinforced how length-prefix encoding avoids delimiter collision
  because the length tells us exactly how many characters to read.
- s.find('#', i) searches for the delimiter starting at index i.
- f"{len(s)}#{s}" dynamically builds each encoded segment using f-strings.
- Pointer movement (i = j + 1 + length) is critical to correctly parse
  sequential encoded strings.
"""

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return res
