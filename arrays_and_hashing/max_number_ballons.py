"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.


Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
link: https://leetcode.com/problems/maximum-number-of-balloons/
"""
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter_text = Counter(text)
        balloon = Counter("balloon")
        res = len(text)
        for w in balloon:
            res = min(res, counter_text[w] // balloon[w])
        return res