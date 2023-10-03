"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

link: https://leetcode.com/problems/valid-anagram/

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        if len(s) != len(t):
            return False
        
        for ls, lt in zip(s,t):
            hash_s[ls] = hash_s.get(ls, 0) + 1
            hash_t[lt] = hash_t.get(lt, 0) + 1
        
        try:
            for k in hash_s.keys():
                print(hash_t[k])
                if hash_s[k] != hash_t[k]:
                    return False
        except Exception:
            return False
            
        return True

print(Solution().isAnagram("anagram", "nagaram"))