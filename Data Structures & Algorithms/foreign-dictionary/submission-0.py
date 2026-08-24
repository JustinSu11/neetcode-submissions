"""
There is a new alien language that uses the English alphabet, but the order of the letters is unknown.

You are given a list of strings words from the alien language's dictionary. It is claimed that the strings in words are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of strings in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

    - The first letter where they differ is smaller in a than in b.
    - a is a prefix of b and a.length < b.length.
"""

"""
Example 1:
Input: words = ["z","o"]

Output: "zo"
"""

"""
Input: words = ["hrn","hrf","er","enn","rfnn"]

Output: "hernf"
"""

"""
Whiteboard:
My first instinct is to create a dict() to store the character as the key and the index as the value.
This is wrong, it's a graph problem.
We'll use DFS for this
We need:
    1. an adjacency list, we iterate through each string adding the characters to a prefix array which will be appended as the value for the key. Key here is the character
    2. 
"""

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        "Build adjList"
        adjList = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))

            foundDiff = False

            for k in range(minLen):
                if word1[k] != word2[k]:
                    foundDiff = True
                    adjList[word1[k]].add(word2[k])
                    break

            if not foundDiff and len(word1) > len(word2):
                return ""

        state = dict()
        result = []
        "dfs"
        def dfs(char):
            if char in state and state[char] == "visiting":
                return False
            if char in state and state[char] == "visited":
                return True

            state[char] = "visiting"
            for neighbor in adjList[char]:
                if not dfs(neighbor):
                    return False

            state[char] = "visited"
            result.append(char)
            return True

        for char in adjList:
            if not dfs(char):
                return ""
        return "".join(reversed(result))

        

        
