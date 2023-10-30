"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
link:https://leetcode.com/problems/word-pattern/description/
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
            hashmap = {}
            string_arr = s.split(" ")

            if len(pattern) != len(string_arr):
                 return False
            
            for p, w in zip(pattern, string_arr):

                if (((p in hashmap) and hashmap[p] != w) or 
                        (w in hashmap.values() and p not in hashmap)):
                    return False

                hashmap[p] = w
            hashmap
            return True

print(Solution().wordPattern("abba", "dog cat cat fish"))