class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    permute(nums) {
        if (nums.length === 0) {
            return [[]]
        }

        let permutations = this.permute(nums.slice(1))
        let res = []
        for (let permutation of permutations) {
            for (let i = 0; i <= permutation.length; i++) {
                let permutation_copy = permutation.slice()
                permutation_copy.splice(i, 0, nums[0])
                res.push(permutation_copy)
            }
        }
        return res
    }
}
