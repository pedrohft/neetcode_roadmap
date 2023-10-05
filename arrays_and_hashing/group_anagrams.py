"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
link: https://leetcode.com/problems/group-anagrams/
"""
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list) -> list():
        hashMap = dict({str("".join(sorted(strs[0]))): [strs[0]]})
        
        for i in range(1, len(strs)):
            print(i)
            key = "".join(sorted(strs[i]))

            if key in hashMap:
                hashMap[key].append(strs[i])
            else:
                hashMap[key] = [strs[i]]

        return hashMap.values()

    def groupAnagrams2(self, strs: list) -> list():
        hashMap = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for l in s:
                count[ord(l) - ord('a')] += 1

            hashMap[tuple(count)].append(s)
        
        return hashMap.values()

print(Solution().groupAnagrams2(["eat","tea","tan","ate","nat","bat"]))