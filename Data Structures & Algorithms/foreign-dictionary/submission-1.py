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
        "seed adjList with a set for each character"
        adjList = {c: set() for word in words for c in word}
        for i in range(len(words) - 1):
            "iterate through the words list 2 at a time and compare"
            word1, word2 = words[i], words[i + 1]
            "get the length of the smallest word"
            minLen = min(len(word1), len(word2))

            foundDiff = False
            "find the first differing character"
            for k in range(minLen):
                if word1[k] != word2[k]:
                    foundDiff = True
                    adjList[word1[k]].add(word2[k])
                    break
            "if there is no differing character and the second word is shorter than the first, this means it is not in lexical order so the claim in the problem statement is not true."
            if not foundDiff and len(word1) > len(word2):
                return ""
        "state to hold visiting/visited values for characters"
        state = dict()
        "result string that we will return later"
        result = []
        "iterate through each character in the adjList and it's neighbor to build resulting character array in lexical order"
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

        

        
