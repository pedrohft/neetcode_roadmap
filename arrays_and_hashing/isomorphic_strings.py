"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
link: https://leetcode.com/problems/isomorphic-strings/
"""
from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        for ls, lt in zip(s,t):

            if ((ls in hash_s and hash_s[ls] != lt) or
                 (lt in hash_t and hash_t[lt] != ls)):
                    return False
            
            hash_s[ls] = lt
            hash_t[lt] = ls

        return True
print(Solution().isIsomorphic("bbbaaaba", "aaabbbba"))