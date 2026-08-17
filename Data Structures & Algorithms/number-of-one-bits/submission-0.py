class Solution:
    def hammingWeight(self, n: int) -> int:
        stringOfN = bin(n)
        return stringOfN.count("1")