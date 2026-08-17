class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        if (nums.length === 0) {
            return -1
        } else if (nums[0] === target) {
            return 0
        } else {
            let left = 0
            let middle = Math.floor(nums.length / 2)
            let right = nums.length -1
            while (left <= right) {
                if (target > nums[middle]) {
                    left = middle + 1
                    middle = Math.floor((right + left) / 2)
                } else if (target < nums[middle]) {
                    right = middle - 1
                    middle = Math.floor(right / 2)
                } else if (target === nums[middle]) return middle
            }  
        }
        return -1 
    }
}
