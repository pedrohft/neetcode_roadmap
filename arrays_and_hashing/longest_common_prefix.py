"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
link: https://leetcode.com/problems/longest-common-prefix/description/
"""
class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        result = ""
        for i in range(len(strs[0])):
            for s in strs:
                if s[i] != strs[0][i] or len(s) == i:
                    return result
            result += strs[0][i]
        return result


print(Solution().longestCommonPrefix(["flower","flow","flight"]))