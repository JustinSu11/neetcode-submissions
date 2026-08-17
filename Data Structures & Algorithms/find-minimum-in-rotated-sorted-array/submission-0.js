class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        if (nums.length == 1 || nums[0] < nums[nums.length-1]) {
            return nums[0]
        } else {
            let left = 0
            let right = nums.length-1
            
            while(left != right){
                if(nums[left] > nums[right]){
                    left++
                } else if(nums[left] < nums[right]){
                    right--
                }
            }
            return nums[right]
        }
    }
}

