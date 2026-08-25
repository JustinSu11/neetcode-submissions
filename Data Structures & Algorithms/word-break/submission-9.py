"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.
"""

"""
Example 1:

Input: s = "neetcode", wordDict = ["neet","code"]

Output: true
"""
"""
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen","ape"]

Output: true
"""

"""
Whiteboard:
I'll keep a cache or a dict() with the key being the starting index of the new substring and the value either true or false of whether or not it can be broken into words from word dict

I'll then recursively call the canBreak() function on the remaining substring
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = dict()
        def canBreak(startIndex):
            if startIndex == len(s):
                return True
            elif startIndex in cache:
                return cache.get(startIndex)
            for i in range(len(s[startIndex: ]) + 1):
                if s[startIndex: startIndex + i] in wordDict and canBreak(startIndex + i):
                    cache.setdefault(startIndex, True)
                    return True
            cache.setdefault(startIndex, False)
            return False

        return canBreak(0)