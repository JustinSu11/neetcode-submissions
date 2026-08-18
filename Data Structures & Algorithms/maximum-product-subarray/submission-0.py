class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        currMax = nums[0]

        currMin = nums[0]

        maxProd = nums[0]

        for num in nums[1: ]:
            temp = max(num, currMin * num, currMax * num)
            currMin = min(num, currMax * num, currMin * num)
            currMax = temp
            maxProd = max(maxProd, currMax)

        return maxProd